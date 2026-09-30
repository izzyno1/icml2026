# One-file local PDF intake

**2026-09-26 update:** the user located the saved file in Downloads. The one
matching named PDF was copied into the intake folder with size/hash checks and
its original retained. Guarded import under acquire_005 succeeded: 65 pages,
1,805,631 bytes, SHA-256
3259e3abb5044c484af4af04d93705ba2c231e5a64b14c002ff7b6f089e1d570.
Title/authors match; original/camera-ready certification is still unverified.
Both screening_001 and independent_001 have actual Pro returns; scoped local
fact checks and reconciliation are saved. The remaining work concerns source,
version and proof-coverage gaps. Do not rerun the historical
enqueue/import example below for this received file: acquire_005 is now accepted
for acquisition only, and its original objective differs from the example.

Manual intake is a contingency for an explicitly supplied file, not the planned
per-paper collection workflow. A guarded API2 PDF probe on 2026-09-26 returned
`ChallengeRequiredError`. The signed-in browser session and the unauthenticated
local client are distinct. A bounded browser-to-local transfer is not yet
implemented or verified; do not claim that copying login state is required.

The following explains the preserved earlier access failure and intake contract.

Signed-in Chrome can open the forum. The guarded local original-PDF request
returned HTTP 403. Browser attachment navigation aborted and the subsequent page
was blocked by browser URL policy. The user confirmed no file was downloaded.
Do not transfer credentials, disable restrictions or repeat a failed request
unchanged. This entrypoint does not automate an external download.

The user may save the single current PDF linked by
[OpenReview J4wRLmh29t](https://openreview.net/forum?id=J4wRLmh29t) as
`exchange/manual_intake/J4wRLmh29t_current.pdf` within the actual project.
The PDF stays local. If the browser cannot save it, retain the error and leave
the acquisition blocked.

## Guarded reception

`tools/workflow.py import-paper --help` is implemented and locally checked.
The command reads only a directly named `.pdf` within `exchange/manual_intake/`.
It refuses absolute/escaping/nested paths, reparse points, hard links, empty or
oversized files, insufficient disk, stale/blocked tasks, and source URLs that do
not exactly match the task's OpenReview ID. Only a pending real acquisition task
can import; there is no running lease while waiting for the user.

The maximum file size is the policy's 60,000,000 bytes. Space accounting includes
the supplied file and reserves the object copy. Streaming reuses byte, time,
disk and SHA-256 checks. A changing input is rejected before object publication.
The supplied file is retained; identical copies share one evidence object and
source. Recovery retains manual-intake provenance in the receipt. The external
manual download itself is outside this program's transfer controls.

The imported source is `current_attachment_unverified_role`, `not_read` even if
declared to be an original submission. The receipt records that declaration
separately, with `origin_verified=false`, `version_verified=false`, and unknown
external download time. Local ingestion time is not a server publication date.
Signature validation is not a full PDF parser or a content-identity check.

Before Pro export, inspect title/authors and version, extract locatable text,
verify necessary prior sources, and record exactly which materials were supplied
and read. Local file intake alone is neither a paper loop nor AI screening.

## Resume after the actual file exists

Use the existing environment. Do not reuse a historical blocked task; if the
suggested ID already exists with a different context, choose a new one rather
than rewriting its hashes.

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py --help
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
& .\tools\python-project.cmd tools\workflow.py import-paper --help
& .\tools\python-project.cmd tools\workflow.py enqueue --task P2_J4wRLmh29t_acquire_005 --paper OR_J4wRLmh29t --stage acquisition --kind real --objective 'Validate one user-supplied PDF, preserving unverified source and version until direct inspection.'
& .\tools\python-project.cmd tools\workflow.py import-paper --task P2_J4wRLmh29t_acquire_005 --file exchange/manual_intake/J4wRLmh29t_current.pdf --url 'https://openreview.net/pdf?id=J4wRLmh29t'
```

For the separately labeled original attachment, use its exact observed URL and
`--declared-role original_submission`. On Windows, a URL containing `&` must
survive the `.cmd` wrapper: use PowerShell's `--%` with a double-quoted URL, as
verified previously. Do not weaken source-URL validation.

Full offline suite: 135 discovered, 133 passed, 2 existing Windows symlink skips.
Eleven new cases cover idempotency, invalid bytes/paths/source declarations, low
space, changed context, input mutation, unverified original declarations and
interrupted receipt recovery. That original test run did not establish a live
import or real review; the later actual file and Pro receipts are described above.
