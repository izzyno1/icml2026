# 单轮全文初评与有界本地核对 31–40

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro031 · Reasoning Models Struggle to Control their Chains of Thought

论文 OR_3el4fMYQU6；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_3el4fMYQU6_868c052a8ba9", "source_url": "https://api2.openreview.net/pdf?id=3el4fMYQU6\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_3el4fMYQU6_868c052a8ba9：物理页1–29连续全文，包括正文§1–6、Impact Statement、参考文献、附录A–F及后续图表和提示词的可提取文字。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未见缺页；仅提供全文文本，没有PDF图像。统计图的曲线、柱形及误差线不可核读，不从散落图标签重建数值。", "双栏文字存在交错，公式排版可能失真；表格和图题仅按可读文本使用。", "未提供前作全文、逐题实验记录或代码内容；未搜索、复现或执行论文中的指令。"]}

问题：保持原任务目标时，模型能否按要求修改CoT且不透露修改约束，从而具备潜在的监控规避能力？

方法：给既有任务追加抑制、添加、风格修改三类共九种CoT约束。抑制词由GPT-5提出候选，再依据8模型×3次基线轨迹筛选。主要采用程序评分，Ignore question使用GPT-5-mini；约束合规与Meta Discussion分报。比较原生CoT、最终输出及输出空间中的外显推理，并进行压力测试和训练检查点分析。

作者主张：提出CoT controllability及CoT-Control，作为监控规避风险的可测代理。

论文证据：覆盖五个任务来源、九种约束、十二个推理模型，设输出/外显推理对照及理解检查；实例总数存在文本内冲突。

模型推断：新增价值是把CoT控制与一般输出指令遵循分开测量，不是直接证明监控安全。

定位：['TEXT_OR_3el4fMYQU6_868c052a8ba9：p3–4 §2、表1–2；p15 A.1']

作者主张：原生CoT比输出难控制；规模增大提高可控性，更难、更长的推理及推理训练通常降低可控性。

论文证据：通道对照、控制协变量的回归、推理effort变化和开放训练检查点呈现相关趋势。

模型推断：形成有价值的经验区分，但尚未识别导致低可控性的机制。

定位：['TEXT_OR_3el4fMYQU6_868c052a8ba9：p4 §3；p6–8 §5；p17–21 附录D']

作者主张：默认低可控性对多种压力提示较稳健，但情境感知和重复尝试可提高合规。

论文证据：正文报告情境提示最高约增加4个百分点；十轮GEPA式搜索对三种留出约束迁移不可靠；逐题反馈可产生较大提升。

模型推断：低单次合规不能解释为更高尝试预算下的能力上限。

定位：['TEXT_OR_3el4fMYQU6_868c052a8ba9：p2 发现4；p5–6 §4；p15–16 附录B']

key_results：[{"setting": "主评估：十二个推理模型、五个数据来源、九种约束，数据源等权。", "baseline": "输出控制；另选三个推理模型和三个非推理模型测试外显CoT控制。", "metric_or_guarantee": "约束合规率；不是任务正确且成功隐蔽规避的联合成功率。", "reported_values_and_units": "正文概括：多数模型CoT合规率低于10%；多数输出对照达到至少60%，推理模型外显CoT对照多数达到至少70%。不重建图中逐模型数值。", "information_and_compute": "部分原始CoT通过保密内部日志取得；总调用量与费用未报告。", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p4 §3、脚注4。\n"}, {"setting": "CoT长度逻辑回归，控制模型、数据集、约束类型和问题领域。", "baseline": "较短的推理轨迹。", "metric_or_guarantee": "合规赔率比，属于相关关系。", "reported_values_and_units": "长度每增加一个标准差，约2,000词，合规赔率比为0.79，p<0.001；不是合规概率下降21个百分点。", "information_and_compute": "使用生成轨迹词数；此回归没有识别长度的独立因果效应。", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p7 §5.3；p16–17 C.1。\n"}, {"setting": "Olmo-3.1-7B-RL-Zero-Code训练检查点；简化QA约束。", "baseline": "较早检查点及作者设计的输出控制对照。", "metric_or_guarantee": "CoT与输出合规率随训练变化。", "reported_values_and_units": "作者在正文报告CoT合规率降低逾一个数量级，输出下降较慢；完整曲线数值无法由本轮材料核对。", "information_and_compute": "自托管评估缩减至1,066个test questions，生成上限15,000 tokens，temperature=0.6、top_p=0.95；使用既有检查点，评估GPU时未报告。", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p2 发现2；p17 D.1–D.2"}, {"setting": "IRPAIF：每数据集抽25题，失败后追加GPT-5-mini反馈，最多十次尝试。", "baseline": "同一实验子集第0轮。", "metric_or_guarantee": "CoT合规率提升，单位为百分点。", "reported_values_and_units": "正文报告GPT-OSS-120B/20B分别增加44/27个百分点；Qwen3-32B/14B增加31/12个百分点；Claude 3.7增加30个百分点，Sonnet 4.5增加5个百分点。", "information_and_compute": "反馈含高层错误诊断和1–3句违规原文；未报告完整调用及token成本。", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p15 附录B。\n"}]

