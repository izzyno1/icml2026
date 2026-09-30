# 单轮全文初评与有界本地核对 11–20

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro011 · What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?

论文 OR_u1i3XoSXQG；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_u1i3XoSXQG_07db110af9bc", "source_url": "https://api2.openreview.net/pdf?id=u1i3XoSXQG\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_u1i3XoSXQG_07db110af9bc：物理页1–37全部所供文本，包括正文§1–8、页9–12参考文献、页13–37附录A–N及表格文本。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["题名匹配，物理页标记连续，未见缺页；仅阅读文本，未查看PDF图像。", "图1–5不可见；图4、5的逐epoch曲线数值不可核读，仅能记录作者文字描述。", "部分双栏文字、公式和表格排版串行；IR公式可结合文字辨认，但正文与附录存在不能自行消解的计算口径冲突。"]}

问题：轨迹SFT提高任务得分，究竟反映可迁移的工具语义能力，还是对训练接口的依赖？

方法：PIPE将动作名或调用标记换成同义词／无意义符号，改写展示文本并将新名回译给原后端；严格拒绝旧名。另让原名与同义别名同时有效，交换展示顺序评测两次。IR以α平滑逐任务调用比率，再取几何均值。

作者主张：提出保持任务语义的PIPE，分离原基准分数中的接口捷径成分。

论文证据：覆盖AgentBench六个、AgentGym十个环境设置，比较原接口与两种扰动，并提供难度判断和行为对照。

模型推断：形成有价值的接口鲁棒性评测；尚不是严格识别潜在语义能力的因果分解。

定位：['TEXT_OR_u1i3XoSXQG_07db110af9bc：页4–6，§4、表1–3；页25–27，表27–29。']

作者主张：IR量化训练接口偏好，并缓解展示顺序及极端调用比率的影响。

论文证据：表4、5及13–18报告双别名评测和α敏感性。

模型推断：属于有用的局部诊断指标；偏好不等于依赖，IR接近1也不证明语义理解。

定位：['TEXT_OR_u1i3XoSXQG_07db110af9bc：页8，§6；页18–19，附录F–H。']

作者主张：任务特定SFT可放大接口依赖，其训练动态随环境变化，并可通过接口多样化缓解。

论文证据：同型号SFT前后出现更大扰动损失和更多旧名调用；§7文字报告部分非单调恢复，附录N提供探索性增广实验。

模型推断：支持语义能力提升与接口脆弱性并存，不支持SFT只学接口或必然损害泛化。

定位：['TEXT_OR_u1i3XoSXQG_07db110af9bc：页6，表3；页9，§7；页18，表10；页28、36–37，附录N及表44–45。']

