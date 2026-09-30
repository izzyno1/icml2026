#!/usr/bin/env python3
"""Small auditable helpers. No LLM calls, web access, or automated novelty verdicts."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
import json
from pathlib import Path
from typing import Any


def validate_graph(g: dict[str, Any]) -> dict[str, Any]:
    ids=[n['id'] for n in g['nodes']]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate paper IDs')
    edges=g['edges']; eids=[e['id'] for e in edges]
    if len(eids)!=len(set(eids)): raise ValueError('Duplicate edge IDs')
    idset=set(ids); adj=defaultdict(set); indeg={x:0 for x in ids}
    for e in edges:
        if e['parent'] not in idset or e['child'] not in idset: raise ValueError('Missing endpoint')
        if e['parent']==e['child']: raise ValueError('Self-edge')
        if e['type'] not in g['types']: raise ValueError('Unknown edge type')
        for side in ('parent_source','child_source'):
            s=e.get(side,{})
            if s.get('source_id') not in g['sources'] or not s.get('locator'): raise ValueError('Missing source or locator')
        if g['types'][e['type']]['count_as_lineage'] and e['child'] not in adj[e['parent']]:
            adj[e['parent']].add(e['child']);indeg[e['child']]+=1
    q=deque(x for x in ids if indeg[x]==0); done=0
    while q:
        x=q.popleft();done+=1
        for y in adj[x]:
            indeg[y]-=1
            if not indeg[y]:q.append(y)
    if done!=len(ids):raise ValueError('Cycle in lineage layer: investigate versions/dates')
    return {'nodes':len(ids),'edges':len(edges),'lineage_is_dag':True,'population_role':g.get('population_role'),'note':'Structural consistency only; not factual, temporal, or novelty validation.'}


def descendants(g:dict[str,Any],paper:str,include_components:bool=False)->dict[str,Any]:
    validate_graph(g)
    if paper not in {n['id'] for n in g['nodes']}:raise ValueError('Unknown paper')
    adj=defaultdict(set)
    for e in g['edges']:
        if g['types'][e['type']]['count_as_lineage'] or (include_components and e['type']=='component_reuse'):
            adj[e['parent']].add(e['child'])
    seen=set();q=deque([paper])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in seen and y!=paper:seen.add(y);q.append(y)
    return {'paper':paper,'direct':sorted(adj[paper]),'descendants':sorted(seen),'direct_count':len(adj[paper]),'descendant_count':len(seen),'scope':'Observed sample graph only; comparisons excluded, deduplicated by paper ID.'}


def identification_bounds(payload:dict[str,Any])->dict[str,Any]:
    """Stratified simple-random sample endpoint estimates. NOT confidence intervals.

    Input: population_role='audited_probability_sample' or 'census',
    strata={stratum: population size}, rows=[{paper_id,stratum,label,human_adjudicated}].
    label is yes/no/unknown for a SINGLE preregistered estimand.
    """
    if payload.get('population_role') not in {'audited_probability_sample','census'}:
        raise ValueError('Non-probability/illustrative data cannot estimate the conference ratio')
    if payload.get('design')!='stratified_srs':raise ValueError('Only declared within-stratum SRS supported')
    if not payload.get('estimand'):raise ValueError('Define the estimand before counting')
    Ns=payload['strata']
    if not Ns or any(not isinstance(n,int) or n<1 for n in Ns.values()):raise ValueError('Invalid stratum sizes')
    rows=payload['rows'];seen=set();by=defaultdict(Counter)
    for r in rows:
        if r['paper_id'] in seen:raise ValueError('Duplicate paper')
        seen.add(r['paper_id'])
        if r['stratum'] not in Ns:raise ValueError('Unknown stratum')
        if r.get('human_adjudicated') is not True:raise ValueError('Only human-adjudicated labels supported')
        if r.get('label') not in {'yes','no','unknown'}:raise ValueError('Invalid label')
        by[r['stratum']][r['label']]+=1
    N=sum(Ns.values());lo=hi=unknown=0.;coverage=[]
    for h,Nh in Ns.items():
        c=by[h];nh=sum(c.values())
        if nh<1 or nh>Nh:raise ValueError('Every stratum needs valid sampled records')
        if payload['population_role']=='census' and nh!=Nh:raise ValueError('Incomplete census')
        w=Nh/N;lo+=w*c['yes']/nh;hi+=w*(c['yes']+c['unknown'])/nh;unknown+=w*c['unknown']/nh
        coverage.append({'stratum':h,'N':Nh,'n':nh,'weight':w})
    return {'estimand':payload['estimand'],'n':len(rows),'N':N,'lower_endpoint_estimate':lo,'upper_endpoint_estimate':hi,'unknown_weighted_share':unknown,'strata':coverage,'interval_type':'Identification-bound endpoint estimates, NOT sampling confidence intervals','limitations':'Sampling error, imperfect adjudication, missing-prior bias, and rubric uncertainty are NOT included.'}


def main()->None:
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='cmd',required=True)
    for cmd in ('validate','descendants','bounds'):
        p=sub.add_parser(cmd);p.add_argument('file',type=Path)
        if cmd=='descendants':p.add_argument('--paper',required=True);p.add_argument('--include-components',action='store_true')
    a=ap.parse_args()
    try:
        obj=json.loads(a.file.read_text(encoding='utf8'))
        result=validate_graph(obj) if a.cmd=='validate' else descendants(obj,a.paper,a.include_components) if a.cmd=='descendants' else identification_bounds(obj)
    except (OSError,KeyError,TypeError,ValueError) as e:ap.error(str(e))
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
