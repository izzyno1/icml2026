# G0-02 checkpoint

The manual exchange now freezes source bytes and records waiting_external without
a running lease. Returned JSON is quarantined and structurally validated during a
new local attempt; the task becomes awaiting_fact_check. It is not scientifically
accepted, human audited, or independent merely because the JSON is valid.

Validation includes synthetic roundtrip, duplicate/conflicting returns, damaged
hashes, stale code/rules/source versions, unknown sources/locators, storage limits,
and process interruption/new-process recovery. A real Pro roundtrip remains pending.
The G0 gate and P2 catalog/paper work remain incomplete until that real return.

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

Next external review: G0_02_pro_001, task G0_02_synthetic_001.
After a real response, copy the unmodified JSON into exchange/inbox and run
`tools/python-project.cmd tools/workflow.py import-pro --review G0_02_pro_001 --file exchange/inbox/G0_02_pro_001/review.json`.
Before P2, inspect actual declared visible/read materials and independently check
the synthetic marker against the local bytes. Do not substitute local simulation.
Then create P2_catalog_002; preserve P2_catalog_001 as historical blocked.

Source publication and main merge are separate. Read actual remote refs/content
before marking upload verified. Raw exchange packages, SQLite, source PDFs, reports,
environment, backups and machine path inventories stay local.