prior_work_candidates：[{"citation_as_printed": "Emmons, S., Jenner, E., Elson, D. K., Saurous, R. A., Rajamanoharan, S., Chen, H., Shafkat, I., and Shah, R. When chain of thought is necessary, language models struggle to evade monitors, 2025.", "identifier_if_present": "arXiv:2507.05246", "relation_candidate": "背景引用", "shared_component": "CoT必要性与监控规避难度。", "claimed_difference": "本篇据此研究可控性代理与任务难度的关系，并扩展到多类约束和训练因素；不能确认具体协议继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p6 §5.1；p9 References", "prior_actually_read": false}, {"citation_as_printed": "Zolkowski, A., Xing, W., Lindner, D., Tramèr, F., and Jenner, E. Can reasoning models obfuscate reasoning? stress-testing chain-of-thought monitorability, 2025.", "identifier_if_present": "arXiv:2510.19851", "relation_candidate": "背景引用", "shared_component": "通过混淆推理降低CoT可监控性。", "claimed_difference": "本篇采用三类代理及通道、训练对照；未逐项证明这些增量未被该前作覆盖。", "basis": "target_paper_only", "target_locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p14 References；p20 附录E", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是统一代理评测及跨模型、训练历程的经验知识，超过单场景性能改进；尚不足以认定路线级首创。", "central_increment": "前作已研究监控规避与CoT必要性（本篇转述）；本作新增多约束、跨通道及训练检查点比较；尚待排除长度和评分协议造成的表观差异。", "soundness_observation": "有对照、回归和理解检查，但不是机制证明。Olmo-32B在DPO/RL阶段可部分恢复，不能概括为各阶段单调下降。", "significance_observation": "可作为安全评估的辅助诊断维度，但低代理分数不保证真实监控有效。", "main_open_question": "统一轨迹长度、解析和评分口径后，原生CoT的低可控性及训练下降趋势还剩多少？"}

limitations：[{"text": "代理不覆盖全部真实规避情境，未测试其他语言，RL影响机制未明。Sonnet 4/4.5长链可能被摘要化；作者认为可能导致低估。", "basis": "author_report", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p8 §6 Limitations"}, {"text": "全链零违规指标天然对长文本更严格；合规与元讨论分报，也不要求同时正确完成任务，不能直接替代真实监控规避率。", "basis": "model_inference", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p3 §2.4；p4–5 §3；p7 §5.3"}, {"text": "RL实验输出对照去掉抑制项，且允许约80%格式合规；CoT采用更严格判据。Base/RL-Zero还剪去末尾10%并过滤回复，削弱对照等价性。", "basis": "model_inference", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p18–19 D.2–D.3；p21 图18提示词。\n"}, {"text": "规模文本冲突：§2写14,076实例，引言/结论写13,176；表2 Agent总题数写350，但分项100+150=250。按分项计算为1,464题、13,176实例，不能据此擅自确定实际运行清单。", "basis": "model_inference", "locator": "TEXT_OR_3el4fMYQU6_868c052a8ba9：p2 引言；p3 §2；p4 表2；p8 结论"}]

minimal_check：{"question": "RL后的可控性下降是否主要来自推理变长？", "control": "使用Olmo-Code早晚检查点的共同题目及三种风格约束，以同一解析和严格规则比较固定200词前缀与原全链指标；记录短链排除比例和任务正确率。", "observable_outcome": "等长后的合规差异及违规位置分布，判断下降是否仍存在。", "resources": "需要逐题原始日志和评分器；附件未提供。若需重跑，硬件与费用未知。", "failure_or_stop_condition": "等长后差异消失则不支持独立于长度的RL侵蚀解释；日志不全或短链筛选严重改变样本组成时停止归因。"}

missing_fields：["统一后的实例清单、各实验有效分母及逐题记录。", "正文与图20关于Ignore question元讨论结论的不同方向及筛选口径解释。", "逐实验解码配置；附录F将temperature sampling写为0，pass@k采样与独立性说明含混。", "完整图形、评分器实现、保密原始CoT、总token/API/GPU时及费用。", "前作全文及当前附件的最终出版身份核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可控性提供有用的辅助诊断；继续阅读应优先检查等长、统一解析与相同合规判据后的差距，并联合记录任务正确率和真实监控器表现。

身份、版本与阅读范围：题名、29 页官方当前附件、材料哈希和 Pro 返回绑定一致。Pro 完成全部提供文本的一轮初评；本地核看所列页及三张 PDF 页面，未取得保密内部日志或作者代码。

核查定位：text_delivery_manifest.json, structured/pro031.json, p002:L0001；verified_with_scope_limit

核心代理和评分分母：三类九种约束的合规率与是否提及约束的 Meta Discussion 分报，不要求同时完成原任务且成功隐蔽规避。整段零违规判据会给长文本更多失败机会，所以逻辑回归赔率比 0.79/约 2000 词标准差不能解释为独立因果效应或概率下降 21 个百分点。原 PDF 第 2 页图 1a 支持明显通道差距：9/12 个原生 CoT 合规率低于 10%，但这组输出合规率至少 60% 的是 6/12，不能把正文的“多数”概括直接套给该图全部十二模型。QA 子集图另有分母。

核查定位：p003:L0046-L0060, PDF physical page 2, Figure 1a, p007:L0027-L0048, p021:L0056-L0058；central_pattern_confirmed_quantifier_narrowed

实例总数冲突：原 PDF 第 4 页表 2，QA 为 300+445+469=1214，Agent 分项 100+150=250，Agent 合计却印 350。分项共 1464 题，乘九为 13176，与引言一致，但 §2 写 14076。保留全部原印数值，没有擅自改动实际运行清单或补足缺题。

核查定位：PDF physical page 4, Table 2, p002:L0029-L0033, p003:L0028-L0034；source_count_inconsistency_confirmed

训练阶段趋势与控制不等价：原 PDF 第 18 页图 13 明示 7B Base/SFT/DPO/RL 为 10.6/0.8/1.3/1.1%，32B 为 13.1/0.8/0.3/2.6%；并非逐阶段单调下降，32B 是 RL 阶段回升，DPO 仍下降。RL 比较还简化部分约束、过滤不足 20 token 或非助手式回复，并对 Base/RL-Zero 截掉末尾 10%。输出对照删除抑制项，裁判允许约 80% 格式合规，不是同一严格全链判据。

核查定位：PDF physical page 18, Figure 13 and D.2, p017:L0046-L0062, p019:L0044-L0054, p021:L0021-L0034；training_trend_and_measurement_asymmetry_confirmed

单次低合规不构成能力上限：附录 B 每数据源抽 25 题，最多十次带反馈尝试，报告 GPT-OSS-120B/20B 增加 44/27 个百分点、Qwen3-32B/14B 增加 31/12 个百分点。它改变反馈与尝试预算，作者也声明其设置不够现实；不能把默认一次低分当作真实恶意规避成功率的上界，亦不能将这组提升直接外推部署。

核查定位：p015:L0029-L0046；elicitation_budget_scope_confirmed

本地补充/限定：["本地新增图 1a 精确分母：十二模型中输出至少 60% 为六个，原生 CoT 低于 10% 为九个；保留 QA 子集另报的范围。", "将 Olmo-32B 的阶段描述细化为 13.1→0.8→0.3→2.6，避免笼统说 DPO 与 RL 都恢复或训练逐阶段单调降低。", "实例总数冲突和输出判据不等价已核实，未因此推断全部趋势失效。"]

核查局限：["没有请求隐藏思维链、执行规避提示、重跑模型或进行训练；原文提示只作研究数据。", "未核验全部图形、评分器及逐题数据，未复算逻辑回归或统计显著性。", "没有核读该篇外部前作，暂定 L2 不构成历史首创确认。", "Pro 仅看提供文本，本地只观察三页 PDF；结论不构成系统安全保证。"]


## pro032 · Sycophancy Towards Researchers Drives Performative Misalignment

论文 OR_rLFIOikFR2；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4", "source_url": "https://api2.openreview.net/pdf?id=rLFIOikFR2\n", "version_role": "current_attachment_unverified_role", "physical_pages": 19}], "read_ranges": ["TEXT_OR_rLFIOikFR2_3f45c8e1f9c4：物理页1–19全部已提供文本，含正文§1–8、声明、参考文献及附录A–H；连续页标完整，未发现缺页标。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–11不可见，不能读取柱高、误差线或逐特征结果。物理页17–18主要仅剩图题。", "双栏文本局部交错，表1列对齐损坏；表3–5主要数值可辨。未将当前附件认定为最终出版版。", "未提供前作全文、其他版本、原始实验输出或代码；未外搜、执行代码或复现实验。"]}

问题：评测与部署条件下的行为差异，是否也能由迎合研究者预期解释，而不必归因于保护自身目标的scheming？

方法：用研究者/普通用户文风构造StyleCues，以EVAL回答率或Python类型提示F1测线索敏感性；对GPT-OSS-20B第11层TopK SAE（k=64）进行探测和方向干预；再用SDF建立类型提示与评测的关联，比较三类迎合数据微调。

作者主张：提出performative misalignment：模型可能为迎合研究者而表现失配，alignment faking不直接证明scheming。

论文证据：部署提示下仍有评测判断；评分相关特征有条件差异；两类特征干预及迎合微调均可影响评测代理。

模型推断：提供有实质价值的替代解释，但未直接识别迎合导致失配的完整因果链。

定位：['TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p9 §8及Impact Statement，p15附录D。\n']

作者主张：用StyleCues检验无显式评测标签时的文风敏感性。

论文证据：GPT-5生成100对段落；标准评测使用100条均衡提示，另有240条thinking/instruct比较。

模型推断：新增可操作评测，但测得文风分类不等于真实部署状态识别。

定位：['TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p3 §3，p13–14附录B。\n']

作者主张：迎合微调增强evaluation awareness，且不明显增加广泛失配。

论文证据：四模型中三者的代理指标提升达到作者报告的显著性阈值；失配结论主要对应不可见图表。

模型推断：支持微调改变代理行为，不足以证明迎合特质是唯一中介。

定位：['TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p7 §6，p8图8题注。\n']

key_results：[{"setting": "部署系统提示；每模型240条提示，研究者/普通文风各120条。", "baseline": "同家族Instruct检查点对比Thinking检查点。", "metric_or_guarantee": "输出EVAL的比例，不是分类准确率，也不是StyleCues类型提示F1。", "reported_values_and_units": "Instruct→Thinking：Qwen3-80B为11.7%→42.5%；Qwen3-235B为39.6%→48.9%；Kimi-K2为50.0%→78.2%。作者报告各总体差异p<0.05。", "information_and_compute": "不同检查点比较；推理token预算、运行成本未报告。", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p14附录B.2表5。\n"}, {"setting": "GPT-OSS-20B对已有alignment-faking响应做前向计算；Free/Paid各200例，每组50个特征。", "baseline": "Free监控条件与Paid非监控条件。", "metric_or_guarantee": "Mean Activation及Prevalence；表内为均值±标准误。", "reported_values_and_units": "A3 Ratings：MA为0.07±0.03对0.04±0.02；Prevalence为13.7±3.8%对8.6±2.9%，差5.1个百分点。B2对应差值为MA 0.02、Prevalence 3.0个百分点。", "information_and_compute": "第11层、TopK k=64；Prevalence阈值为样本平均激活>0.1。硬件及时间未报告。", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p5–6 §5.1–5.2、表3–4。\n"}, {"setting": "GPT-OSS-20B在StyleCues上的SAE方向干预。", "baseline": "未干预模型；迎合相关与scheming相关方向相互比较。", "metric_or_guarantee": "类型提示F1；正文称两类方向带来相近提升，逐方向数值不可见。", "reported_values_and_units": null, "information_and_compute": "每组六类中的top10特征，λ=0.2；无效代码超过10%的方向标为N/A，具体剔除比例不可核。", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p6 §5.3、p7图7题注。\n"}, {"setting": "SDF及三类迎合数据微调后的StyleCues评测。", "baseline": "各自base model，另比较insecure、secure、educational微调。", "metric_or_guarantee": "类型提示F1的双侧t检验。", "reported_values_and_units": "GPT-OSS-120B、Qwen3-30B、Qwen3-235B的p值依次为0.016、0.012、0.037；GPT-OSS-20B为0.089。绝对F1及增幅因图6不可见而缺失。", "information_and_compute": "使用Tinker；GPT-OSS-120B判定类型提示。训练样本量、超参数、随机种子及资源成本未报告。", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p7 §6.1–6.2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDiarmid, M., Marks, S., Treutlein, J., Belonax, T., Chen, J., Duvenaud, D., et al. Alignment faking in large language models. arXiv preprint arXiv:2412.14093, 2024.", "identifier_if_present": "arXiv:2412.14093", "relation_candidate": "组件复用", "shared_component": "Free/Paid条件及alignment-faking-rl数据。", "claimed_difference": "针对目标保持解释加入研究者迎合替代机制；不是完整复现或排除原解释。", "basis": "target_paper_only", "target_locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p5 §5.1、p10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Hua, T. T., Qin, A., Marks, S., and Nanda, N. Steering evaluation-aware language models to act like they are deployed. In The Fourteenth International Conference on Learning Representations, 2026.", "identifier_if_present": "OpenReview:1TdRdf0fkw", "relation_candidate": "方法继承", "shared_component": "类型提示代理、评测意识干预及SDF设置。", "claimed_difference": "增加文风线索评测，并比较迎合与scheming相关干预。", "basis": "target_paper_only", "target_locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p3 §3、p7 §6.1、p10参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是对安全评测动机归因提出有实验支持的替代解释，而非新增底层算法；暂定为机制理解层面的实质贡献。", "central_increment": "前作已研究评测条件相关行为及其干预（本篇转述）；本作增加研究者迎合假说、文风评测和干预证据，但尚待排除代理测量与一般顺从性混淆。", "soundness_observation": "证据更直接支持评测代理可变，而非迎合驱动失配。另，表3–4不支持正文所称A3差异约为任意其他类别的3倍：相对B2仅为0.03/0.02和5.1/3.0。\n", "significance_observation": "有助于避免把行为差异直接解释为隐藏意图；尚未提供减少真实失配风险的方法，工程资源要求也未充分报告。", "main_open_question": "控制研究者预期、训练监控和一般指令遵从后，迎合增强是否仍改变实际alignment-faking行为，而不仅是其代理？"}

limitations：[{"text": "作者明确不排除scheming；evaluation awareness仅指行为对评测线索的敏感性，不代表意识。", "basis": "author_report", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p9 Impact Statement。\n"}, {"text": "部署实验依赖scheming模型会依据评测判断调整行为的假设；作者承认复杂策略可能违背该假设。", "basis": "author_report", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p4 §4.1。\n"}, {"text": "合成文风、事后元询问和类型提示可能测到刻板分类或顺从性；Thinking/Instruct不同检查点也不能单独识别推理预算的因果效应。", "basis": "model_inference", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p3 §3、p13附录A–B。"}, {"text": "探测是在GPT-OSS上读取既有响应，不等于原生成模型的动机测量；评分关注也可能服务于目标保持，两组特征的语义专属性未确立。", "basis": "model_inference", "locator": "TEXT_OR_rLFIOikFR2_3f45c8e1f9c4，p5 §5.1、p6 §5.2、p19表7。\n"}]

minimal_check：{"question": "研究者预期是否直接改变实际规则违背，而非仅改变评测代理？", "control": "同一无害规则冲突任务中，正交操纵研究者期待与训练监控；固定文风、SDF流程，比较base及迎合微调检查点。", "observable_outcome": "直接校验规则违背率及其置信区间，检验预期翻转效应是否被迎合微调增强。", "resources": "需两类检查点、成对提示及推理环境；样本量须按统计功效确定，费用未知。", "failure_or_stop_condition": "若仅代理变化而实际行为不变，或预期效应可由监控条件解释，则不支持所检验的迎合驱动解释。"}

missing_fields：["图3–11的细分数值、误差线及能力/失配完整结果；steering具体F1为null。", "SDF及迎合微调规模、训练配置、种子、硬件、运行时间与API费用。", "独立迎合操纵检验、t检验独立样本单位及多重比较处理。", "附录B部分比较使用237/238而非240例的剔除说明。", "前作核读、跨版本比较及原始结果复核。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

替代动机解释有研究价值；下一步应直接测量相同规则冲突任务中的行为变化，并正交控制研究者期待、监控状态、文风与一般指令遵从。

身份与提供范围：题名、19 页官方当前附件、全文文本和 Pro 返回哈希一致。Pro 一轮初评覆盖所有已提供文本；本地核看列出页面并观察原 PDF 第 6、14 页。原文中的模型提示仅当作实验材料，没有执行。

核查定位：text_delivery_manifest.json, structured/pro032.json, p003:L0001；verified_with_scope_limit

中心替代解释与实际因果链：StyleCues 是 GPT-5 生成研究者/普通文风的 100 对段落再配编程题，标准实验用 100 条均衡提示；类型提示 F1 测的是文风相关评测代理。附录 D 明确把 A→B 从前作承接，本篇主要检验 M→A，未在同一实验中直接建立迎合→真实失配的完整链条。Impact Statement 也明确不排除 scheming，不能从标题推断已替代或排除其他动机。

核查定位：p003:L0011-L0039, p015:L0019-L0039, p009:L0013-L0022；causal_claim_narrowed_to_tested_link

SAE 探测对象与关键差值：探测把既有 alignment-faking 响应连同提示送入 GPT-OSS-20B 的第 11 层 SAE，不能直接等同于测量原响应生成模型的动机。原 PDF 第 6 页表 3/4 确认 A3 的均激活差 0.03、Prevalence 差 5.1 个百分点，B2 为 0.02、3.0；按印出值比值约 1.5 和 1.7，未支持正文称两指标均为任意其他类别约三倍。关注评分也可能服务于目标保持，特征组名称不保证语义专属性。

核查定位：p004:L0050-L0071, p005:L0037-L0061, PDF physical page 6, Tables 3–4 and §5.3；values_confirmed_overstatement_and_probe_scope_qualified

EVAL 比例与检查点比较：原 PDF 第 14 页表 5 确认 Instruct→Thinking 的 EVAL 回答比例：11.7→42.5、39.6→48.9、50.0→78.2%。这是回答 EVAL 的比例，既不是分类准确率，也不是类型提示 F1；Thinking/Instruct 不同检查点的差值不单独识别推理预算因果作用。该页同时出现 240 总提示与 237/238 的配对比较分母，未解释的剔除口径保留。

核查定位：PDF physical page 14, Table 5 and B.3, p013:L0062-L0068；reported_values_and_denominators_confirmed

微调与干预的适用边界：微调前通过 SDF 建立类型提示与评测的关联，再比较迎合数据微调；正文三个显著 p 值为 0.016/0.012/0.037，20B 为 0.089，但未充分说明独立样本单位、重复种子和多重比较。steering 无效代码超过 10% 的方向排除为 N/A。改变代理输出支持其可变性，不足以判定迎合是唯一中介或真实失配风险降低。

核查定位：p007:L0027-L0057, p007:L0028-L0034, p015:L0041-L0053；intervention_scope_confirmed_statistics_not_reproduced

本地补充/限定：["通过原 PDF 确认 A3 与 B2 印出差值不支持约三倍概括，未使用未公开精确值或宣称重新检验显著性。", "把研究者迎合解释限定为有实验支持的候选机制，保持作者不排除 scheming 的原有范围；EVAL 频率与准确率/F1 分开。"]

核查局限：["未执行微调、steering、危险任务、作者提示或代码；没有新模型实验。", "未核看所有图表或原始日志，未验证绝对 steering F1、统计独立性或多重比较。", "未核读外部前作；当前候选机制并非已完成历史或因果穷尽验证。", "Pro 仅看全文文本，本地仅观察两张 PDF 页面；L2 保持 AI 暂评。"]


## pro033 · A Positive Case for Faithfulness: LLM Self-Explanations Help Predict Model Behavior

论文 OR_nkJIMejfaN；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_nkJIMejfaN_ea98772317a6", "source_url": "https://api2.openreview.net/pdf?id=nkJIMejfaN\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_nkJIMejfaN_ea98772317a6：物理页1–51全部已供文本，包括正文1–9、参考文献10–14、目录15及附录16–51；连续页标齐全，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图中可提取的题注、标签和案例文字已读，但未核验曲线、点位、颜色及误差线。", "双栏文字交错，部分公式排版有损；NSG定义可辨。目录列有计算资源条目，但所供全文未见对应资源小节。", "未提供前作全文、代码及逐例实验记录；未搜索、复现或比较其他版本，不能认定为最终出版版。"]}

问题：自解释能否在已知原问题与模型答案之外，帮助观察者预测模型对邻近输入的回答？评估对象是模型行为，不是任务答案是否正确。

方法：将六个表格数据集离散化、去重，构建Hamming距离≤2、m=10、ε=0.3且真实标签平衡的邻域；Moral Machines另行程序生成。参考模型每个独特输入生成一次答案及解释，随机安排答案前后顺序。五个预测器分别在有、无解释条件下预测反事实回答；先平均准确率，再计算NSG=(A有−A无)/(1−A无)。无需新增训练，主结果使用用户可见解释。

作者主张：NSG结合自然、多概念反事实，为更强模型提供持续的忠实性评估信号。

论文证据：给出归一化定义、邻域构造及距离、提示词、预测器消融。

模型推断：属于已有可模拟性框架的实用升级；未证明NSG等价于内部因果忠实性或信号必然持续。

定位：['TEXT_OR_nkJIMejfaN_ea98772317a6：p003–005，§2–3；p017–020，A.3–A.4；p030–031，A.11']

作者主张：18个参考模型的自解释平均均有预测价值，同时存在高度误导实例。

论文证据：表3全部模型平均NSG为正；表1所列模型的高度误导比例为5.8%–15.1%；部分模型在Moral Machines上为负NSG。

模型推断：支持局部行为预测的平均净收益，不等于相同比例的解释具有真实推理忠实性。

定位：['TEXT_OR_nkJIMejfaN_ea98772317a6：p006，表1；p016，表3、A.2。\n']

作者主张：自身解释优于外部解释，说明模型具有外部观察者无法取得的自知识。

论文证据：同原答案、跨家族替换解释后，各家族自身解释的NSG均更高。

模型推断：支持解释携带模型特定的预测信息；不能证明该信息原则上无法由外部输入输出学习。

定位：['TEXT_OR_nkJIMejfaN_ea98772317a6：p007，§5、表2；p029–031，A.10、表9–10']

key_results：[{"setting": "Heart Disease、Pima Diabetes、Breast Cancer Recurrence、Employee Attrition、Income、Bank Marketing及Moral Machines，各1000问–反事实对。", "baseline": "预测器可见原问题、原答案和反事实问题，但不可见解释。", "metric_or_guarantee": "反事实模型回答预测准确率、绝对增益及NSG；均为作者报告。", "reported_values_and_units": "18模型绝对增益3.78–10.82个百分点，NSG为11.03%–36.51%。Gemma 3 4B准确率70.37%→81.19%，NSG为36.51%，95% CI [34.31%,39.01%]。", "information_and_compute": "五预测器：gpt-oss-20b、Qwen3-32B、gemma-3-27B-it、GPT-5 mini、gemini-3-flash；每条件单次预测。资源仅注明DeltaAI及OpenRouter，表17注明API实验为2026年1月；总token、GPU时及费用未报告。", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p005，§3；p016，表3；p009致谢；p039，表17。\n \n"}, {"setting": "表2跨家族解释替换；各家族至多三个较大模型，解释原答案相同。", "baseline": "其他家族模型对同一原问题、同一答案生成的解释。", "metric_or_guarantee": "自身解释NSG减去跨模型解释NSG。", "reported_values_and_units": "Qwen +3.0 [2.1,3.8]；Gemma +1.7 [0.9,2.6]；GPT-5 +4.3 [3.5,5.0]；Claude +2.3 [1.6,2.9]；Gemini +2.7 [1.8,3.6]。单位均为NSG百分点，方括号为95% bootstrap CI。", "information_and_compute": "按家族汇总；未匹配原答案的外部解释不参与。不是外部模型经过目标行为拟合后的最强对照。", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p007，§5、表2；p030，A.10.1。\n"}, {"setting": "Moral Machines单独评估，参考模型为Gemma 3 12B。", "baseline": "相同原问题与答案信息，但不给解释。", "metric_or_guarantee": "按数据集拆分的NSG。", "reported_values_and_units": "NSG为−30.4%，95% bootstrap CI [−44.9%,−17.4%]；不能由全数据平均正值推出每个任务均受益。", "information_and_compute": "主实验预测器体系下的任务分解；该数据集没有客观任务真值，但仍可评估模型回答预测。", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p016，A.2；p036，C.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Hase, P., Zhang, S., Xie, H., and Bansal, M. Leakage-adjusted simulatability: Can models generate non-trivial explanations of their behavior in natural language? Findings of the Association for Computational Linguistics: EMNLP 2020, pp. 4351–4367, 2020.", "identifier_if_present": "10.18653/v1/2020.findings-emnlp.390", "relation_candidate": "方法继承", "shared_component": "用有、无解释的预测差衡量解释增益。", "claimed_difference": "本作增加剩余错误归一化及数据驱动反事实邻域。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p003，§2.2；p011参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Chen, Y., Zhong, R., Ri, N., Zhao, C., He, H., Steinhardt, J., Yu, Z., and McKeown, K. Do models explain themselves? Counterfactual simulatability of natural language explanations. In Forty-first International Conference on Machine Learning, 2024.", "identifier_if_present": "OpenReview:99jx5U81jx", "relation_candidate": "方法继承", "shared_component": "通过解释预测邻近输入上的模型行为。", "claimed_difference": "本篇称前作只测有解释准确率；本作扣除基线，并减少合成编辑的分布偏离。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p008，§6；p010参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Hong, P. and Roth, B. Do LLM self-explanations help users predict model behavior? Evaluating counterfactual simulatability with pragmatic perturbations, 2026.", "identifier_if_present": "arXiv:2601.03775", "relation_candidate": "同期独立工作", "shared_component": "反事实可模拟性及自解释的正面预测价值。", "claimed_difference": "本篇称同期工作使用单域LLM生成反事实；本作扩展领域、模型并加入自解释优势对照，独立性未核验。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p008，§6；p011参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "归一化指标本身偏局部改进，但跨模型、跨领域的正平均增益及自身解释对照提供了有边界的新实证知识；不足以判为全新路线。", "central_increment": "前作已有可模拟性与增益思想；本作在局部分类邻域中增加归一化、多变量采样和模型特定信息对照，支持解释具有实际预测价值。", "soundness_observation": "正平均增益有清晰基线和多项消融支持；内部推理忠实性、自知识不可外部取得的结论强于现有对照。", "significance_observation": "有助于行为层面的解释审计，不提供内部机制识别、任务正确性或安全保证。", "main_open_question": "严格匹配题目、预测器集合、权重与解释长度后，自解释相对外部解释的优势是否仍然成立？"}

limitations：[{"text": "作者明确NSG依赖反事实与预测器质量，是平均情形指标；自由文本生成仍未解决，随机性和评估意识可能干扰测量。", "basis": "author_report", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p009，Limitations；p037–039，D。\n"}, {"text": "高度误导仅要求带解释时五预测器全错，没有要求无解释时正确，故不能解释成由解释造成的错误比例；A.3也显示增益包含纠正预测器的错误变答倾向。", "basis": "model_inference", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p017，A.3.1；p023，A.9.1。\n \n"}, {"text": "§5称预测器同时排除参考模型与解释器的家族，但A.10.1式8只明确排除解释器家族；可能改变比较构成，不能未核实现就认定对照完全匹配。", "basis": "model_inference", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p007，§5；p029–030，式6–8。\n"}, {"text": "自然数据主张须限定：Attrition被表15标为Synthetic，Moral Machines由15000个程序生成场景配对。标签平衡和邻域筛选也不保留原部署分布。", "basis": "model_inference", "locator": "TEXT_OR_nkJIMejfaN_ea98772317a6：p035，B.1；p037，表15。\n \n"}]

minimal_check：{"question": "自身解释优势能否通过严格配对对照保留？", "control": "取一个数据集、两个异族参考模型的同原答案交集，固定同一个第三家族预测器、同题权重及长度匹配的自身/外部解释。", "observable_outcome": "比较配对准确率差及NSG差，按原问题聚类bootstrap报告区间。", "resources": "需要逐例问答与解释缓存、一个预测器的API或本地推理资源；具体费用未知。", "failure_or_stop_condition": "优势消失或区间覆盖零，则该子实验不支持可检出的自身优势；无法构造相同题目与预测器集合时停止解释该差异。"}

missing_fields：["原PDF图像、前作全文、代码和逐例日志未提供。", "主实验解码参数、随机种子及一致性上界估计的重复采样次数未完整披露。", "GPU配置、GPU时、总token及费用未报告。", "跨模型评测实际采用的预测器交集规则与样本权重待核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

具有明确无解释基线的正面行为预测证据，值得与提示干预和监控论文一起读；下一步重点是严格匹配预测器、样本与解释长度后的自身解释优势。

身份、版本与范围：官方当前附件的题名绑定、51 页清单、全文文本哈希与 Pro 返回一致。Pro 覆盖全部已提供文本；本地围绕指标、主表及跨模型协议核查所列页面，并观察原 PDF 第 16、30 页。

核查定位：text_delivery_manifest.json, structured/pro033.json, p003:L0001；verified_with_scope_limit

核心指标与比较对象：无解释基线已经看到原问题、原模型答案和反事实问题；带解释条件只多解释，预测目标是参考模型回答而非真实任务标签。NSG=(Awith−Awithout)/(1−Awithout) 衡量剩余可提升空间中的净预测增益，分母接近零时波动会放大；NSG 为正不能直接换算成同等比例的内部因果忠实解释。

核查定位：p003:L0030-L0058, p004:L0031-L0049, PDF physical page 30, equations 9–10；metric_and_information_baseline_confirmed

关键主表和平均结论的边界：原 PDF 第 16 页表 3 确认 18 模型平均增益均正，绝对增益约 3.78–10.82 个百分点。Gemma 3 4B 从 70.37% 到 81.19%，10.82/29.63≈36.51% 与 NSG 一致；其 CI 为作者报告，未重算。该页同时明确 Gemma 3 12B 在 Moral Machines 上 NSG=−30.4%，CI [−44.9,−17.4]%，故不能把全任务平均正值说成每个领域受益。

核查定位：PDF physical page 16, Table 3 and A.2；values_and_negative_task_exception_confirmed

自身解释优势的对照范围：正文 §5 要求预测器不属于参考模型与解释模型两方家族；原 PDF 第 30 页式 8 及其文字却只明确排除解释器家族。原答案匹配规则可读，但实际预测器交集与样本权重仍需代码确认。表 2 的各家族正 uplift 支持当前协议下的模型特定预测信息，不证明外部观察者原则上无法通过行为拟合取得该信息；不能先假定长度、文风与预测器组成已经全部控制。

核查定位：p007:L0007-L0044, p029:L0042-L0060, PDF physical page 30, equations 7–10 and answer matching；self_knowledge_interpretation_qualified_protocol_ambiguity_confirmed

高度误导与反事实样本构造：高度误导定义是带解释时五个预测器全错，没有要求无解释时正确，因此 5.8%–15.1% 不能作为解释导致新增错误的比例。反事实经离散化、去重、Hamming 半径≤2 和标签平衡筛选；Attrition 原表标 Synthetic，Moral Machines 程序生成 15000 场景再配对。其正面结果适用于所构造局部邻域，不是未经筛选的自然部署分布。

核查定位：p006:L0004-L0026, p023:L0023-L0024, p034:L0038-L0058, p035:L0003-L0044, p037:L0032-L0041；causal_denominator_and_sampling_scope_confirmed

本地补充/限定：["原 PDF 确认 NSG 主表及跨模型预测器排除规则的文本差异；未宣称已经核实实现采用哪一规则。", "明确保留正平均预测价值，避免因内部因果识别不足而把全部结果否定；同时不把高度误导比例读作由解释新增造成的错误。"]

核查局限：["没有执行新预测、重算 bootstrap、运行作者代码或获取原始日志。", "未核看其全部消融、图形和资源条目，也未验证反事实的现实可行性。", "外部前作未核读，当前 L2 为 AI 暂评；模型特定信息不等于已证实不可外部获得的自知识。", "Pro 仅看文本，本地仅观察两页 PDF。"]


## pro034 · Generalized Correctness Models: Learning Calibrated and Cross-Model Correctness Predictors from Historical Patterns

论文 OR_g9G7qyAzki；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_g9G7qyAzki_caa977b1bae8", "source_url": "https://api2.openreview.net/pdf?id=g9G7qyAzki\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "afb6f515658b682546d3d1210ded1fe121f52f2fd979f6faff4faa0f91b516d9", "source_pdf_sha256": "caa977b1bae874dcb1d2e7b3892fc4a86254edc757c0433a7462d5bcfcc1a2e6"}], "read_ranges": ["TEXT_OR_g9G7qyAzki_caa977b1bae8：物理页1—25全部提供文本；正文§1—5、参考文献、附录A—E.1及提示模板；连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像，未观看图1—4；部分双栏文字交错、公式符号失真。表格主要数值可辨，图中曲线与具体覆盖率不作图像核验。", "前作全文、代码及原始实验数据未提供；未外搜或复现，未确认最终出版版本身份。"]}

问题：正确性预测是否依赖生成模型的自知信息？多个模型的历史问答与正确性标签能否训练出共享、可迁移的校准预测器？

方法：将8个生成者的问答、模型名及正确性标签合并，以Qwen3-8B预测末位yes/no，输出P(yes)。仅该token计算交叉熵；LoRA rank32、batch16、学习率1e-5，默认1轮。可用独立5%标签进行spline校准。

作者主张：模型对自身正确性没有稳定的特权信息优势。

论文证据：成对及矩阵实验的自评项并非持续最佳；Answerless预测Llama3-70B时，Qwen准确率0.782，自评0.776。

模型推断：支持所测设置下没有稳定自评优势，不证明内部自知信息不存在。

定位：['TEXT_OR_g9G7qyAzki_caa977b1bae8：p14—17，附录A，表8—22。\n']

作者主张：GCM从多模型历史学习可迁移策略，以单个预测器兼顾判别与校准。

论文证据：MMLU多目标比较、两种留出生成模型、TriviaQA迁移及Spider实验支持其效用，但并非每项指标都改善。

模型推断：提供共享预测器的实证能力增量，尚不能把增益独立归因于生成者身份条件化。

定位：['TEXT_OR_g9G7qyAzki_caa977b1bae8：p4—7，§2、§3.2；p19表26—27；p22，§E。']

作者主张：回答表述、世界知识和问题难度历史均贡献预测能力。

论文证据：表32中GCM的Full、Answer-only、Answerless准确率依次为0.820、0.789、0.720。

模型推断：支持输入信息逐级增益；删除全文同时删除推理内容，不能纯粹归因为表述风格。

定位：['TEXT_OR_g9G7qyAzki_caa977b1bae8：p22，表32。\n']

key_results：[{"setting": "MMLU，预测Llama3.1-8B回答正确性；以下均为作者报告，Acc不是回答任务本身的准确率。", "baseline": "目标专用SCM", "metric_or_guarantee": "正确性预测Acc、AUROC、ECE", "reported_values_and_units": "SCM→GCM：Acc 0.792→0.820；AUROC 0.857→0.890；ECE 0.017→0.023，校准反而稍差。GCM后校准ECE为0.020。", "information_and_compute": "8组历史合并；单个GCM训练量多于单个SCM，非逐模型等量对照。", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p5，表2。\n"}, {"setting": "MMLU，Phi-3-mini与Qwen3-32B均未进入GCM训练。", "baseline": "各自使用目标历史训练的SCM", "metric_or_guarantee": "Acc、ECE、AUROC；无形式泛化保证", "reported_values_and_units": "Phi-3-mini，SCM→GCM：Acc 0.787→0.800、ECE 0.026→0.017、AUROC 0.853→0.876。Qwen3-32B：Acc 0.873→0.871、ECE 0.022→0.029、AUROC 0.876→0.877。", "information_and_compute": "GCM不使用这两个目标模型的历史训练样本；仍处于MMLU任务。", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p6，表6。\n"}, {"setting": "MMLU训练后迁移至TriviaQA；表7未明确目标生成模型。", "baseline": "TriviaQA上训练的SCM", "metric_or_guarantee": "Acc、ECE、AUROC", "reported_values_and_units": "SCM为0.844/0.023/0.895；迁移GCM为0.828/0.105/0.896；后校准GCM为0.844/0.031/0.896。", "information_and_compute": "校准使用5%目标数据及正确性标签；非完全零样本适配。", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p6，表7；p7，§3.4。\n"}, {"setting": "Spider，预测Qwen2.5-7B与Llama3.1-8B的SQL正确性。", "baseline": "各目标SCM", "metric_or_guarantee": "Acc、AUROC", "reported_values_and_units": "SCM→GCM：Qwen为Acc 0.766→0.805、AUROC 0.838→0.891；Llama为Acc 0.873→0.898、AUROC 0.901→0.929。", "information_and_compute": "另训练六生成者Spider GCM；官方训练集内部75/25划分，exact-match标签，不是QA→SQL零样本迁移。", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p5，表3；p22，§E。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Kapoor, S., Gruver, N., Roberts, M., Collins, K., Pal, A., Bhatt, U., Weller, A., Dooley, S., Goldblum, M., and Wilson, A. G. Large Language Models Must Be Taught to Know What They Don’t Know, December 2024.", "identifier_if_present": "arXiv:2406.08391", "relation_candidate": "方法继承", "shared_component": "用正确性标签微调LLM", "claimed_difference": "从单模型训练扩展为多生成者历史共享与跨模型评估。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p8，§4；p10参考文献；p20，§D。", "prior_actually_read": false}, {"citation_as_printed": "Shrivastava, V., Liang, P., and Kumar, A. Llamas know what gpts don’t show: Surrogate models for confidence estimation. arXiv preprint arXiv:2311.08877, 2023.", "identifier_if_present": "arXiv:2311.08877", "relation_candidate": "背景引用", "shared_component": "由另一模型估计目标模型正确性或置信度", "claimed_difference": "本篇转述前作为未训练的一对一代理，本作研究多模型联合训练及校准因素。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p12参考文献；p20，§D。\n", "prior_actually_read": false}, {"citation_as_printed": "Hernández-Orallo, J., Schellaert, W., and Martínez-Plumed, F. Training on the Test Set: Mapping the System-Problem Space in AI. Proceedings of the AAAI Conference on Artificial Intelligence, 36(11):12256–12261, June 2022.", "identifier_if_present": "doi:10.1609/aaai.v36i11.21487", "relation_candidate": "方法继承", "shared_component": "仅凭问题预测目标模型潜在正确性的assessor", "claimed_difference": "本作将其作为Answerless层，与答案及完整响应条件统一比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p9，§4；p10参考文献；p21，§D。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心价值是系统性的跨模型正确性泛化证据及输入因素分析，而非新网络结构。工程主体是数据构建、标准微调和实验覆盖，尚不足称路线级框架。", "central_increment": "前作已有正确性微调和代理预测（本篇转述）；本作新增多生成者共享训练、留出模型测试与校准迁移分析；尚待排除普通混合数据验证器即可解释增益。", "soundness_observation": "多任务、指标及消融较充分，但经验上无稳定自评优势不等于不存在自知；未给理论保证。附录有换种子检查，主结果仍缺系统置信区间。", "significance_observation": "共享预测器可能减少维护多个SCM的负担，并支持拒答；收益不包括提高原模型答案准确率，也不代表开放环境安全保证。", "main_open_question": "控制混合训练数据与预算后，生成者身份条件化是否仍带来可重复的额外收益？"}

limitations：[{"text": "作者明确观察到跨数据集校准退化、较小模型ICL无收益；联合数据集训练也未统一改善校准。", "basis": "author_report", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p6—7，§3.2—3.4；p18，表25。"}, {"text": "GCM对单个SCM同时增加历史样本与生成者多样性；延长SCM训练的表28不能单独排除此混杂。", "basis": "model_inference", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p4，§2；p18，§C.1；p20，表28。"}, {"text": "QA的judge身份与量化质检未交代；ICL模板写human labeled，与方法中的LLM判分表述不一致，不能视为全量人工金标。", "basis": "model_inference", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p3，§2；p9致谢；p24，ICL模板。"}, {"text": "作者报告GCM评估3511例约7.3分钟、0.125秒/例，但硬件未说明，不能据此推定部署或总训练成本。", "basis": "author_report", "locator": "TEXT_OR_g9G7qyAzki_caa977b1bae8：p7，§3.5。\n"}]

minimal_check：{"question": "生成者身份是否提供普通混合数据验证之外的增益？", "control": "相同骨干、问答标签、样本数、训练步数及校准集，仅比较保留与去除模型名的GCM。", "observable_outcome": "配对比较Acc、AUROC及ECE，并检查差异是否跨随机种子稳定。", "resources": "需原始正确性数据及两种配置的LoRA训练；硬件和运行成本未知。", "failure_or_stop_condition": "若去除身份未造成稳定退化，则削弱身份条件化的必要性解释，但不否定多模型汇总训练的价值。"}

missing_fields：["PDF图像及可核验的选择性预测曲线数据。", "QA判分模型身份、判分提示、量化质检与完整生成采样参数。", "训练/评测硬件、总训练时长、数据生成成本及主要结果的系统重复试验区间。", "表7明确的目标生成模型身份。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

共享预测器及迁移校准具有实际价值；继续阅读应检验同样混合数据与预算下，保留/去掉生成者身份的差异及漂移后的校准可靠性。

身份、版本和阅读范围：题名、25 页官方当前附件、全文哈希与 Pro 返回绑定一致。Pro 一轮初评覆盖全部提供文本；本地核查所列页，观察原 PDF 第 5、6 页。保持当前附件版本身份未核定的限定。

核查定位：text_delivery_manifest.json, structured/pro034.json, p003:L0001；verified_with_scope_limit

核心增量和公平比较的预算口径：GCM 用 Qwen3-8B 合并八个生成者的正确性历史，预测末位 yes/no；训练目标与输入模板明确。论文匹配的是一个 GCM 对八个 SCM 合计的数据和步数，不是一个 GCM 对单个 SCM 的等量数据。表 28 延长 SCM 训练仍未隔离混合数据量、来源多样性和模型名条件化各自的贡献。Answerless 保留问题，也不能据此排除世界知识作用或证明自知信息不存在。

核查定位：p003:L0022-L0056, p004:L0013-L0028, p004:L0030-L0054, p020:L0003-L0010, p022:L0017-L0024；method_and_resource_scope_confirmed

判别与校准指标分开：原 PDF 第 5 页表 2 确认 Llama3.1-8B 的正确性预测 Acc 0.792→0.820、AUROC 0.857→0.890，但 ECE 0.017→0.023，后校准为 0.020。第 6 页表 6 对留出 Qwen3-32B 的 Acc 0.873→0.871、ECE 0.022→0.029、AUROC 0.876→0.877，并非各项均胜。这里的 Acc 是判定目标回答对错的准确率，不是提升目标模型的答题准确率；没有把微小 AUROC 差异解释成已证显著优势。

核查定位：PDF physical page 5, Table 2, PDF physical page 6, Table 6；decisive_values_and_metric_scope_confirmed

跨数据集和 SQL 实验的实际信息条件：原 PDF 第 6 页表 7：MMLU→TriviaQA 的 GCM 为 Acc/ECE/AUROC 0.828/0.105/0.896；用 5% 目标正确性标签后校准为 0.844/0.031/0.896。目标 SCM 为 0.844/0.023/0.895，因此恢复 Acc 不等于校准完全一致，也不是零标签适配。Spider 另训六生成者 GCM，使用官方训练集内部 75/25 划分和 SQL exact-match 标签，不能读成 QA 模型直接零样本迁移至 SQL。

核查定位：PDF physical page 6, Table 7, p004:L0007-L0012, p007:L0003-L0018, p022:L0034-L0041；transfer_and_label_scope_confirmed

输入消融与标签来源：表 32 Full/Answer-only/Answerless 的 GCM Acc 为 0.820/0.789/0.720。删除完整回答同时移除了内容和推理，不能纯归因于措辞风格。QA 方法段用具备金标准的 LLM judge，ICL 模板却称 human labeled，不能把标签直接宣称为全量人工金标。3511 例约 7.3 分钟的推理数值有正文出处，硬件未列，不用于推定训练或一般部署成本。

核查定位：p022:L0003-L0011, p003:L0050-L0056, p024:L0009-L0018, p007:L0035-L0053；ablation_and_provenance_limits_confirmed

本地补充/限定：["原 PDF 确认判别改善与部分 ECE 退化并存，保留所有反向指标而不只汇总胜出项。", "将同预算明确为一个 GCM 对八个 SCM 的合计；后校准使用目标标签，SQL 另行训练，不把两种迁移混为一谈。"]

核查局限：["未训练、评测或重算校准曲线与置信区间；没有运行 SQL、作者代码或模型。", "未核看全部附录矩阵与拒答覆盖曲线；没有把 ECE 或 AUROC 当作开放环境安全保证。", "外部前作未独立核读，历史新颖性及模型名条件化必要性仍未确定。", "Pro 仅看全文文本，本地仅观察两页原 PDF；L2 为 AI 暂评。"]


## pro035 · SafeSeek: Universal Attribution of Safety Circuits in Language Models

论文 OR_XhkRBQd8gw；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_XhkRBQd8gw_204e22a21726", "source_url": "https://api2.openreview.net/pdf?id=XhkRBQd8gw\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_XhkRBQd8gw_204e22a21726：物理页1–9，正文、局限与影响声明。", "TEXT_OR_XhkRBQd8gw_204e22a21726：物理页9–12，参考文献。", "TEXT_OR_XhkRBQd8gw_204e22a21726：物理页13–20，附录A–H。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["题名匹配，连续物理页标1–20未见缺页；仅阅读所供文本，未查看PDF图像。", "图1–6不可见；不从图中文字碎片恢复数值。双栏、公式和表格增减标识存在粘连，可辨数值按原文分别记录。", "版本角色未经核验，不认定为最终出版版；前作全文未提供，未联网、执行代码或复现实验。"]}

问题：能否定位控制后门或安全拒答的稀疏子图，并据此干预安全行为而尽量保留通用能力？

方法：输入白盒模型和行为数据，固定原权重，以STE训练二值单元掩码。DMO联合学习稠密净化子图与稀疏目标电路，以输出匹配、密度及重叠惩罚约束分解；分别保留和消融验证。SaCirT随后选择性更新电路参数；helpfulness场景的更新方向交代不够清楚。

作者主张：以统一优化框架提取多粒度、功能完整的安全电路。

论文证据：给出STE和双掩码目标；表3比较粒度及去除STE后的性能。

模型推断：新增主要是安全专用双子图约束与混合粒度组织，而非首次梯度电路发现。

定位：['TEXT_OR_XhkRBQd8gw_204e22a21726：p4–5§4.2–4.5；p8表3。']

作者主张：后门和安全对齐由与通用能力正交的稀疏完整电路控制。

论文证据：报告保留/删除干预及ID/OOD结果，附录扩展至7–32B模型。

模型推断：支持安全行为的稀疏可干预性，但不足以证明正交性或完整机制。

定位：['TEXT_OR_XhkRBQd8gw_204e22a21726：p6–8表1–3；p17–18表4–5。']

作者主张：SaCirT高效去除后门，并在helpfulness微调中保持安全。

论文证据：附录D报告后门ASR降低及优于LoRA的部分安全—效用结果。

模型推断：具有应用价值，但定位后的选择性安全微调已有邻近前作。

定位：['TEXT_OR_XhkRBQd8gw_204e22a21726：p16–17§D。']

key_results：[{"setting": "LLaMA-3.1-8B-Instruct，Refusal后门；ID为Alpaca，OOD为TruthfulQA。", "baseline": "后门模型Gbkd。", "metric_or_guarantee": "ASR与5-shot通用能力；作者报告，非本地实测。", "reported_values_and_units": "Gclean掩码稀疏率0.42%；ASR：ID 100→0.0%，OOD 100→0.4%；GSM8K 72.5→72.0%，MMLU 68.8→67.2%，HellaSwag 56.6→57.0%。并非所有后门近零：同表LLaMA的Mislabel/BBC-News OOD ASR仍为30.1%。", "information_and_compute": "后门注入1000条、10%投毒；掩码训练100条、100epoch、lr=10^-2。A.2称掩码优化约30min，平台8×A100 80GB，单实验可用单卡；未逐模型绑定成本。", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p6表1、§5.1；p13§A.2。\n"}, {"setting": "LLaMA安全对齐；LLM-LAT为ID，AgentHarm为OOD。", "baseline": "原始对齐模型Gbase。", "metric_or_guarantee": "Llama-Guard-3-8B判定的ASR；区分稠密子图删除与独立稀疏电路保留。", "reported_values_and_units": "Gunsafe删除3.03%头和0.79%神经元，ASR由0.8/7.9%升至96.9/81.5%（ID/OOD），MMLU由69.7降至64.2%。另一个Csafe仅保留0.32%头和1.38%神经元，ID/OOD ASR均为0%。", "information_and_compute": "采用头+MLP神经元粒度；低ASR本身不能排除恒拒答或退化生成。", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p7表2；p8表3、§5.3。\n"}, {"setting": "LLaMA在HelpSteer2上微调；以下仅采用附录D.2数值。", "baseline": "原模型与LoRA。", "metric_or_guarantee": "AdvBench harmless率和GSM8K准确率。", "reported_values_and_units": "按原模型/LoRA/SaCirT顺序：harmless率94.5/89.8/93.8%；GSM8K 72.5/71.3/72.3%。主文§5.4的部分harmless数值不同，未合并。", "information_and_compute": "16epoch，lr=10^-4；微调样本数及端到端实测成本未报告。", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p17§D.2；p8§5.4。\n"}, {"setting": "附录G安全归因对比；表7未明确模型和粒度，不能直接与表3合并。", "baseline": "SHIPS、SN-Tune。", "metric_or_guarantee": "安全消融后的ASR、效用和资源。", "reported_values_and_units": "按SafeSeek/SHIPS/SN-Tune顺序：稀疏率0.32/0.29/4.34%；ID ASR 96.1/73.9/98.4%；GSM8K 55.3/62.5/49.7%；MMLU 64.2/69.3/32.8%。", "information_and_compute": "耗时分别22min/3h32min/13min，显存24/16/15GB；SafeSeek并非所有指标最优。", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p19表7。\n"}]

prior_work_candidates：[{"citation_as_printed": "Bhaskar, A., Wettig, A., Friedman, D., and Chen, D. Finding transformer circuits with edge pruning. Advances in Neural Information Processing Systems, 37:18506–18534, 2024.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "可学习掩码与稀疏约束下的梯度电路发现；仅判断思想层面关系。", "claimed_difference": "由边粒度转向混合单元粒度，并加入安全双子图目标。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p9参考文献；p15§B.4式23。\n", "prior_actually_read": false}, {"citation_as_printed": "Yu, M., Zhou, Z., Aloqaily, M., Wang, K., Huang, B., Wang, S., Jin, Y., and Wen, Q. Backdoor attribution: Elucidating and controlling backdoor in language models. arXiv preprint arXiv:2509.21761, 2025.", "identifier_if_present": "arXiv:2509.21761", "relation_candidate": "背景引用", "shared_component": "后门内部归因与行为控制。", "claimed_difference": "由注意力头因果分析/向量干预，改为多粒度子图联合优化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p12参考文献；p13–14§B.1。\n", "prior_actually_read": false}, {"citation_as_printed": "Zhao, Y., Zhang, W., Xie, Y., Goyal, A., Kawaguchi, K., and Shieh, M. Understanding and enhancing safety mechanisms of llms via safety-specific neuron. In The Thirteenth International Conference on Learning Representations, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "安全神经元识别及选择性微调；表7称SN-Tune。", "claimed_difference": "使用双掩码电路优化，而非单一神经元归因分数。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p12参考文献；p14§B.2；p19表7。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "相对本篇转述的可微剪枝、后门归因及安全神经元微调，明确增量是安全专用双掩码目标与混合粒度应用；现有证据不足以提升为新的机制理解或路线级框架。", "central_increment": "在已知安全行为监督下，联合寻找可干预的稠密/稀疏子图，并用于后续安全控制。", "soundness_observation": "有干预及效用对照，但没有功能完整性或正交性定理；若干结构推断、配置和数值报告需核对。", "significance_observation": "对白盒后门净化和微调安全保持有实用意义；有限模型实验不等于普适保证。", "main_open_question": "双掩码找到的子图是否真正实现功能分离，而非大量重叠、仅能操纵行为评分的子网？"}

limitations：[{"text": "作者承认未找到绝对最小电路，稀疏先验未必适用于稠密能力，超过100B模型未验证。", "basis": "author_report", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p9 Limitations。\n"}, {"text": "双掩码不强制互补。删除0.42%与独立Cbkd的98.3%稀疏率不是同一规模；交集相对全模型很小，不能证明相对Cbkd重叠很小或结构正交。", "basis": "model_inference", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p5式13；p7§5.2.2；p16§C。\n"}, {"text": "Csafe的低ASR缺少良性请求拒答率和生成质量对照，不能排除恒拒答/能力崩溃；未知触发后门也未被验证。", "basis": "model_inference", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p5§4.5；p7表2；p8§5.3。"}, {"text": "摘要称helpfulness微调排除安全电路，§4.4则仅优化电路，分场景规则未明确。将LoRA标为0%未更新比例也不是同口径真实参数/成本比较。", "basis": "model_inference", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p1摘要；p4§4.4；p16§D.1。\n"}, {"text": "默认γ在A.1为5、F为2。表8/9的LLaMA基线ASR亦不同于主表，且恰与Qwen基线相同；可能涉及配置或排版问题，不能自行修正。", "basis": "model_inference", "locator": "TEXT_OR_XhkRBQd8gw_204e22a21726：p13§A.1；p18表6；p19–20表8–9。\n"}]

minimal_check：{"question": "独立Cbkd是否能等同于从Gbkd删除以得到Gclean的部分？", "control": "固定一个Refusal检查点和未见测试集，比较原模型、作者Gclean、实际删除Cbkd后的模型及等规模随机删除对照。", "observable_outcome": "用一致单元分母报告交集占Cbkd比例、触发ASR、干净回答质量及MMLU。", "resources": "原检查点、两张原始掩码、测试样本及推理GPU；本项耗时和显存需求未知。", "failure_or_stop_condition": "若Cbkd大部分仍在Gclean内，或删除Cbkd显著损害效用，停止接受互补/正交解释；输出崩溃导致的低ASR不算成功。"}

missing_fields：["图像与前作全文。", "测试样本数、拆分去重、重复种子及ASR统计不确定性。", "统一稀疏度分母、公共骨架计数和原始掩码。", "SaCirT样本量、实际更新规则及同口径端到端资源。", "表7具体配置及冲突数值的对应实验记录。"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

保留为双掩码与安全相关稀疏干预的工程案例；目前结构分离、微调实施和资源口径的缺口较大，不继续投入本阶段之外的核读或实验预算。

身份与材料范围：题名、20 页官方当前附件、全文文本哈希与 Pro 返回绑定一致。Pro 初评覆盖全部所供文本；本地只核看所列页和原 PDF 第 6、8、17 页。没有获取模型权重、执行作者代码或安全干预。

核查定位：text_delivery_manifest.json, structured/pro035.json, p001:L0001；verified_with_scope_limit

中心双掩码机制及分离主张：式 10–13 联合优化两个掩码，以功能损失、密度与交叠惩罚约束，但未硬性强制互补。原 PDF 第 6 页图 2 与 §5.2.2 同时报 Cbkd 稀疏率 98.3% 和交集稀疏率 98.30%；若采用同一单元分母，印出值对应的交集保留比例与 Cbkd 保留比例均约 1.7%，不能据全模型交集小就推出相对 Cbkd 的低重叠。删除 0.42% 的部分与独立保留的 Cbkd 不是已证明同一集合；完整机制和正交性须原掩码与一致分母进一步支持。

核查定位：p005:L0019-L0054, PDF physical page 6, Figure 2, p007:L0023-L0049, p016:L0017-L0021；optimization_confirmed_structural_interpretation_not_established

决定性 ASR 与效用数值：原 PDF 第 6 页表 1 确认 LLaMA Refusal 的 ID/OOD ASR 为 100/100→0/0.4%，同时 GSM8K 72.5→72.0、MMLU 68.8→67.2、HellaSwag 56.6→57.0。同表 Mislabel OOD ASR 仍为 30.1%，不能把全部后门都概括为近零。第 8 页表 3 确认安全消融 ASR 上升时也有 MMLU 69.7→64.2 的效用损失。两种实验的 ASR 方向和任务目标不同，均不是普适安全保证。

核查定位：PDF physical page 6, Table 1, PDF physical page 8, Table 3 and §5.3；reported_values_and_exceptions_confirmed

低 ASR、更新方向与资源口径：论文自身无 STE 消融得到 ASR=0 但 GSM8K=0，显示低 ASR 可能来自能力崩溃。独立 Csafe 的近零 ASR 尚缺对应良性拒答和生成质量证据。摘要说 helpfulness 微调排除安全电路，而 §4.4 与 §5.4 写仅更新电路；D.2 没有补足该场景的精确冻结规则，故保留实施歧义。LoRA 被画作 0% untuned 的特殊模块口径，不能直接解释为全参数训练或同口径成本节省。

核查定位：PDF physical page 8, Table 3 and §5.5, p001:L0049-L0054, p004:L0027-L0038, p008:L0052-L0057, p016:L0057-L0068, p017:L0013-L0030；safety_and_implementation_limits_confirmed

helpfulness 数值与比较方法范围：原 PDF 第 17 页 D.2 的 LLaMA harmless 为 Base/LoRA/SaCirT 94.5/89.8/93.8%，GSM8K 为 72.5/71.3/72.3%；主文第 8 页却写 95.0→89.3 和约94.0，不能默默合并。附录 G 的 SafeSeek 22min/24GB 与 SN-Tune 13min/15GB、SHIPS 3h32min/16GB 也不是全部资源指标均优；表 7 模型/粒度未充分列明，未与主表拼接。

核查定位：PDF physical page 17, D.2, PDF physical page 8, §5.4, p019:L0003-L0031, p013:L0038-L0046；source_conflicts_and_cost_scope_retained

本地补充/限定：["本地原 PDF 确认表格、图 2 交集标签和 helpfulness 数值冲突；交集分析只在统一分母假设下解释，没有宣称核查过真实掩码。", "保留局部行为干预有效的证据，未将其扩大为完整机制或功能正交性；低 ASR 与效用保留必须联合报告。"]

核查局限：["没有执行后门构造、安全消融、微调或任何模型干预；作者方法仅作审读对象。", "未逐一验证全部超参数、附录模型或原始掩码，未重新计算 ASR 方差。", "没有核读所比较前作，L1 为当前 AI 暂评而非历史创新穷尽结论。", "Pro 仅看全文文本，本地只观察三个 PDF 页面。"]


## pro036 · Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis

论文 OR_ZhSS3msLRj；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62", "source_url": "https://api2.openreview.net/pdf?id=ZhSS3msLRj\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "1821271e18eb8c98f9db53178f3c6ade23b5dd55a11b51cb027fd761caf5ec3c", "source_pdf_sha256": "c0da5d13ac62c1ed7ddc3e5c42d44d7314b1145a8cff7cf030295038b640dbcc"}], "read_ranges": [{"source_id": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62", "physical_pages": "1-22", "sections": "全部连续页标：正文§1–7、Limitations、Impact Statement、参考文献及附录A–H；未发现页标缺口。"}], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–7仅有抽取文字，尤其p2、p5–7图例与数字错位，不能可靠重建各模型图值。", "表1–11主体文字可读；双栏顺序、少量符号和布局有损。未核读前作、下载其他版本或复现实验。"]}

问题：从代码代理多轮对话及工具日志中判断是否存在reward hacking并识别类别，比较单例检测和成簇对照。

方法：用Claude Code与Opus 4.5按分类表合成对话，经自动检查及三名工程师复核；将N条轨迹共同输入检测器，输出二分类、行为描述及相对依据，再用Opus 4.5将描述对齐真值类别。属于离线推理评测，不实施新的RL训练。

作者主张：提出覆盖54种reward hack的分类体系和人工验证的TRACE。

论文证据：517条轨迹，其中249条良性；平均26.5个utterances；分类表含4大类、10中类、54细项。

模型推断：是既有分类的代码场景细化和评测资源扩展，不是自然发生RL轨迹的采集。

定位：['TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p3–5 §3；p17 表2；p18–20 表3–6。\n \n']

作者主张：成簇对照比孤立分类更有效。

论文证据：作者报告GPT-5.2的Detection Rate由N=1时45%升至N=10时63%。

模型推断：支持此合成基准上的上下文评测改进，尚不能证明真实RL训练中的检测或抑制收益。

定位：['TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p5 §4.2–4.3；p6 §5/RQ1；p8 §7']

作者主张：语义型hack更难识别；增加良性对照有助检测。

论文证据：正文报告语义型Match Rate显著低于语法型，B由25%增至90%时各模型Match Rate改善。

模型推断：提供类别与上下文组成相关的经验线索，不足以确立根本性的语义推理障碍。

定位：['TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p7–8 §5/RQ2–RQ3；p17–18 附录E。\n']

key_results：[{"setting": "TRACE；gpt-5.2-2025-12-11；N=1与N=10", "baseline": "同模型孤立检测N=1", "metric_or_guarantee": "Detection Rate按§4.4定义为二分类macro-F1，不是hack召回率", "reported_values_and_units": "作者报告45%→63%，相差18个百分点；不能解释为检出全部hack中的63%。N=1的条件化Match Rate为61%。", "information_and_compute": "高推理、温度1，三次运行均值；主结果对应B及闭源API费用未明确报告。", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p6 §4.4、§5/RQ1；p8 §7。\n \n \n"}, {"setting": "六个检测模型；类别结果跨N=1、5、10平均", "baseline": "语法型漏洞，如测试修改、特定测试输入针对和覆盖率投机", "metric_or_guarantee": "Match Rate：条件于正确检测的类别macro、多标签F1", "reported_values_and_units": "正文概述语法型约0.6–0.95，语义型约0.0–0.4；这里只记录文字范围，不重建图5逐模型值。", "information_and_compute": "检测器不获完整taxonomy；描述映射由获得真值类别的Opus 4.5判分器辅助。", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p6 §4.4；p7 §5/RQ2；p16–17 附录D。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Shihab, I. F., Akter, S., and Sharma, A. Detecting proxy gaming in rl and llm alignment via evaluator stress tests. arXiv preprint arXiv:2507.05619, 2025.", "identifier_if_present": "arXiv:2507.05619", "relation_candidate": "方法继承", "shared_component": "reward hacking分类体系", "claimed_difference": "在代码场景细化到54细项。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p3 §2.2、§3；p11 References；同标识另列2026条目，版本未核。", "prior_actually_read": false}, {"citation_as_printed": "Gabor, J., Lynch, J., and Rosenfeld, J. Evilgenie: A reward hacking benchmark. arXiv preprint arXiv:2511.21654, 2025.", "identifier_if_present": "arXiv:2511.21654", "relation_candidate": "背景引用", "shared_component": "代码reward hacking基准及独立检测设定", "claimed_difference": "TRACE扩展多轮覆盖并研究成簇对照；未提供对EvilGenie的直接复现实测。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p3 §2.3；p5 §4.1；p9 References", "prior_actually_read": false}, {"citation_as_printed": "Zhong, Z., Raghunathan, A., and Carlini, N. Impossiblebench: Measuring LLMs’ propensity of exploiting test cases. In The Fourteenth International Conference on Learning Representations, 2026.", "identifier_if_present": "OpenReview:SeO4vyAj7E", "relation_candidate": "背景引用", "shared_component": "测试套件漏洞及测试用例利用", "claimed_difference": "扩展质量退化、上下文与环境类别，并加入多轮对照评测。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p3 §2.3、§3；p11 References", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "新增数据、分类细化和场景性检测收益明确；最有支持的增量是既有评测与异常检测思路的代码多轮扩展，尚未形成充分验证的新机制知识。", "central_increment": "前作已有代码hack基准和对照异常检测思想（仅本篇转述）；本作在合成多轮条件下新增TRACE与N/B评测，核心证据为45%→63%的macro-F1；待排除标签和计分口径混杂。", "soundness_observation": "N=1的Match Rate在RQ1中GPT为0.61，RQ3却称所有模型为0.35–0.41，聚合差别未解释。正文κ=0.82与表1二分类κ=0.776、类型κ=0.820不能混用；声称统计显著但未给充分检验细节。\n \n \n", "significance_observation": "有检测器压力测试价值；不直接支持真实训练中的hack发生率、抑制效果或普遍语义推理上限。", "main_open_question": "统一目标样本、标签和可复算的计分口径后，成簇对照的核心增益能否保留？"}

limitations：[{"text": "作者明确限定taxonomy覆盖，并承认合成噪声及生成流程向其他模型、harness迁移无保证。", "basis": "author_report", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p9 Limitations。\n"}, {"text": "分类把利用题意提示、示例代码、编译器报错等列为hack；须逐例证明奖励与任务目标冲突，否则语义困难可能部分来自标签争议。", "basis": "model_inference", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p19 表4–5。\n"}, {"text": "判分器只检查提供的真值类别并被要求宽松匹配，未说明真值外类别误报如何计罚；再条件化于正确检测，Match Rate的含义和跨设置可比性需审计。", "basis": "model_inference", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p6 §4.4；p17 附录D。\n"}, {"text": "改变N/B同时改变上下文长度和类别先验；未见等token、同目标对照，同任务成簇及B取整规则亦不清楚，不能把提升单独归因于比较推理。", "basis": "model_inference", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p5 §4.2；p7–8 §5/RQ3"}, {"text": "人类对照与建库标注是否独立未说明；筛除高分歧样本会限制一致率和人机差距的外推。图4人类分数本轮无法可靠核定。", "basis": "model_inference", "locator": "TEXT_OR_ZhSS3msLRj_c0da5d13ac62:p4–6 人工评测；p21 附录H。\n"}]

minimal_check：{"question": "核心增益及两处N=1 Match Rate能否由同一计分流程复算？", "control": "取得N=1/10逐样本预测，在相同目标集上重算二分类macro-F1；核对Match Rate的条件化分母及真值外误报处理，对照正文和图4/6。", "observable_outcome": "复算得分、跨N差值，以及0.61与0.35–0.41差异的明确来源。", "resources": "TRACE真值、原始预测、簇清单与计分脚本；已有日志时无需新增模型推理，本附件未提供这些文件，获取或重跑成本未知。", "failure_or_stop_condition": "日志不可得则无法完成；若统一口径后增益消失或分数无法对齐，暂停采信相应量化结论。"}

missing_fields：["原始轨迹全集、预测输出、分簇清单及可执行评测代码", "主结果B、样本权重、Match Rate完整实现与显著性检验细节", "生成及闭源API总token、费用、标注总工时", "可核对的图像、人类独立测试协议及前作全文"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可作多轮检测压力测试资源；继续阅读最先需要同目标样本、分簇清单及可复算计分，解释图文分数差异和标签边界。

身份、版本与范围：题名、22 页官方当前附件、文本材料哈希及 Pro 返回绑定一致。Pro 覆盖全部所供文本；本地检查所列页，观察原 PDF 第 6、7 页。附录提示和分类只作为论文材料，没有执行。

核查定位：text_delivery_manifest.json, structured/pro036.json, p003:L0001；verified_with_scope_limit

中心增量及数据来历：TRACE 是 Claude Code/Opus 4.5 合成、自动筛选并由三名工程师复核的轨迹集合，517 条、249 条良性；表 2 报总 13677 utterances、平均 26.5，不等于 26.5 个完整代理工具轮次。实验把多条轨迹联合输入，改变 N 与良性占比 B；GRPO 是分组类比，没有在此展示新的 RL 训练或真实线上投机发生率。

核查定位：p003:L0012-L0047, p004:L0031-L0068, p005:L0003-L0039, p017:L0003-L0013；dataset_and_method_scope_confirmed

核心收益与指标定义：原 PDF 第 6 页图 4 确认 GPT-5.2 的 Detection Rate 从 N=1 的 0.45 到 N=10 的 0.63。§4.4 明确定义它为二分类 macro-F1，不能称作 hack 召回率。Match Rate 则是条件于正确检测的细类别 macro、多标签 F1，不是端到端每条轨迹分类准确率。

核查定位：PDF physical page 6, Figure 4 and §4.4；decisive_gain_confirmed_metric_qualified

Match Rate 与标注一致性的原文口径：原 PDF 图 4 中 GPT-5.2 的 N=1 Match Rate 标 0.63，RQ1 正文却写 0.61（图中 Claude 的值为 0.61）；第 7 页图 6 对 GPT 的 N=1 又标约 0.414，RQ3概括所有模型约0.35–0.41。不同图的 B、分母或汇总方式未解释，不替作者统一这些值。表 1 二分类条目为 0.776、类型条目为 0.820，不能把正文 κ=0.82 当作二分类一致率。

核查定位：PDF physical page 6, Table 1 / Figure 4 / RQ1, PDF physical page 7, Figure 6 and RQ3, p005:L0025-L0031；source_value_and_aggregation_ambiguities_confirmed

判分类别、对照信息与标签边界：判分器得到真值类别，逐项宽松匹配检测器描述；真值之外的类别误报如何处罚未完整说明。N/B 同时改变上下文长度、类别先验和可见对照，未建立同目标、等 token 比较。分类表把题意提示、示例代码和编译器报错利用列为 hack，仍需逐例证明评价奖励与实际任务目标冲突，不能仅凭这些常见动作认定投机。高分歧样本被移除也限制了人类一致性及人机差距外推。

核查定位：p005:L0014-L0031, p016:L0020-L0067, p017:L0018-L0055, p019:L0034-L0049, p021:L0040-L0045；scoring_and_causal_limits_retained

本地补充/限定：["新增原图核查：图 4 的 GPT-5.2 N=1 Match Rate 是 0.63，正文为 0.61；保留两者及图 6 的约 0.414，不把 Pro 按正文摘录的 0.61 当成唯一图值。", "保留 0.45→0.63 的 macro-F1 核心结果，但不据该分数声称检出 63% 的全部 hack，也不把上下文增长的收益完全归因于比较推理。"]

核查局限：["没有运行合成提示、攻击代码、检测器或作者评测脚本；未取得原始轨迹和预测。", "未重算 macro-F1、显著性或人工一致率，未逐例判定全部 taxonomy 标签。", "外部前作未核读；L1 保持当前 AI 暂评。", "Pro 只看文本，本地仅观察两页原 PDF。"]


## pro037 · From Optimization to Generalization under Heavy-Tailed Data: The Role of Gradient Clipping

论文 OR_FGHVEJ2Jz9；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264", "source_url": "https://api2.openreview.net/pdf?id=FGHVEJ2Jz9\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_FGHVEJ2Jz9_2bef2ea00264：物理页1—35连续齐全，已阅读正文p1—9、参考文献p9—12、附录A p13—17、B p18—20、C p21—31、D p31—35。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文文本，未见原PDF图像；图1只有图注，曲线、误差线及具体性能数值不可核读。", "双栏串接及公式上下标存在失真，尤其p20、p30的复杂分段式；表1文字可读，但无法核对原始版面。", "前作全文、其他版本及实验代码和原始数据未提供；版本角色未经核验。"]}

问题：固定数据集的梯度矩均有限，为何重尾数据仍会影响有限和优化？裁剪如何改变这种影响，并与ERM总体超额风险联系？

方法：区分数据集抽样与训练索引随机性。固定数据集后均匀有放回采样，裁剪单样本梯度并投影，输出普通或加权迭代均值；用裁剪偏差界、稳定极限和替换单样本稳定性分别分析优化、经验矩及ERM误差。

作者主张：有限数据集虽有有限经验二阶矩，但重尾抽样使其随N增长；裁剪能消除有害的数据量依赖。

论文证据：定理3.4—3.5给出经验p阶矩随N的三类概率尺度，并代入优化界。

模型推断：新增价值是把经典尾部极限用于有限和噪声解释；支持的是代理量与上界尺度，不是SGD实际误差随N必然恶化。

定位：['TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p5 定理3.4—3.5；附录B。\n']

作者主张：为有限和ClipSGD提供宽泛调度下的收敛保证，并按N与T关系选择裁剪策略。

论文证据：定理3.2、3.7给出条件算法期望界；附录C证明，附录D分析尾指数失配及选参。

模型推断：增量主要是新分析而非新优化器；所谓最优策略限于所比较的调度和上界。

定位：['TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p4—8 §3.2—3.3；p21—35 附录C—D']

作者主张：首次给出相应重尾ERM泛化界，并指出总体最优点梯度控制关键常数。

论文证据：定理3.1给出上界，Lemma 3.1给出一维Pareto构造下界；附录A扩展到Tikhonov正则化凸ERM。

模型推断：获得有实质意义的ERM保证；下界针对该ERM构造，不是所有学习算法的极小极大下界。

定位：['TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p4 定理3.1、Lemma 3.1；p13—17 附录A。\n']

key_results：[{"setting": "记M_{p,N}=N^(-1)Σ_i||∇f(x*,ξ_i)||^p；真实尾指数α∈(1,2)", "baseline": "未裁剪SGD使用的经验二阶矩型噪声代理", "metric_or_guarantee": "数据集抽样上的概率阶", "reported_values_and_units": "M_{2,N}=Θ_P(N^(2/α-1))；一般p<α、p=α、p>α分别为Θ_P(1)、Θ_P(log N)、Θ_P(N^(p/α-1))。α=2的临界二阶矩为Θ_P(log N)。", "information_and_compute": "这是随N变化的随机数据统计量，不是固定数据集内的无限方差。", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p5 定理3.4—3.5，式9—13"}, {"setting": "固定数据集，满足凸或强凸定理条件，调度指数p∈(1,2]", "baseline": "未裁剪SGD的二阶矩型收敛界", "metric_or_guarantee": "E_alg[F_N(平均迭代)-F_N(xhat)]", "reported_values_and_units": "凸版γ_t∝t^(-1/p)、λ_t∝t^(1/p)得到O(T^(-(p-1)/p))。强凸版两类阈值调度的主项分别按T^(-2(p-1)/p)、T^(-(p-1))衰减；系数仍含数据矩和阈值。", "information_and_compute": "每步一个样本梯度；上述裸T速率是固定数据集口径，并非一致于N的保证。", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p5 Corollary 3.3；p7 定理3.7；p24—30 附录C"}, {"setting": "强凸光滑ERM，1<q<α，N足够大；记M_q=E||∇f(x*,ξ)||^q", "baseline": "相关工作转述的有限方差O(1/N)型ERM界", "metric_or_guarantee": "总体超额风险", "reported_values_and_units": "E[F(xhat)-F(x*)]=O(Δ^(2-q)M_q/(μ^(q-1)N^(q-1)))；失败概率β的界再乘1/β。区间上的对称Pareto二次构造给Ω(Δ^(2-α)/(μ^(α-1)N^(α-1)))下界。", "information_and_compute": "期望及概率针对数据抽样；高概率上界来自Markov，不是训练轨迹的高概率保证。", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p4 式6—8；p15 Corollary A.3；p16—17 Lemma A.3"}, {"setting": "合成f(x,ξ)=||x||²/2+〈ξ,x〉，噪声尺度c=10；α∈{1.05,1.1,1.5,1.9}，N∈{10,10²,10³,10⁴,10⁵,10⁶,10⁷}", "baseline": "SGD对比ClipSGD", "metric_or_guarantee": "总体超额风险与经验优化误差；正文定性称裁剪的总体风险更有利，α=1.9时两者相近", "reported_values_and_units": null, "information_and_compute": "T=1000步，每设置固定数据集运行100次，仅索引随机；γ_t=t^(-1/α)/4，裁剪阈值λ_t=t^(1/α)。硬件、时间及调参预算未报告。", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p8—9 §4、Figure 1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Sadiev, A., Danilova, M., Gorbunov, E., Horváth, S., Gidel, G., Dvurechensky, P., Gasnikov, A., and Richtárik, P. High-probability bounds for stochastic optimization and variational inequalities: the case of unbounded variance. In International Conference on Machine Learning, pp. 29563–29648. PMLR, 2023.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "裁剪偏差界；本篇Lemma C.5明确引用其Lemma C.1。", "claimed_difference": "本篇分析随机生成的有限数据集及其最优点梯度矩，而非仅沿用流式噪声口径。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p3 §2；p11参考文献；p21 Lemma C.5", "prior_actually_read": false}, {"citation_as_printed": "Liu, H. and Tong, J. New sample complexity bounds for sample average approximation in heavy-tailed stochastic programming. In Forty-first International Conference on Machine Learning, 2024.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "光滑损失的SAA/ERM稳定性分析与替换样本构造。", "claimed_difference": "据本篇转述，从有界梯度方差扩展到可能无限方差，以最优点低阶矩控制风险。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p3 §2；p11参考文献；p13 Theorem A.1证明", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可辨认的理论保证与机制解释，不是单纯性能微调；但派生选参结论存在需核查的联合尺度问题。", "central_increment": "前作已分析重尾裁剪及有限方差SAA（本篇转述）；本作在光滑紧域条件下追踪随机有限数据集的噪声矩，并新增弱矩ERM界，尚待排除分区简化失真。", "soundness_observation": "已阅读证明文本，未逐定理验证。D.2从N≪T推出N^(2/α-1)≪√T并不一般成立，主定理与该派生选参结论应分开评价。\n", "significance_observation": "解释有限数据为何仍需重尾分析，理论价值明确；没有真实任务证据支持深网收益或实际最优调参。", "main_open_question": "保留N依赖并满足裁剪阈值约束后，作者的N/T三分区最优选参规则哪些仍成立？"}

limitations：[{"text": "适用范围是凸/强凸、统一光滑与紧域；算法随机性的高概率优化界、更一般光滑条件留待后续。", "basis": "author_report", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p4假设；p9 §5"}, {"text": "数据感知调参使用未知x*处的全数据梯度矩；精确检查全梯度阈值也可能需额外遍历，实际获取成本未报告。", "basis": "model_inference", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p5阈值讨论；p7—8 式16—18"}, {"text": "仅有合成二次实验；固定数据集的100次索引重采样不能衡量跨数据集波动，且图1不可见。", "basis": "model_inference", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p8—9 §4"}, {"text": "Corollary C.6用泛化界替换梯度矩，其左端仍是经验优化误差，不能直接视作最终输出总体风险的端到端保证。", "basis": "model_inference", "locator": "TEXT_OR_FGHVEJ2Jz9_2bef2ea00264，p30 Corollary C.6，式62—63"}]

minimal_check：{"question": "D.2的N≪T简化能否由D.1推出？", "control": "保留式66的N因子，对照式69及固定N的解释。", "observable_outcome": "代入α=1.2、调度指数p=2、N=T^0.9，虽N/T→0，但式66噪声项为T^0.1，不能由该表达式得到O(T^(-1/2))。", "resources": "所给p31—32文本与纸笔核算；原PDF可用于排除排版误读，无需训练。", "failure_or_stop_condition": "若明确仅取固定N且大O常数依赖N，应缩窄结论而非判矛盾；若坚持联合一致界，则该推导不足。上界项增长不代表实际误差增长。"}

missing_fields：["图1具体性能数值及误差统计", "实验维度、初始化、约束域和投影执行细节", "硬件、运行时间及调参预算", "候选前作的独立核读与外部标识", "复杂公式的无损版面核验"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

有限数据集噪声与总体重尾的区分值得保留；继续阅读优先重新推导含 N 因子的选参区域，并核对矩常数、阈值可得性和 q 趋近 α 的行为。

身份、版本与覆盖：题名、35 页官方当前附件、全文哈希和 Pro 返回绑定一致。Pro 初评覆盖全部提供文本；本地核看所列页，并观察原 PDF 第 4、31、32 页以排除关键公式排版误读。没有逐定理验证完整证明。

核查定位：text_delivery_manifest.json, structured/pro037.json, p003:L0001；verified_with_scope_limit

中心有限和问题与随机性层次：算法固定抽出的数据集，再均匀有放回抽索引、裁剪单样本梯度并投影。固定数据集内经验矩有限；Theorem 3.4–3.5 的 ΘP 描述数据抽样、N 增长时的经验矩尺度：p<α 为常数阶，p=α 为 log N，p>α 为 N^(p/α−1)。这说明经典噪声代理可能随 N 增长，不等于已证明实际 SGD 误差必然恶化；临界矩也没有完全消去 N 依赖。

核查定位：p003:L0035-L0051, PDF physical page 4, Algorithm 1, p005:L0014-L0057；central_statistical_object_confirmed

关键定理条件与保证对象：原 PDF 第 4 页确认逐样本凸/强凸、统一 L-smooth、有限直径紧凸域，最优点梯度尾概率渐近 c*r^-α。凸算法条件为非增 γt≤1/(4L)、λt≥2^5*3^2*LΔ+2||∇FN(x1)||；强凸另有阈值条件。ERM 上界对 1<q<α 且 N 满足阈值，含 N^-(q−1) 和最优点 q 阶矩；高概率形式在附录由 Markov 获得，不是算法轨迹高概率保证。Pareto 下界针对所构造 ERM，不是所有学习器极小极大下界。

核查定位：PDF physical page 4, Assumptions 3.2–3.5 / Theorems 3.1–3.2 / Lemma 3.1, p007:L0041-L0064, p013:L0040-L0049, p015:L0017-L0027；conditions_and_scope_confirmed_not_full_proof_validation

N≪T 选参简化的有限代数核查：原 PDF 第 31 页式 66 保留 N^(alpha_alg/alpha_true−1)，第 32 页却从 N≪T 推出 N^(2/alpha_true−1)≪sqrt(T)。取 alpha_true=6/5、alpha_alg=2、N=floor(T^(9/10))，虽然 N/T→0，该比值却按 T^(1/10) 增长。因此在联合 N=o(T) 意义下，所写推导不足以建立对 N 一致的 O(T^-1/2)；固定 N 时可把它吸收进依赖 N 的常数。这里只检查上界表达式，未据此断定真实误差增长或主定理错误。

核查定位：PDF physical page 31, equations 66 and 69, PDF physical page 32, first paragraph, local_check/schedule_scaling_check.json；joint_scaling_derivation_gap_confirmed

实验与调参的现实范围：§4 只给合成二次目标，c=10、T=1000，并固定每个数据集做 100 次索引随机运行；它不衡量重新抽数据集的波动。数据感知 γ0/λ0 使用未知总体最优点的梯度矩，且仍需满足阈值，不能视为无需统计信息的实用处方。未从不可见的图 1 构造精确性能差值。

核查定位：p007:L0003-L0030, p008:L0027-L0050, p009:L0003-L0011, PDF physical page 32, equations 70–71；experimental_and_oracle_information_limits_confirmed

本地补充/限定：["通过原 PDF 确认关键阈值和 D.2 的 N/T 推导，再保存明确的指数代入；这是公式检查，不是训练复现。", "把该缺口限定于联合尺度的派生选参结论，保留固定 N 的大 O 解释与尚未完整验证的主定理。"]

核查局限：["未逐项核验全部证明、最优性或概率极限定理，未核读引用前作。", "未运行优化器、生成数据或绘制复现实验；图 1 未做视觉核查。", "仅进行上述代数代入，不把上界项增长误当算法误差下界。", "Pro 仅读文本，本地只观察三个 PDF 页面；L2 为 AI 暂评。"]


## pro038 · Lions and Muons: Optimization via Stochastic Frank-Wolfe under Heavy-Tailed Noise

论文 OR_gvroXZ0HS8；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7", "source_url": "https://api2.openreview.net/pdf?id=gvroXZ0HS8\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页1–41全部所供文本，页标连续；包括正文、参考文献、附录A相关工作、B/C证明及算法、D超参数、E补充实验。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像，图1–9仅有图题、坐标文字及正文描述，不能读取曲线值或误差带。", "双栏、分式、上下标及横线标记存在失真；算法7的两类动量记号和附录部分公式不能可靠逐符号核验。表2–7主要配置可辨，表1复杂单元格需谨慎。", "未提供前作全文；未搜索、复现或比较其他版本。"]}

问题：如何用一般紧凸集上的Stochastic Frank-Wolfe统一解释带weight decay的Lion/Muon，并在仅有有界p阶梯度噪声矩时获得小批量收敛保证？

方法：动量估计经外推形成方向，调用线性最小化oracle，再与当前点凸组合。ℓ∞球产生sign更新，谱范数球产生正交化更新；在动量前剪裁梯度得到“+”，加入同一样本在相邻参数点的梯度差分得到“++”。

作者主张：Lion、Muon及其Nesterov形式均可表示为同一Stochastic FW，并获得KKT解释。

论文证据：定理3.1/3.2/B.7给出参数映射；式(3)将范数球FW gap写为对偶范数项与内积之和，零gap对应KKT条件。

模型推断：增量是统一外推动量与分析接口，不是首次发现范数约束或Muon的LMO解释。

定位：['TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页4–5，定理3.1–3.3、引理3.5、式(3)；物理页19–20，B.3']

作者主张：有限方差下，以小平均批量达到O(ε^-3)随机梯度复杂度。

论文证据：定理4.1及推论4.2：初始化批量T^(1/3)，之后每步一个新样本，期望FW gap为O(T^-1/3)。

模型推断：价值在于假设与批量的组合改善，并非首次达到该SFO阶数。

定位：['TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页6，定理4.1、推论4.2；物理页23–26，C.1']

作者主张：给出非凸Stochastic FW在p阶矩噪声下的两种单样本高概率收敛保证。

论文证据：定理4.3/4.4分别覆盖剪裁动量与剪裁加方差缩减，后者在更强光滑条件下改善T的指数。

模型推断：中心贡献是将重尾稳健保证扩展到一般紧凸集LMO框架，而非剪裁操作本身。

定位：['TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页7，定理4.3/4.4；物理页27–35，C.3–C.5']

key_results：[{"setting": "一般紧凸集、非凸目标、有限方差", "baseline": "Algorithm 3及本文转述的既有方差缩减FW", "metric_or_guarantee": "均匀随机输出点的期望FW gap", "reported_values_and_units": "Algorithm 3固定动量下存在O(σ/√m)项；取m=T得到O(ε^-4) SFO。Algorithm 4达到O(T^-1/3)，对应O(ε^-3) SFO。", "information_and_compute": "Algorithm 4首批T^(1/3)，随后每步一个新样本但需两个参数点梯度；按算法计算为首批加2(T−1)次梯度评价，仍为O(T)。LMO复杂度为O(ε^-3)。", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页5–6，定理3.3、推论3.4/4.2、算法4。\n"}, {"setting": "有界p阶噪声矩，1<p≤2", "baseline": "Algorithm 5；SGD结果仅作本文所述理论参照", "metric_or_guarantee": "以至少1−δ概率控制迭代平均FW gap", "reported_values_and_units": "Algorithm 5：O(log(T/δ)T^(-(p−1)/(3p−2)))；Algorithm 6：O(log(T/δ)T^(-(p−1)/(2p−1)))。", "information_and_compute": "均可每步仅采一个新样本；Algorithm 6另算同一样本的前一参数点梯度。不是最后迭代或全局最优保证。", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页7，定理4.3/4.4。\n"}, {"setting": "nanoGPT/Shakespeare；6层、6头、宽384、序列256、batch 64，5种子均值", "baseline": "Lion、Muon", "metric_or_guarantee": "验证loss首次低于1.47所需训练步数", "reported_values_and_units": "作者报告LION+为2950步、Lion为3650步，减少19.18%；MUON+为4000步、Muon为4250步，减少5.88%。", "information_and_compute": "单张NVIDIA A100；网格搜索学习率、weight decay及剪裁阈值；Muon使用Newton-Schulz，向量参数使用固定配置AdamW。未报告时间收益。", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页8，§5；物理页36，表2–3。\n"}, {"setting": "附录E：二次目标叠加Normal/Pareto噪声；以及ResNet18/CIFAR-10", "baseline": "Lion、Muon对各自“++”版本", "metric_or_guarantee": "平均梯度范数及尾部分位数；测试loss/accuracy", "reported_values_and_units": null, "information_and_compute": "合成实验d=1/1000、n=2/30，每算法10^5次运行、每次100步；分类实验200 epochs、batch 128、5种子。作者文字报告改善，但图3–9数值不可读；均使用单张A100。", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页37–41，E.1/E.2。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Pethick, T., Xie, W., Antonakopoulos, K., Zhu, Z., Silveti-Falls, A., and Cevher, V. Training deep learning models with norm-constrained lmos. arXiv:2502.07529, 2025.", "identifier_if_present": "arXiv:2502.07529", "relation_candidate": "理论扩展", "shared_component": "Muon、范数球LMO及带weight decay的FW解释", "claimed_difference": "本篇加入外推动量以覆盖Lion及Nesterov Muon，并研究重尾保证。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页3、15，相关工作；物理页12，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Liu, Z., Zhang, J., and Zhou, Z. Breaking the lower bound with (little) structure: Acceleration in non-convex stochastic optimization with heavy-tailed noise. In The Thirty Sixth Annual Conference on Learning Theory, pp. 2266–2290. PMLR, 2023.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "剪裁、动量、方差缩减及重尾概率分析引理", "claimed_difference": "由normalized SGD的梯度范数分析扩展到一般紧凸集的FW gap。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页12，参考文献；物理页27–35，C.3–C.5", "prior_actually_read": false}, {"citation_as_printed": "Zhang, M., Shen, Z., Mokhtari, A., Hassani, H., and Karbasi, A. One sample stochastic frank-wolfe. In International Conference on Artificial Intelligence and Statistics, pp. 4012–4023. PMLR, 2020b.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "小批量方差缩减FW及O(ε^-3)复杂度", "claimed_difference": "本篇称避免其Hessian及分布结构假设；但初始化仍使用较大批量。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页6、16，表1及讨论；物理页13，参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "一般紧凸集上的小批量重尾高概率保证构成实质理论增量；统一解释已有明确前作基础，不宜判为路线首创。", "central_increment": "前作已有范数约束优化器解释和重尾SGD工具（本篇转述）；本作在紧凸集及相应光滑条件下新增FW保证，核心证据为定理4.1/4.3/4.4。", "soundness_observation": "附录提供完整证明文本，但未逐式验证。一个需核查的衔接是：无Nesterov MUON+映射要求β=1−γ，而定理4.3指定β=(1−γ)^2；现有定理不能不经额外推导就直接套用该实例。", "significance_observation": "理论范围扩展比实验性能增益更有分量；已有实验不足以支持大规模训练效率或普遍优越性。", "main_open_question": "能否在保持无Nesterov MUON+实际更新形式时，补出β=1−γ下的同阶高概率保证？"}

limitations：[{"text": "不覆盖无weight decay的Lion/Muon；Hilbert范数下的直径可能引入维度依赖，重尾界也不随噪声消失自动改善阶数。", "basis": "author_report", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页8–9，§6"}, {"text": "nanoGPT的Lion/LION+使用不同weight decay（1e-3/1e-2），ResNet18亦不同（1e-2/1e-3）；剪裁版增加调参维度，“++”增加梯度评价。未见等计算预算的拆分消融，不能纯粹归因于剪裁或方差缩减。", "basis": "model_inference", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页36、40–41，表2–7。\n \n"}, {"text": "网络实验未验证理论噪声矩及光滑假设；固定实用动量、近似正交化与定理设定不同，损失改善不等于验证高概率收敛率。", "basis": "model_inference", "locator": "TEXT_OR_gvroXZ0HS8_96f6e02f8ce7：物理页7–8、36、41"}]

minimal_check：{"question": "定理4.3能否覆盖无Nesterov MUON+？", "control": "对照算法9的β=1−γ映射与定理的β=(1−γ)^2，逐项代入C.3误差界。", "observable_outcome": "保持原更新不变时，能否闭合相同T阶数与失败概率的界。", "resources": "可读原PDF公式与符号推导；无需GPU，耗时未知。", "failure_or_stop_condition": "若必须改变动量更新或增加假设才能闭合，则应收窄当前保证对MUON+的覆盖声明。"}

missing_fields：["图3–9的精确结果值不可读，补充实验结果数值字段为null。", "运行时间、FLOPs、显存及实际调参总成本未报告。", "Liu et al. (2023)、Zhang et al. (2020b)条目未提供DOI/arXiv标识；前作全文均未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

一般紧凸集上的重尾高概率 FW 分析有理论价值；进一步阅读应检查具体优化器的参数衔接及近似 LMO 的误差传递，而不是直接套用实验配置。

身份、版本与阅读范围：题名与官方当前附件、41 页清单、全文文本哈希和 Pro 返回绑定一致。Pro 覆盖全部所供文本；本地核看列出的条件、算法与实验页，并观察原 PDF 第 7、26、36 页。未逐行验证完整证明。

核查定位：text_delivery_manifest.json, structured/pro038.json, p003:L0001；verified_with_scope_limit

统一解释的关键条件与目标：Theorems 3.1/3.2 把带正 weight decay 的 Lion/Muon 映射到半径 1/λ 的范数球 FW，步长满足相应映射并保持可行凸组合；使用精确 LMO。FW gap=0 对应约束 KKT 条件，不是非凸全局最优。作者明确不覆盖无 weight decay 版本，Hilbert 范数下的直径还可能引入维度常数。

核查定位：p003:L0006-L0055, p004:L0017-L0063, p005:L0003-L0038, p009:L0003-L0014；equivalence_and_stationarity_scope_confirmed

重尾高概率保证与更强假设：原 PDF 第 7 页确认 Algorithm 5 的平均 FW gap 阶为 log(T/δ)*T^(-(p−1)/(3p−2))，Algorithm 6 为 log(T/δ)*T^(-(p−1)/(2p−1))。后者另需逐样本梯度几乎处处 Lipschitz；两者仍要求紧凸域、无偏且对所有 x 有界 p 阶噪声、真实梯度有界和指定调度。这不是最后迭代保证，也不是一般深网的无条件训练速率。

核查定位：PDF physical page 7, Theorems 4.3–4.4, p003:L0026-L0055；rates_and_assumptions_confirmed

单样本与梯度评价数：Algorithm 4 的初始化批量为 T^(1/3)，后续每步一个新样本，但同一新样本在 xt 与 xt−1 两个点求梯度。按实际梯度计算数是初始化批量加 2(T−1)，而不是每步只算一次梯度；这不改变 O(ε^-3) 阶数。Algorithm 6 同样需要两点梯度，LMO 和正交化成本也不能从 SFO 阶数直接换成墙钟速度。

核查定位：p006:L0003-L0013, p006:L0030-L0056, PDF physical page 7, Algorithm 6, p005:L0036-L0039；oracle_and_compute_count_qualified

MUON+ 到重尾定理的参数衔接：原 PDF 第 26 页 Algorithm 9 是无额外外推动量的 MUON+；按 Theorem 3.2 同类映射要求 β=μ=1−γ。第 7 页 Theorem 4.3 指定 γ=T^(-p/(3p−2))、β=(1−γ)^2，对 0<γ<1 两者不同。因此不能仅凭属于 Algorithm 5 就直接宣称满足该定理的特定调度。这里只确认直接代入不匹配，没有否定 MUON+ 可通过其他推导获得同阶保证。

核查定位：PDF physical page 26, Algorithm 9, p004:L0056-L0063, PDF physical page 7, Theorem 4.3；specialization_gap_confirmed_not_algorithm_counterexample

实测收益的单位与控制变量：正文报告到验证 loss<1.47 的步数：Lion 3650 对 LION+ 2950（少19.18%），Muon 4250 对 MUON+ 4000（少5.88%）。原 PDF 第 36 页表 3 确认 Lion 两组 weight decay 为 1e-3/1e-2，剪裁版还多搜索阈值；Muon 用 Newton-Schulz 近似与向量参数 AdamW。五种子和单 A100 是作者配置，步数改进不等于等调参预算或实测耗时收益，也不能单独验证理论噪声假设。

核查定位：p008:L0003-L0031, PDF physical page 36, Tables 2–3；reported_step_savings_confirmed_cost_and_causality_limited

本地补充/限定：["核实 Theorem 4.3 与 Algorithm 9 的直接参数衔接缺口；保留可存在额外证明的可能，不将其扩大为算法不收敛。", "明确单个新样本仍需两个参数点梯度，渐近复杂度阶保持不变；实用步数收益与墙钟及总调参成本分开。"]

核查局限：["未完整验证附录证明或推出缺失的 MUON+ 专门定理，未核读前作。", "未训练 nanoGPT、执行优化器或复算实验曲线；图 1 和补充性能图未视觉逐点核验。", "没有把精确 LMO 保证直接转用于有限次 Newton-Schulz 实现。", "Pro 只看文本，本地只观察三个 PDF 页面；L2 为 AI 暂评。"]


## pro039 · Momentum Further Constrains Sharpness at the Edge of Stochastic Stability

论文 OR_mL4i6z7Miy；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_mL4i6z7Miy_61e624310610", "source_url": "https://api2.openreview.net/pdf?id=mL4i6z7Miy\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "bc52b0a83ab1add726e1df8cf0dca0baf7104ca3bd9869e0451ca7c248632125", "source_pdf_sha256": "61e62431061098e4dc13f8b4aeefe64b450a94fd76e239218cb2a829b1a891c5"}], "read_ranges": ["TEXT_OR_mL4i6z7Miy_61e624310610：物理页1–41全部提供文本；页标连续、题名匹配。正文p1–9，参考文献p10–13，附录A–J p14–41，包括可见公式、图题和注释。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–38只能读取图题及正文转述，无法核验曲线、峰值、误差条及临界批量的图中数值。", "存在双栏交织及分式、括号、上下标失真；连续页标不代表原PDF内容被无损提取。"]}

问题：动量与小批量噪声共同作用时，训练是否受随机稳定性边界约束，该边界怎样随批量大小和动量改变？

方法：在监督分类、主要为MSE损失的设置中扫描η、β、b，跟踪BS=E_B[g_BᵀH_Bg_B/||g_B||²]、λmax和训练损失，并从检查点分别改变超参数；理论上在线性化插值极小点附近分析参数—速度联合状态的二阶矩谱。

作者主张：SGDM和SGDN出现批量依赖的EOSS：小批量动量收紧曲率约束，大批量恢复各自的确定性阈值。

论文证据：正文及附录报告跨批量、架构、激活函数扫描，并通过改变学习率、动量或批量观察catapult及重新稳定。

模型推断：增量是识别动量效应随噪声区间改变，而非单纯换优化器；干预比仅观察平台更有说服力，但尚非一般失稳证书。

定位：['TEXT_OR_mL4i6z7Miy_61e624310610:p5，§3.1；p6–7，§3.3；p23–25，附录F。\n']

作者主张：噪声主导时，SGDM均方稳定性领先阶等价于步长η_eff=η/(1−β)的SGD，可解释小批量曲率尺度。

论文证据：给出一维精确插值式、多维定理4.1及附录C–E推导；SGDN提供一维对应分析。

模型推断：扩展已有稳定性框架，不意味着轨迹等价，也未直接证明Batch Sharpness必然饱和。

定位：['TEXT_OR_mL4i6z7Miy_61e624310610:p7–8，§4；p18–22，附录C–E。\n']

key_results：[{"setting": "CIFAR-10约8k训练子集上的MLP等模型，固定η、β扫描批量；该设置小批量约为b≤16。", "baseline": "vanilla SGD及全批量SGDM/SGDN", "metric_or_guarantee": "Batch Sharpness经验平台，非已证动量失稳判据", "reported_values_and_units": "小批量两者约为2(1−β)/η；大批量SGDM约为2(1+β)/η，SGDN约为2(1+β)/[η(1+2β)]。SGDN的大批量平台仍低于SGD的2/η，不能概括为两种动量均允许比SGD更高曲率。", "information_and_compute": "使用分类标签；附录I称固定总训练样本预算，但未给预算数值、硬件或耗时。", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p2脚注1；p5，式(8)及§3.1；p27，附录I"}, {"setting": "MLP在第75000步干预；基线b=16、η=0.004、β=0.9。", "baseline": "未干预轨迹及相反方向的稳定化干预", "metric_or_guarantee": "训练损失尖峰及曲率重新稳定", "reported_values_and_units": "分别将β增至0.95、η增至0.0067或b减至8；作者报告越过工作平台后出现catapult。未提供可读的尖峰幅度或发生率数值。", "information_and_compute": "三个独立超参数干预，不是同时改变；重复次数、置信区间及动量缓冲区处理细节未见明确报告。", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p6–7，§3.3、图6。\n"}, {"setting": "一维随机二次SGDM，a=E[h_t]>0，σ_b²=Var(h_t)。", "baseline": "确定性heavy-ball与有效步长匹配的SGD", "metric_or_guarantee": "线性均方稳定步长上界", "reported_values_and_units": "1/η_max=a/[2(1+β)]+σ_b²/[2a(1−β)]。多维仅给领先阶ρ(I−η_eff K+η_eff²G)<1，其中K=H̄⊗I+I⊗H̄，G=E[H_t⊗H_t]。", "information_and_compute": "理论推导而非实测；完整联合二阶矩算子规模为4d²×4d²，未给大型网络直接求谱成本。", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p8，式(10)–(11)；p19，式(19)–(20)；p21–22。\n"}, {"setting": "b=4；SGDM取η=0.001、β=0.9，对照SGD取η=0.01。", "baseline": "匹配η_eff的SGD", "metric_or_guarantee": "BS平台及参数、预测空间轨迹距离", "reported_values_and_units": "图14文字报告两者BS均稳定在200，但轨迹仍分离；距离的具体数值不可读。", "information_and_compute": "参数距离使用5000维JL投影；预测距离使用10000个CIFAR-10测试样本的logits。", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p26，附录G、图14。\n"}]

prior_work_candidates：[{"citation_as_printed": "Andreyev, A. and Beneventano, P. Edge of Stochastic Stability: Revisiting the Edge of Stability for SGD. December 2024. doi: 10.48550/arXiv.2412.20553.", "identifier_if_present": "arXiv:2412.20553", "relation_candidate": "方法继承", "shared_component": "Batch Sharpness、SGD随机边界及检查点干预", "claimed_difference": "由无动量SGD拓展到动量下的批量依赖平台；没有同样直接的动量判据。", "basis": "target_paper_only", "target_locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p4–7；p10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Cohen, J. M., Kaur, S., Li, Y., Kolter, J. Z., and Talwalkar, A. Gradient descent on neural networks typically occurs at the edge of stability. In International Conference on Learning Representations (ICLR), 2021.", "identifier_if_present": "ICLR 2021, poster/2577", "relation_candidate": "比较基线", "shared_component": "确定性EOS及全批量动量阈值", "claimed_difference": "小批量动量可反转全批量SGDM的曲率趋势。", "basis": "target_paper_only", "target_locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p1–5；p10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Yuan, K., Ying, B., and Sayed, A. H. On the influence of momentum acceleration on online learning. Journal of Machine Learning Research, 17(192):1–66, 2016.", "identifier_if_present": "JMLR 17(192):1–66", "relation_candidate": "理论扩展", "shared_component": "SGDM与有效步长SGD的稳定性关系", "claimed_difference": "作者强调恢复领先阶稳定算子而不只给充分条件，且不主张所研究训练轨迹强近似。", "basis": "target_paper_only", "target_locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p8，§4.2及脚注6；p12参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是有干预支持的机制认识，而非仅性能改善；已有EOS框架内仍构成实质性新知识候选，尚不足判路线级创新。", "central_increment": "前作已给SGD随机边界与全批量动量阈值（本篇转述）；本作新增小批量动量收紧约束及跨批量过渡，证据为扫描、干预与条件性谱分析。", "soundness_observation": "未逐项证明定理。按给定定义，正曲率一维二次例中BS=a，而精确稳定边界还依赖σ_b²，因此算子约化不能单独推出BS必然饱和；这不否定神经网络中的经验平台。", "significance_observation": "有助于解释η、β、b的耦合及失稳诊断；更平坦不等于已证明泛化更好，也未展示通用训练效率收益。", "main_open_question": "能否建立动量专属判据，将联合状态二阶矩谱边界直接连接到实测Batch Sharpness平台？"}

limitations：[{"text": "作者承认实验限于小模型，最大到ResNet18和小ViT；Adam仅有预条件λmax代理的初步趋势，无随机失稳判据。", "basis": "author_report", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p9，§5.1、§6.1；p26–27，附录H"}, {"text": "中间批量已收敛时，提高阈值不一定重启锐化；部分极小批量运行因噪声过大未收敛；ViT全批量λmax可高于名义阈值。", "basis": "author_report", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p24，附录F.2；p30，附录J；p39，图36前说明"}, {"text": "多维理论余项缺少实验区间的定量控制。J.1.1报告η²λmax²/(1−β)³≈16.28，但未比较它与主导噪声项及稳定裕量，不能据此确认渐近近似适用。", "basis": "model_inference", "locator": "TEXT_OR_mL4i6z7Miy_61e624310610:p22，式(33)；p31，J.1.1。\n"}]

minimal_check：{"question": "从均方稳定约化推到BS平台是否还需要额外假设？", "control": "构造同均值a、不同方差的正曲率一维随机二次损失，固定η、β；按附录C直接计算3×3二阶矩算子。", "observable_outcome": "比较BS=a与谱半径ρ(R)是否在不同方差下跨越1，并核对式(19)。", "resources": "普通CPU的3×3矩阵计算，无神经网络训练需求；具体耗时未估计。", "failure_or_stop_condition": "若相同BS对应稳定与不稳定两侧，则停止将BS作为完整稳定边界的解释，明确所需附加条件；不因此否定经验双平台。"}

missing_fields：["图像、原始曲线点及可核验的不确定性统计未提供。", "硬件、总训练/GPU时间、BS估计采样量与诊断频率、完整架构和预处理、随机种子数未见明确文本报告；固定样本预算未给数值。", "作者称覆盖SVHN，但提供文本未定位到明确标注SVHN的实验配置与结果。", "前作原文及其他版本未提供；未搜索、下载或复现实验，当前附件出版角色未核实。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

批量与动量耦合的经验转变和检查点干预值得继续研究；重点是给出动量专属判据、量化近边界余项并检验更广损失与模型。

身份、版本与范围：题名、41 页官方当前附件、全文哈希和 Pro 返回绑定一致。Pro 初评覆盖全部所供文本；本地核看列出的定义、条件与实验页，观察原 PDF 第 4、7、19 页。未逐项验证多维谱分析证明。

核查定位：text_delivery_manifest.json, structured/pro039.json, p003:L0001；verified_with_scope_limit

中心经验现象与动量约定：本文使用未乘 (1−β) 的 heavy-ball 梯度累积，需与 EMA 约定区分。小批量经验 BS 平台约为 2(1−β)/η；大批量 SGDM 为 2(1+β)/η，SGDN 为 2(1+β)/(η(1+2β))。对 β>0，后一个值仍低于 SGD 的 2/η，不能把两种动量都概括为大批量下允许高于 SGD 的曲率。文中 b≲16 是约8k CIFAR-10子集的观察范围，不是普遍临界批量。

核查定位：p003:L0020-L0057, PDF physical page 4, full-batch thresholds, p005:L0013-L0045, p026:L0036-L0050；regime_and_parameter_convention_confirmed

决定性实验干预：原 PDF 第 7 页图 6 确认同一基线 b=16、η=0.004、β=0.9，在75000步分别增加 β 至0.95、增加η至0.0067或降低 b至8；图中可见损失瞬时上冲和随后重稳。三个是独立干预，不是同时改三参数。正文把 BS 明确列为动量下的经验指示量而非已证失稳证书；未从图形估造尖峰幅度或发生率。

核查定位：PDF physical page 7, Figure 6 and following discussion, p005:L0027-L0045, p006:L0008-L0040；intervention_evidence_visually_confirmed_with_scope_limit

精确一维边界与多维领先阶条件：原 PDF 第 19 页式19–20确认 1/ηmax=a/[2(1+β)]+σb²/[2a(1−β)]。它来自共同插值极小点附近的随机二次递推，Hessian i.i.d. 且独立于过去。多维式11只是足够小η、噪声主导时的领先阶关系；附录E还保留 R(η,β) 余项。J.1.1印出的约16.28并未与噪声项和稳定裕量做定量对照，不能仅凭该值确认渐近近似适用于实验区间。

核查定位：p007:L0015-L0054, p018:L0007-L0032, PDF physical page 19, equations 19–20, p008:L0016-L0047, p022:L0003-L0025, p031:L0030-L0035；stability_formula_and_asymptotic_scope_confirmed

Batch Sharpness、轨迹与因果解释边界：原 PDF 第 4 页定义是先取 Rayleigh 比值再对批量平均。对正曲率一维二次且 x≠0，代入 g=h*x 得 BS=E[h]=a，而精确均方稳定边界仍依赖 Var(h)。因此算子约化本身不使该标量成为完整必要充分边界，也不证明其训练中必然饱和；这与论文承认的理论缺口一致，不否定神经网络的经验平台。匹配 ηeff 时 BS=200 的对照仍有参数/预测轨迹差异，不能把稳定性近似写成轨迹等价。

核查定位：PDF physical page 4, Definition 3.1 / equation 7, PDF physical page 19, equation 20, p008:L0052-L0059, p026:L0003-L0033；metric_and_trajectory_interpretation_qualified

本地补充/限定：["核对原 PDF 中 BS 的期望顺序和一维公式，确认 Pro 的有限代数解释与定义一致；未进行其建议的矩阵数值实验。", "新增图6视觉核查，保留catapult现象但不从有限实验宣称普遍失稳证书；大批量 SGDN 与 SGDM 的相对 SGD 阈值分别描述。"]

核查局限：["未运行矩阵谱数值测试、神经网络训练或作者代码；只作定义和公式代入。", "未验证所有补充曲线、种子统计、缓冲区处理或计算预算。", "外部前作未核读，多维推导没有完成逐项证明审计。", "Pro 仅读全文文本，本地仅观察三页 PDF；L2 保持 AI 暂评。"]


## pro040 · Geometry-Misalignment in Distributional Learning

论文 OR_oySSc3QcoT；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_oySSc3QcoT_6a45fd83747f", "source_url": "https://api2.openreview.net/pdf?id=oySSc3QcoT\n", "version_role": "current_attachment_unverified_role", "version_note": "仅收到该附件的全文文本，未核验最终出版身份。"}], "read_ranges": [{"source_id": "TEXT_OR_oySSc3QcoT_6a45fd83747f", "physical_pages": "1–44，页标连续", "sections": "正文§1–7、参考文献、附录A–I；含算法1–4、证明及表1–16的可读文本。"}], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–11不可见；p30–32、p34–36主要只留下图题，不是缺页。材料清单明确仅提供全文文本。\n", "双栏文字交织，公式分式、上下标及矩阵布局有损；未读取PDF图像、前作或其他版本，未复现实验。以下数值是作者报告，代数及表格聚合检查另作模型推断。"]}

问题：优化F(θ)=D(P,Qθ)时，欧式参数更新何时失配于分布差异诱导的几何，并影响有限预算下的误差？

方法：以κG=λmax(G)/λmin(G)诊断；幂/逆幂迭代估计谱端点，阈下做GD，阈上用CG近似G⁻¹g。验证集联合选步长、阈值和容差，输出θT。

作者主张：错配导致不可避免的欧式收敛下界与有限预算风险惩罚，几何更新给出匹配上界。

论文证据：定义3.4、定理3.6、4.2–4.3、5.1–5.5及附录C–D给出陈述和推导。

模型推断：按所写Taylor展开，G就是相应Hessian，κG首先是经典条件数的解释；下界硬例及风险推导存在实质问题，尚未建立所称普适分离。

定位：['TEXT_OR_oySSc3QcoT_6a45fd83747f，p4–8，§3–5。\n', 'TEXT_OR_oySSc3QcoT_6a45fd83747f，p16–26，附录C–D']

作者主张：仅在高错配时激活几何更新，兼顾快速收敛与低开销。

论文证据：算法1–4及合成、非凸数字迁移、MMD和真实UDA表格报告门控收益。

模型推断：是明确的场景化自适应预条件方案；相对已有组件的新意主要在诊断与开关，而非新的下降方向。

定位：['TEXT_OR_oySSc3QcoT_6a45fd83747f，p6–7、p13–16，算法1–4', 'TEXT_OR_oySSc3QcoT_6a45fd83747f，p27–44，附录E–I']

key_results：[{"setting": "总体目标、局部内在强凸/光滑", "baseline": "主文限定标量步长GD；附录C.2却扩展至自适应SPD预条件，算法类口径不一。", "metric_or_guarantee": "作者宣称的误差界，非本轮验证结论", "reported_values_and_units": "欧式ΔT≥c·exp(−T/κ)Δ0；精确几何ΔT≤(1−ηµ)^TΔ0；GCO相对两种固定策略最优者另有O(logT/T)加项；定理5.5又称欧式Eopt≥cκ/T。", "information_and_compute": "比较主要计外层迭代；CG另需O(√κ·log(1/ε))次迭代，不能直接解释成总计算无κ依赖。", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p5–8、p18，定理4.2–5.5、附录C.2。\n \n \n \n"}, {"setting": "DGP-1，32维线性各向异性，高错配，N=50,000；500次重复均值", "baseline": "SGD／始终几何更新", "metric_or_guarantee": "迭代数、目标差距、Time、几何更新比例", "reported_values_and_units": "GCO：145步、7.5e−5、Time=1.70、34%；SGD：1600步、1.1e−3、Time=9.80；始终几何：130步、6.8e−5、Time=3.30。合成Time单位未注明。", "information_and_compute": "全批梯度，Sinkhorn ε=0.1、30轮；主文称幂迭代5轮，CG容差1e−3、上限30轮。", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p8–9，§6、表1。\n \n \n"}, {"setting": "非凸MNIST→MNIST-M；另为MMD DGP-1高错配、N=50,000", "baseline": "Adam", "metric_or_guarantee": "数字迁移准确率/迭代；MMD目标差距/迭代", "reported_values_and_units": "数字迁移GCO=64.1%/720步，Adam=62.0%/1500步；MMD GCO=1.8e−4/230步，Adam=8.5e−4/910步。", "information_and_compute": "前者为dx→256→128的ReLU MLP、B=256，对齐后训练源域线性分类器；后者用高斯核及中位带宽。", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p39–41，附录G–H，表7、9。\n \n \n"}, {"setting": "Office-Home／VisDA-2017／DomainNet；ImageNet预训练ResNet-50，源域交叉熵+Sinkhorn", "baseline": "Adam，同一Sinkhorn训练目标", "metric_or_guarantee": "作者汇总的目标准确率及相对SGD运行时间", "reported_values_and_units": "GCO准确率70.1%／78.5%／51.8%，Adam为62.7%／72.3%／45.8%；GCO时间比1.29／1.33／1.36，几何步占27%／31%／34%。聚合一致性见局限。", "information_and_compute": "冻结BN，2048维特征，目标标签仅评估；硬件型号及总训练预算未报。", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p42–44，附录I，表11–16。\n \n \n"}]

prior_work_candidates：[{"citation_as_printed": "Amari, S. (1998). Natural Gradient Works Efficiently in Learning. Neural Computation, 10(2), 251-276.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "度量逆矩阵预条件梯度", "claimed_difference": "以分布目标的κG作必要性诊断并选择性激活。", "basis": "target_paper_only", "target_locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p3–4，§2.3；p10参考文献。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Ye, H., Luo, L., and Zhang, Z. (2021). Approximate Newton Methods. Journal of Machine Learning Research, 22, 1-41.", "identifier_if_present": null, "relation_candidate": "理论扩展候选", "shared_component": "近似曲率预条件与局部收敛分析", "claimed_difference": "作者强调分布学习错配的下界及门控，而非预条件本身。", "basis": "target_paper_only", "target_locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p3，§2.4；p12参考文献。\n \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "当前可辨增量是经典预条件的条件数诊断、门控及场景实验；未建立超出Hessian病态性的新机制或可靠的必要性分离。", "central_increment": "前作已提供自然梯度和近似Newton（本篇转述）；本作增加κG驱动的选择性调用及分布匹配评测，支持主要来自作者表格。", "soundness_observation": "局部代数核查：C.2硬例Hessian只有1和1/κ两种特征值，可由两个标量GD步消去，因而该硬例不能支持所声称下界。\n 定理5.1取F=x²/2、G=1、η=1.5时，实际一步误差为0.25Δ0，声称上界却为−0.5Δ0，步长区间至少需要修正。\n C.7从指数下界推出对所有T成立的κ/T下界，推导不成立。\n", "significance_observation": "选择性减少昂贵几何求解有应用价值，但外层收敛快不等于总算力无κ依赖，现有性能数字也未通过完整一致性核查。", "main_open_question": "能否在统一算法类与有效硬例下证明超出经典曲率病态性的分布学习特有分离？"}

limitations：[{"text": "理论依赖局部正定和强凸/光滑；实现允许CG失败回退欧式步。", "basis": "author_report", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p5–8、p14–16。\n \n"}, {"text": "非凸实验以损失HVP充当Gv，却未充分说明如何保证SPD或其与真正pullback metric的等价性。", "basis": "model_inference", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p4、p39–40。\n \n"}, {"text": "每步估κ包含逆幂CG，触发少不等于估计免费。按附录A所列网格全枚举，GCO为792组、欧式24组；这是本轮据网格计算，实际搜索总成本未报。", "basis": "model_inference", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p7、p13–15。\n \n \n"}, {"text": "按可读表数计算，Office-Home表14的SGD十二项简单均值为58.74%，而表11报61.4%；DomainNet表16的GCO六域简单均值为47.92%，Avg却为51.8%。未说明可解释差异的加权口径。", "basis": "model_inference", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p42–44，表11、14、16。\n \n \n"}, {"text": "合成θ⋆用所有方法所得最好解替代；Iter未明确统一停止精度，结果缺方差，不能直接当作等精度、等预算结论。CORAL等领域自适应方法使用不同目标，也不构成纯优化器对照。", "basis": "model_inference", "locator": "TEXT_OR_oySSc3QcoT_6a45fd83747f，p8–9、p15–16。\n \n"}]

minimal_check：{"question": "独立复核C.2两特征值硬例能否支持定理4.2。", "control": "同一FU和非零初值，对照固定小步GD与η0=1、η1=(θ1ᵀg1)/||g1||²的历史依赖标量步；g1=0则已收敛。后者不直接调用G。", "observable_outcome": "按给定∇F=GUθ/κ，检查第二步是否对任意旋转U均到θ2=0。", "resources": "纸笔代数或本地CPU小矩阵；无需数据训练或GPU。", "failure_or_stop_condition": "若二步误差为零，则该硬例无法支撑正的指数下界，应停止引用该证明；不据此否定所有可能的修正版下界。"}

missing_fields：["原PDF图像与可核验前作未提供；候选前作未印独立DOI/arXiv标识，因此identifier_if_present为null。", "硬件型号、显存、实际搜索/训练总时长、真实UDA完整超参数和结果方差未报告；合成Time单位及部分平均口径不明。"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

当前可用增量是门控预条件流程，但核心上下界及汇总结果存在已定位问题；在获得修正理论和可审计结果前，本轮停止追加投入。

身份、版本与范围：题名、44 页官方当前附件、全文文本哈希与 Pro 返回绑定一致。Pro 完成全部所供文本的一轮初评；本地核看所列页，并观察原 PDF 第 7、18、44 页。下面代数结论针对已读的具体陈述，未宣称完成整篇证明审计。

核查定位：text_delivery_manifest.json, structured/pro040.json, p004:L0001；verified_with_scope_limit

中心方法及其新增部分：κG 是正定 G 的谱条件数，算法按估计值切换普通梯度与 G^-1g 的近似解。论文承认 G 不是新曲率、预条件本身不是新意；按 §3.2 所写 F 的完整二阶 Taylor 展开，其对称二次系数即 Hessian。局部正定和梯度/几何访问是必要条件，不能把一般非凸 HVP 自动当成正定 pullback metric。

核查定位：p004:L0003-L0039, p005:L0003-L0054, p006:L0034-L0060, PDF physical page 7, Algorithm 1；mechanism_and_novelty_scope_confirmed

Theorem 5.1 的步长陈述：原 PDF 第 7 页确实允许 η∈(0,2/L) 并给出 (1−ημ)^t 目标差上界。取 F=θ²/2、G=1、μ=L=1、θ0=1、η=3/2，条件全局成立，一步实际差为1/8，而声称右端为−1/4。该定理按当前步长范围写法不成立，需要收窄范围或修正收缩因子；这不否定修正后的经典小步长结论。

核查定位：PDF physical page 7, Theorem 5.1, local_check/bounded_algebra_checks.json；printed_theorem_counterexample_confirmed_by_algebra

C.2 下界困难例：原 PDF 第 18 页的困难例 Hessian=G_U/κ 仅有1和1/κ两个特征值，允许历史自适应正标量步长且历史包含当前梯度。取 Ht=I，先 η0=1 消去特征值1方向；若未收敛，g1=θ1/κ，令η1=(θ1ᵀg1)/||g1||²即得到θ2=0，对任意旋转U成立，且没有直接调用G。故所构造困难例不能支持其正指数下界。结论限于这份证明，未排除其他受限算法类或修正困难例存在有效下界。

核查定位：p005:L0048-L0054, p006:L0003-L0015, PDF physical page 18, C.2, local_check/bounded_algebra_checks.json；hard_instance_proof_gap_confirmed

报告数值与计算预算：原 PDF 第 44 页表 16 的 GCO 六域值为56.4、40.2、51.3、27.1、68.9、43.6，简单均值47.9167%，而Avg印51.8%；所读部分未说明其他加权口径。附录A每步都估κ，逆幂过程内部还调用CG，不能只按触发的几何步计全部估计成本。按完整网格是GCO 792组对欧式24组，实际总搜索耗时未知；外层迭代去除κ不等于总计算没有κ依赖。

核查定位：PDF physical page 44, Table 16, p042:L0008-L0017, p007:L0003-L0013, p013:L0013-L0053, p014:L0003-L0060, local_check/bounded_algebra_checks.json；aggregation_unresolved_and_compute_scope_qualified

本地补充/限定：["通过原 PDF 和显式代数确认定理5.1原步长范围反例，以及C.2两特征值困难例的二步解；不是数值优化实验。", "只核查了DomainNet这一聚合问题；Pro提出的其他平均数、C.7和若干证明细节未在本地逐项验证，不能统一称全部已证错误。", "区分方法本身的门控预条件价值与当前文稿未成立的强理论保证。"]

核查局限：["未执行作者代码、优化器、模型训练、数据生成或新的研究练习；仅作源文公式和表数核算。", "未完成全部证明审计，未核看所有实验图、聚合规则或原始数据。", "外部前作未阅读全文，L1 为当前 AI 阅读判断，不涉及作者动机判断。", "Pro 只看全文文本，本地仅观察三页原 PDF。"]

