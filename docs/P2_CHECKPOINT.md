# P2 检查点

已完成三篇有明确限制的模型初筛闭环：Hedging、Foundations、Learning to Theorize。
三篇共22项主张；当前整篇新意均为U。第三篇原稿40页、当前43页及LPN58页、NLI26页，
已交给两个独立开启的Pro对话并收到真实返回，完成本地证据核查、分歧登记和短验收。
独立Pro提出局部L2候选，本地因前作训练条件、版本和同条件对照缺口保留U。
人工审计、校准、完整证明认证和实验复现未做，账号记忆隔离未知。

本轮按用户要求在第三篇完成后汇总，未启动第四篇Pro。P2十篇试点尚未完成，P3/P4未授权。
十篇便利候选的官方主轨spotlight身份已逐项核实，20份当前/原始附件均已取得并核对题名。
文件库存为30个PDF、671个物理页、18篇文献（10篇目标、8篇前作），不代表全部已读或验收。
三篇已交审材料共366页文本，第二篇另取得的9页原稿未纳入其已完成的Pro版本对照；
所有canonical camera-ready映射仍未知。

现有离线基线160项：158通过、2跳过、0失败，含四项实际强制进程恢复。
本次仅核对报告和当前代码/规则哈希一致，未重复声称又运行160项。
目录旧代码绑定在第三篇验收前被拒绝，以P2_catalog_pilot10_003重新核查原来源字节，旧记录保留。
重复导入/重复接收未增加结果；新进程恢复和SQLite完整性通过，运行租约与待外部返回均为零。
正文、SQLite、原始Pro交换包留本地；未创建PR或合并main。

贡献卡：[Hedging](../published/papers/OR_J4wRLmh29t/full_text_001.json)、[Foundations](../published/papers/OR_aIH1jyU37z/full_text_001.json)、[Learning to Theorize](../published/papers/OR_wsA8LgHU5U/full_text_001.json)。
[三篇研究汇总](../published/reports/P2_three_papers_20260926.md) · [下载库存](../published/evidence/P2_download_coverage.json)。

当前闭环任务：`P2_J4wRLmh29t_loop_003`、`P2_aIH1jyU37z_loop_003`、`P2_wsA8LgHU5U_loop_001`。
当前目录重核：`P2_catalog_pilot10_003`，核查保存的来源字节和身份，未冒充重新抓取远端。
最新两份review：`P2_wsA8LgHU5U_screening_001`、`P2_wsA8LgHU5U_independent_001`均已格式验证，
事实由`P2_wsA8LgHU5U_factcheck_001`和闭环任务接受；旧格式任务的awaiting_fact_check不是仍在等外部返回。

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py --help
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
```

继续同一P2的计划下一task_id：`P2_reYe33OKVp_evidence_001`；review_id：`P2_reYe33OKVp_screening_001`。
本轮按用户要求停在三篇，未启动该审读。恢复时不盲目重建不可变包、不重跑旧下载清单，先核对账本。
同步仅在实际读回远端提交及文件字节后确认；活动库、正文和完整交换包留本地。
