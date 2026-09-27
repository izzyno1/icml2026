# ICML 2026 当前恢复入口

唯一根目录为 C:\Projects\icml2026。先恢复事实与当前授权，不依赖旧聊天，不在备份或旧聊天目录重建。

读取顺序：README.md → 原 AGENTS.md → docs/PLAN_REVISION_20260927.md → PROJECT_SPEC.md → configs/project_policy.json → configs/rubric.json → docs/IMPLEMENTATION_STATUS.md → 本地 NOW.md 与最近任务检查点。

本次当前检查点是规划、验收与GitHub同步；它不授权新的模型调用或全量研究。只有收到明确研究启动指令才执行01_START_PROJECT.md。在已有启动授权范围内不要逐批重新询问。

在本机核对并顺序执行：

```powershell
Set-Location -LiteralPath C:\Projects\icml2026
.\tools\python-project.cmd tools\workflow.py --help
.\tools\python-project.cmd tools\workflow.py status
.\tools\python-project.cmd tools\workflow.py recover
.\tools\python-project.cmd tools\workflow.py preflight
```

代码/规则/测试报告哈希完全匹配才复用 state/offline_acceptance.json；不匹配完成必要验收，不改旧记录。NOW.md由账本生成，禁止手改任务状态。

已完成的计时任务 SCREEN_timing10_001 保留原报告和版本：exchange/SCREEN_timing10_001/RESUME.md。不要重跑其完成脚本，不覆盖计时或原始回答。历史三篇研究在 published/reports/P2_three_papers_20260926.md；published/status.json 是旧三篇时点快照，当前规划状态看 published/plan_checkpoint_20260927.json。

后续研究入口任务建议 SCREEN_production50_v2_001（规划名，尚未创建）；先检查是否存在，有则恢复不覆盖。DiReCT 新增审读也先查记录，不重复发送。五并发是外部目标，不是已实测能力；本地账本保持单写入。缺少模型/材料/额度时记录实际边界，其他已授权且不依赖它的工作继续。

GitHub沿用codex/g0-exchange。核对实际远端HEAD和同步回执，不把历史SHA当永久最新。只处理明确文件，不 git add .、不强推、不 reset --hard，不读或发布凭据、原始对话和运行库。

复用唯一.venv和现有工具。40/50GB及每卷30GB保护保持。报告完成/失败、当前版本、实际存储、下一就绪任务与准确恢复位置，不承诺会话关闭后的后台工作。
