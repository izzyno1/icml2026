# P2 检查点 — 2026-09-26

首篇模型初筛闭环已接收，P2整体尚未完成。当前12个PDF、9篇文献（3篇目标与6篇前作），
十条题录是便利候选，不能用于推断会议总体。

| 单元 | 实际状态 |
| --- | --- |
| Hedging 身份与版本 | 官方当前65页、原始投稿49页；定稿映射未知 |
| 首篇真实 Pro | 历史10项初筛、独立6项复核；新146页文本包返回8项 |
| 本地核对 | 8项限定原文/公式检查、版本对照、精确小例、三类证据边 |
| 恢复 | 新进程复核、幂等导入/接收、SQLite完整性通过；桌面重启未测 |
| 第二篇 Foundations | 23页正文及三篇前作30页已实际交Pro初筛 |
| 第三篇 Learning to Theorize | 官方当前43页已取得并核对首页身份，尚未科学审读 |
| 人类审计、校准、实验复现 | 未做 |

首篇记录 `P2_J4wRLmh29t_loop_001` 是有明确未知项的模型初筛闭环，不能解释成整篇
数学正确、历史首创或L0/L3裁定。贡献卡记录零边际回退反例、覆盖数中间公式反例、
尚未闭合的概率证明步骤和原稿/当前稿的适用范围差异；未把局部问题升级为全篇结论。
[贡献卡](../published/papers/OR_J4wRLmh29t/full_text_001.json)；
[证据图](../published/graphs/P2_J4wRLmh29t.md)。

首篇当前146页文本真实回传已通过格式检查。初次kind枚举错误原件留隔离区，Pro实际
重发仅改8个kind字段，其余解析值逐项相同。第二次导入new_reception=false。
原始返回、旧stale绑定与全部来源字节分别保留；未用本地模拟冒充。

第二篇review_id `P2_aIH1jyU37z_screening_001`，task_id
`P2_aIH1jyU37z_screening_task_001`；等待外部结果无running租约，返回后开本地短核验。
前作包含Ravanbakhsh2020、Maron2019 ICML正文/补充、Barbero2022。
Maron的ICML论文不等于其另一篇ICLR论文；后者及Bodnar2022等未取得部分仍记缺失。
第二、三篇原始投稿尚未取得，当前附件不能冒充投稿时版本。

最新完整离线验收150项：148通过、2跳过、0失败，4项实际进程中断恢复。
代码与规则未变，因此沿用同哈希验收回执并明确日期；论文事实核对另外记录。
磁盘由preflight实测，包括Git、交换包、分片及登记外部存储；40/50GB和每卷30GB保留规则继续执行。

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
# 实际第二篇返回件保存后：
& .\tools\python-project.cmd tools\workflow.py import-pro --review P2_aIH1jyU37z_screening_001 --file exchange/inbox/P2_aIH1jyU37z_screening_001_browser.json
```

原始PDF/SQLite/完整交换留本地。只同步审阅清单中的小型结果与代码，main未合并，未创建PR。
是否已上传以本地远端逐字节读回回执为准。P3/P4未授权，不承诺关闭会话后继续运行。