key_results：[{"setting": "AgentGymPlus／SciWorld，Qwen3-8B，测试200项；依次为原接口、同义扰动、符号扰动。", "baseline": "同型号任务特定SFT前。", "metric_or_guarantee": "Reward，采用论文表中分值；不是成功率。", "reported_values_and_units": "训练前60.08／55.28／50.80；训练后86.16／67.11／59.50。表列平均扰动变化分别为−7.04、−22.86分。", "information_and_compute": "该环境列2120条训练轨迹。附录K对Qwen3-8B报告全参SFT、Adam学习率1e−5、ZeRO-3、bf16、默认1epoch；GPU数量和耗时未报。", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页6表3、页16表9、页21附录K、页33表26。\n"}, {"setting": "AgentBenchPlus／WebShop，AgentLM-70b。", "baseline": "同模型原接口；不是同底座训练前后对照。", "metric_or_guarantee": "任务Reward；另列双别名协议的无量纲IR。", "reported_values_and_units": "原接口50.2，同义扰动2.33，符号扰动0；但双别名IR为0.93。两种诊断不能直接等同。", "information_and_compute": "使用既有轨迹训练模型；性能扰动严格拒绝旧名，IR评测则允许两种别名。", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页5表1、页8表4。\n"}, {"setting": "AgentGymPlus／SciWorld，Gemma3-4b，SFT前后。", "baseline": "未接受该任务轨迹SFT的同型号模型。", "metric_or_guarantee": "IR；严格扰动下的旧接口调用次数／任务。", "reported_values_and_units": "IR：0.88→7.69。旧名调用：同义扰动0.15→13.22，符号扰动0.01→14.27次／任务。均为作者报告，IR数值存在下述一致性疑点。", "information_and_compute": "IR采用α=1和两种展示顺序；Gemma专属完整训练配置未明示。", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页8表5、页18表10。\n"}, {"setting": "gpt-5.1对原／同义／符号接口任务说明作难度判断。", "baseline": "原接口任务说明。", "metric_or_guarantee": "平均总体难度，1–5分。", "reported_values_and_units": "AgentBenchPlus：2.44／2.43／2.54；AgentGymPlus：3.64／3.66／3.70。", "information_and_compute": "评价假定智能体能够理解动作说明；这是模型判断，不是实际执行难度等价证明，API成本未报。", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页5，§4.2、表2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Fu, D., He, K., Wang, Y., Hong, W., Gongque, Z., Zeng, W., Wang, W., Wang, J., Cai, X., and Xu, W. Agentrefine: Enhancing agent generalization through refinement tuning. arXiv preprint arXiv:2501.01702, 2025.", "identifier_if_present": "arXiv:2501.01702", "relation_candidate": "背景引用", "shared_component": "接口微扰下轨迹模型的脆弱性问题。", "claimed_difference": "本篇从改进训练转向评测归因与量化诊断。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页2，§2.1；页10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Chen, Z., Liu, K., Wang, Q., Zhang, W., Liu, J., Lin, D., Chen, K., and Zhao, F. Agent-flan: Designing data and methods of effective agent tuning for large language models. arXiv preprint arXiv:2403.12881, 2024.", "identifier_if_present": "arXiv:2403.12881", "relation_candidate": "比较基线", "shared_component": "轨迹调优及格式遵循与推理的区分。", "claimed_difference": "本篇用接口干预重评；未对Agent-FLAN训练设计作因果消融。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页7，§4.3；页10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Zeng, A., Liu, M., Lu, R., Wang, B., Liu, X., Dong, Y., and Tang, J. Agenttuning: Enabling generalized agent abilities for llms. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 3053–3077, 2024.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "AgentInstruct轨迹及AgentLM模型。", "claimed_difference": "从原接口能力提升转向跨接口鲁棒性和训练动态诊断。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页4，§4.1；页12参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "跨环境干预、训练前后比较和旧名调用统计提供实质评测知识，超过单场景性能改进；但不足以认定路线级首创。", "central_increment": "前作已讨论接口脆弱和格式过拟合（仅据本篇转述）；本作增加可复用PIPE及双别名诊断，展示部分训练收益不能跨接口保持；尚待排除提示改写混杂和统计错误。", "soundness_observation": "性能退化与旧名调用证据相互支持；IR定义和数字的一致性缺陷明显限制量化解释。", "significance_observation": "有助于避免将固定接口优化误读为通用能力；工程价值在跨环境评测封装，而非新训练算法。", "main_open_question": "IR异常来自标签、聚合实现还是表格记录，修正后是否仍支持训练接口偏好及其动态解释？"}

limitations：[{"text": "部分联网环境被排除；IR仅测AgentBench五个、AgentGym六个环境，后者依据旧接口调用较多而选择，并非全部16个设置的无偏覆盖。", "basis": "author_report", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页8脚注2–3、页15附录C.2。\n"}, {"text": "后端等价不保证模型适配难度等价。表21连TextCraft功能说明中的词也替成z标记，故不能直接接受完整功能描述保留的前提；LLM难度判断不能排除此混杂。", "basis": "model_inference", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页33，表21。\n"}, {"text": "§6先平均两次运行的计数再取log；附录F先算各次log再平均，通常不等价。表12与17又称同设置，却给Gemma3-4b／SciWorld／α=1的算术均值0.25、几何均值7.69；若来自同组比率则违反算术均值不小于几何均值，不能仅归因于异常值。", "basis": "model_inference", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页8§6、页18式2–3、页30表12、页32表17。\n"}, {"text": "未报告主要性能结果的多种子区间；增广实验缺同表0%基线及固定总训练量说明，表45收益并非单调，不能把接口多样性视为已确立的普遍修复。", "basis": "model_inference", "locator": "TEXT_OR_u1i3XoSXQG_07db110af9bc：页21附录K、页28附录N、页36–37表44–45。\n"}]

minimal_check：{"question": "表12与表17能否由同一批双别名调用日志复现？", "control": "固定Gemma3-4b／SciWorld、任务集合、两种展示顺序、ori/syn标签及α=1，分别按正文和附录口径计算，并在同一比率集合上比较算术与几何均值。", "observable_outcome": "确定实际聚合实现，复核0.25、7.69及SFT前后偏好方向。", "resources": "作者逐任务调用计数及对应运行日志、普通CPU；无需重新训练。原始日志未提供。", "failure_or_stop_condition": "缺日志则停止核证；统一口径后无法复现表值或训练效应消失，则IR量化解释未通过。"}

missing_fields：["图像及逐epoch精确数值。", "原始日志、代码、前作全文、最终版本身份。", "逐模型完整配置、解码与随机种子、GPU型号及卡数、训练推理耗时、API成本。", "IR实际聚合口径；AgentLM-14b与AgentLM13b名称对应关系。", "prior_work_candidates[2].identifier_if_present：参考条目未列独立标识符。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

接口扰动对照值得读；优先统一IR定义、审计功能说明是否等价，再解释训练依赖程度及修复收益。

题名版本范围：首物理页题名和绑定ID一致，官方当前37页附件全文输入完整核验，Pro声明全部文本已读且未见图像，范围与实际一致。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro011_attachment_preview_full.txt；pass_with_version_limit

中心评测与IR差别：§3.2将动作名称改为同义名或符号，声称保持可执行后端、任务和观察；§6双别名实验则让原名与同义名都有效，并平衡展示顺序。严格扰动下的适配失败与同时有效时的调用偏好是不同问题，IR≈1不能独自证明语义鲁棒。

核查定位：p003:L0050-L0068, p008:L0029-L0056；protocol_distinction_confirmed

训练收益与脆弱性并存：原PDF Table3的Qwen3-8b/SciWorld训练前原/同义/符号60.08/55.28/50.80，训练后86.16/67.11/59.50；平均扰动损失由7.04变22.86分，但扰动后的绝对Reward仍提高。Table10确认Gemma3-4b旧名调用同义0.15→13.22、符号0.01→14.27次/任务。不能由更大相对损失推出训练完全没有增加能力。

核查定位：p006:Table3, p018:Table10, local_check/p006.png；reported_values_match_nonexclusive_interpretation

IR聚合定义冲突：正文先平均两次运行的原/同义计数再取log比；附录F先分别算log均值再跨顺序平均。比值与log非线性，两者一般不等价，本文未交代实际实现采用何者。

核查定位：p008:L0052-L0056, p018:L0054-L0069；definition_order_difference_confirmed

算术/几何表格的可比性：原PDF Table12在α=1、TrajSFT Gemma3-4b/SciWorld印算术均值0.25；Table17印几何IR7.69。§G称同实验设置，所印公式若作用于同一组正比值应满足算术≥几何，故两表无法在这一解释下兼容。鉴于上述聚合顺序也不一致，不能仅凭表格确定哪项数字或标签错误，需逐任务日志确认实际计算对象。

核查定位：p018:Eq4, p019:L0037-L0040, p030:Table12(b), p032:Table17, local_check/p030.png, local_check/p032.png；conditional_incompatibility_confirmed_root_cause_unknown

本地补充/限定：[{"kind": "qualification", "detail": "AM–GM疑点必须带同一组比值的条件；两种聚合顺序本来不同，不能直接把它说成已证明实现违反数学不等式。"}]

核查局限：["未获得双别名调用日志，未复算全部IR或多种子区间。", "Pro指出TextCraft说明改写可能丢失语义，本地未全面审计该问题，不能声称整个扰动设计不等价。", "未执行环境、训练或作者代码；前作仍仅为候选关系。"]


## pro012 · CIRBench: Evaluating Large Language Models as LLVM IR Optimizers

论文 OR_D1ahrfGJ5e；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_D1ahrfGJ5e_24293ad7974f", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_D1ahrfGJ5e_24293ad7974f：物理页1–54全部所供文本，包括正文、参考文献、目录及附录A–Q；页标连续，未发现整页缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；所有插图不可见。表1、表3部分列与公式排版失真，未恢复不可辨认的图表数值。", "附录M.1的-O3函数正文明确省略；评测工件、原始日志及前作全文未提供。当前附件身份未核验，不认定为最终出版版。"]}

问题：LLM能否直接分析、修复和优化LLVM IR，在保持语义的同时获得真实运行时收益？

方法：将既有程序编译、切片、归一化并筛选，构建四赛道。Analysis输出JSON；Repair修复注入错误；Refactor执行或识别单个pass；Transform自由改写。先验LLVM结构合法性，再用Alive2确定性裁决，否则回退执行哈希测试；NOT-EQ不能被测试覆盖。仅对通过者测时，区分直接编译与追加-O3。

作者主张：提供覆盖四类编译职责的正确性感知基准及标准化开源工具链。

论文证据：含100例Analysis、200例Repair、200例Refactor、300例Transform；附录给出提示、注错、筛选和评测流程。

模型推断：本篇所述前作已有IR数据与优化验证，本作新增跨任务的统一诊断能力，而非新优化算法或等价性证明方法。

定位：['TEXT_OR_D1ahrfGJ5e_24293ad7974f：p4 §3.1；p17–42 B–H。\n']

作者主张：揭示被测LLM的IR理解、语义可靠性与性能优化之间的差距。

论文证据：六主模型及三补充模型存在Valid–Equiv差距；两个CPU后端的动态速度中位数均未超过-O3，偶有大幅加速。

模型推断：支持将模型视为待验证的候选生成器；不能证明分析错误导致优化失败，附录也承认相关性检查不确定。

定位：['TEXT_OR_D1ahrfGJ5e_24293ad7974f：p8–9 表4–5；p44 表10–11；p51 O；p54 表21。\n']

key_results：[{"setting": "100例Analysis，GPT-5。", "baseline": "LLVM分析oracle。", "metric_or_guarantee": "规范化EM与micro-F1。", "reported_values_and_units": "作者报告EM=70%、F1=84.0%；EM的95% bootstrap区间为70±9个百分点。", "information_and_compute": "表13另报GPT-5整套k=5评测2689次调用、35.62M tokens、约212美元；不是Analysis单独成本，也不是现价。", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p45 表13；p46 表14。\n \n"}, {"setting": "200例Repair及200例Refactor-Normal，GPT-5。", "baseline": "Repair-Hard对照Hint；Refactor参照指定pass输出。", "metric_or_guarantee": "Equiv@1/5与Refactor EM@1/5。", "reported_values_and_units": "Repair-Hint为85.5%/92.0%，Hard为74.0%/87.0%；Refactor为22.5%/29.5%，EM@1/5均为0%。", "information_and_compute": "Hint额外提供验证器错误及位置；生成预算k∈{1,5}。", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p8 表4。\n"}, {"setting": "GPT-5 Transform：全部300例与单函数子集分别统计。", "baseline": "混合语义判据与仅Alive2认证判据。", "metric_or_guarantee": "Valid@1、Equiv@1/5、Equiv_formal@1/5。", "reported_values_and_units": "全集Valid@1=80.6%，Equiv@1/5=73.3%/92.7%；单函数子集Equiv_formal@1/5=40.8%/48.3%。分母不同，不能直接相减解释误判率。", "information_and_compute": "formal统计将不等价、超时、unknown和不支持均计失败；混合判据仅对不确定结果回退测试。", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p8 表4；p37 F.8、表8。\n \n"}, {"setting": "六主模型、AMD Ryzen 9 7950X，语义检查通过的Transform候选。", "baseline": "同工具链-O3。", "metric_or_guarantee": "动态运行时间加速比。", "reported_values_and_units": "GPT-5的Direct/Copilot中位数为0.85×/0.99×；主实验最大4.96×属于Deepseek-V3.2-Exp Direct，其中位数为0.90×。", "information_and_compute": "LLVM 19.1.0；单线程、固定频率和绑核；每binary运行10次取平均。速度表如何选择多个候选未明确。", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p9 表5；p37 F.7。\n \n"}, {"setting": "九模型补充实验，Intel Core i9-11900K。", "baseline": "该后端-O3。", "metric_or_guarantee": "动态加速比。", "reported_values_and_units": "Direct中位数范围0.41–0.83×，Copilot为0.90–0.96×；Llama 4 Maverick Direct最大8.17×，故4.96×不是全文所有设置的最大值。", "information_and_compute": "作者称沿用主实验编译参数及计时协议。", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p53–54 Q、表21。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Yang, Z., Qiu, L., Lyu, F., Zhong, M., Chai, Z., Zhou, H., Cui, H., and Feng, X. Ir-optset: An optimization-sensitive dataset for advancing llm-based ir optimizer. Advances in Neural Information Processing Systems, 38, 2026.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "IR来源、pass选择及归一化工具链约定。", "claimed_difference": "新增四赛道与统一分层验证和性能评测。", "basis": "target_paper_only", "target_locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p4–5 §3；p27 D.3；p12参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Jiang, H., Zhu, J., Wan, Y., Fang, B., Zhang, H., Jin, R., and Guan, Q. Can large language models understand intermediate representations in compilers? In Forty-second International Conference on Machine Learning, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "直接评估LLM对编译器IR的理解。", "claimed_difference": "本作扩展至修复、受控pass改写及性能变换；具体覆盖仍需核读前作。", "basis": "target_paper_only", "target_locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p16 A.1；p10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Taneja, J., Laird, A., Yan, C., Musuvathi, M., and Lahiri, S. K. Llm-vectorizer: Llm-based verified loop vectorizer. In Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization, pp. 137–149, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "经验证的模型生成优化与性能评测。", "claimed_difference": "表1作功能覆盖比较，非同预算实测对赛；CIRBench不限于循环向量化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p2 表1；p12参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可执行、跨编译职责的统一评测能力，而非验证器或优化算法首创；暂不足支持路线级L3判断。", "central_increment": "在既有IR资源上新增四赛道任务、统一接口及正确性与性能分离的比较。", "soundness_observation": "主表支持可靠性不足的描述，但混合验证不是全输入保证；附录示例存在可核对的oracle矛盾，实际标签尚未审计。", "significance_observation": "对IR助手诊断有价值；工程工作集中于切片、注错、语义验证和稳定测时，不能据此认定具备生产编译器替代能力。", "main_open_question": "附录N.2的oracle错误是否只是非测试示例的写作失误，还是同类错误进入真实标签并影响模型排序？"}

limitations：[{"text": "作者承认checksum回退不是证明、未系统审计预训练污染，且Challenge富集高优化潜力样例；结论不能外推为一般工作负载上的收益保证。", "basis": "author_report", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p34 F.2；p37 F.8；p43 I。\n \n"}, {"text": "N.2把可见的2条load写成4条，把回边源body写成loop，并仅凭参数不同判NoAlias。N明确不属测试集，不能由此断言全部数据错误，但足以要求标签审计。", "basis": "model_inference", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p49–50 N.1–N.2。\n \n \n"}, {"text": "Refactor原输入已与参考输出等价，恒等回传亦可满足Equiv；该指标本身不证明执行指定pass。EM则只度量规范化后的精确匹配。", "basis": "model_inference", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p26 D.2；p51 N.3。\n \n"}, {"text": "作者称预算匹配，但多数输出上限使用提供商默认值，表13调用数不同；严格等预算尚未得到说明。过滤后速度统计也缺少共同实例分母和候选选择细节。", "basis": "model_inference", "locator": "TEXT_OR_D1ahrfGJ5e_24293ad7974f：p44–45 K、表12–13；p37 F.7。\n \n"}]

minimal_check：{"question": "附录示例暴露的oracle问题是否进入真实Analysis评测集？", "control": "固定LLVM 19.1.0和原分析配置，重新生成100例Analysis标签，对照发布JSON；N示例只作不计分回归检查。", "observable_outcome": "记录标签不一致率与类型，重点检查load计数、loop latch和alias标签。", "resources": "实际IR、原标签、分析配置及LLVM工具链；无需LLM调用，CPU耗时未报告。", "failure_or_stop_condition": "发现实际标签错误即暂停沿用相关排名；缺工件或关键配置则停止，不能以示例错误推算整集错误率。"}

missing_fields：["实际评测工件和逐候选日志未附，无法复核标签、失败计数及分母。", "Alive2资源和展开参数、哈希容差具体数值、Transform候选选择规则、整套CPU耗时未明确报告。", "所列前作条目无DOI或arXiv标识；未核读前作、未搜索网页、未执行代码或复现实验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

统一IR评测值得继续读；使用排名前应核查真实Analysis标签，采用优化建议时需区分验证器、形式证明与有限执行测试。

身份版本与范围：首物理页题名匹配；官方当前附件和54页全文输入绑定。Pro声明全部正文附录文本已读、图像未见，与实际材料相符；版本仍为当前附件，非已确认定稿。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro012_attachment_preview_full.txt；pass_with_version_limit

中心统一评测与正确性口径：p4明确100 Analysis、200 Refactor、200 Repair、300 Transform。F.8的Equiv为混合语义守卫：Alive2有确定结论则采用，只有超时/unknown/unsupported等才回退checksum；明确not-eq不被测试覆盖，且checksum通过不是证明。Pro把形式认证子集与全部300例分母区分正确。

核查定位：p004:L0026-L0038, p037:L0025-L0043；counts_and_layered_validation_confirmed

决定性性能值与条件：原PDF Table5的perf列确认GPT-5 Direct/Copilot中位数0.85×/0.99×，Deepseek-V3.2-Exp Direct最大4.96×、中位0.90×；不能将llvm-mca预测列当运行时间，也不能用最大值代替典型收益。p6为LLVM19.1.0与AMD7950X，F.7明确绑核、固定频率、每实例10次平均；均为作者报告。

核查定位：p006:§4.1, p009:Table5, p037:L0011-L0022, local_check/p009.png；values_column_mapping_and_timing_scope_checked

示例oracle疑点及边界：p49明确附录N示例不在评测集。印出的函数只有p50两条load，回到header loop的边来自body；N.2却写四条load及loop为latch。原PDF确认不是提取丢行。函数两个指针参数没有不相交契约，不能仅因参数不同推出NoAlias；LLVM19.1官方参考也明确允许同一指针传给两个参数。这些问题只验证到演示例，不能推算100个实际Analysis标签错误率。

核查定位：p049:L0044-L0063, p050:L0004-L0039, local_check/p050.png, local_check/llvm_reference.json, https://releases.llvm.org/19.1.0/docs/LangRef.html#parameter-attributes；illustrative_errors_confirmed_real_dataset_not_audited

形式认证结果：F.8 Table8单函数子集GPT-5的formal@1/@5为40.8%/48.3%，不可与全集混合Equiv率直接相减解释误判概率；资源限制导致的未证明不等价于错误。

核查定位：p037:L0037-L0054；formal_denominator_and_unknown_status_checked

本地补充/限定：[]

核查局限：["没有编译或执行示例、安装LLVM、重跑Alive2或重测性能；结论仅为可见材料的有限核对。", "未查实际800例数据、预训练污染、第二CPU结果或全部成本表；未核读前作全文。", "演示例缺陷不等于实际评分集已被证明错误，Pro的L2为暂定贡献判断。"]


## pro013 · Disentangling Geometry, Performance, and Training in Language Models

论文 OR_kNb6NNhKgE；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_kNb6NNhKgE_1d1b04932df1", "source_url": "https://api2.openreview.net/pdf?id=kNb6NNhKgE\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_kNb6NNhKgE_1d1b04932df1：物理页1–9，摘要、正文§1–6及影响声明", "TEXT_OR_kNb6NNhKgE_1d1b04932df1：物理页9–15，参考文献", "TEXT_OR_kNb6NNhKgE_1d1b04932df1：物理页16–29，附录A.1–A.5、B、C，表1–16及全部图注"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["29页文本标记齐全，未见缺页；未提供PDF图像。图1–31仅有图注和部分坐标文字，不能核验散点、曲线或读出图上数值。", "双栏文字局部交错，公式1–3的排版与符号有损；表格多数可逐行读取，但表文冲突不能自动校正。", "未提供前作全文、其他版本、原始实验记录或代码；不确认该附件为最终出版版。"]}

问题：输出映射W及末token末层表示H的几何指标，能否跨任务、规模和训练设置预测性能；低有效秩是否解释小模型晚期退化？

方法：作者报告预训练108个OLMo-style模型，规模标记为4–75M，使用Pile的8–128B tokens；改变batch size、weight decay、学习率及衰减。计算归一化奇异值熵的指数作为有效秩，并比较其他几何指标与ID/OOD、微调、遗忘和量化后的loss；使用残差/偏Spearman及五折验证增量R²。

作者主张：有效秩主要反映训练选择，不能作为可靠的跨设置性能代理。

论文证据：跨超参存在高秩低性能及低秩较好性能的反例；表3–4中R(W)与loss的原始相关较强，控制超参后显著减弱，增量预测R²为负。

模型推断：提供了对几何代理适用边界的实质经验澄清，不等于证明几何完全没有预测信息。

定位：['TEXT_OR_kNb6NNhKgE_1d1b04932df1:p4–8, §3–5; p20–21, Tables 3–4']

作者主张：低有效秩并非小模型饱和的原因，而是共现现象。

论文证据：正文报告Pythia-14M晚期loss恶化伴秩骤降，而匹配配置的OLMo-14M没有退化；8B tokens、batch size 32的OLMo-14M虽低秩仍未退化。

模型推断：反例否定低秩是饱和的充分条件，但不能据此否定其必要性或条件性因果作用。

定位：['TEXT_OR_kNb6NNhKgE_1d1b04932df1:p4–5, §3.2, Figure 5。\n']

作者主张：更换几何指标或改测H，仍不能可靠预测下游性能。

论文证据：正文报告W与H的几何变化不同；附录扩展至IsoScore、架构和语料变化，但表7–8仍显示R(H)具有任务依赖的预测增益。

模型推断：支持区分测量对象与评测任务，而非将所有指标统一判为无信息。

定位：['TEXT_OR_kNb6NNhKgE_1d1b04932df1:p8–9, §5; p24, Tables 7–8; p27–28, A.4–A.5']

key_results：[{"setting": "108模型套件；Pile-10K ID及Dolma-100 Code OOD loss", "baseline": "偏相关控制训练超参；预测基线包括模型规模、compute和token数", "metric_or_guarantee": "R(W)的原始/偏Spearman与五折增量R²", "reported_values_and_units": "ID：ρ=-0.699→-0.130，ΔR²=-0.003；OOD：ρ=-0.672→-0.127，ΔR²=-0.004，均无量纲。原始相关标为p<0.05，偏相关未标显著。", "information_and_compute": "作者报告预训练约3000 GPU小时；GPU型号与逐实验成本未报告。数值为作者报告，未本地复现。", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p9, Impact Statement; p20–21, Tables 3–4。\n \n \n"}, {"setting": "末checkpoint分别微调于StarCoder-Python和OpenWebMath", "baseline": "不含几何指标的预测基线", "metric_or_guarantee": "微调loss的增量R²", "reported_values_and_units": "R(W)：-0.003/-0.002；R(H)：0.071/0.030，依次对应两个数据集，均无量纲。", "information_and_compute": "batch size 32；微调token数和步数未报告。表7报告mixed-effects系数，不能将其当作偏相关与表8直接比较。", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p16, A.1; p24, Tables 7–8。\n \n"}, {"setting": "GPTQ后在Pile-10K及Dolma-100 Code评估", "baseline": "控制训练超参的关联分析及不含几何指标的预测基线", "metric_or_guarantee": "R(W)与量化后loss的偏Spearman及增量R²", "reported_values_and_units": "ID：偏ρ=-0.210，ΔR²=0.006；OOD：偏ρ=-0.223，ΔR²=0.018；偏相关均标为p<0.05。", "information_and_compute": "未报告量化位宽、校准集与预算；该结果针对量化后loss，不等同于量化造成的独立损失增量。", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p22–23, Tables 5–6。\n \n"}, {"setting": "OLMo-4M输入/输出embedding绑定消融", "baseline": "untied embeddings", "metric_or_guarantee": "ID loss与有效秩百分比", "reported_values_and_units": "tied：loss 6.78、有效秩56.15%；untied：loss 6.68、有效秩48.65%。更高有效秩未带来更低loss；loss对数底未注明。", "information_and_compute": "附录补充实验；独立重复和该对照的完整训练预算未说明。", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p28, A.5, Table 15。\n"}]

prior_work_candidates：[{"citation_as_printed": "Godey, N., de la Clergerie, É. V., and Sagot, B. Why do small language models underperform? studying language model saturation via the softmax bottleneck. In First Conference on Language Modeling, 2024b.", "identifier_if_present": "OpenReview:MoitXWlXcS", "relation_candidate": "反驳", "shared_component": "输出矩阵低秩与小模型饱和的联系", "claimed_difference": "本作提供OLMo低秩但不退化的反例，收窄因果解释；并非已核实推翻前作全部结论。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p1–2, §1; p11, References", "prior_actually_read": false}, {"citation_as_printed": "Diehl Martinez, R., Lesci, P., and Buttery, P. Tending towards stability: Convergence challenges in small language models. Findings of the Association for Computational Linguistics: EMNLP 2024, pp. 3275–3286, 2024b.", "identifier_if_present": "10.18653/v1/2024.findings-emnlp.187", "relation_candidate": "背景引用", "shared_component": "有效秩、收敛及小模型性能", "claimed_difference": "保留总体相关趋势，但新增多超参、跨任务反例和条件统计。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p2–3, §1–2; p10, References", "prior_actually_read": false}, {"citation_as_printed": "Machina, A. and Mercer, R. Anisotropy is not inherent to transformers. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 4892–4907, June 2024.", "identifier_if_present": "10.18653/v1/2024.naacl-long.274", "relation_candidate": "组件复用", "shared_component": "余弦相似度、isotropy及权重/表示几何分析", "claimed_difference": "本作系统比较指标受训练设置影响的程度及跨任务预测价值。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p8, §5; p12, References", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是受控实验揭示几何代理的适用边界，而非简单复现或新算法包装；属于实质经验认识，但尚非路线级框架。", "central_increment": "前作将Pythia低秩与退化联系起来（仅本篇转述）；本作在多超参OLMo小模型中新增反例与条件统计，显示这种联系不能直接跨设置推广。", "soundness_observation": "弱化代理指标的结论有支持；排除因果关系的措辞过强。统计表文及训练配置冲突降低精确结论的可信度。", "significance_observation": "对几何诊断、模型选择和小模型训练有实际参考价值；108模型实验有工程投入，但未建立大模型普适机制。", "main_open_question": "核清训练配置和统计口径后，R(W)在留出训练配置上的增量预测价值是否仍接近零？"}

limitations：[{"text": "作者承认仅研究小模型与末层表示，微调超参大多固定，结果属于观察性而非充分因果识别；每规模仅18个观察、4–5个控制变量，且小模型更常处于过大batch区间。", "basis": "author_report", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p29, Appendix C, Table 16。\n"}, {"text": "token预算实验同时改变batch size；固定token数改变batch又会改变优化步数，且学习率未随batch重新调优，不能将差异解释为单一因素的纯效应。", "basis": "model_inference", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p6–7, §4.1; p16, Table 2"}, {"text": "表3中I(W)的ΔR²为0.029，与旁文0.002–0.004及低于0.5%的概括冲突；表3/11的R(W)偏相关分别为-0.130/-0.261，未说明口径差异，不能择一当作已核实结果。", "basis": "model_inference", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p20, Table 3及旁文; p27, Table 11。\n \n"}, {"text": "§3.1及表2的weight decay含0.5，图例写0.05；学习率倍率分别写0.1/10/100和1/0.1/10；表1与表2的默认衰减终值也不同。这些可能是笔误或提取问题，本轮不能纠正。", "basis": "model_inference", "locator": "TEXT_OR_kNb6NNhKgE_1d1b04932df1:p3, §3.1; p4, 图例; p16, Tables 1–2"}]

minimal_check：{"question": "控制训练配置后，R(W)缺乏增量预测价值能否复现？", "control": "核对逐模型配置和表3/11控制集；按唯一训练配置分组五折，对比相同超参基线与加入R(W)的预测器，所有拟合仅使用训练折。", "observable_outcome": "各折ΔR²及不确定区间，并检查默认配置重复是否影响结果。", "resources": "逐模型指标、配置/种子及回归脚本；可做CPU统计分析，不需重训，具体耗时未知。", "failure_or_stop_condition": "无法确认配置和控制集则停止数值比较；若加入R(W)产生稳定留出增益，应收缩无额外预测力的结论。"}

missing_fields：["图像及图上原始数据", "随机种子、独立重复与默认配置重复的处理方式", "微调token数/步数、H采样与测量时点", "GPTQ位宽、量化范围及校准预算", "GPU型号、逐实验及微调/评测成本", "超参数冲突、统计表文差异与回归实现的澄清"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

对使用几何指标作诊断和模型选择有实质参考价值；继续读控制变量、验证划分及反例条件，优先核清配置和表文冲突后再使用精确统计。

身份版本和全文范围：题名、paper/review ID、材料哈希匹配，官方当前附件29页，Pro声明全部提供文本已读并保留图像/排版局限。原文说明6规模各18配置，共108模型。

核查定位：first_page_text.txt, text_delivery_manifest.json, p016:Table2 caption；pass_with_version_limit

中心反例与因果边界：原PDF Figure5与p5文本显示Pythia-14M晚期loss恶化伴秩下降；另一个8B-token、batch32的OLMo-14M低秩仍未恶化。它足以反驳低有效秩必然带来饱和的充分条件说法；因架构、预算和动态同时不同，不能排除所有条件性因果作用或必要性。

核查定位：p005:L0003-L0033, p005:Figure5, local_check/p005.png；counterexample_supported_scope_narrowed

R(W)的核心统计：原PDF Table3确认ID原始ρ−0.699、偏ρ−0.130、预测ΔR²−0.003；Table4为OOD−0.672、−0.127、−0.004。原始相关与控制后关联不同，负增量R²也不是因果证明；只是该预测协议中加入指标没有改善留出拟合。

核查定位：p020:Table3, p021:Table4, local_check/p020.png；values_match_conditional_statistical_interpretation

不能把所有几何指标说成无信息：Table3的Isotropy I(W)增量R²为0.029，旁文却概括0.002–0.004且额外解释率<0.5%，原PDF确认表文不一致。p24的微调表中R(H)增量0.071及0.030也与R(W)接近零不同。应保留指标、测量对象与任务条件，不能作全称无用结论。

核查定位：p020:Table3 and adjacent text, p024:Tables7-8, local_check/p020.png；published_table_text_conflict_and_object_specificity_confirmed

本地补充/限定：[]

核查局限：["未独立重算108模型统计，未确认全部训练超参冲突或所有量化设置。", "图中仅作趋势与标签核验，未从曲线回读未报告的精确值。", "没有大型模型外推、前作全文核读或实验复现；L2为Pro暂定判断。"]


## pro014 · MetaOthello: A Controlled Study of Multiple World Models in Transformers

论文 OR_0wPUeZOZ9o；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763", "source_url": "https://api2.openreview.net/pdf?id=0wPUeZOZ9o\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_0wPUeZOZ9o_b8c9f83d0763：物理页1–9，正文§1–7、致谢与Impact Statement。", "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763：物理页9–10，参考文献。", "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763：物理页11–16，附录A–C.1及图8–12的可抽取文字。全部16页文本已读，页标记连续；不代表读取了原始图像。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–12图像未提供；曲线、误差条及图12密集格点的对应关系不能可靠核验，不据零散图形标签补数值。", "双栏阅读顺序、公式上下标及表1部分行错位；仅使用对应关系明确的正文、题注和表格报告。", "未提供前作或其他版本，当前附件的出版版本身份未核定。"]}

问题：同一Transformer如何共享并仲裁相同棋步语法下互相冲突的规则与棋盘状态？此处world model指可重构潜在状态的内部表征，不是强化学习中的显式前向动力学模型。

方法：构造8×8游戏：NoMidFlip改变翻子规则，DelFlank改变初始化、合法性与删除规则，Iago置换token映射。以棋步序列训练单游戏及双游戏GPT，再用棋盘/game-ID线性探针、正交对齐、分量消融和steering分析状态及下一步预测。

作者主张：不同规则共用可因果迁移的棋盘表征，而非完全隔离的子模型。

论文证据：探针几何对齐超过随机基线；正文报告跨规则探针改变棋盘的效果接近匹配探针，图3精确误差未能核读。

模型推断：支持存在共享的可干预状态分量，不排除其他任务特有编码。

定位：['TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p4–5 §5.2、图2–3。\n']

作者主张：Iago与Classic的表征可由单个正交旋转跨层转换，体现抽象结构共享。

论文证据：探针对齐及留出序列上的残差流转换均有效，但最后一层例外。

模型推断：支持所训练同构游戏间的坐标兼容性，不证明完整表征严格等价。

定位：['TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p5–6 §5.3，p14 附录C.1。']

作者主张：规则冲突由局部电路仲裁；共同可信时中层路由，另一规则极稀有时提前选择。

论文证据：定位L4 MLP→L5 head 5→L5 MLP；留出歧义前缀可双向steer，runner-up head对照无相应效果。DelFlank则在第2–3层干预有效。

模型推断：消融与行为干预支持局部因果作用；两种仲裁状态的成因仍属比较性解释。

定位：['TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p6–8 §5.4–5.5。\n']

key_results：[{"setting": "单游戏与50/50 Classic–NoMidFlip混合模型的下一token预测。", "baseline": "单游戏模型；α另以词表均匀预测为零分参照。", "metric_or_guarantee": "α=1−DKL(P_GT||Qθ)/DKL(P_GT||U)，无量纲，不是准确率。", "reported_values_and_units": "作者报告均值±CI：纯Classic 0.995±0.002，纯NoMidFlip 0.988±0.003；混合模型对应0.991±0.003、0.983±0.004。", "information_and_compute": "单/混游戏20M/40M序列，250 epochs，batch4096，长度≤60；探针用10万独立采样序列、80/20划分。硬件与GPU小时未报告。", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p4 表1，p11 附录A.2–A.3。\n"}, {"setting": "Classic–Iago探针对齐及留出序列的残差流转换。", "baseline": "随机探针对齐、未施加旋转。", "metric_or_guarantee": "探针余弦相似度；Iago目标下α。", "reported_values_and_units": "作者报告余弦约0.03→0.98，随机对齐约0.68；无旋转α=−2.9。第1–7层施加全局Ω后接近基线，未从图中补取精确α。", "information_and_compute": "Ω为512×512正交矩阵；拟合与测试序列分离，拟合样本量未报告。", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p5 §5.3、图2，p14 C.1。\n"}, {"setting": "Classic–NoMidFlip留出歧义前缀，在出现排除另一规则的落子前干预。", "baseline": "不干预；runner-up layer-5 head的自身方向干预。", "metric_or_guarantee": "仅在一个游戏合法的落子集合中，Classic所占概率质量比例。", "reported_values_and_units": "作者报告基线0.48；全电路向Classic steering后0.68，向NoMidFlip后0.01；runner-up对照保持基线附近。", "information_and_compute": "方向学习集与测试前缀不重合；该评测样本量、完整强度预算未报告。", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p8 §5.4.2。\n"}, {"setting": "Classic–DelFlank共同合法前缀，读取第5层DelFlank棋盘探针。", "baseline": "不施加game-ID steering。", "metric_or_guarantee": "棋盘探针准确率。", "reported_values_and_units": "作者报告67.1%；第2层steering后77.4%，第3层后75.8%。", "information_and_compute": "在既有混合模型早层添加game-ID方向，观察下游表征；评测规模未报告。", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p8 §5.5、p9 图7题注。\n"}]

prior_work_candidates：[{"citation_as_printed": "Li, K., Hopkins, A. K., Bau, D., Vi´egas, F., Pfister, H., and Wattenberg, M. Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task, June 2024.", "identifier_if_present": "arXiv:2210.13382", "relation_candidate": "方法继承", "shared_component": "Othello-GPT、棋盘解码及因果干预。", "claimed_difference": "从单规则扩展到多规则冲突与仲裁。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p2 §2、p10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Nanda, N., Lee, A., and Wattenberg, M. Emergent Linear Representations in World Models of Self-Supervised Sequence Models. In Proceedings of the 6th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP, pp. 16–30, Singapore, 2023. Association for Computational Linguistics.", "identifier_if_present": "10.18653/v1/2023.blackboxnlp-1.2", "relation_candidate": "方法继承", "shared_component": "mine/yours/empty线性探针与向量steering。", "claimed_difference": "新增跨规则探针迁移及冲突处理电路分析。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p2 §2、p4 §5.2.2、p10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Hua, T., Yun, T., and Pavlick, E. mOthello: When Do Cross-Lingual Representation Alignment and Cross-Lingual Transfer Emerge in Multilingual Models?, April 2024.", "identifier_if_present": "arXiv:2404.12444", "relation_candidate": "背景引用", "shared_component": "多词表Othello的表征对齐问题。", "claimed_difference": "本篇称前作固定规则且对齐依赖anchor tokens；本作研究规则冲突及旋转转换，未直接复现前作。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p2 §2、p10 References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是具有行为干预证据的共享状态与局部仲裁机制，不只是变体任务上的性能改进；尚不足支持普遍机制或路线级首创。", "central_increment": "前作已有单规则probe-and-steer（本篇转述）；本作在双规则冲突下新增跨规则复用及局部仲裁证据，尚待排除训练偶然性与频率混杂。", "soundness_observation": "随机对齐基线、留出干预和强对照构成互补证据；但全部模型仅seed42训练一次，区间和bootstrap不覆盖训练随机性，全层γ=5亦未充分优化。\n", "significance_observation": "提供真值已知的多规则解释试验台，不能直接外推自然语言模型或机器人世界模型。", "main_open_question": "早层选择与中层仲裁的差异，究竟源于规则结构还是候选规则后验稀有度？"}

limitations：[{"text": "仅测试50/50成对混合、单一8层架构及合成任务；线性探针可能遗漏非线性机制。", "basis": "author_report", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p9 §7。\n"}, {"text": "DelFlank的‘OOD’指该游戏分量下极稀有，不代表前缀在整个混合分布中罕见；线性解码下降不能证明另一棋盘完全消失。", "basis": "model_inference", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p8 §5.5。"}, {"text": "不同规则对同时改变后验稀有度与动力学，未隔离仲裁层位变化的原因；纯/混模型总训练数据不同，亦非等算力比较。", "basis": "model_inference", "locator": "TEXT_OR_0wPUeZOZ9o_b8c9f83d0763，p8 §5.5、p11 A.2。"}]

minimal_check：{"question": "匹配歧义程度后，早/中层干预差异是否仍存在？", "control": "用现有两个混合检查点，按前缀长度、冲突格数及游戏后验熵匹配样本，比较各层同范数steering、无干预及随机方向。", "observable_outcome": "比较规则偏好变化的峰值层位及下游棋盘准确率。", "resources": "现有检查点、探针和游戏引擎；需新增受控前缀与前向干预，硬件和运行成本未知。", "failure_or_stop_condition": "匹配后层位差异消失则削弱规则结构解释；找不到共同支持样本则停止，不能强作因果归因。"}

missing_fields：["原始图像、部分图中精确数值、前作原文及其他版本。", "硬件、GPU小时、Ω拟合样本数及部分干预评测规模。", "Iago的64-token、65-move与附录66词表口径未协调，pass/pad映射实现待核。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

真值可知的多规则试验台和留出干预值得继续读；下一重点是匹配后验歧义程度、干预范数及训练重复后，仲裁层位差异能否保持。

身份版本与范围：首物理页题名和冻结名单一致，官方当前16页附件与真实输入和Pro哈希相符。Pro声明全文文本已读、图像未提供；本地另检查关键文字页面。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_material_limits

共享表示的证据强度：§5.2既比较探针几何，也进行跨规则棋盘干预；p4明确所有8层同时加向量且γ=5，脚注承认可能过度干预、强度未完全优化。该结果支持特定可干预共享分量，不排除任务专有或非线性编码，也不单独量化容量节约。

核查定位：p004:L0029-L0063；intervention_present_strong_intervention_limit_retained

关键因果行为数值：原PDF p8确认留出歧义前缀上Classic独有合法落子的概率质量份额0.48→0.68，反向到0.01；runner-up head对照近基线。DelFlank第5层棋盘探针67.1%，早层2/3 steering后77.4/75.8。Pro没有把这些量混成全任务准确率，数字与源文一致。

核查定位：p008:L0017-L0043, local_check/p008.png；reported_values_and_conditioning_match

性能指标与训练比较：Table1的α针对预测概率与真值的重合，不能当普通准确率；纯Classic/NoMidFlip为0.995/0.988，混合对应0.991/0.983。A.2明确纯/混模型分别20M/40M序列、250epochs、batch4096，因而不是等总训练量比较。

核查定位：p004:Table1, p011:L0021-L0034, p012:B.1；metric_and_training_budget_scope_checked

可推广性与统计范围：A.4明确所有模型及探针固定seed42且模型只训练一次；置信区间不能覆盖训练随机性。§5.5的稀有是相对DelFlank分量，规则动力学和后验稀有度同时变化，早层/中层仲裁差异的原因尚未被独立隔离。

核查定位：p011:L0052-L0055, p008:L0066-L0083；seed_and_component_distribution_limits_confirmed

本地补充/限定：[]

核查局限：["未下载检查点、运行游戏引擎或执行作者代码，未验证全部16页的所有曲线数值。", "本地未完整检查跨层正交旋转拟合数据与最后层例外，保留为Pro报告范围。", "前作未独立核读，所有机制结论限所测架构和规则分布，非普遍性证明。"]


## pro015 · Language Model Circuits Are Sparse in the Neuron Basis

论文 OR_OrviwFWcN4；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_OrviwFWcN4_ff67e999e80b", "source_url": "https://api2.openreview.net/pdf?id=OrviwFWcN4\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_OrviwFWcN4_ff67e999e80b：物理页1–9，正文§1–8、致谢与Impact Statement。", "TEXT_OR_OrviwFWcN4_ff67e999e80b：物理页9–14，参考文献。", "TEXT_OR_OrviwFWcN4_ff67e999e80b：物理页15–42，附录目录及A–H，包括全部可读表格文字；连续页标1–42无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文提取文本，未见PDF图像；图1–15的曲线、热图及图结构不能核验，不从残留坐标或图题推算数值。", "双栏文字交错，部分公式上下标、补集横线和排版失真；表中多处描述被省略或含字符占位符。", "未提供前作、其他版本及实验原始记录；未搜索、运行作者代码或复现实验，出版版身份未核实。"]}

问题：不训练稀疏字典，能否在原有MLP神经元基底找到与SAE同等稀疏、忠实且具有可解释干预效果的任务电路？

方法：以投影前MLP激活的“神经元×token位置”为节点。配对用激活差、非配对用零基线，结合RelP修改后的反传归因筛选节点；冻结注意力权重、归一化尺度和SiLU门，乘法反传采用half rule。边归因阻断中间MLP路径以估计直接影响，输出加权电路；最终消融与steering在原模型执行。

作者主张：MLP激活基底能产生与SAE同样稀疏、忠实的电路。

论文证据：SVA比较显示投影前基底显著优于投影后坐标，RelP进一步缩小SAE差距；附录扩展至Gemma-2-2B/9B及零消融。

模型推断：提供了改变基线选择的实质性经验知识，但稀疏任务电路不等于所有神经元单义。

定位：['TEXT_OR_OrviwFWcN4_ff67e999e80b：p4–5，§5.1–5.3', 'TEXT_OR_OrviwFWcN4_ff67e999e80b：p20–21，§D–E']

作者主张：建立无需另训字典的细粒度神经元电路追踪流程。

论文证据：节点及边消融支持RelP的有效性；§B给出half rule守恒解释，MIB补充粗粒度模块验证。

模型推断：新增价值主要在基底、粒度和流程整合，不将RelP或half rule本身视为独占首创。

定位：['TEXT_OR_OrviwFWcN4_ff67e999e80b：p4–6，§5.2、§5.4；p17–19，§B–C']

作者主张：神经元电路可恢复潜在推理步骤，并用于用户建模分析。

论文证据：州府任务有直接干预；附录分析10,000道加法题、54道多语反义词题及合成用户建模，借助标签AUROC定位特征。

模型推断：多为既有CLT发现的跨模型复现；附录相关性结果不能全部提升为干预验证。

定位：['TEXT_OR_OrviwFWcN4_ff67e999e80b：p7–8，§6；p28–42，§H']

key_results：[{"setting": "Llama 3.1-8B base；四项SVA，每项300对定位数据、40对留出数据；均值消融。", "baseline": "MLP输出、其他神经元表示及Llama Scope 8×宽度SAEs；IG与RelP比较。", "metric_or_guarantee": "归一化faithfulness理想值1，电路completeness理想值0；节点数。", "reported_values_and_units": "作者正文报告：IG下投影前电路比MLP输出电路小约100倍；RelP约200个节点达到近理想指标，未给可直接核读的精确纵轴值。", "information_and_compute": "IG使用10次反传，RelP使用1次；不能据此断言端到端快10倍。", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p3–5，§4–5.2。\n \n \n"}, {"setting": "SVA边裁剪；预选1,000个MLP节点，每例至多约500,000条候选边。", "baseline": "10步IG-inputs；不阻断中间MLP的RelP。", "metric_or_guarantee": "边数—faithfulness/completeness关系。", "reported_values_and_units": "带stop-gradient的RelP在约100,000条边时faithfulness超过80%；正文未提供对应completeness精确值。", "information_and_compute": "需对筛选节点计算边归因；总反传次数、显存及壁钟时间未报告。", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p6，§5.4。\n"}, {"setting": "MIB的Llama 3.1模型；IOI、Arithmetic、MCQA、ARC-E、ARC-C；注意力头/MLP粒度，反事实消融。", "baseline": "EAP(CF)、EAP-IG-inputs(CF)等；基线取自MIB原文。", "metric_or_guarantee": "CMD，无量纲，越低越好。", "reported_values_and_units": "RelP五任务依次0.01、0.00、0.11、0.15、0.15，平均0.08；EAP(CF)平均同为0.08，EAP-IG-inputs(CF)为0.10。按刊载精度并非独占最佳均值。", "information_and_compute": "RelP取三个随机种子均值，并报告最佳RelP变体；表中未列离散程度。", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p19，§C、表3。\n"}, {"setting": "Llama 3.1-8B-Instruct；50道城市→州→州府问题。", "baseline": "未干预的原模型；与CLT工作仅作跨模型定性对应。", "metric_or_guarantee": "节点数量与干预后的下一词元预测变化。", "reported_values_and_units": "Texas案例自动取得257个节点，再人工选23个解释；干预L23/N8079-使多数题首选由州府变为州，正文未给精确比例。23节点不应当作已验证的完整充分电路。", "information_and_compute": "归因目标为top-5 logits之和，τ=0.005；手动排除12个神经元；单神经元乘数为0至2、步长0.25。", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p7–8，§6。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Marks, S., Rager, C., Michaud, E. J., Belinkov, Y., Bau, D., and Mueller, A. Sparse feature circuits: Discovering and editing interpretable causal graphs in language models. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025.", "identifier_if_present": "OpenReview:I4e82CIDxv", "relation_candidate": "方法继承；比较基线", "shared_component": "SVA、IG-activations、消融评价及代码。", "claimed_difference": "改用投影前MLP神经元和RelP，检验SAE是否必要。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p3–5，§4–5；p12，References", "prior_actually_read": false}, {"citation_as_printed": "Jafari, F. R., Eberle, O., Khakzar, A., and Nanda, N. Relp: Faithful and efficient circuit discovery in language models via relevance patching. arXiv:2508.21258, 2025.", "identifier_if_present": "arXiv:2508.21258", "relation_candidate": "组件复用；同期独立工作候选", "shared_component": "RelP替代反传与相关传播规则。", "claimed_difference": "本作强调单个MLP神经元及神经元间边；脚注称同期开发，独立性未外核。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p4，§5.2及脚注4；p11，References", "prior_actually_read": false}, {"citation_as_printed": "Lindsey, J., Gurnee, W., Ameisen, E., Chen, B., Pearce, A., Turner, N. L., Citro, C., Abrahams, D., Carter, S., Hosmer, B., Marcus, J., Sklar, M., Templeton, A., Bricken, T., McDougall, C., Cunningham, H., Henighan, T., Jermyn, A., Jones, A., Persic, A., Qi, Z., Thompson, T. B., Zimmerman, S., Rivoire, K., Conerly, T., Olah, C., and Batson, J. On the biology of a large language model. Transformer Circuits Thread, 2025.", "identifier_if_present": "https://transformer-circuits.pub/2025/attribution-graphs/biology.html\n", "relation_candidate": "组件复用；比较基线", "shared_component": "州府、多语等案例及机制解释框架。", "claimed_difference": "以Llama神经元而非CLT特征获得类似结果，不是同模型受控对比。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p7–8，§6；p12，References；p28–34，§H", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是经基底与归因对照支持的新经验认识，不只是替换组件后的单点性能提升；既有电路框架未被根本重建，不判L3。", "central_increment": "前作能用SAE/CLT追踪电路（仅本篇转述）；本作在所测条件下用投影前神经元与RelP达到同阶稀疏、忠实表现，并获得可干预案例。", "soundness_observation": "原模型消融提供实质支持；§B说明冻结系数下half rule的归因守恒，不等于§3.2的电路completeness，也不证明全局因果解释正确。", "significance_observation": "提供免训稀疏字典的强基线；不等于整个解释流程零成本或模型推理加速。", "main_open_question": "统一归因方法、误差节点计数与测试分布后，神经元和SAE的等稀疏结论能否保持？"}

limitations：[{"text": "完整电路仍难人工理解，聚类和自动描述待改进；串行autograd导致低计算利用率。", "basis": "author_report", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p8，§7 Limitations"}, {"text": "SVA仍是模板任务；非配对定位也保留目标/反事实输出logit差评价。SAE误差项可计为节点，解释粒度需区分；附录标签筛选未明确独立留出验证。", "basis": "model_inference", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p3–5，§4–5.3；p28，§H"}, {"text": "用户建模依赖预填人口属性输出，不能直接推出自然对话中存在同样可定位的潜在用户信念。", "basis": "model_inference", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p41，§H.3"}, {"text": "报告口径待核：10万条边被称为10%，但候选边上限写为50万；§G.1称过滤的L9/N4255等仍列于表13，过滤作用范围不清。", "basis": "model_inference", "locator": "TEXT_OR_OrviwFWcN4_ff67e999e80b：p6，§5.4；p27，§G.1；p41–42，表13"}]

minimal_check：{"question": "在未参与筛选的新nounpp句型上，神经元与SAE是否仍同等稀疏？", "control": "固定Llama 3.1-8B及定位集，两基底均使用RelP和同一均值消融；明确SAE误差节点的统一计数规则。", "observable_outcome": "预设|faithfulness−1|≤0.05且|completeness|≤0.05，比较达到条件所需节点数及重采样区间。", "resources": "8B权重、对应8×SAE和新测试句型；需保存激活与反传的计算资源，具体GPU、显存和时长未知。", "failure_or_stop_condition": "神经元稳定需要更多节点则不支持该测试域的等稀疏结论；无法统一消融和节点计数时停止比较。"}

missing_fields：["图中精确曲线、原始实验数据及独立复现结果。", "可读文本中的SVA重复实验不确定性、硬件配置、显存、壁钟时间和总成本。", "用户建模样本量及附录AUROC的独立筛选/测试划分。", "前作全文及目标附件的最终出版版本确认。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

免另训稀疏字典的神经元基底是值得采用的解释性基线；继续阅读前先明确节点计数、消融和阈值，并在未参与筛选的新模板上比较。

题名版本范围：首物理页题名匹配，官方当前42页附件与Pro ID及哈希一致。Pro说明只读全页文本、未见图像，和本次材料一致；当前版没有被认证为最终出版版。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心基底比较与单位：§4–5比较投影前MLP激活、MLP输出和其他位置，并使用Llama Scope 8倍宽SAE；误差项可计为SAE节点。§3把同一单元在不同token位置视作不同节点，电路规模不能直接当作全局独立神经元或模型参数压缩数。最终消融在原模型而非局部替代模型上执行。

核查定位：p002:L0052-L0058, p004:L0024-L0042；baseline_node_unit_and_original_model_evaluation_confirmed

评价范围及近理想表述：四个SVA模板各用300对定位、40对留出；faithfulness理想1、circuit completeness理想0。p5文字称约200节点近理想，图2有faithfulness超过1的区间。本地只确认作者的近似表述及曲线趋势，不从小图判定200点满足特定容差，也不能把越大faithfulness一律当越忠实。

核查定位：p003:L0014-L0054, p005:L0037-L0061, p005:Figure2, local_check/p005.png；reported_approximation_preserved_exact_threshold_unverified

计算步骤与术语边界：p5明确IG用10次反传、RelP一次；这不是端到端10倍加速测量。p4的half rule“completeness”指归因分数逐层守恒，不能和§3.2电路消融完备性混同，也不是全局因果正确性的证明。

核查定位：p004:L0043-L0056, p005:L0053-L0055, p003:§3.2；cost_and_completeness_distinctions_checked

MIB结果与比较口径：Table3列RelP的五项CMD为0.01/0.00/0.11/0.15/0.15，均值0.08；EAP(CF)平均也0.08，不能称按印出精度独占最佳。该实验为更粗的注意力头/MLP粒度，RelP三种子平均，其他基线取原MIB；不直接证明所有神经元粒度任务等稀疏。

核查定位：p019:L0003-L0018, p019:L0034-L0055；numbers_and_granularity_match

本地补充/限定：[{"kind": "local_qualification", "detail": "补充图2有faithfulness超1区间；约200节点是作者近似报告，尚未用原始数据验证同时达到预设的faithfulness/completeness容差。"}]

核查局限：["未执行原模型、训练SAE、下载权重或复现SVA/城市州府干预。", "未核验全部42页图表、约10万边比例或附录过滤列表的其他Pro疑点。", "前作和同期RelP工作仍未全文核读；不裁定独占首创，L2为暂定模型判断。"]


## pro016 · Intrinsic Task Symmetry Drives Generalization in Algorithmic Tasks

论文 OR_QDVz3V4Vle；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_QDVz3V4Vle_cace47e640a4", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_QDVz3V4Vle_cace47e640a4：物理页1—44全部已提供文本，涵盖正文、参考文献及附录A—J；连续页标无缺口。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1—59均无图像，仅图题及正文描述可读；不能独立核验曲线、PCA形状、收敛步数或误差条。", "双栏顺序、公式上下标及表1、表3部分符号有损；表2的p值可读。", "未提供前作、其他版本、代码或原始日志；不认定本附件为最终出版版。"]}

问题：网络为何在算法任务中先记忆、后泛化，并形成特定低维表示几何？

方法：从数值对、节点对或关系三元组预测类别；以输出分布的对称KL衡量交换/结合代理、最短路距离加法和比较一致性，联合跟踪PCA维数及梯度对齐。训练时加入这些一致性损失，另比较几何正则与负权抑制。

作者主张：内在对称性驱动泛化；训练依次经历记忆、对称性获取和几何组织，泛化发生于第二阶段。

论文证据：覆盖六种模运算、六类图和二维/三维比较；报告对称违背量、梯度对齐与泛化同步，以及20种子的软阈值关联。几何和时间顺序主要依赖不可见图。

模型推断：跨域指标与干预形成有价值的机制证据，但尚不能确证对称性是独立、主导原因。

定位：['TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页5—7、20—23，§6—7、附录B/C']

作者主张：对称性辅助损失比纯几何或优化器加速更可靠；促进和抑制实验支持因果作用。

论文证据：作者报告相对vanilla、GrokFast及几何正则的收敛改进；无weight decay的MLP亦有效，反向加权则损害泛化。

模型推断：支持已知结构先验的实用价值；不等于证明无额外信息、等计算预算下仍有同等收益。

定位：['TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页8—9、32—38，§8、附录E/F']

key_results：[{"setting": "模加p=113、7×7 lattice、二维比较7×7实体；各20种子，成功定义acc>0.99。", "baseline": null, "metric_or_guarantee": "最大实例级对称违背量的soft-threshold关联检验。", "reported_values_and_units": "三任务p值依次为9.5367×10^-7、2.734×10^-2、3.125×10^-2，均无量纲；不是效果量。", "information_and_compute": "按附录G默认配置：单层4头Transformer，d=128、FFN=512，无LayerNorm；训练比例30%/80%/20%，weight decay为1/3/1；AdamW最多100000 epochs。", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页22—23附录C表2、物理页38附录G。\n \n"}, {"setting": "模加，两层MLP，80%训练比例，无weight decay。", "baseline": "同设定不加symmetry-prompting的模型。", "metric_or_guarantee": "达到完全泛化的训练进度。", "reported_values_and_units": "作者报告最多缩短两个数量级；原始epoch数不可见，不能换算为壁钟加速。", "information_and_compute": "硬件、耗时与辅助损失的额外前向预算未报告。", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页6图8文字说明、物理页9§8.4。\n"}, {"setting": "已知运算构成阶p循环群，单位元0、生成元1；选择特定Cayley表条目。", "baseline": null, "metric_or_guarantee": "命题7.4声称可唯一重建完整运算表。", "reported_values_and_units": "需要2p−1项，占全部条目的(2p−1)/p²，渐近约2/p。", "information_and_compute": "这是条件性存在构造，不是随机样本泛化界或网络训练保证；所写集合与条目计数不一致。", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页8§7.3、物理页43—44附录J.4。\n"}]

prior_work_candidates：[{"citation_as_printed": "Nanda, N., Chan, L., Lieberum, T., Smith, J., and Steinhardt, J. Progress measures for grokking via mechanistic interpretability. In The Eleventh International Conference on Learning Representations, 2023.", "identifier_if_present": "OpenReview:9XFSbDPmdW", "relation_candidate": "背景引用", "shared_component": "grokking阶段划分及模加表示几何。", "claimed_difference": "以跨任务对称性补充电路形成与cleanup解释。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页6§6.3、物理页10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Tan, Z. and Huang, W. Understanding grokking through a robustness viewpoint. arXiv preprint arXiv:2311.06597, 2023.", "identifier_if_present": "arXiv:2311.06597", "relation_candidate": "方法继承", "shared_component": "交换性归纳偏置，仅据本篇转述暂定。", "claimed_difference": "扩展到结合性代理、图距离和比较一致性及其训练动力学。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页2§2、物理页11参考文献", "prior_actually_read": false}, {"citation_as_printed": "Wang, P. and Wang, Z. Why neural network can discover symbolic structures with gradient-based training: An algebraic and geometric foundation for neurosymbolic reasoning, 2025.", "identifier_if_present": "arXiv:2506.21797", "relation_candidate": "背景引用", "shared_component": "群不变性、代数结构与表示几何的联系。", "claimed_difference": "本作增加跨域grokking阶段、进度指标与正反干预证据。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页2§2、物理页11参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是跨任务机制理解，而非单个正则项；现有材料支持有意义的暂定判断，但不足以升为路线级新框架。", "central_increment": "前作已描绘电路/几何并使用交换性偏置（本篇转述）；本作在已知规则的小型任务上新增跨域对称性阶段及干预证据；尚待排除监督信息和优化混杂。", "soundness_observation": "未逐一定理验证。命题7.1证明使用未声明的连通性；7.3只推出有序性，未保证等距网格；7.4所写M含2p项却计为2p−1。这些缺口限制理论支撑，不直接否定全部经验结果。\n \n", "significance_observation": "可用于受控grokking诊断和加速；工程上属于小模型辅助训练，未展示大规模系统或真实任务收益。", "main_open_question": "限制为训练可见信息并匹配计算预算后，对称性促进/抑制是否仍有特异性因果效果？"}

limitations：[{"text": "作者明确限于受控、对称性可指定的任务；附录H自动发现仅验证计数任务中的预设置换候选。", "basis": "author_report", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页9 Limitations、物理页39附录H"}, {"text": "图和比较三元组按真实最短路或排序采样，未说明是否仅由训练可见关系产生，额外结构监督风险未排除。", "basis": "model_inference", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页16附录A.2、物理页19附录A.3、物理页32附录E.1.2"}, {"text": "比较度量假定Bradley–Terry加性log-odds，强于普通传递性；负权抑制也可能直接损伤正确输出，未充分排除一般性优化干扰。", "basis": "model_inference", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页19附录A.3、物理页38附录F"}, {"text": "3D lattice的常规分析使用7³节点，加速实验改为4³；不能跨实验直接比较难度。辅助损失与GrokFast的调参、计算配平情况未交代。", "basis": "model_inference", "locator": "TEXT_OR_QDVz3V4Vle_cace47e640a4，物理页8—9§8、物理页38附录G"}]

minimal_check：{"question": "图任务加速是否依赖训练外的全图结构？", "control": "固定7×7 lattice划分，比较vanilla、原版最短路约束、仅由训练标签可确认的三元组约束；匹配三元组数量及总前后向预算。", "observable_outcome": "多种子达到99%/100%测试准确率的成功率、步数与壁钟耗时。", "resources": "原始采样和训练实现、小型Transformer；硬件及工时未知。", "failure_or_stop_condition": "训练内三元组不足以配平时停止并报告不可比；若优势只在全图版本出现，则不能排除额外监督解释。"}

missing_fields：["soft-threshold数值、检验方法、零假设及阈值选择流程未说明。", "学习率、batch size、辅助权重、三元组采样预算、调参范围、硬件与壁钟成本未报告。", "熵正则π的具体定义及非原生结合运算的代理实现不充分；加速/抑制实验的完整数值和多种子统计不可得。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

结构一致性作为grokking诊断有阅读价值；优先核查仅用训练内关系且计算配平时，促进/抑制效果是否仍具有特异性。

身份与完整范围：首物理页题名匹配；当前官方44页附件的ID和全文哈希与Pro一致，Pro声明全文文本已读并保留不可见曲线的局限。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心干预及结构信息：§8通过已知任务的交换/结合、最短路距离加法和比较一致性辅助损失进行促进，附录F用负权抑制。A.2按真实最短路采样中间节点，E.1.2明确复用该指标作训练正则；是否只用训练可见关系未交代。支持结构先验有用，不足以排除额外信息及一般优化干扰。

核查定位：p008:§8.1-8.3, p016:L0003-L0012, p032:L0022-L0024, p038:L0003-L0010；intervention_and_information_requirement_confirmed

决定性统计与成本口径：Table2为20种子、acc>0.99的soft-threshold检验，p值9.5367e−7、2.734e−2、3.125e−2与Pro一致。图9横轴是epoch而不是墙钟；未据图补写精确加速值，也不能把最多两数量级epoch减少直接视为总计算或时间减少。

核查定位：p022:L0005-L0013, p023:L0021-L0033, p008:Figure9, local_check/p008.png；reported_pvalues_and_epoch_units_checked

条件化重建命题及可修复计数：命题7.4预先假定阶p循环群、单位元0、生成元1，并只说存在特定条目集，不是随机样本或神经网络泛化保证。p43所印两列集合含2p项，却计2p−1，确有集合/计数不一致；删去冗余(0,1)即可得到2p−1，且后文已写a≠0。这个局部修复并不否定命题的存在性内容，不能仅据排写问题认定定理错误。

核查定位：p008:Proposition7.4, p043:L0024-L0052；scope_checked_printed_count_issue_with_simple_repair

训练及外推范围：附录G为单层4头、维128/512、无LayerNorm、AdamW至多100000epochs；图任务常规7³而加速用4³，不能跨实验直接比较难度。

核查定位：p038:L0019-L0043；configuration_and_cross_experiment_difference_checked

本地补充/限定：[{"kind": "qualification", "detail": "7.4集合计数问题可通过删除冗余(0,1)修复；应保留这一说明，不把局部笔误当作存在性命题的反例。"}]

核查局限：["未重算soft-threshold统计、运行训练或测量额外计算；p值不是效果量。", "Pro对7.1/7.3的其他证明疑点未在本地完整裁定；没有宣布所有定理得到验证或被证伪。", "没有前作全文核读、实验复现或新增第二轮模型调用。"]


## pro017 · Unsupervised Disentanglement Without Compromises : How Functional Orthogonality Enforces Identifiability

论文 OR_GDDYhRWpG4；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3", "source_url": "https://api2.openreview.net/pdf?id=GDDYhRWpG4\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "97c20185aa49fd15beb1c89e1914f072a6e5f8c3c7a47279f74478158e58512f", "source_pdf_sha256": "8c1d413ffff3d519c300037ddbe83451f2d74d0af1c9926c09e75db80a9e3046"}], "read_ranges": [{"source_id": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3", "physical_pages": "1-38", "content": "已读全部连续页标文本：正文1-9页；影响声明、致谢及参考文献10-12页；附录A、B为13-27页；附录C为27-31页；附录D为31-38页。未发现页标缺口，33-38页仅有图题等文本。"}], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文抽取文本，未见PDF图像；Fig.1-16不可见，不能读取Fig.3箱线图数值或核验定性重建。", "Table 1、2数值可读；部分公式、上下标和双栏顺序混排，尤其Eqs.(37)、(41)、(61)，不保证符号完整。", "未提供前作、其他版本或实验代码；当前附件身份未确认为最终出版版。\n"]}

问题：仅凭观测数据，能否恢复彼此相关的潜在因素，允许的歧义仅为坐标置换和逐坐标可逆重参数化？

方法：理论研究等价模型间h=f⁻¹∘g的相对标架，借超立方体边界与解析性推出坐标分离。实验以Residual Flow拟合观测，用可学习先验容纳因素相关性，最大化log p(x)−CIMA；另引入边界正则，推理经逆流输出潜表示。

作者主张：功能正交可使一般非线性生成模型在没有统计独立或因果监督的情况下可识别。

论文证据：Prop.1、2分别给出独立源与相关源的充分条件；App.A通过边界固定相对标架证明置换及逐坐标重参数化等价类。关键是Asm.1还包含Eq.(4)，不只有Jacobian列正交。

模型推断：中心增量是相关因素的条件化识别保证；这是加入几何、高阶和边界先验后的结果，不是否定无额外归纳偏置时的不可能性。

定位：['TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p3，Asm.1、Eqs.(3)-(4)；p15，Preliminary 2(v)。\n', 'TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p4-6，Prop.1-2、Asm.2；p19，App.A.3']

作者主张：VAE的解耦来自先验的全局独立压力与后验的局部正交偏置；显式正交正则可将该能力移植到flows。

论文证据：有无CIMA的合成对照及Table 2支持正交正则有效；Table 1中将对角高斯后验换成flow后验后，多项解耦指标下降。

模型推断：为已有VAE—IMA解释补充对照证据，而非首次提出该机制；更换后验也改变表达能力和优化，尚不能完全隔离正交性的因果作用。

定位：['TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p8-9，§6、Table 1；p31-32，App.D.1、Table 2']

key_results：[{"setting": "合成d∈{3,6,9}；独立均匀源或相关源；Möbius及非保形QD映射。", "baseline": "无正交约束的normalizing flow。", "metric_or_guarantee": "Spearman MCC、nonlinear Amari distance；作者报告加约束后改善，独立与相关设置表现相近。", "reported_values_and_units": null, "information_and_compute": "每配置10000点、30次运行，共720个模型；相关源通常为0.75 pNF＋0.25 Uniform。Fig.3数值不可读，不能量化相关源增益。", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p6-7，§5、Fig.3；p27，App.C.1"}, {"setting": "Table 2：d=6、独立源；未按混合函数类别拆分。", "baseline": "无约束NF、VAE、β-TCVAE。", "metric_or_guarantee": "Spearman MCC，越高越好。", "reported_values_and_units": "正交NF 0.9575±0.0544；无约束NF 0.7091±0.0492；VAE 0.8213±0.0868；β-TCVAE 0.8880±0.0759。均无量纲；±含义未明确。", "information_and_compute": "NF用64层残差流，每层3层MLP、宽128；Adam学习率10⁻³、batch 256，训练至收敛。硬件与训练时长未报告。", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p29，App.C.3；p32，Table 2。\n"}, {"setting": "dSprites、3DShapes；每种模型10个随机种子。", "baseline": "β-VAE；比较替换为flow后验的β-FlowVAE。", "metric_or_guarantee": "MIG，越高越好。", "reported_values_and_units": "dSprites：0.1070±0.0706→0.0443±0.0194；3DShapes：0.2279±0.1791→0.0617±0.0215。均为β-VAE→β-FlowVAE，无量纲；±按原文保留。", "information_and_compute": "作者称其他架构及训练流程相同；后验flow细节、β取值及资源未完整报告。以上均为作者结果，非本地复现。", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p9，Table 1、§6。\n"}]

prior_work_candidates：[{"citation_as_printed": "Gresele, L., Von Kügelgen, J., Stimper, V., Schölkopf, B., and Besserve, M. Independent mechanism analysis, a new concept? Advances in neural information processing systems, 34:28233–28248, 2021.", "identifier_if_present": null, "relation_candidate": "理论扩展；组件复用", "shared_component": "功能正交、IMA及CIMA惩罚。", "claimed_difference": "本篇称前作排除特定非线性退化解；本作增加相关源与更一般QD情形的条件化保证。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p2，§2；p11，参考文献；p29，Eq.(68)。\n", "prior_actually_read": false}, {"citation_as_printed": "Buchholz, S., Besserve, M., and Schölkopf, B. Function classes for identifiable nonlinear independent component analysis. Advances in Neural Information Processing Systems, 35:16946–16961, 2022.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "限制非线性函数类以取得可识别性。", "claimed_difference": "本篇将其描述为保形等受限类结果，本作主张扩展到非保形QD及相关因素。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p2、p4；p10，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Reizinger, P., Gresele, L., Brady, J., Von Kügelgen, J., Zietlow, D., Schölkopf, B., Martius, G., Brendel, W., and Besserve, M. Embrace the gap: Vaes perform independent mechanism analysis. Advances in Neural Information Processing Systems, 35:12040–12057, 2022.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "因子化VAE后验诱导IMA式正交偏置。", "claimed_difference": "本作将该既有机制纳入局部—全局条件解释，并添加后验替换实验。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p8，§6；p12，参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心是允许相关潜因素的实质性条件化识别保证，而非新正则或单纯性能提升；但前作覆盖和证明完整性尚未独立核实。", "central_increment": "前作已提供IMA正交原则和惩罚（本篇转述）；本作在高阶相对标架、边界正则与组合完整支撑下新增相关源识别论证。", "soundness_observation": "CIMA只直接约束一阶列正交，文中未证明其落实Eq.(4)。此外，App.A.2 p18的Eq.(43)→(44)由点态Jacobian分解转成全局函数分解、App.A.3 p19由满支撑落实闭域非退化的步骤需进一步核查；不能把定理表述视作已验证结论。", "significance_observation": "可能为相关因素恢复提供理论依据；不等于识别因果图，也未证明恢复结果必然对应人类语义概念。", "main_open_question": "所训练的流模型是否确实满足Prop.2所需的高阶相对标架与闭域正则条件，而非仅满足近似正交和先验满支撑？"}

limitations：[{"text": "作者承认组合缺失会破坏支撑条件；总体满支撑不保证有限数据覆盖，d=9亦有优化失败。", "basis": "author_report", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p21，App.A.4；p30，App.C.4"}, {"text": "完整Jacobian计算难扩展到高维图像；边界修正需要额外域知识，不能概括为实践中只加正交即可。", "basis": "author_report", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p30，App.C.3-C.4。\n"}, {"text": "主文独立先验写Gaussian，附录写Logistic；Eq.(68)约束生成Jacobian Jg⁻¹，而p30描述对解混Jg的列施加惩罚，实际实现对象待核。", "basis": "model_inference", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p6，§5；p29，Eqs.(64)、(68)；p30，App.C.3"}, {"text": "附录学得先验支撑R^d，sigmoid仅用于展示；其与有界、闭域正则假设的对应尚不充分。Table 1也缺少表达能力及优化匹配，不能将全部下降唯一归因于正交偏置消失。", "basis": "model_inference", "locator": "TEXT_OR_GDDYhRWpG4_8c1d413ffff3:p20，App.A.3讨论；p29，App.C.3；p8-9，§6"}]

minimal_check：{"question": "相关源恢复在多大程度上依赖附加边界先验？", "control": "固定d=3相关源、10000点、架构和配对种子，保留同一CIMA，仅开关App.C.4边界损失。", "observable_outcome": "比较MCC、Amari、拟合KL及出界率。", "resources": "需明确边界采样及损失实现；建议两组各5次配对运行，未执行。GPU型号和耗时未知。", "failure_or_stop_condition": "若仅加边界组稳定恢复，则实践效果依赖域先验；若两组拟合质量不匹配或边界实现不明，停止单因素归因。此检验不直接证伪条件化定理。"}

missing_fields：["Fig.3分配置数值及全部图像证据。", "真实独立先验、实际正则Jacobian对象、边界损失权重与使用范围。", "训练步数、硬件、时长、显存、测试样本量及超参数搜索预算。", "Table 2聚合细节、两表±的统计定义、β-FlowVAE完整配置。", "前作全文与条目外标识、其他版本、独立证明核验及复现结果。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

相关潜因素的条件化识别框架值得读，但优先核查整个模型类的高阶条件、边界正则及所训练flow是否满足它们。

身份版本范围：题名、ID及哈希符合官方当前38页附件，Pro声明所有提供文本已读、图像不可见；本地另看假设与数表原页。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心理论不是只有一阶正交：原PDF Assumption1除Eq3的Jacobian列正交外，还明列Eq4：相对标架所有纯方向各阶导数为零须推出所有混合导数为零，且作用于整个模型类。p15证明确实在角点利用这一高阶条件，再借解析延拓推广常值标架。因此不能把结果简写为任意模型只需正交Jacobian就可识别。

核查定位：p003:Assumption1, Eqs3-4, p015:L0023-L0057, local_check/p003.png；additional_assumption_and_its_proof_role_confirmed

相关因素的全局条件及等价类：Assumption2要求有界、单连通支撑，经逐坐标严格单调变换成为超立方体，copula满支撑；Prop2同时引用Assumptions1/2。Def1允许置换和逐坐标重参数化，不等于恢复唯一数值坐标、因果图或人类命名概念。闭域邻域的解析/非退化条件也进入所读证明。

核查定位：p003:L0003-L0019, p005:L0040-L0061, p006:L0029-L0038, p015:L0003-L0012；conditional_identifiability_scope_checked

实证数字及适用设置：原PDF Table2明确d=6独立源，Spearman MCC：约束NF0.9575±0.0544、无约束0.7091±0.0492、VAE0.8213±0.0868、β-TCVAE0.8880±0.0759。和Pro一致；这些数值不能直接量化相关源收益，±含义仍按原文未知处理。

核查定位：p032:Table2, local_check/p032.png；numbers_match_independent_source_setting_retained

定理与训练正则之间的联系：§5使用既有CIMA正则和可学习先验，并称其落实Assumption1；但该段描述的是Jacobian正交训练，未在所核页面给出Eq4及闭域条件的实现检验。实验改善支持方法在所测配置有效，不能替代验证全部定理前提。

核查定位：p006:L0032-L0045, p003:Eq4, p015:L0031-L0057；theory_to_implementation_gap_preserved_not_falsified

本地补充/限定：[]

核查局限：["未独立验证Prop1/2完整证明；Pro指出的点态到全局分解、先验及Jacobian方向冲突仍为待核问题。", "未运行残差流、β-FlowVAE或边界消融，未量化相关源实验的图形结果。", "未全文核读IMA等前作，不裁定历史首创；L2是暂定模型判断。"]


## pro018 · On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models

论文 OR_TBaUfO9znF；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf", "source_url": "https://api2.openreview.net/pdf?id=TBaUfO9znF\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "f699b3a3e26f5bd841d84fe7ad11da0835f5c73e9c0a2a28437c43c1c8906cbf", "source_pdf_sha256": "787f7c6ee1cf30d198d52d052a73d54613fe66a5f9d2b420de01216aa3f5c73f"}], "read_ranges": ["TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页1–34连续全文；正文§1–7、参考文献及附录A–L均已阅读，未发现物理页标缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–18只有图题及部分提取标签，未核见曲线、柱高和拓扑图。", "双栏文字和部分分式混排；表1–11主要文字可读，但不能自行订正正文与表格的配方、预算冲突。", "未提供前作全文、其他版本、代码、数据及实验日志。"]}

问题：预训练原语覆盖、mid-training与RL数据难度及预算，如何共同影响更复杂运算和跨语境推理？

方法：从算术DAG生成问题、推导和答案，分别调节运算数与语境模板。100M模型从零预训练10B tokens，按实验加入next-token mid-training及GRPO。将输出解析为依赖图，仅当所有gold节点的依赖、数值及最终答案均正确时计为成功；另比较过程与结果奖励。

作者主张：只有预训练留有能力空间且RL数据位于edge of competence时，RL才产生真正能力增益。

论文证据：100M正文报告相应趋势；500M表2中edge训练的外推收益最大，但easy训练也提高困难题pass@128。

模型推断：支持难度匹配影响泛化的条件性知识，不支持将“只有”视为普遍必要条件。

定位：['TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页4–5，§3；物理页21，表2。']

作者主张：预训练中少量目标语境原子示例可为RL跨语境组合提供必要基础。

论文证据：100M仅暴露B语境op=2时，正文报告1%明显优于0–0.1%；500M表3的0.1%组已可有效求解。

模型推断：展示暴露量与后训练效果的交互，但1%不是通用阈值，也未单独识别语境识别与算术原语学习的作用。

定位：['TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页5–6，§4；物理页22，表3；物理页25–27，附录H。']

作者主张：固定算力下，mid-training与RL互补，最优分配取决于目标难度及指标。

论文证据：500M和7B存在混合方案优于纯RL的设置；但附录L明确报告100M预算≥8.4B时纯RL的困难题pass@128最高。

模型推断：提供有价值的阶段分配证据，而非混合训练必胜规律；“安装先验”仍主要是行为层解释。

定位：['TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页6–7，§5；物理页22，表4；物理页24，表8；物理页34，Observation 8。\n']

key_results：[{"setting": "500M合成模型；RL训练op=11–14，评测op=15–20。", "baseline": "同设置Base及RL op=7–10。", "metric_or_guarantee": "过程验证pass@1、pass@128。", "reported_values_and_units": "Base分别14.6%、45.3%；edge-RL分别26.2%、53.2%；easy-RL的pass@128也达48.9%。均为作者报告。", "information_and_compute": "F.1称沿用合成协议；500M具体预训练token预算未明确列出。", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页21，表2。\n"}, {"setting": "500M；改变预训练B语境暴露量，RL后评测B语境op=15–20。", "baseline": "0%与0.1%暴露组。", "metric_or_guarantee": "过程验证pass@128。", "reported_values_and_units": "0%、0.1%、1%、10%暴露分别对应0.0%、51.5%、51.6%、54.0%。", "information_and_compute": "比较的是不同预训练暴露组的RL后结果，不能当作同一Base的RL增量。", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页22，表3。\n"}, {"setting": "500M阶段预算分配实验；评测op=15–20。", "baseline": "Full RL。", "metric_or_guarantee": "过程验证pass@128。", "reported_values_and_units": "Full RL为53.2%；60% RL加40% mid-training为66.6%。", "information_and_compute": "作者声明固定预算；表4未逐设置报告实际FLOPs。", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页22，表4。\n"}, {"setting": "Qwen2.5-7B Base；按初始成功率分桶进行数学RL。", "baseline": "Qwen2.5-7B Base。", "metric_or_guarantee": "pass@32；真实任务的过程验证实现未说明。", "reported_values_and_units": "AIME 2025：Base 13.3%，easy/edge各33.3%，hard 60.0%；MATH-500：Base 84.8%，hard-RL 81.4%。", "information_and_compute": "每桶20K题、GRPO 80步；hard指pass@32失败但pass@128非零，筛题成本未报告。", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页22，F.2；物理页24，表7。\n"}, {"setting": "500M，RL数据op=11–14，加入过程奖励。", "baseline": "相同RL数据下的outcome-only奖励。", "metric_or_guarantee": "过程验证pass@1、pass@128的绝对变化。", "reported_values_and_units": "op=11–14分别增加0.52、1.05个百分点；op=15–20分别变化−0.06、+0.03个百分点。", "information_and_compute": "该表未明确逐项奖励混合系数及运行方差；小幅变化不能据此认定统计显著。", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页23，表6。\n"}]

prior_work_candidates：[{"citation_as_printed": "Zhou, Y., Liu, H., Chen, Z., Tian, Y., and Chen, B. Gsm-infinite: How do your llms behave over infinitely increasing context length and reasoning complexity?, 2025b.", "identifier_if_present": "arXiv:2502.05252", "relation_candidate": "组件复用", "shared_component": "算术依赖图、语境渲染和正反向生成。", "claimed_difference": "本作将生成框架用于三阶段干预及过程验证分析。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：§2.1、附录B；物理页11参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Yuan, L., Chen, W., Zhang, Y., Cui, G., Wang, H., You, Z., Ding, N., Liu, Z., Sun, M., and Peng, H. From f(x) and g(x) to f(g(x)): Llms learn new skills in rl by composing old ones, 2025.", "identifier_if_present": "arXiv:2509.25123", "relation_candidate": "背景引用", "shared_component": "研究RL能否组合已有技能解决未见组合；未确认方法继承。", "claimed_difference": "本作进一步操纵预训练覆盖、RL难度和mid-training预算。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页11参考文献、物理页12附录A。\n", "prior_actually_read": false}, {"citation_as_printed": "Wang, Z., Zhou, F., Li, X., and Liu, P. Octothinker: Mid-training incentivizes reinforcement learning scaling, 2025.", "identifier_if_present": "arXiv:2506.20512", "relation_candidate": "背景引用", "shared_component": "mid-training改善后续RL效果。", "claimed_difference": "本作强调受控合成环境中的阶段预算扫描，未声称首创mid-training。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页7 Discussion 3、物理页11参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是联合控制训练阶段后得到的条件性经验知识，而非新RL算法；多组干预与跨规模补充超出单点性能改进，但不足以认定路线级创新。", "central_increment": "前作已报告技能组合与mid-training促进RL（仅本篇转述）；本作新增暴露量、任务难度和阶段预算的交互证据，尚待排除评测与配方混杂。", "soundness_observation": "消融较丰富；但“只有edge才提升”强于表2和表7支持范围，且预算、配方存在内部不一致。", "significance_observation": "对RL训练数据筛选和阶段资源分配有实际启发；过程奖励的500M增益较小，不能概括为一致大幅提升。", "main_open_question": "提高Base的采样预算后，RL的困难题可解覆盖优势是否仍存在，还是主要体现已有成功轨迹的概率重分配？"}

limitations：[{"text": "作者明确将结果限定为经验发现：暴露阈值、难度分桶和最佳配比依赖规模、数据及目标域。", "basis": "author_report", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页23，F.2总结。\n"}, {"text": "有限pass@128不能证明模型支持集扩大。验证器严格匹配gold依赖，可能拒绝等价推导；额外节点又不计分，故通过不等于内部推理因果忠实。", "basis": "model_inference", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页18，附录D。\n"}, {"text": "7B实验并未控制原始预训练，目标暴露后RL也含目标域数据，且缺少零额外暴露加相同RL的对照，不能证明额外暴露是必要条件。", "basis": "model_inference", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页23、25，F.2及表9。\n"}, {"text": "§5将1B监督tokens与100步RL并列为等预算，但表11将100步RL对应到2.10B；式9还将512K-token批量再乘序长。等算力结论需核对执行单位。", "basis": "model_inference", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页7、32、34。\n"}, {"text": "表10与正文难度配方不完全一致，尤其§I出现op=8–20预训练条目；未核实实际配置前，不能将该设置的op=15–20称为完全未见外推。", "basis": "model_inference", "locator": "TEXT_OR_TBaUfO9znF_787f7c6ee1cf：物理页28，附录I；物理页31，表10。\n"}]

minimal_check：{"question": "核心困难题覆盖增益是否对更大采样预算稳健？", "control": "固定100M Base与edge-RL检查点及同一op=15–20测试集；统一温度0.7、生成上限1024 tokens和验证器，将k从128扩至1024。", "observable_outcome": "比较逐题成功覆盖与配对不确定区间；差距消失支持概率重分配解释，持续存在仅支持更大有限预算下的优势。", "resources": "两个检查点、带gold DAG的测试集及采样算力；无需重新训练，GPU型号和所需时长未知。", "failure_or_stop_condition": "缺检查点或可靠gold图时停止；增益消失则不再将原pass@128结果作为稳健能力扩展证据。"}

missing_fields：["100M主结果中依赖图形读取的精确数值不可核读。", "未报告训练硬件、GPU时、总实验FLOPs、独立随机种子和置信区间；合成测试集题量未明确。", "500M/7B完整逐设置训练预算、真实任务过程验证细节及难度筛选成本未充分报告。", "预算单位、正文与表10配方冲突未解决；前作及历史新颖性未外部核读。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

三阶段交互的联合设计值得读；采用能力扩展或最优预算结论前，先核清验证器、实际FLOPs和更大有限采样下的覆盖差。

身份、版本与阅读范围：首物理页完整题名与输入清单一致；官方当前34页附件的哈希和Pro身份绑定通过。Pro按所供全页文本初评并说明图像未提供，符合实际材料。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心实验的验证器含义：附录D要求每个gold节点的依赖集合及数值正确，且末答案匹配；额外预测节点不进入ProcessAcc。它约束显式输出轨迹，不证明内部计算因果忠实，也可能拒绝不同但正确的分解；真实7B基准如何提供对应gold DAG未在所核页面落实。

核查定位：p018:L0003-L0047；process_metric_definition_checked_scope_limited

edge优势与排他措辞：原PDF Table2的困难op15–20：Base pass@1/128=14.6/45.3，edge-RL=26.2/53.2；easy-RL pass@128也为48.9，hard-RL为49.3。支持edge在该设置点估计最强，不直接支持只有edge才有任何外推增益。有限k的覆盖变化不能证明原模型概率支持集为零或发生扩张。

核查定位：p021:Table2, local_check/p021.png；reported_values_match_exclusivity_not_established

暴露比例与预算依赖：Table3在500M下0.1%目标暴露已有困难题pass@128=51.5%，1%=51.6%，所以1%不是通用阈值。Table4的60%RL混合为66.6，高于Full RL53.2；但附录L Observation8明确更高预算时纯RL的困难题pass@128最高，不能概括混合训练始终胜出。

核查定位：p022:Tables3-4, p034:L0019-L0032, local_check/p022.png；values_and_reported_exception_confirmed

等预算与分布口径：§5正文把1B监督tokens和100步RL并列为等预算，Table11却将100步RL列在2.10B预算行；需要实际执行单位才能采用精确等算力比较。p22把mid op9–12和RL op11–14称distributionally disjoint，但操作数支持有11–12重叠；若指其他维度或样本不重叠，应另给定义。

核查定位：p007:L0015-L0023, p034:Table11, p022:L0035-L0040；published_protocol_ambiguities_preserved

本地补充/限定：[{"kind": "additional_local_qualification", "detail": "补充所谓disjoint实验的操作数区间重叠；不能从文字把它当作难度支持完全分离的证据。"}]

核查局限：["未核查全部7B实验、所有配方冲突或过程奖励显著性，未执行生成器和训练。", "上述差值为论文点估计，不是本地重测或统计显著性裁决。", "未核读前作全文，L2保持为Pro暂定判断。"]


## pro019 · PRISM: Demystifying Retention and Interaction in Mid-Training

论文 OR_giNBsVVFGt；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_giNBsVVFGt_242fa396cbc6", "source_url": "https://api2.openreview.net/pdf?id=giNBsVVFGt\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页1–34全部已提供文本，包括正文、影响声明、参考文献、附录A–J及生成示例。连续页标齐全，题名与清单一致；未核读原PDF、前作或其他版本，未复现实验。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–10的图像不可见；图2实际混合采样百分比缺失，训练曲线只有部分文字标签，不能核验曲线形态或单调性。", "多数表格数值可辨；双栏存在串行，式(1)的概率比与嵌套运算排版失真，不能完整核对目标函数。", "附录J部分生成内容由作者主动删节，不等于材料缺页；当前附件是否最终出版版未经确认。"]}

问题：如何安排中训练数据、上下文长度及后续RL，使数学、代码和科学能力提升，同时识别一般能力与长上下文的损失？

方法：将一般网页、指令数据与领域推理文本混合，按Math-only、MC、MCS配置继续训练基座；用中训模型筛选RL题，再做GRPO。另研究15%基座与85%中训权重合并后追加长上下文训练。

作者主张：约27B高质量中训练能跨模型改善推理，并保持一般能力；领域混合存在协同。

论文证据：表3–5显示数学、代码明显提高，但一般能力并非逐项保持；Mistral-7B的GPQA-D从26.94降至24.07。

模型推断：支持配方的广泛实用性及任务间取舍，不支持所有能力无损提升。

定位：['TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页5–6，表3–5。\n']

作者主张：合并基座并进行短期长上下文训练，可恢复长上下文且维持推理收益。

论文证据：128k RULER显著恢复，但仍低于基座；代码提高同时伴随科学与部分数学指标下降。

模型推断：是已有操作的有效恢复配方，不是无代价保留保证。

定位：['TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页6–7，§7.1、表6；物理页13，附录B.3。']

作者主张：PRISM为RL提供稳定初始化，比直接对基座RL更有效。

论文证据：表16的MC/MCS跨阶段组合普遍改善领域得分；但作者明确报告Granite-4-H Micro的RL训练崩溃。

模型推断：支持已测稠密模型的初始化收益；稳定性不能推广到混合架构，更未证明中训练必不可少。

定位：['TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页17–20，附录G–I、表16；物理页8，§8。\n']

key_results：[{"setting": "Granite-3.3-8B，Base→MCS中训练。", "baseline": "同一基座模型。", "metric_or_guarantee": "作者报告分数；Code Avg为LCB/CF均值，Math Avg为AIME24/25/MATH500均值。", "reported_values_and_units": "Code Avg：2.07→10.58；Math Avg：8.95→48.75；GPQA-D：22.56→29.12。LB-V1：66.15→66.48，但HellaSwag：83.46→78.12，TruthfulQA：52.24→46.96，均为分。", "information_and_compute": "约27B tokens、8k上下文；默认25000步、AdamW、学习率5e-5、bf16。数学每题采样64次，代码3次，最大生成32k tokens；未提供完整GPU成本。", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页5表3、物理页12表8、物理页13表10、物理页14附录C。\n"}, {"setting": "Granite-3.3-8B，MC中训练→权重合并→全参数长上下文训练。", "baseline": "原基座及未恢复的MC中训模型。", "metric_or_guarantee": "RULER与领域得分，不构成恢复保证。", "reported_values_and_units": "128k RULER：基座59.09、中训6.46、合并后恢复42.16。相对中训，Code Avg：10.71→25.54；GPQA-D：19.02→15.82；MATH500：74.22→68.91，均为分。", "information_and_compute": "15%基座+85%中训权重；追加1000步，使用长样本筛选和BFD打包；实际训练总tokens未报告。", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页7表6、物理页13表11–12。\n"}, {"setting": "Granite-3.3-8B，MCS中训练后使用MC数据做RL，取表16所列结果。", "baseline": "MCS中训检查点；另对照MC中训后同样使用MC做RL。", "metric_or_guarantee": "领域平均分及GPQA科学得分。", "reported_values_and_units": "Code Avg：10.58→20.38；Math Avg：48.75→52.04；GPQA：29.12→52.86。MC中训→MC RL的GPQA为35.52分。", "information_and_compute": "筛后19k数学、17k科学、7k代码题；MC组合不使用科学题。RL默认每步64题×16响应、1000步、16k上下文、学习率5e-7；GB200节点，卡数与GPU小时未报。", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页15附录E、物理页17表15、物理页20表16。\n"}]

prior_work_candidates：[{"citation_as_printed": "Wang, Z., Zhou, F., Li, X., and Liu, P. Octothinker: Mid-training incentivizes reinforcement learning scaling, 2025.", "identifier_if_present": "arXiv:2506.20512", "relation_candidate": "方法继承", "shared_component": "中训练促进RL、加入一般指令数据、问答文本格式。", "claimed_difference": "由主要数学研究扩至多域、能力保留及更多模型。", "basis": "target_paper_only", "target_locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页3§3、物理页12附录A.1、物理页11参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Zhang, C., Neubig, G., and Yue, X. On the interplay of pre-training, mid-training, and rl on reasoning language models, 2025.", "identifier_if_present": "arXiv:2512.07783", "relation_candidate": "同期独立工作", "shared_component": "比较预训练、中训练与RL的阶段作用。", "claimed_difference": "本篇称该研究主要为小规模，PRISM扩展至3–24B模型。", "basis": "target_paper_only", "target_locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页2–3§2、物理页11参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Liu, E., Neubig, G., and Xiong, C. Midtraining bridges pretraining and posttraining distributions, 2025.", "identifier_if_present": "arXiv:2510.14865", "relation_candidate": "同期独立工作", "shared_component": "中训练连接训练阶段并保留一般能力。", "claimed_difference": "PRISM侧重领域混合、长上下文及下游RL的联合评测。", "basis": "target_paper_only", "target_locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页2§2、物理页10参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心新增主要是既有中训练→RL路线的多域、多模型验证与配方改进；失败边界有实用价值，但尚未建立可区分的新机制解释。", "central_increment": "前作已研究中训练促进RL（仅据本篇转述）；本作新增更广评测、长上下文恢复和跨阶段数据组合证据，支持位置为表3–16。", "soundness_observation": "固定token预算的对照有价值，但“保留”“必要”“普适稳定”强于实际证据；平均分、筛题机制和部分数据不一致需分别审查。", "significance_observation": "对训练配方选择与避免能力回退有工程参考价值；覆盖范围不等于新算法或因果机制。", "main_open_question": "排除中训模型筛题、格式门槛及额外监督和算力后，相对直接RL的优势还剩多少？"}

limitations：[{"text": "作者承认跨模型预训练数据和规模不同，不能将收益直接归因于架构；混合架构RL稳定性尚未解决。", "basis": "author_report", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页5§6、物理页8§8、物理页18–19附录I。"}, {"text": "RL题由PRISM模型筛选，且不满足<think>格式即不给正确性奖励，可能不利于基座；未提供等总训练算力的充分对照。", "basis": "model_inference", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页15附录E–F、物理页18附录H。\n"}, {"text": "未见重复训练及置信区间；没有完整领域因子设计或移除一般网页的对照，不能严格归因协同和保留机制。去污染流程、评测提示及科学采样设置不充分。", "basis": "model_inference", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页3–5§3–5、物理页12附录A、物理页14附录C。"}, {"text": "同一MC分项的Math Avg在表4/8/16为44.33，表6为44.99，口径未解释；J.9是缓冲液题，J.11却是光子题生成，不能据此作同题阶段比较。", "basis": "model_inference", "locator": "TEXT_OR_giNBsVVFGt_242fa396cbc6：物理页5/7/12/20，表4/6/8/16；物理页30–32，J.9–J.11。\n"}]

minimal_check：{"question": "基座的RL劣势是否被思考格式门槛放大？", "control": "同一小批RL题分别由基座与PRISM采样16次；对同一批输出同时按原格式门槛和仅答案正确性评分，不重新训练。", "observable_outcome": "比较格式有效率、答案正确率及被门槛抹去的正确响应比例。", "resources": "需两个8B检查点、原提示格式与正确性验证器；推理硬件和耗时未知。", "failure_or_stop_condition": "取消门槛后差距不缩小，则该混杂解释不获支持；缺检查点或奖励实现则停止。此检查不证明等算力优势。"}

missing_fields：["图2完整数据采样权重及配方搜索预算", "长上下文恢复的实际训练长度与总tokens", "中训练硬件、RL节点数量、GPU小时和完整评测成本", "科学评测采样与代码多样本聚合细节", "重复训练方差、完整去污染记录", "表间数值及附录科学示例不一致的解释"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

当前贡献研究已能把它定位为有实用价值的多域配方与边界证据；暂不加深机制归因。若后续要实际采用该训练路线，再优先检查等总预算和格式门槛对照。

身份版本范围：首物理页题名与承接候选一致，官方当前34页全文和Pro的ID/哈希匹配；Pro声明完整文本已读且图像不可见，范围相符。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心配方价值与保留边界：Table3显示Granite3.3-8B从Base到Math+Code+Science：LB-V1均值66.15→66.48，但HellaSwag83.46→78.12、TruthfulQA52.24→46.96。Table4领域分数增加为Code2.07→10.58、Math8.95→48.75、GPQA-D22.56→29.12。均值保持不能解释为所有能力无损，Pro的局部配方价值判断有来源依据。

核查定位：p005:Tables3-4；reported_scores_and_retention_tradeoff_checked

长上下文恢复的决定性数值：原PDF Table6确认128k RULER为59.09→6.46→42.16（Base、MC、15/85合并加全参数LC）；恢复后仍未回到基座。相对MC，Code Avg10.71→25.54同时GPQA-D19.02→15.82、MATH50074.22→68.91。支持有效恢复配方，不是无代价恢复保证。

核查定位：p007:Table6, local_check/p007.png；values_and_cross_capability_costs_match

直接RL比较的潜在混杂：附录E用中训后的Granite模型每题16响应筛选RL题；F规定只有满足thinking格式才评正确性，不符给0奖励，另有结束与重复惩罚。该条件可能影响基座对照，未量化之前不能作为已证明优势根因，也不能据此确认中训练是必要阶段。

核查定位：p015:L0023-L0032, p015:L0060-L0063, p016:L0062, p017:Table15, p018:L0063-L0068；selection_and_reward_contract_confirmed_causal_effect_unmeasured

稳定性及计算范围：Table15为64题×16响应、1000步、16k上下文、KL系数0.05、GB200节点；缺卡数和GPU小时。附录I明示Granite-4H-Micro曾先提升后退化并出现不连贯输出，不能把成功的稠密模型结果推广为全部架构稳定。

核查定位：p017:Table15, p018:L0070-L0079；hyperparameters_and_failure_case_checked

本地补充/限定：[]

核查局限：["未复核全部七模型、重复训练方差、数据污染或额外训练成本。", "Pro提出的其他Math Avg及示例对应问题未逐项独立核验；此处不当作已确认错误。", "无前作全文核读、作者代码执行或实验复现；L1是暂定模型判断，不等于没有价值。"]


## pro020 · Post-Training with Policy Gradients: Optimality and the Base Model Barrier

论文 OR_nnWlTi7A7a；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_nnWlTi7A7a_4d6e5772f142", "source_url": "https://api2.openreview.net/pdf?id=nnWlTi7A7a\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_nnWlTi7A7a_4d6e5772f142：物理页1–9，正文§1–7；页10–11，致谢、影响声明及参考文献；页12–24，附录A；页24–28，附录B；页28–34，附录C。连续页标1–34齐全，均已阅读所供文本。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1、图2仅图注及混杂坐标文本可见，不能核验曲线或读取精确图示数值。", "双栏交错及公式上下标、分式局部失真；未逐式校勘，也未独立证明全部定理。", "前作全文、其他版本及代码内容未提供；未搜索、下载或复现。"]}

问题：基座模型的正确序列概率如何限制PG后训练的误差与奖励查询成本？过程反馈能否绕开序列级稀疏奖励障碍？

方法：固定特征ϕ，仅训练自回归softmax线性权重；将0/1奖励PG转写为凸对数损失上的在线梯度下降，使用梯度范数自适应步长。LQ描述正确整序列概率的低分位，token-level LQ描述正确前缀下最差下一token概率的低分位。Algorithm 1/2先采当前策略，失败后分别整序列或逐token从基座与Uniform等权混合中探索；自适应保证对应随机选取的迭代模型。

作者主张：ORM下PG变体近minimax最优，LQ刻画突破基座低覆盖区域的指数查询障碍。

论文证据：Corollary 3.6给出多查询PG上界；Theorem 5.3–5.4对特定阶梯LQ困难族给出下界；Theorem 5.5给出监督预训练的最坏LQ限制。

模型推断：实质新增是覆盖质量与查询复杂度的联系，而非将coverage profile取广义逆这一命名；最坏情形不等于每个低LQ实例都困难。

定位：['TEXT_OR_nnWlTi7A7a_4d6e5772f142：页5–9，§3.2、§5；页29–34，附录C。']

作者主张：过程奖励通过token-level LQ消除奖励查询数对N的指数依赖。

论文证据：Theorem 4.1及附录B将最坏查询上界从含k^N变为含Nk。

模型推断：揭示反馈粒度带来的计算分离，但使用了更强的监督oracle，不能解释为免费算法改进。

定位：['TEXT_OR_nnWlTi7A7a_4d6e5772f142：页7–8，Theorem 4.1、Algorithm 2；页24–28，附录B。']

作者主张：简单自适应SGD与PG可实现近最优统计及在线学习保证。

论文证据：SGD测试错误界由常数步长的Õ(N/(γ²T))改为Õ(1/(γ²T))；Uniform行为PG累计错误上界Õ(k^N/γ²)，对应下界在足够长时域为Ω(k^N/(Nγ²))。

模型推断：是已有优化组件上的非平凡分析；N=1时具有独立在线分类价值，但一般N下每步高效不代表总查询数为多项式。

定位：['TEXT_OR_nnWlTi7A7a_4d6e5772f142：页4–5，Proposition 2.2、Remark 3.3及脚注；页8，Theorem 5.4。']

key_results：[{"setting": "ORM、Assumption 2.1；令m=min{ceil[Q_q0((1−o(1))ε)^−1],k^N}。", "baseline": "固定混合行为策略、每轮一次查询：Q=T=Õ(m/(γ²ε))。", "metric_or_guarantee": "随机迭代模型满足1−E[p(y*|x)]≤ε。", "reported_values_and_units": "Algorithm 1：T=Õ(1/(γ²ε))次迭代，期望奖励查询Q=Õ((m+ε^−1)/γ²)。Theorem 5.3在特定阶梯LQ困难族上给Q=Ω̃(Q_q((1+o(1))ε)^−1/γ²)及T=Ω(1/(γ²ε))下界。", "information_and_compute": "精确ORM，可对同一context多次查询；下界要求D≥k/γ²及定理规定的γ范围。查询复杂度不等于FLOPs。", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页6，Corollary 3.4、3.6；页8，Theorem 5.3；页19，查询预算证明。\n \n"}, {"setting": "监督预训练n个独立样本，输出固定特征的线性自回归策略q。", "baseline": "所有此类监督预训练算法。", "metric_or_guarantee": "最坏情形下的LQ上限。", "reported_values_and_units": "D≥k/γ²时，存在满足margin条件的分布，使n≲1/(γ²ε)时Q_q(ε)≤k^−N。", "information_and_compute": "计监督样本，不是训练时间；不能理解为所有数据分布上的结论。", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页8–9，Theorem 5.5；页33–34，附录C.3。\n"}, {"setting": "精确PRM、Algorithm 2；a=min{QTL_q0((1−o(1))ε)^−1,k}。", "baseline": "ORM多查询算法最坏Q=Õ((k^N+ε^−1)/γ²)。", "metric_or_guarantee": "期望生成错误≤ε。", "reported_values_and_units": "T=Õ(1/(γ²ε))；Q=Õ((Na+ε^−1)/γ²)，最坏为Õ((Nk+ε^−1)/γ²)次奖励查询。", "information_and_compute": "查询验证正确前缀；逐token探索预算另含被Õ隐藏的log N因素。", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页7，Theorem 4.1；页26–27，证明。\n"}, {"setting": "合成混合数据，N=128、d=k=32；比较on-policy ORM与PRM。", "baseline": "相同基座初始化的ORM后训练。", "metric_or_guarantee": "低初始概率中心的正确序列概率及测试错误。", "reported_values_and_units": "作者将初始概率<10^−12的4/32个中心归为off-support，正文报告PRM改善而ORM未改善；具体终点数值无法核验。", "information_and_compute": "基座Adagrad 1000步、学习率0.1、batch 256；PG 4000步、学习率0.1、batch 1024；训练批次均为新抽样，测试1024例。硬件与耗时未报告。", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页9，§6；图1图像不可见。\n \n"}, {"setting": "Qwen3-8B与Qwen3-8B-Base，Math-500共500题。", "baseline": "Qwen3-8B-Base。", "metric_or_guarantee": "用每题采样正确率估计LQ。", "reported_values_and_units": null, "information_and_compute": "每题64次生成，temperature=0.7、top-p=0.95、top-k=50；图示LQ数值不可核验，硬件及生成长度预算未报告。", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页6，图2a；页9，§6。\n"}]

prior_work_candidates：[{"citation_as_printed": "Chen, F., Huang, A., Golowich, N., Malladi, S., Block, A., Ash, J. T., Krishnamurthy, A., and Foster, D. J. The coverage principle: How pre-training enables post-training. arXiv preprint arXiv:2510.15020, 2025a.", "identifier_if_present": "arXiv:2510.15020", "relation_candidate": "理论扩展", "shared_component": "coverage profile及自适应监督优化思路。", "claimed_difference": "转向PG后训练的查询复杂度与下界；监督分析无需大mini-batch。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页1、4–5、12；参考文献页10。", "prior_actually_read": false}, {"citation_as_printed": "Chen, F., Jia, Z., Rakhlin, A., and Xie, T. Outcome-based online reinforcement learning: Algorithms and fundamental limits. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025b.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "ORM在线学习及复杂度问题；未确认算法继承。", "claimed_difference": "本篇称前作侧重样本复杂度、计算效率不清，转而分析可实现PG变体。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页1，§1；参考文献页10。", "prior_actually_read": false}, {"citation_as_printed": "Beygelzimer, A., Pal, D., Szorenyi, B., Thiruvenkatachari, D., Wei, C.-Y., and Zhang, C. Bandit multiclass linear classification: Efficient algorithms for the separable case. In Proceedings of the 36th International Conference on Machine Learning, volume 97 of Proceedings of Machine Learning Research, pp. 624–633. PMLR, 2019.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "可分多类线性分类、bandit反馈及错误界。", "claimed_difference": "作者声称在较弱margin条件下达到N=1的近最优高效保证，并推广到序列。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页3，§1.2；页5，Remark 3.3；参考文献页10。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是非平凡复杂度保证及ORM—PRM计算分离，超过局部调参；仍处于既有PG与coverage框架内，未证路线级首创。", "central_increment": "前作已研究覆盖与监督训练（本篇转述）；本作在γ可分固定特征序列模型中新增LQ依赖的PG上下界及PRM多项式保证，证据见§3–5；全流程障碍的联合量词仍待核。", "soundness_observation": "已阅读附录论证但未完成形式核验。C.1与C.3使用不同困难标签族，不能仅由两个独立最坏下界自动推出每个低LQ模型均面临指数查询困难。", "significance_observation": "有助于区分统计样本效率、奖励查询成本与监督粒度；不是端到端Transformer、标准PPO或GRPO的直接保证。", "main_open_question": "能否对同一预训练输出及任务族联合证明低LQ与指数ORM查询难度，充分支撑端到端base-model barrier解释？"}

limitations：[{"text": "假设精确过程奖励；学习PRM、噪声及不可分响应仍是开放扩展。", "basis": "author_report", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页9，§7。"}, {"text": "off-support指概率极小，不是严格零支撑；64次生成全错不能证明真实成功概率为零，Qwen模型对照也不能独立识别RL的因果作用。", "basis": "model_inference", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页2，§1；页6，图2讨论；页9，§6。"}, {"text": "合成实验使用on-policy Adagrad，而最优理论主要针对指定自适应步长及探索策略；相同步数不代表ORM与PRM等查询或等算力。", "basis": "model_inference", "locator": "TEXT_OR_nnWlTi7A7a_4d6e5772f142：页4、6–9；页20，Proposition A.8。"}]

minimal_check：{"question": "C.3的低LQ困难族本身是否也强制指数ORM查询？", "control": "对照Algorithm 1混合探索，测试依次查询1^N、2^N后使用相同监督更新的结构化策略。", "observable_outcome": "是否至多两次ORM查询即可恢复每个context的完整标签，从而区分低LQ与逐实例搜索困难。", "resources": "附录C.3及Lemma C.3即可先作纸笔核查，无需LLM训练；未实测任何运行成本。", "failure_or_stop_condition": "若常数次查询成立，则停止把两个独立下界直接拼接为逐实例障碍，要求联合困难构造；这不自动否定各自的minimax定理。"}

missing_fields：["Math-500实验的可核验LQ数值及图1、图2精确曲线结果缺失。", "硬件、耗时、完整生成预算及多随机种子不确定性未报告。", "部分前作未印唯一标识，相关identifier_if_present为null；前作内容均未核读。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

LQ、统计样本和奖励查询分离对理解后训练边界有价值；继续阅读时重点核查完整量词、行为策略及精确前缀oracle，而非直接套用到真实LLM。

身份版本范围：题名匹配，官方当前34页附件、全文哈希及Pro ID一致。Pro声明读完所有所供文本，图像未提供，材料范围相符。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心保证的模型假设：§2冻结特征ϕ，只训练softmax线性权重；每个context有唯一正确序列，正确前缀上满足γ-margin且特征范数有界。这不是端到端Transformer或标准GRPO的一般保证。

核查定位：p003:L0019-L0042；model_class_and_margin_scope_confirmed

过程奖励提供的额外信息：Eq4要求精确判定整个前缀是否等于唯一正确前缀。Theorem4.1以指定Algorithm2和自适应步长给T=Otilde(1/(γ²ε))、Q=Otilde((N*min(QTL逆分位,k)+ε⁻¹)/γ²)，保证随机迭代模型的期望生成错误。最坏查询项Nk与ORM的k^N不同，但反馈更强，查询数也不等同FLOPs或墙钟。

核查定位：p007:Eq4,Theorem4.1, local_check/p007.png；formula_units_and_feedback_condition_checked

与监督训练比较的限制：Corollary4.2另需AssumptionB.3，且同页作者明确这一组合尚未优于相同监督标签预算下的自适应SGD。不能概括为PG无条件优于监督训练。

核查定位：p007:Corollary4.2 and following paragraph；additional_condition_and_author_caveat_confirmed

最坏下界量词：C.3明确称其构造不同于前两个定理，正确序列为(B_i,…,B_i)、B_i∈{1,2}。这支持保留Pro提出的联合困难族问题：独立的预训练低LQ和后训练最坏查询界不能被本地直接拼成每个低LQ实例的端到端障碍。未执行其两候选查询检验，也未裁定是否存在其他联合证明。

核查定位：p033:L0030-L0042；construction_difference_observed_joint_claim_unverified

本地补充/限定：[]

核查局限：["未完成附录所有证明或最优性优先权审计，未重跑合成或Qwen实验。", "Pro提出的常数查询对照仍是后续问题，不作为本地已执行或已证明的反例。", "无前作全文核读或新增第二轮模型调用。"]

