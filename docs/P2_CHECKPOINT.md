# P2 检查点

已完成两篇有明确限制的模型初筛闭环：Hedging 的65页当前附件、49页原稿和32页前作；
Foundations 的23页当前附件和30页前作。第二篇两个真实 Pro 对话各返回7项分析，
均经隔离导入、幂等核验和本地限定事实检查；贡献卡和局部证据图已生成。
两篇论文整体新意均为 U；第二篇仅对同条件有限置换群平均子机制保留局部覆盖判断。
人工审计/校准、完整证明认证和实验复现未做，账号记忆隔离未知。

十篇便利候选的官方主轨 spotlight 身份已分别核实；这不是会议总体。
当前本地12个PDF、9篇文献，其中3篇是目标论文；第三篇43页已抽取，真实 Pro 审读尚未开始。
第二篇原稿和所有正式 camera-ready 映射仍有缺口。四请求 API 下载已成功；扩展十篇清单
已通过本地验证，联网扩展尚未执行。正文、数据库和原始交换包留本地。

新增受目录/来源/代码版本约束的下载清单，最多10篇、20个精确PDF URL，失败即停。
修正前作误计入十篇目标上限的问题；未知和混合身份仍保守计入目标，前作升级目标也受限。
完整离线验收160项：158通过、2跳过、0失败，含四项实际中断恢复。
代码变化后已用新短任务重核目录及两篇结果；历史任务和 Pro 哈希没有改写。
P2继续逐篇推进，P3/P4未授权，未创建PR或合并main。

贡献卡：

- [Hedging](../published/papers/OR_J4wRLmh29t/full_text_001.json)
- [Foundations](../published/papers/OR_aIH1jyU37z/full_text_001.json)
- [十篇身份与来源](../published/catalog/P2_pilot10_identity.json)

当前新验收任务：`P2_J4wRLmh29t_loop_002`、`P2_aIH1jyU37z_loop_002`、`P2_catalog_pilot10_002`。
旧 Pro 返回和卡片的旧代码绑定保留；新任务核查来源字节和事实范围，不冒充新 Pro 返回。

恢复：`tools/python-project.cmd tools/workflow.py recover`，随后 `status`、`preflight`。
待运行清单：`tools/python-project.cmd tools/openreview_session.py --plan --reviewed-plan exchange/download_plans/P2_pilot10_20260926_v2.json`。
实际联网使用同参数加 `--run`，只在隐藏交互输入中临时使用凭据。
下一 review_id：`P2_wsA8LgHU5U_screening_001`，尚未导出。

文档/代码同步以本地远端读回回执为准，运行态与完整证据不上传。
