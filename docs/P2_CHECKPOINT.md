# P2 检查点 — 2026-09-26

P2 尚未完成。已接收 **1 篇 ICML 2026 主轨正文、2 篇前作及 1 份补充材料**，
合计三篇文献、四个 PDF；真实论文闭环仍为零。原始投稿缺失，当前附件的正式
版本角色未认证。下载数量、格式验收和模型意见不等于科学验收。

首篇是 *Hedging on the Frontier: Learning New Tasks with Few Samples*，
OpenReview `J4wRLmh29t`。用户保存的 PDF 经受保护接收：65 页、1,805,631 字节，
SHA-256 `3259e3abb5044c484af4af04d93705ba2c231e5a64b14c002ff7b6f089e1d570`。
标题和作者与官方题录匹配；原件保留。65 页均已提取可定位文本，不能称全部读完。

受保护下载还取得 Mansour 等 AISTATS 2021 的 12 页正文和 4 页补充材料，
以及 Mourtada 等 COLT 2023 的 2 页扩展摘要；最后一项不是完整证明论文。
实际 URL、字节哈希、来源角色和 Pro 输入页码见
[来源清单](../published/evidence/P2_J4wRLmh29t.json)。正文和完整抽取文本留本地。

另外两篇 spotlight 候选 `aIH1jyU37z`、`wsA8LgHU5U` 各作一次受保护正文请求，
均为 HTTP 403，未取得 PDF。官方 `mlresearch/v306` 仓库已查，但所见树只有
README 和 PR 模板，没有论文文件。十条候选仍是便利选择，总体规模未知。

## 真实 Pro 与本地核验

首轮 `P2_J4wRLmh29t_screening_001` 已在实际 Chrome Pro 对话完成。
五份文本附件提供主文第 1–14、22–26、57–61 页，以及三份前作文件的完整文本。
Pro 未收到 PDF 图像；数学符号提取可能失真。可见模式为 Latest / Pro，后端未知。

第一份可见回复含界面引用换行，被 JSON 验证拒绝并隔离保留；同一对话实际重发
代码块后通过格式、版本、来源和定位检查。相同回传的重复导入没有重复接收。
两份原始回复及差异记录均在本地保存，没有用本地模拟替代 Pro。

十项主张已作有范围限制的本地原文核对，登记在 `P2_J4wRLmh29t_factcheck_001`。
部分关键页已看原图，并计算零裕量并列和尾积分两个局部检查。第 27 页的粗网格
证明实际存在，只是未进入首轮任务包；不能把输入缺口写成论文缺陷。
这些检查不证明整篇数学正确性、完整前作覆盖或新意，整体标签仍为 **U**。

另开 Pro 对话进行独立 AI 复核，使用同一冻结证据，未提供首轮意见；账户记忆是否
完全隔离无法核实，不能宣称完全盲法。第二轮实际返回 6 项，原文保留并通过
隔离导入；重复导入未重复接收。本地 `P2_J4wRLmh29t_reconcile_001` 已登记
6 组对照和新增局部检查，包括双模型零阈值例、MON 不推出模数右连续的例子、
以及尾积分常数的可修补范围。数学新主张仍按核验范围分别记录，未认证全部证明。
人工审计、人工校准及实验复现均未做。[当前状态](../published/status.json) 区分
真实回传、格式验收、本地对照与整篇未闭环。

首篇官方 API2 PDF 请求进一步定位为 `ChallengeRequiredError`，要求浏览器验证。
已登录 Chrome 与本地访客请求不共享验证状态；自动保存与受保护入库的衔接仍未
打通。不再把逐篇手动下载作为后续批量方案。详情见[下载诊断](PUBLIC_SOURCE_ROUTES.md)。

小型成果：[贡献卡](../published/papers/OR_J4wRLmh29t/screening_001.json)、
[局部关系图数据](../published/graphs/P2_J4wRLmh29t_partial.json)。比较和背景引用
不计方法继承；作者自述的证明依赖保留未核读前作的限制。

## 当前工程验收与恢复

在唯一 `.venv` 补装官方 PyMuPDF 1.28.2 Windows wheel 后，本次重新运行完整
135 项测试：**133 通过、2 跳过、0 失败**，含四项真实强制进程中断后的恢复。
跳过的是既有 Windows 符号链接权限案例。活动代码/规则哈希匹配本次验收，
原 AGENTS.md 未变；未新增 API、插件或全局权限改动。

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py --help
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
```

本地下载索引：`reports/DOWNLOADED_PAPERS_20260926.md`；真实运行检查点：
`reports/P2_acquisition_20260926.json`；恢复交接：`reports/P2_HANDOFF.md`。
等待外部回复时没有 running 租约。实际返回保存后，独立复核导入命令为：

```powershell
& .\tools\python-project.cmd tools\workflow.py import-pro --review P2_J4wRLmh29t_independent_001 --file exchange/inbox/P2_J4wRLmh29t_independent_001_browser.json
```

下一依赖单元是回传对照 `P2_J4wRLmh29t_reconcile_001`，之后补版本和前作证据
`P2_J4wRLmh29t_evidence_gaps_001`；实际当前任务由状态文件和账本确定。
后续补充审读使用新 `P2_J4wRLmh29t_supplement_001`，不能改写旧包或旧任务哈希。

GitHub 同步以本地远端读回回执为准；正文、SQLite、原始交换包及机器日志留本地。
功能分支未合并 main，Git 推送认证和本地提交作者身份仍未实测。
一篇真实闭环验收前不扩大科学分析；P3/P4 未获授权。

## 历史检查点 — 2026-09-25

以下零正文、未导出和 acquire_005 未创建的状态是历史，旧“下一任务”不可重跑。
恢复只使用上方当前入口及账本。

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
