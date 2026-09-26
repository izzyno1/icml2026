# Public paper routes checked on 2026-09-25

2026-09-26 update: one user-supplied ICML 2026 PDF is now registered and locally
extracted (Hedging, 65 pages). Two prior works were acquired through the guarded
PMLR downloader: Mansour 2021 main paper and supplement, and Mourtada 2023's
two-page extended abstract. The latter is not its full proof paper.

The official [mlresearch/v306 repository](https://github.com/mlresearch/v306)
describes ICML 2026, but its complete inspected main tree
`b3b1748fa2fac7ec916eb1dee8fee9f0691d9450` contains only README.md and a PR
template, no PDFs. Another two requested main-track candidates (aIH1jyU37z and
wsA8LgHU5U) were checked on their public spotlight forums; each guarded current
PDF request returned HTTP 403 once. No unchanged retry or credential transfer.

The sections below preserve the 2026-09-25 source investigation. Their earlier
zero-PDF and not-exported statements are historical; current counts and real
Pro exchange status are in [P2_CHECKPOINT.md](P2_CHECKPOINT.md).

No complete ICML 2026 PDF collection was verified. Repository names, advertised
counts and download instructions do not establish that PDF bytes are distributed.

| Resource | Observed contents | Use and limit |
| --- | --- | --- |
| [KIM-JAKE/ICML2026-Papers](https://github.com/KIM-JAKE/ICML2026-Papers) | Searchable conference metadata and schedule, `papers.js`; README discloses title-generated labels/TLDRs | Candidate discovery, not primary contribution evidence or a verified population |
| [gisbi-kim/icml2026-explorer](https://github.com/gisbi-kim/icml2026-explorer) | Explorer, raw conference metadata, links to the official public feeds | Candidate/source matching; not a PDF archive |
| [Drbellamy/icml-2026](https://huggingface.co/datasets/Drbellamy/icml-2026) | Queryable title/author/abstract/schedule records and OpenReview PDF URLs | Card explicitly says PDFs are not redistributed. Single-title viewer/API query timed out in this check |
| [GenAI4ELab/papercli-papers-icml](https://huggingface.co/datasets/GenAI4ELab/papercli-papers-icml/tree/main/pdfs/icml) | Actual PDF shard; Chrome directory view lists 2023, 2024 and 2025, not 2026 | Potential prior-work source. The displayed 25.8 GB was not downloaded; no claim of complete coverage or universal paper license |
| [acensia/paper-shelf](https://github.com/acensia/paper-shelf/tree/main/ICML2026) | Selected paper descriptions and `source.txt`; `.gitignore` excludes `*.pdf` | README's “PDF downloaded” describes the maintainer's local state. Inspected Do We Need Adam folder has only source.txt; Learning to Theorize folder has NO_PDF_AVAILABLE.txt |
| [ICML 2026 Open Reproductions](https://huggingface.co/spaces/ICML-2026-agent-repro/challenge) | Public paper index, extracted claims and third-party reproduction links | Found exact first-paper title/authors/forum and alphaXiv link. Claims and toy reproduction status are not this project's evidence or independent review |

The repository explorer points to the official
[orals/posters feed](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json)
and [abstracts feed](https://icml.cc/static/virtual/data/icml-2026-abstracts.json).
These are future catalog candidates, not locally collected or fully audited here.
Different repositories report different counts and mixtures of event types. None
of those totals is adopted as the verified main-research population.

## First-paper mirrors

Paper: *Hedging on the Frontier: Learning New Tasks with Few Samples*.
Official identity: [ICML poster 64858](https://icml.cc/virtual/2026/poster/64858),
OpenReview J4wRLmh29t. The following independent public PDF links were observed:

- [alphaXiv versioned PDF](https://pdfs.assets.alphaxiv.org/2605.30997v1.pdf), linked
  by the [alphaXiv paper page](https://www.alphaxiv.org/abs/2605.30997).
- [ResearchGate public PDF](https://www.researchgate.net/publication/405562119_Hedging_on_the_Frontier_Learning_New_Tasks_with_Few_Samples/fulltext/6a1d06097076b91843485bd4/Hedging-on-the-Frontier-Learning-New-Tasks-with-Few-Samples.pdf),
  linked by its [publication page](https://www.researchgate.net/publication/405562119_Hedging_on_the_Frontier_Learning_New_Tasks_with_Few_Samples).

The web retrieval service reported both as 70-page PDFs. Exposed pages 1-3 match
the title and Tobias Wegel, Federico Di Gennaro, Geelon So and Fanny Yang. The
first page displays arXiv:2605.30997v1, 29 May 2026; the manuscript heading is dated
June 1, 2026. These are preprint-version observations. Neither original-submission
nor camera-ready equivalence was established; the PDFs were not read in full.

**Local protected retrieval still failed:** alphaXiv robots disallowed the PDF
request; ResearchGate returned HTTP 403 after the robots check. One attempt per
new URL, no automatic redirect, retry, credential transfer or policy bypass.
No PDF bytes, PDF hash or complete paper text entered the local evidence ledger.
Web readability is recorded separately from local acquisition.

## Implementation and next gate

The downloader admits only these two exact mirror URLs, with the existing
capacity, robots, timeout and streaming guards. The ledger now has an explicit
`preprint` role. These mirror URLs reject original/camera-ready/revised labels;
invalid roles fail before reserving space or making a request. Source URL, bytes
and a separately checked version record must identify the actual preprint version.

Full offline acceptance after the code change: 124 cases, 122 passed, 2 Windows
symlink-permission skips, 0 failures. Seven new mirror/version cases are included;
four actual forced-process recovery cases remain in the full suite. This does not
constitute successful live paper acquisition or scientific acceptance.

P2 remains incomplete: zero local paper PDFs and zero real paper loops. No real
Pro review was exported. Next acquisition task is P2_J4wRLmh29t_acquire_004, only
after a concrete available source/access change; prior blocked attempts remain.
Next review is P2_J4wRLmh29t_screening_001, not exported. No P3/P4 work is authorized.

## Later login and author-source follow-up

Chrome login was subsequently confirmed. The guarded original-submission PDF
request still returned HTTP 403. Browser navigation aborted and the subsequent
page was blocked by browser URL policy; the user confirmed no download.

[Tobias Wegel's ETH page](https://sml.inf.ethz.ch/group/tobiasw/) links the paper
to arXiv, slides and its [author code repository](https://github.com/FedericoDiGennaro/Hedging-on-the-Frontier).
The repository tree at `6329a100ef977b0a225d470ea93c5913cb5bcc30` was not truncated:
14 entries, no PDF/TeX/archive files. Its README describes scripts and partial
figure data, not a redistributed paper. No author code or dataset was executed
or downloaded. This bounded inspection is not an exhaustive mirror search.

Current next task is `P2_J4wRLmh29t_acquire_005`, after an actual file/access change.
The new [manual intake](MANUAL_PDF_INTAKE.md) preserves unverified origin/version
and does not turn a link or code repository into paper evidence.
