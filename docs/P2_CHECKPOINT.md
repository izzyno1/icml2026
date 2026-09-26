# P2 检查点 — 2026-09-26

P2 未完成：2 篇目标论文有正文，3 篇前作有文件，共 7 个 PDF、5 篇文献；
真实论文闭环 0。十条题录是便利候选，总体数量未知。

| 文件 | 页数 | 来源和范围 |
| --- | --- | --- |
| Hedging 当前附件 | 65 | 官方 API 成功；与用户保存件哈希相同；camera-ready 角色未知 |
| Hedging 原始投稿 | 49 | 官方 originally_submitted_PDF；匿名版本，单独保留 |
| Foundations of Equivariant Deep Learning | 23 | 官方 API 当前附件；标题/作者核对，尚未科学分析 |
| Mansour 2021 正文 / 补充 | 12 / 4 | PMLR；首篇方法比较前作 |
| Mourtada 2023 | 2 | PMLR 扩展摘要；完整证明未取得 |
| Lecué–Rigollet 2014 | 14 | 作者站点期刊 PDF；题名/作者/DOI 核对 |

官方 API 登录已经实际成功。第四个 PDF 请求 wsA8LgHU5U 在传输中中断，保留
3,014,656 字节分片，不计完整对象。旧日志仅记录 LocalGuardOrProtocolRejected，
未确定具体保护原因。修正减少目录扫描开销并细分脱敏错误；没有关闭下载保护，
修正版尚未重新请求该 PDF。无需把逐篇手动下载作为后续方案。

首篇初筛 `screening_001` 真实返回 10 项，另一对话 `independent_001` 返回 6 项；
格式/来源/定位检查、重复导入及限定本地原文和数学核对均已落盘。首轮意见未提供
给第二轮，但账号记忆隔离未知。代码更新后两份旧包保留历史 stale，不改旧哈希。
`P2_J4wRLmh29t_evidence_gaps_001` 已在当前基线重新核对旧字节和新增版本身份，
这不是第三次 Pro 返回或全部科学结论重验。

新 `P2_J4wRLmh29t_supplement_001` 绑定提交
`d9cdef0a9da95fa2efaafee628ff7337f8ab2705`，包含首篇当前65页、投稿49页、
Lecué–Rigollet14页、Mansour12+4页、Mourtada2页，共146页可定位文本。
实际传递和回传状态由 published/status.json 与本地浏览器回执记录；不能用导出成功
冒充 Pro 已读。未提供原 PDF 像素和实验数据，Mourtada 全文及更广前作检索仍缺。

最新离线验收 **150 项：148 通过、2 跳过、0 失败**，含4项实际强制中断恢复。
规则和代码绑定当前离线报告；AGENTS.md 未改。人类审计、人工校准和实验复现均未做。
整体新意保持 U，不从便利样本推断总体；一篇真实闭环后才能扩展科学分析。

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
& .\tools\python-project.cmd tools\workflow.py status
& .\tools\python-project.cmd tools\workflow.py recover
& .\tools\python-project.cmd tools\workflow.py preflight
# 仅在实际返回件已保存后导入：
& .\tools\python-project.cmd tools\workflow.py import-pro --review P2_J4wRLmh29t_supplement_001 --file exchange/inbox/P2_J4wRLmh29t_supplement_001_browser.json
```

下一 task_id：`P2_J4wRLmh29t_supplement_task_001`，review_id：
`P2_J4wRLmh29t_supplement_001`；等待外部审读不持 running 租约。返回后新开短验收。
正文/SQLite/原始交换留本地。已授权功能分支同步，未请求创建 PR，main 未合并；
只有远端读回回执证实的文件称已上传。P3/P4 未获授权。
