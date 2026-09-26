# G0-02 checkpoint

The manual exchange now freezes source bytes and records waiting_external without
a running lease. Returned JSON is quarantined and structurally validated during a
new local attempt; the task becomes awaiting_fact_check. It is not scientifically
accepted, human audited, or independent merely because the JSON is valid.

Validation includes synthetic roundtrip, duplicate/conflicting returns, damaged
hashes, stale code/rules/source versions, unknown sources/locators, storage limits,
and process interruption/new-process recovery. A real signed-in Chrome Pro
roundtrip passed for G0_02_pro_002: complete inline logical files, preserved raw
JSON, structural import, idempotent repeat and local synthetic-fact check.
Exact model unknown (UI Latest / Extra High, account Pro); human audit not run.
The later metadata change has a new code hash; the G0 receipt preserves its
original baseline and must not be rebound. See docs/P2_CHECKPOINT.md for P2.

Current research coverage: zero real-paper loops, zero new paper PDFs, zero human
audits; population unknown. Historical sample claims and graph fixtures are local
unverified inputs, not this checkpoint's scientific output.

Use the existing local .venv. No installation is needed for G0 (stdlib only).
Run `tools/python-project.cmd tools/workflow.py --help`, then `status`, `recover`,
and `preflight`. Local full acceptance: `tools/python-project.cmd tools/run_stage_tests.py`.
The published active suite is runnable with
`tools/python-project.cmd tools/run_offline_tests.py --active-only`.
Create `cache/tmp` when restoring into an empty clone. The wrappers expect the
existing local runtime layout; Git does not include runtimes or machine config.
For a separately configured Python, invoke the same Python scripts directly.

Historical completed review: G0_02_pro_002, task G0_02_synthetic_002.
The unmodified JSON was saved under exchange/inbox. Historical import command:
`tools/python-project.cmd tools/workflow.py import-pro --review G0_02_pro_002 --file exchange/inbox/G0_02_pro_002/review.json`.
The marker BLUE and missing prior work were checked against local bytes; novelty
remained U. P2_catalog_002 was then created. Both old catalog tasks are preserved;
current source-access blockers are recorded in docs/P2_CHECKPOINT.md.

Source publication and main merge are separate. Read actual remote refs/content
before marking upload verified. Raw exchange packages, SQLite, source PDFs, reports,
environment, backups and machine path inventories stay local.
