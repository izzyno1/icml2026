# Minimal manual Pro exchange v1

`workflow.py export-pro --task TASK --review REVIEW [--round screening|independent_ai_review]`
requires an existing pending task, available source bytes, and an explicit list of
provided locator labels in task `inputs.provided_ranges[source_id]`. Source records
retain stable paper identity, URL, version role, hash, and missing ranges. Real tasks
require every code/rule file to match Git HEAD; synthetic tasks may precede a baseline.

The immutable package contains TASK.md, manifest.json, sources.json, rules.json,
review.template.json and materials. The manifest binds schema, task/review/paper/round,
base commit, rule/code/input/prompt hashes, evidence snapshot, and every package file.
Manifest self-hash is held in SQLite, avoiding a self-referential file hash.
An export transitions the task to waiting_external without claiming a lease.

Copy the actual returned bytes under exchange/inbox, then run:
`workflow.py import-pro --review REVIEW --file exchange/inbox/RETURN.json`.
Inputs are confined to the inbox, capped at 1 MB, and copied unchanged to a
SHA-named quarantine object before validation. Each local validation attempt is
bounded to 300 seconds. Duplicate accepted bytes are idempotent; conflicting drafts
cannot overwrite a validated draft. Stale input needs a new explicit task/review.

`binding` must exactly match the template. Required fields: model (unknown allowed),
origin (pro_conversation or local_simulation), visible_files, read_sources, claims,
candidate_sources, supplement_requests, limitations, independence.
Each read source has source_id and ranges drawn from supplied locator labels;
each claim has claim_id, kind, text, evidence, prior_comparison, conditions,
uncertainty and suggested_label. Evidence has source_id and locator from actual
declared read ranges. Kinds: author_claim/direct_evidence/inference/unknown.
Labels: U/L0/L1/L2/L3. Candidate URLs never become ledger evidence automatically.

Success means **format_validated / awaiting_fact_check** only. The raw result remains
a draft; no entry is added to the scientific results table. A source locator label
being well formed does not establish that it supports a claim. AI screening,
independent AI review, human audit, and fact validation remain separate. Origin and
model names are declarations, not cryptographically authenticated identities.

Storage uses the existing measured project/external-volume budget. Packages are
limited to 20 MB including materials; only text, Markdown and PDF sources are copied.
Nothing executes returned content. No archives are extracted. No APIs are invoked.

Recovery: `workflow.py recover` rechecks frozen inputs and regenerates receipts.
An interrupted import returns to waiting_external; rerun the exact import command
to open a fresh short attempt. A committed import remains idempotent even if receipt
writing was interrupted. A package written before its ledger transaction is an
orphan: preserve it, inspect it, and export with a new review_id; it is never silently
adopted or deleted. This conservative export recovery needs an explicit new ID.

Receipts are local under exchange/sync_receipts. They do not imply GitHub upload.
Synthetic tests and local simulations do not establish a real Pro roundtrip.
