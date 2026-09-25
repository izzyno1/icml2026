# P2 acquisition checkpoint — 2026-09-25

P2 is incomplete: zero registered paper PDFs and zero real paper loops.
OpenReview Chrome login is now confirmed. The forum shows the correct title,
authors, spotlight status and a separately labeled original-submission PDF.
The protected local original-PDF request still returned HTTP 403 once.
Browser attachment navigation aborted and its follow-up page was blocked by
browser URL policy. The user confirmed that no file downloaded. This does not
establish that the current PDF is missing or inaccessible to the user.

[Manual PDF intake](MANUAL_PDF_INTAKE.md) is implemented and its help checked.
The new full offline suite has **135 cases: 133 passed, 2 skipped, 0 failed**.
It retains unverified provenance/version and unread status. No dependency was
installed, no server/browser restriction was bypassed, and no PDF is claimed read.

## Evidence and coverage

The official call and venue configuration distinguish main research from position
papers. Ten first-page spotlight candidates are a convenience selection, not a
verified population or probability sample. No ICML 2026 PMLR volume was verified
by the bounded checks.

First candidate: *Hedging on the Frontier: Learning New Tasks with Few Samples*,
OpenReview J4wRLmh29t, public decision tDQyc5CqkT. The protected ICML individual
HTML object is 85,564 bytes, SHA-256
`b85ba2f9c63c45230aa5688d77a2a6bd9017dc799b98a1f250511a4f95cb3219`.
Title/authors/forum were checked in HTML lines 2359–2473. This is metadata only.
The forum reports publication April 30 and modification September 22, 2026.
Its revision page displays no revisions; that UI does not establish version
completeness or prove that the current PDF is camera-ready.

Independent arXiv:2605.30997v1 mirrors returned 70-page PDF previews to the web
service. Only exposed pages 1–3 were inspected; no local PDF or full reading is
claimed. Local alphaXiv robots denial, ResearchGate 403 and arXiv/export.arxiv.org
robots 406 remain recorded. Links and previews are not locally acquired body
evidence. See [public source routes](PUBLIC_SOURCE_ROUTES.md).

The author's ETH page and code repository were additionally checked. The complete
repository tree at 6329a100ef977b0a225d470ea93c5913cb5bcc30 had 14 entries and no
PDF or TeX source. No author code, benchmark dataset or reproduction was run.

G0_02_pro_002 is a historical successful real Pro synthetic exchange with fully
provided inline inputs, preserved JSON, idempotent import and four synthetic
claim checks. Later code changes make it stale for reuse without erasing that
history. No real-paper Pro screening, independent AI review, human audit,
prior-paper full-text comparison, contribution card or paper graph is complete.

## Current recovery

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py --help
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
& .\tools\python-project.cmd tools\workflow.py import-paper --help
```

Local checkpoint: `reports/P2_intake_checkpoint.json`; current handoff:
`reports/P2_HANDOFF.md`. The latest GitHub sync receipt separately records the
actually verified branch/commit/files. Source objects, raw exchanges and SQLite
remain local; GitHub is not a runtime backup.

Next task: **P2_J4wRLmh29t_acquire_005**, not created; wait for a real file or a
supported bounded transfer. Next review: **P2_J4wRLmh29t_screening_001**, not
exported. Keep catalog _001/_002 and acquisition _001 through _004 historical
and blocked; never rewrite their hashes for a new attempt.

One real-paper loop must pass before expansion to at most ten. P3/P4 remain
unauthorized. Original AGENTS.md is unchanged; no work after session closure is
promised.
