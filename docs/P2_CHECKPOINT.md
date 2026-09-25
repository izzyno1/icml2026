# P2 public mirror checkpoint — 2026-09-25

Latest follow-up: [public source routes](PUBLIC_SOURCE_ROUTES.md) records checked
GitHub/Hugging Face catalogs, an older-year PDF archive, and two actual first-paper
preprint links. Both returned 70-page PDFs through the web service; local protected
retrieval stopped at alphaXiv robots denial and ResearchGate HTTP 403. No local
PDF or full-text reading is claimed. Explicit preprint-role and exact-mirror-URL
support passed the new full suite: 124 cases, 122 passed, 2 skipped, 0 failures.
The older 117-case counts below describe the preceding implementation.

P2 is incomplete. The real Pro synthetic roundtrip passed; protected full-text
acquisition remains blocked after checking independent public sources. No real paper loop, novelty assessment,
prior-work reading, independent AI review, human audit, or paper evidence graph
has been completed.

The official ICML call identifies the main research OpenReview group separately
from position papers. A protected download saved that page and the public venue
configuration. Ten candidate titles/IDs were observed on the first spotlight page;
this convenience selection cannot estimate conference proportions or population.
The PMLR index did not establish an ICML 2026 volume in this check.

The first candidate selected for a paper attempt is *Hedging on the Frontier:
Learning New Tasks with Few Samples*, OpenReview J4wRLmh29t. Its public forum
shows ICML 2026 spotlight and public decision tDQyc5CqkT. The original-submission
link is visible, but no original or current PDF bytes were obtained. arXiv
2605.30997v1 is a separately observed May 29 preprint candidate; it is not recorded
as the January original, a camera-ready copy, or locally read full text.

The bounded notes API redirected to human verification. The verification page
was opened for the user; a subsequent check showed Chrome ERR_BLOCKED_BY_CLIENT.
The protected OpenReview PDF request returned HTTP 403. The independent arXiv
metadata attempt stopped at robots HTTP 406. No cookies/tokens were read or
transferred, no CAPTCHA was solved by the agent, and no mirror bypass was used.
The user subsequently confirmed that OpenReview registration/activation is still
under review and authorized independent public sources. No further OpenReview
login retry is required now. The official ICML individual page
https://icml.cc/virtual/2026/poster/64858 was retrieved through the protected
downloader: 85,564 bytes, SHA-256
`b85ba2f9c63c45230aa5688d77a2a6bd9017dc799b98a1f250511a4f95cb3219`.
Its title, authors and forum link were checked in raw HTML lines 2359-2473.
This is metadata, not paper text.

The arXiv bulk-access documentation recommends export.arxiv.org for programmatic
access. A single protected request for the versioned preprint stopped at robots
HTTP 406 before requesting the PDF. Author and institutional pages were inspected
within the same ten candidates: several full-paper links still lead to arXiv;
the OC-space institutional PDF instead redirects to Shibboleth login. Search
leads and repository READMEs are not substituted for paper evidence. No author
code, dataset, or third-party reproduction was run or downloaded. Discovery was
bounded, not an exhaustive claim that no alternative source exists.

Raw browser captures, source objects and failures remain local. The small public
coverage record is `published/catalog/P2_catalog_002.json`.

Five new offline cases cover metadata JSON/HTML, invalid MIME/binary/oversized
responses, refusal before any socket at low disk, and recovery after bytes are
saved but before registration. Current full suite: 117 discovered, 115 passed,
2 symlink-permission skips, 0 failures; four existing forced-process recovery
cases passed. No paper parsing dependency has been installed.

G0 review G0_02_pro_002 was sent through signed-in Chrome (account Pro, menu
Latest, Extra High; exact model unknown). Six complete logical files were pasted
inline. The real JSON response was preserved, imported twice (second idempotent),
and all four synthetic claims checked locally. Human audit remains not run.
Its completed receipt preserves the prior code baseline. Subsequent metadata
code changes correctly mark that old task stale for reuse; they do not erase the
historical observed roundtrip. Do not rewrite its binding to the newer code.

Resume in the actual local project using:

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py --help
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
```

Read local `reports/P2_mirror_checkpoint.json` and the latest GitHub sync
receipt. Continue with an actually available independent public paper source or
user-provided evidence. OpenReview account approval is optional to that route;
do not repeat a login request while the user is waiting for account review. Do not
retry the same blocked source unchanged or export browser credentials. A preprint
must retain its own version role rather than being called the original or final.

Next task: P2_J4wRLmh29t_acquire_004, only after a concrete new source/access change.
Next review (not exported):
P2_J4wRLmh29t_screening_001, only after actual located evidence and necessary
prior work are available. Preserve blocked P2_catalog_001, P2_catalog_002 and
P2_J4wRLmh29t_acquire_001, _002 and _003. This follow-up changed code but not rules;
the full suite was rerun and the current 124-case receipt binds the new code. Do not mark P2 complete or expand beyond one paper
before its full loop passes. P3/P4 remain unauthorized.
