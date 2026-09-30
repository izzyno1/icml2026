# 单轮全文初评与有界本地核对 81–90

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro081 · Alignment between Brains and AI: Evidence for Convergent Evolution across Modalities, Scales and Training Trajectories

论文 OR_XrRqY9QOSa；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8", "source_url": "https://api2.openreview.net/pdf?id=XrRqY9QOSa\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "1ab29d6522186e01afd5c7f6e583dd35d9e231b3dac9a83a4d83813a68bad0b8", "source_pdf_sha256": "3f589ba4eeb8e9a530a0c3730043bff990cb4e6bc380f956d78644531d748eb6"}], "read_ranges": ["TEXT_OR_XrRqY9QOSa_3f589ba4eeb8：物理页1—20连续全文；正文1—9页、参考文献9—14页、附录A—G及图表提取文字15—20页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未见页标缺口，但未提供PDF图像；图1—7的散点、曲线、皮层映射和聚类结构不能视觉核验。", "双栏文字存在串行，公式及图表标签可能失真；表格可读数值按作者报告提取，不自行修正异常。"]}

问题：模型性能提升是否伴随更强脑表征对齐；对齐是否在训练中领先性能；层深和测量尺度如何对应皮层组织？

方法：图像输入视觉模型，首条COCO图注输入语言模型，均与同一图像诱发fMRI比较。提取逐块特征及语言模型末token；高维特征经PCA保留至少95%方差后计算RBF-CKA，组织为180脑区、8层深分箱并平均4被试；另分析训练轨迹、核尺度及聚类。

作者主张：630模型、6000万余对齐测量显示，性能较高的模型自发形成更强脑对应。

论文证据：表5报告模态内部相关；表7控制参数量后，两个主要汇总关系仍显著。

模型推断：扩大既有现象的覆盖范围；配置测量数不是独立样本数，也不能据此比较语言与视觉的总体能力。

定位：['TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p3—4§3.1、p17表5、p18表7。']

作者主张：脑对齐提前出现，且过去对齐预测未来性能比反向更稳定。

论文证据：表6的10条轨迹中，正向显著9条，反向显著3条。

模型推断：提供早期训练指标的候选经验知识，但未建立对齐促进性能的机制因果关系。

定位：['TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p5—6§3.3、p18附录G表6。']

作者主张：对齐具有模态特异的层级组织，深层视觉逐渐接近语言表征。

论文证据：正文报告视觉深层、语言中层及关联网络偏好；表9给出随层深下降的跨模态对齐向量距离。

模型推断：支持脑对齐特征空间中的趋近，不等于原始内部计算机制相同。

定位：['TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p4—7§3.2—3.4、p19表9。']

key_results：[{"setting": "主模型池的模态内性能—对齐相关，作者报告。", "baseline": "不同性能模型；无干预对照。", "metric_or_guarantee": "Pearson r、95% CI及FDR p值。", "reported_values_and_units": "语言Leaderboard 2：r=0.89，CI=[0.79,0.94]，FDR p<1.1e-12；视觉ImageNet：r=0.53，CI=[0.47,0.59]，FDR p<1.5e-43。相关系数无量纲。", "information_and_compute": "4被试；每人按文中记数含24980训练、2770测试刺激，实际CKA取样拆分未明；GPU型号及耗时未报告。", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p15 A.1、p17表5。\n"}, {"setting": "控制log10参数量的可用数据子集。", "baseline": "同一子集的原始相关。", "metric_or_guarantee": "偏Pearson相关。", "reported_values_and_units": "语言Average，n=35：0.880→0.544，p=8.8e-4；视觉ImageNet，n=578：0.496→0.307，p=5.1e-14。语言MMLU-PRO偏相关0.273，p=0.119，不能称所有基准仍显著。", "information_and_compute": "只控制参数量，不等于控制训练数据、算力或家族。", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p18表7。\n"}, {"setting": "10条训练轨迹的lag-1双向Granger F检验。", "baseline": "反向预测及不含另一变量滞后项的自回归。", "metric_or_guarantee": "表6按p<0.05统计显著轨迹数。", "reported_values_and_units": "对齐→性能：Pythia 6/6、MixNet 3/4；性能→对齐：1/6、2/4。MixNet-XL正向p=0.370，不显著。", "information_and_compute": "Pythia使用既有检查点；MixNet从零训练ImageNet-1K并按对数间隔保存检查点。具体训练预算和该表所用性能指标未明示。", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p15 A.4、p18表6。\n"}, {"setting": "视觉与语言模型脑对齐向量的深度分箱比较。", "baseline": "深度1/8对比8/8。", "metric_or_guarantee": "Wasserstein距离与余弦相似度。", "reported_values_and_units": "Wasserstein：0.01519→0.00564；余弦相似度：0.9827→0.9955；跨8箱Spearman分别−1.00、+1.00。不是原始模型激活间距离。", "information_and_compute": "表9未给这些趋势的不确定区间。", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p18—19附录G表9。\n"}]

prior_work_candidates：[{"citation_as_printed": "Conwell, C., Prince, J. S., Kay, K. N., Alvarez, G. A., and Konkle, T. A large-scale examination of inductive biases shaping high-level visual representation in brains and machines. Nature Communications, 15(1):9383, 2024.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "NSD上的多模型脑表征比较。", "claimed_difference": "据本篇转述，前作224视觉模型及物体选择性皮层；本作扩至语言、全皮层及训练动力学。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p8§4、p10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "AlKhamissi, B., Tuckute, G., Bavard, A., and Schrimpf, M. From language to cognition: How LLMs outgrow the human language network. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "语言模型训练中的脑对应变化。", "claimed_difference": "前作为语言诱发轨迹；本作使用图像诱发fMRI并纳入视觉训练轨迹。方向性分析是否已被前作覆盖待核。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p8§4、p9 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Huh, M., Cheung, B., Wang, T., and Isola, P. Position: The platonic representation hypothesis. In Proceedings of the 41st International Conference on Machine Learning (ICML), 2024.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "高性能模型表征趋同假说。", "claimed_difference": "本篇自述以人脑替代模型间趋同目标，作为外部生物锚点；不据此认定首次引入脑比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p8§4、p11 References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "暂定增量主要在跨训练轨迹的早期对齐和方向预测这一经验知识，而非测量数量或新算法；未达到路线级机制发现。", "central_increment": "前作已有视觉脑比较和语言训练轨迹（本篇转述）；本作在图像诱发条件下联合两模态、全皮层和方向检验，证据为表5—9，尚待排除共同训练趋势。", "soundness_observation": "静态相关有明确数据；纵向解释、噪声上限和内部统计口径存在重要待核点，不能将相关或Granger预测等同机制因果。", "significance_observation": "可为脑对齐评测和早期训练诊断提供线索；未展示据此改善训练的效果。工程成本因资源账本缺失无法量化。", "main_open_question": "去除共同训练趋势并采用合适采样和留后预测后，脑对齐是否仍有独立的领先预测价值？"}

limitations：[{"text": "被动看图及低时间分辨率fMRI限制外推；语言结果是视觉语义对齐，不是一般语言能力。作者另承认指标依赖及基准污染风险。", "basis": "author_report", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p9 Limitations。\n"}, {"text": "未交代Granger的平稳性、去趋势、时间网格处理及表6多重校正；显著性方向不对称本身不足排除共同训练趋势。", "basis": "model_inference", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p7§3.5、p18附录G表6。"}, {"text": "A.3使用6/8深度的最高5%脑区均值，但选择与评估是否独立不明；参数偏相关也未控制模型家族、训练语料等混杂。", "basis": "model_inference", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p15 A.3、p18表7。\n"}, {"text": "报告口径需核：主文36语言模型，附录F/G却写38；表7子集缩减未解释。正文计数举式630×30×180×4×12实际为163296000，并非所写约59500000；这不等于已确定真实总量。", "basis": "model_inference", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p2§2.2、p17 F、p18表7、p19 G。\n"}, {"text": "表1称FDR校正却列出表5的原始p值；表5部分Spearman区间上界超过1；Δ称CKA差但报告−5.30，归一化不清。跨被试两两CKA均值也未被证明是模型对齐的严格上界。", "basis": "model_inference", "locator": "TEXT_OR_XrRqY9QOSa_3f589ba4eeb8，p3§2.2、p4表1、p6§3.4、p17表5、p18 Noise ceiling。\n"}]

minimal_check：{"question": "对齐的领先预测能否超出共同训练趋势？", "control": "在原10条轨迹上明确训练进度网格并去趋势；比较仅含性能历史和训练进度的模型，与加入对齐历史的模型，反向同样处理。", "observable_outcome": "时间分块留后预测误差是否稳定降低，并在多重校正后保留正向优势。", "resources": "需检查点时间、对齐及性能原始序列；仅重算统计，不需重新训练模型，具体耗时未知。", "failure_or_stop_condition": "优势消失或反向同样强，则不支持独立领先指标；缺原始序列或有效时间点不足则停止并记录不可检验。"}

missing_fields：["原始图像、逐模型及逐检查点数据、可核对模型清单。", "实际CKA刺激拆分、重复试次处理、脑区选择独立性及各结果完整聚合规则。", "核尺度清单与归一化的统一定义；正文和附录设置存在不一致。", "Granger具体性能指标、时间序列诊断及表级多重校正规则。", "训练种子、完整超参数、硬件数量、GPU时和内存成本。", "前作全文及未印出的DOI/arXiv标识；当前附件出版版本身份。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

早期对齐可作候选训练诊断，但要先拿原始序列澄清进度、去趋势、多重检验和测量清单，才支持独立领先信号。

身份、模态与测量单位：完整题名和20页附件绑定。语言模型输入同一图像的首条COCO图注，脑数据是四名被试看图诱发fMRI；这是视觉语义对应，不是一般语言诱发脑活动或多感官智能。630模型由36语言和594视觉组成，附录另出现38语言，需核清可用子集。多层/脑区/核的CKA配置不是独立研究样本。

核查定位：p001 title, p002, experimental framework, p015, A.1–A.3, PDF physical page17, F；identity_modality_and_dependence_scope_confirmed

静态相关和控制变量：原图2及表5确认语言Leaderboard2 Pearson .89、95%CI[.79,.94]、FDRp<1.1e−12；视觉ImageNet .53、CI[.47,.59]、FDRp<1.5e−43。参数偏相关汇总仍为.544/.307，但MMLU-Pro .273、p.119不显著。只控制log参数量，未控制家族、训练语料等，不能称排除所有规模混杂。

核查定位：PDF physical page4, Figure2, PDF physical page17, Table5, PDF physical page18, Table7；decisive_correlations_and_partial_control_limits_confirmed

纵向领先与共同趋势：原图4为训练进度对数轴且两条不同单位y轴；表6按p<.05计正向9/10、反向3/10。未见平稳性/去趋势、非均匀时间网格和检验族说明，方向不对称不能单独排除共同训练驱动。以全部20方向检验作为同一族的条件示例，Holm .05校正保留6条Pythia正向、0反向；这是基于印出p值的本地算术，非原始轨迹重分析，也不证明方向效应消失。

核查定位：PDF physical page6, Figure4, p007, Section3.5, p015, A.4, PDF physical page18, Table6, local_check/granger_printed_p_holm20.json；uncorrected_direction_counts_confirmed_conditional_multiplicity_check_saved

测量总数及统计报告冲突：原式630×30×180×4×12实际为163296000，不是印出的约59500000；A.3列11个核尺度而计数式用12。不能据此确定实际运行数，需模型/层/核清单。表1称FDR却对应表5原始p列。表5多个Spearman区间上界>1，可能是未约束近似区间，但方法未明，不能把上界当可达相关值。

核查定位：p002, aggregation count, p015, kernel list, PDF physical pages4/17, Tables1/5, local_check/granger_printed_p_holm20.json；count_arithmetic_and_statistical_label_conflicts_confirmed

天花板与表征趋近解释：跨被试两两CKA均值未被证明为模型CKA的严格上界；超过它不等于达到所有可恢复脑信号。表9随深度Wasserstein .01519→.00564、余弦.9827→.9955是脑对齐向量空间的趋近，不是原激活计算机制相同。A.3选6/8深度的最高5%脑区，选择与评估独立性未说明。核尺度Delta正文称CKA差但给−5.30，图注称normalized，统一尺度仍需解释。

核查定位：PDF physical page18, noise ceiling, p019, Table9, p015, A.3, p003/p006–p007, scale definition；noise_ceiling_and_mechanistic_inference_not_established

本地补充/限定：["补做印出20个方向p值的条件Holm示例：6正向/0反向；明确检验族假设，未替作者选择协议。", "超1的相关区间记为方法/解释问题，不把它自动认定为原始数据造假或所有相关无效。"]

核查局限：["仅对印出p值和乘法作本地算术，没有重做时间序列分析、模型训练或脑数据拟合。", "未核读前作、完整模型清单或刺激划分，不能确认机制因果与真实测量总量。", "第1页仅读标题开头，版本角色未确认。"]


## pro082 · Multi-task Linear Regression without Eigenvalue Lower Bounds: Adaptivity, Robustness, and Safety

论文 OR_D5Ijcnz1L9；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_D5Ijcnz1L9_7aad88144300", "source_url": "https://api2.openreview.net/pdf?id=D5Ijcnz1L9\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "fb846f4bc2966de5d7ea4bc443536d973e39c0dc4d4e1f2d8c5c650b1c43b69b", "source_pdf_sha256": "7aad881443009dd759e651fd4474277249d5ff88bcd2238fbc7c0d32535e482c"}], "read_ranges": ["TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页1–47连续全文，含正文§1–8、参考文献及附录A–I。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["题名与清单一致，连续页标未见缺页；版本角色未经核实。", "图1–4图像、曲线和误差条不可见；部分双栏文字、分式及上下标失序，表1数值可读。", "未提供前作全文、代码内容或实验原始数据；未搜索、复现或逐条核证全部证明。"]}

问题：多数任务参数在未知ℓ2半径δ内相近、少数任务参数任意时，能否在奇异或快速谱衰减设计下获益，并在迁移无益时保持独立学习速率？

方法：联合最小化Σ_j w_j[f_j(θ_j)+λ_j∥θ_j−β∥Σ_j]，以经验二阶矩衡量任务与中心的预测差异。等样本量时w_j=1；异质样本量时w_j=n_j、λ_j∝√(d/n_j)。无需已知δ、ε、S或B；线性使用平方损失，GLM使用负对数似然。

作者主张：以预测几何正则与balancedness替代欧氏正则及逐任务LBSM要求。

论文证据：给出联合凸目标，并在行空间上处理秩亏；通过局部汇聚等价性和离群损失Lipschitz扰动建立分析。

模型推断：实质增量是更弱平均覆盖条件下的几何化扩展，而非首次提出稳健多任务学习。

定位：['TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页4–7，§3–5；物理页15–27，附录B–C。']

作者主张：同时获得自适应、鲁棒和安全保证，并推广至总体风险、GLM及异质样本量。

论文证据：定理2给出无balancedness要求的安全界和有条件迁移界；定理3–5提供扩展；总体任务近极小极大性借助前作正交设计子模型下界。

模型推断：安全指常数及对数因子意义下匹配ITL速率，不是每次实验均优于ITL；总体风险也不是无条件摆脱谱限制。

定位：['TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页7–9，定理2–4；物理页35–36，定理5；物理页43–45，附录H。']

key_results：[{"setting": "固定设计线性模型、每任务n个样本；迁移部分要求B≲min(1/ε,m)。", "baseline": "ITL；本篇转述的ARMUL理论。", "metric_or_guarantee": "以至少1−κ概率同时控制各任务样本内预测MSE。", "reported_values_and_units": "固定充分大的q、忽略对数：所有任务E_j^in≲d/n；内点E_j^in≲Bd/(mn)+min{Bδ²,d/n}+B²ε²d/n。", "information_and_compute": "λ=q√(dζ/n)，ζ=log(16m/κ)；条件独立、1-sub-Gaussian噪声，∥Σ_j∥op≤1；理论针对精确最小化解。", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页7，定理2；物理页26–27，附录C.4。\n"}, {"setting": "任务内i.i.d.设计的总体预测风险。", "baseline": "样本内界及独立任务速率。", "metric_or_guarantee": "经验风险向总体风险转换。", "reported_values_and_units": "E_j≤ν_jE_j^in；已知∥θ_j⋆∥≤ξ并作Σ_j半范数投影时，E_j≲E_j^in+Õ(ξ²U_j²/n)。", "information_and_compute": "ν_j来自经验与总体二阶矩可比性，U_j控制协变量范数尾部；一般Type 2分布获得常数ν的样本阈值仍为Õ(U_j²/γ)，γ为最小非零总体特征值。", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页8，定理3；物理页35，附录E；物理页44，引理7。"}, {"setting": "合成线性数据：n=100、m=30、d=30，ε=0.1、α=1、总体balancedness为1，δ从0.2扫至3.2。", "baseline": "DP、ITL、ARMUL。", "metric_or_guarantee": "总体MSE，作者报告。", "reported_values_and_units": "全任务MSE范围0.0138–0.0259，最佳竞争基线始终高于0.041；内点MSE范围0.0022–0.0136。", "information_and_compute": "30次Monte Carlo；本法与ARMUL均5折交叉验证、8个q候选；数值来自正文，不从不可见图线读取。", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页12，附录A.1。"}, {"setting": "HAR：30人各为一任务，561维原始特征、不做PCA，standing对其余活动；每任务80%训练、20%测试。", "baseline": "DP、ITL、ARMUL，均使用logistic损失。", "metric_or_guarantee": "测试分类错误率，作者报告。", "reported_values_and_units": "均值%（跨划分SD，百分点）：本法1.25（0.32）；DP 7.61（0.46）；ITL 4.67（0.51）；ARMUL 5.24（0.43）。", "information_and_compute": "30次随机划分；本法与ARMUL使用5折验证，q=0.05至0.50、步长0.05。未报告硬件或耗时。", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页14–15，附录A.2、表1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Duan, Y. and Wang, K. (2023). Adaptive and robust multi-task learning. The Annals of Statistics, 51(5):2015–2039.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "污染任务模型、ARMUL共享中心目标；附录引理11和13明确复用其扰动与不变区域引理。", "claimed_difference": "欧氏范数改为任务预测半范数，以单侧平均覆盖替代逐任务LBSM，并转向预测风险保证。", "basis": "target_paper_only", "target_locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页3，式(2)；物理页10，参考文献；物理页46–47，引理11、13。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "允许奇异设计且保留稳健迁移与安全速率，是实质性保证扩展；尚非路线级新范式。", "central_increment": "前作已有自适应稳健MTL（本篇转述）；本作在平均几何覆盖下新增无逐任务谱下界的预测保证，证据为定理2及附录证明；前作覆盖和B最优性待核。", "soundness_observation": "主要证明链可追踪，但未逐条核证。预测MSE不能无条件等同于前作参数误差；近似优化实现与精确解定理之间缺少误差控制。", "significance_observation": "澄清病态协变量不必阻断安全迁移；现有实验仍以合成诊断和单个真实数据集为主。", "main_open_question": "统一范数约束、调参预算和优化精度后，矩阵加权是否仍能解释HAR中的大幅优势？"}

limitations：[{"text": "安全界不要求B有限，但迁移界要求B及污染程度足够小；离群指参数不相近，并非任意破坏全部观测模型。", "basis": "author_report", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页3、5、7，模型、假设1及定理2。"}, {"text": "HAR标签与PCA流程不同于前作，不能跨论文直接比表；Bemp≈30也不是未知内点集合对应B的认证。", "basis": "author_report", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页6，经验诊断；物理页14–15，附录A.2。"}, {"text": "实验未明确GLM参数半径、曲率界及求解容差；L-BFGS-B使用数值floor，尚不能确认实际求解满足全部理论条件。", "basis": "model_inference", "locator": "TEXT_OR_D5Ijcnz1L9_7aad88144300：物理页5，实现；物理页8，假设2；物理页14–15，附录A.2。"}]

minimal_check：{"question": "HAR增益是否主要来自正则几何？", "control": "固定一个训练测试划分与5折索引，统一参数域、求解精度和q网格，仅替换欧氏范数与矩阵半范数。", "observable_outcome": "配对测试错误率差异及两目标的最优性残差。", "resources": "HAR数据和凸优化器；作者代码需另行获取核读，硬件与运行成本未知。", "failure_or_stop_condition": "任一目标未充分收敛则停止归因；差异消失则削弱实验机制解释，但不据此否定统计定理。"}

missing_fields：["最终出版版本身份", "图1–4逐点数值及误差条", "实验硬件、耗时、内存和迭代预算", "GLM实验约束及数值求解精度", "前作独立核读与实验复现"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

将参数误差转向预测几何、并分开安全与迁移条件，是可继续研究的明确保证增量；实验后续需统一优化精度和GLM域。

身份、目标与模型假设：完整题名及47页附件绑定。中心改动是共享中心非平方范数从欧氏改为经验Sigma半范数，衡量设计上的预测差异。仍假设线性条件模型、独立次高斯噪声及协方差算子范数归一化≤1；离群是任务参数任意，非任意破坏全部观测。预测误差不等于无谱下界时的参数误差。

核查定位：p001 title, p003, model/Definition1, PDF physical page4, Eq6–7；identity_objective_and_statistical_target_confirmed

安全速率与有利迁移的区别：原Theorem2对所有任务给q²(d/n)log(16m/kappa)级安全界，无需B有限；更快内点界要求所有任务包括离群的Sigma_j≤B Sigma_S且B≲min(1/epsilon,m)，含Bd/(mn)、min(Bdelta²,q²d/n)、q²B²epsilon²d/n。安全是速率与常数意义，不是每次都优于ITL；近极小极大也不包含任意B最优性。

核查定位：p005, Assumption1, PDF physical page7, Theorem2/optimality discussion；decisive_rate_and_conditions_confirmed

总体与GLM附加条件：原Theorem3需经验/总体可比因子nu，或已知参数半径xi、同半范数投影及协变量尾尺度U的xi²U²/n余项。一般Type2可比性的样本门槛仍为tildeOmega(U²/gamma)，gamma为总体最小非零特征值。GLM另需已知有界参数域和链接曲率正下界；标题不能扩展成任何总体/GLM风险无条件摆脱谱条件。

核查定位：PDF physical page8, Theorem3/Assumption2, p035, population proof, p044, Lemma7；population_and_glm_scope_confirmed

HAR实证与balancedness诊断：原表1错误率1.25±.32%、DP7.61±.46%、ITL4.67±.51%、ARMUL5.24±.43%，30次随机80/20划分、30被试、561维、不做PCA；标签standing不同于前作sitting，不能跨论文直接比表。Bemp约30用全任务平均：由Sigma_j≤m Sigma_all可知Bemp≤m=30，故其接近该诊断上限，不能单凭此值称离退化很远。Bemp不认证未知内点B；实证收益与充分条件宽松性分开。

核查定位：p006, empirical diagnostic, p014, A.2, PDF physical page15, Table1 and paragraph；empirical_values_and_diagnostic_upper_bound_confirmed

KL解释与求解实现边界：同方差Gaussian固定设计KL为n||theta−beta||_Sigma²/(2sigma²)，所以本文非平方半范数正比sqrt(KL)，不是p4所说的KL本身。这个解释修正不改变所列凸目标。实现用L-BFGS-B并在范数梯度加入floor，未报GLM参数域、求解容差或总耗时，不能把精确最小化解的统计界当作实现已验证。

核查定位：PDF physical page4, objective interpretation, p005, Implementation, p014, tuning protocol；sqrt_kl_interpretation_corrected_optimization_accuracy_unverified

本地补充/限定：["补充Bemp≤m的直接Loewner界；HAR约30已接近全任务诊断的上限。", "非平方预测半范数与sqrt(KL)成比例，校正正文解释但保留方法与定理范围。"]

核查局限：["未验证47页全部证明、作者代码或前作全文；没有HAR重训。", "Bemp和KL仅局部代数核查，未估计真实内点集合或理论常数。", "第1页仅读题名，未量化图中逐点误差或算力，版本角色未确认。"]


## pro083 · Exact Functional ANOVA Decomposition for Categorical Inputs Models

论文 OR_qC9FEfYjai；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_qC9FEfYjai_468efc7f0cd3", "source_url": "https://api2.openreview.net/pdf?id=qC9FEfYjai\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "1b40df2eea3312debcdf24bc55cd9f2254274df8ae5058b3ec38f6d1054bf353", "source_pdf_sha256": "468efc7f0cd378129098cf2dfb96ff03865a141666c6fdf14c213bd325320fcf"}], "read_ranges": ["TEXT_OR_qC9FEfYjai_468efc7f0cd3：物理页1–18全部文本，包括正文§1–6、影响说明、参考文献及附录A.1–A.6、B.1–B.2、C。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["页标1–18连续，未发现缺页；仅有文本，未查看PDF图像或图1–3。", "双栏文字与部分公式混排；表5幂次及维度对应不清，未采用其网格规模数值。", "补充代码和前作全文未提供；附件是否最终出版版未经核实。"]}

问题：如何把具有相关分类输入的黑盒预测分解为主效应及高阶交互，并处理非矩形、稀疏支持？

方法：输入支持上的模型输出及联合或经验分布；构造φ_A^z=∏[1{x_i=z_i}−1{x_i=N_i−1}]/p_A(x_A)，求解Gram系统Γc=μ，按变量集合聚合为f_A，再等分交互得到Shapley归因。稀疏情形按低阶优先选独立列，高维按秩预算截断。

作者主张：任意依赖和稀疏支持下均可精确构造层级正交ANOVA；满支持时唯一，独立时恢复经典ANOVA及相应SHAP。

论文证据：定理3.2、推论3.4–3.5及附录证明；附录C在作者称满足满支持条件的设置中报告接近机器精度的正交性。

模型推断：显式构造具有实质理论增量，但稀疏支持下字典自动正交的断言存在手算反例，不能把完整保证视为已证实。

定位：['TEXT_OR_qC9FEfYjai_468efc7f0cd3：p4定理3.2及推论3.4–3.5。\n', 'TEXT_OR_qC9FEfYjai_468efc7f0cd3：p12–15，附录A。']

作者主张：利用观测支持、向量化和低秩选基，以一次全局计算高效解释大量样本。

论文证据：算法1及表6–7展示秩预算下的重建精度与耗时；MNIST另采用常量像素筛除、方差排序及局部空间搜索。

模型推断：体现可用的计算方案，但高维结果属于近似重建，并非全交互精确分解；依赖情形的ANOVA归因也未证明等同于通常的条件SHAP。

定位：['TEXT_OR_qC9FEfYjai_468efc7f0cd3：p5–9，§4–5、式(23)。']

key_results：[{"setting": "独立均匀满网格：CAR EVALUATION的Random Forest与NURSERY的MLP。", "baseline": "KernelSHAP，背景样本200。", "metric_or_guarantee": "完整分解及Shapley计算时间；两种归因之间的100×ISE。", "reported_values_and_units": "作者报告耗时分别0.5秒、54秒；表3–4的100×ISE最大值分别为2.89、4.4。", "information_and_compute": "网格大小分别1728、12960；所有实验使用MacBook Pro M4、32GB内存。未报告KernelSHAP联盟采样预算和对应耗时。", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p7表2–4及比较段，p16附录B.1。\n"}, {"setting": "经验分布上的稀疏数据：MUSHROOMS/XGB、POKER/Transformer、CONNECT-4/Random Forest、DOTA2/深层全连接网络。", "baseline": "各自原黑盒输出；不是统一的外部解释器速度比较。", "metric_or_guarantee": "所选秩、重建R²和耗时。", "reported_values_and_units": "MUSHROOMS：秩86，R²≈1，MSE≈10^-15，0.3秒；POKER：秩5000，R²=0.79，10分钟；CONNECT-4：秩5000，R²=0.70，37分钟；DOTA2：秩4000，R²=0.41，39分钟。均为作者报告。", "information_and_compute": "基于经验概率及模型输出；采用上述M4/32GB硬件。高维三任务均为预算截断。", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p7 MUSHROOMS段、p8表6。\n"}, {"setting": "Binarized MNIST，60000×784，解释MLP预测类别3的概率。", "baseline": "仅主效应：秩674，R²=0.54，10秒。", "metric_or_guarantee": "低秩重建R²、相对MSE和耗时。", "reported_values_and_units": "秩5000：R²=0.83，相对MSE=15%，300秒；秩10000：R²=0.86，相对MSE=12%，15分钟。均为作者报告。", "information_and_compute": "M4/32GB；使用像素筛选、方差排序和空间邻域限制，不是无结构的穷举搜索。", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p9表7及相邻段落。\n"}, {"setting": "附录C合成二阶交互任务，n=10000，XGB为100棵深度2树；取表8的d=6行。", "baseline": "TreeHFD。", "metric_or_guarantee": "嵌套分量间最大绝对内积；两方法Shapley值的积分平方差。", "reported_values_and_units": "正交性指标：本法1.42×10^-16，TreeHFD为8.31×10^-3；Shapley积分平方差3.81×10^-4。双方完整重建仅有文字报告。", "information_and_compute": "作者称满足满支持条件，但未说明具体输入分布和类别数；该指标检查f_A与f_B，并非枚举所有低阶函数g。", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p17表8，p18指标定义。\n"}]

prior_work_candidates：[{"citation_as_printed": "Hooker, G. Generalized functional anova diagnostics for high-dimensional functions of dependent variables. Journal of Computational and Graphical Statistics, 16(3):709–732, 2007.", "identifier_if_present": "http://www.jstor.org/stable/27594267\n", "relation_candidate": "理论扩展", "shared_component": "层级正交的Generalized Functional ANOVA。", "claimed_difference": "本作给出有限分类域显式构造。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p2背景、p4§3.2、p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Il Idrissi, M., Bousquet, N., Gamboa, F., Iooss, B., and Loubes, J.-M. Hoeffding decomposition of functions of random dependent variables. Journal of Multivariate Analysis, pp. 105444, 2025.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "依赖输入分解的存在性和唯一性。", "claimed_difference": "由存在性推进到可计算构造，并声称覆盖稀疏支持。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p4§3.2、p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Bénard, C. Tree ensemble explainability through the hoeffding functional decomposition and treehfd algorithm. Advances in Neural Information Processing Systems, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "ANOVA主效应、交互及归因计算。", "claimed_difference": "本作不限树模型，声称精确正交并处理稀疏支持。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p1–2相关工作、p10参考文献、p17–18附录C。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "核心是显式分解构造与理论保证，而非单纯性能改进，新意暂评L2；但稀疏正交性有具体反例，等级不代表正确性认可，也不证明历史首创。", "central_increment": "前作已研究依赖输入ANOVA的存在唯一性及树模型估计（本篇转述）；本作在有限分类域新增逆概率字典和矩阵求解。满支持部分未被下述反例否定，任意稀疏支持推广则需修正。", "soundness_observation": "按定义3.1手算：令支持为{0,1,2}²去掉(2,2)，剩余8点等概率。φ_{12}^{(0,0)}仅在(0,0)、(0,2)、(2,0)取8、−8、−8，故均值−1，不与常数正交；该列也不是主效应加和，可能通过秩检验。这直接否定引理A.3的无条件字典正交性，式(42)把缺失组合当作可完整配对。另引理A.2由算子可逆推出子空间span(G_A)不变，论证亦有缺口。此为文本定义的局部推导，非实验复现。\n", "significance_observation": "若修复支持约束，可为分类黑盒提供统一全局分解；现有稀疏重建精度不能替代层级正交和归因有效性证明。", "main_open_question": "如何约束或重构稀疏字典，使求解结果真正层级正交，同时保留所宣称的计算优势？"}

limitations：[{"text": "作者承认维数灾难、贪心搜索瓶颈及稀疏分解不唯一；给出的搜索最坏复杂度为O(|E|r²)，低秩预算并未消除指数候选空间。", "basis": "author_report", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p6复杂度段、p8–9讨论。"}, {"text": "经验分布上的精确重建不等于总体分解正确；缺少未观测组合、重采样稳定性和样本外归因检验。", "basis": "model_inference", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p6经验分布说明、p7–9实验。"}, {"text": "TreeSHAP、attention rollout与ANOVA不一定解释同一量；残差均摊也可能改变归因。图像未提供，不能独立验证视觉解释质量。", "basis": "model_inference", "locator": "TEXT_OR_qC9FEfYjai_468efc7f0cd3：p7–9，图1–3、式(23)。"}]

minimal_check：{"question": "删去一个支持点后，算法选出的交互列是否仍层级正交？", "control": "对照为3×3完整均匀网格；处理组删除(2,2)，其余8点均匀。均按低阶优先、交互索引(0,0)优先选基。", "observable_outcome": "检查φ_{12}^{(0,0)}的均值和入选情况；手算预测处理组均值−1而对照为0，且处理组该列可增加主效应空间的秩。", "resources": "纸笔或至多9点的枚举脚本，无需训练黑盒；运行成本未测。", "failure_or_stop_condition": "任一入选交互与常数内积非零，即否定秩选基自动保证层级正交；若必须增加筛选约束，则原算法或适用条件需修改。"}

missing_fields：["训练时长、随机种子、重复运行方差及明确训练/评测划分未报告。", "基线耗时、KernelSHAP联盟采样预算、数值秩阈值未报告。", "附录C具体分布与类别数、MNIST邻域搜索细节不完整。", "未提供图像、补充代码和前作全文；未搜索、运行作者代码或复现实验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

显式满支持构造可继续研究；稀疏应用前须补正交约束或修改字典，不能直接采用现有精确ANOVA宣称。

身份及精确性对象：完整题名与18页附件一致。定义3.1以边缘概率倒数加权分类对比，Gram系统求系数；满支持唯一性、稀疏支持选定基后的系数唯一性、高维低秩近似是三个不同结论。重建模型输出不自动证明分量层级正交或总体归因正确。

核查定位：p001 title, PDF physical pages3–4, Definition3.1/Theorem3.2/Corollary3.4, p005–p006, selected basis and low-rank；identity_construction_and_exactness_scope_confirmed

八点稀疏支持的精确算术核查：按原定义取3×3网格删(2,2)，其余8点等概率。phi12^(0,0)在(0,0)/(0,2)/(2,0)为8/−8/−8，均值−1。按低阶优先选基，主效应秩5，加该交互秩6，故不会被秩检验丢弃。令黑盒f等于该列，继续选至满秩8并精确解Gram系统，重建误差为0，但返回交互均值−1、常数0而E[f]=−1。完整9点对照交互均值0。独立Fraction脚本与逐点/系数结果已保存，不是作者实验复现。

核查定位：PDF physical page3, Definition3.1, PDF physical page6, Algorithm1, local_check/check_sparse_dictionary.py, local_check/sparse_dictionary_check.json；sparse_dictionary_and_rank_selected_orthogonality_counterexample_confirmed

证明缺口与反例边界：原式42把受限支持的和拆成完整二点乘积，删角后配对抵消不成立。A.2还从MA在整个函数空间可逆推出span(MA GA)=span(GA)，这不一般成立：一维二分类p=(1/4,3/4)，psi=(1,−1)、phi=(4,−4/3)不同张成直线。后者只是证明步骤缺口，不直接否定总字典张成。八点例否定无条件字典正交/仅秩选基保证，未否定另加约束的稀疏ANOVA存在性或满支持构造。

核查定位：p013, LemmaA.2/A.3, PDF physical page14, Eq42–44；support_factorization_and_subspace_invariance_gaps_scoped

高维结果实际为近似：原表6 POKER秩5000/R².79/10分钟，CONNECT4秩5000/.70/37分钟，DOTA2秩4000/.41/39分钟，不能称全交互精确分解。MNIST表7秩5000 R².83/300秒，10000 .86/15分钟，依常量像素筛除、方差排序及局部空间搜索；这些耗时是重建流程，不是与所有解释器统一预算的速度比较。

核查定位：PDF physical page8, Table6, p009, Table7 and preprocessing；approximation_and_runtime_scope_confirmed

归因含义：作者只在独立输入时联系经典SHAP；依赖/稀疏设置的分量等分不可自动视为通常的条件SHAP。式23将未解释残差均摊给全部特征，能保持总和却不自动保持无关特征归因等性质。图1的MNIST可视化和图3的扑克重要性是特定模型解释，不能替代正交性或样本外归因检验。

核查定位：PDF physical page3, Eq5/Figure1, PDF physical page8, Eq23/Figure3；attribution_semantics_and_residual_convention_bounded

本地补充/限定：["已完成Pro提出的8/9点枚举，并扩至精确选基和Gram求解：完全重建仍可不正交。", "反例范围限定原字典及选基保证，未否定一切稀疏HFD或满支持结论。"]

核查局限：["只运行最多9点的独立有理数代数脚本，未执行作者代码、黑盒训练或论文数据集实验。", "未全面证明修订方法或核读前作；未确认经验分布之外的归因有效性。", "第1页仅读标题开头，部分页仅读打印段落；版本角色未确认。"]


## pro084 · Approximating f-Divergences with Rank Statistics

论文 OR_6dI31vzkqT；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9", "source_url": "https://api2.openreview.net/pdf?id=6dI31vzkqT\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "10fc63ed6a244c175e1c41d75d6434b03b39955f8a9d48da90c3e98b87e7765e", "source_pdf_sha256": "3bffc2b3f1e99ea680580ce4f380187e0df2670e2d75efd72553c36338c50f49"}], "read_ranges": ["TEXT_OR_6dI31vzkqT_3bffc2b3f1e9：物理页1–40全部所供文本，包括正文1–9页、参考文献10–12页、附录A–F第13–40页；连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供原PDF或图1–16图像；不能独立判断生成图像质量或读取曲线数据。", "部分双栏文字、公式上下标及矩阵方向混排；表1、3、4、5、6主要数值可辨。出版版本身份未核实。"]}

问题：仅凭两组样本，如何避免显式密度比拟合和变分优化，构造具有误差保证的f散度代理，并用于生成学习与两样本检验？

方法：对X∼µ统计K个参考样本中不大于X的个数，得到K+1格秩分布q_n=Eµ[b_n,K(Fν(X))]，计算D_K=(K+1)^−1Σf((K+1)q_n)。实际以经验CDF和Bernstein基求值；高维平均投影结果，目标是sliced f散度。生成训练另用软秩、近端更新和分位映射。

作者主张：将TV秩近似推广至一般f散度，建立单调下界、逼近速率、有限样本界和渐近正态性。

论文证据：定理2.3给出D_K≤D_(K+1)≤D_f；定理2.5在Hölder密度比下给出O(K^−α/2)，更强条件下为O(K^−1)；附录B给出证明和统计极限推导。

模型推断：主要增量是一般f的可控近似与统计保证，而非首次引入秩直方图。

定位：['TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p3–5/定理2.3–3.4；p15–24/附录B。\n']

作者主张：通过切片处理高维数据，并将秩散度转为生成运输和预训练目标。

论文证据：定理3.2证明切片极限为SD_f≤D_f；算法1–2及MNIST、CIFAR-10和合成训练实验展示可用性。

模型推断：是既有切片与运输路线上的扩展；不等于原高维f散度的一致估计，也未证明生成动力学收敛。

定位：['TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p4–9/§3–4.4；p31–33/§C.4–C.6。\n']

key_results：[{"setting": "固定K的两样本估计；另有已知参考ν的一维oracle极限", "baseline": "总体秩散度D_K；oracle情形比较原散度D_f", "metric_or_guarantee": "期望绝对误差界及√N渐近正态性", "reported_values_and_units": "误差≤Lf(K+1)√(2π)(N^−1/2+M^−1/2)。oracle情形在r∈C²、f二阶导有界且√N≪K≪N时，√N(估计−D_f)趋于方差Varµ[f′(r(Fν(X)))]的零均值正态分布。", "information_and_compute": "oracle结论不包含估计ν的误差；固定K切片CLT同样只对µ采样。", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p20/定理2.6；p22–24/定理3.3–3.4。\n \n"}, {"setting": "一维Gaussian均值平移∆=1；Laplace(0,1)对N(0,1)重尾失配", "baseline": "Gaussian解析KL；重尾KL使用每分布10^7样本的Monte Carlo参考", "metric_or_guarantee": "KL估计/参考比，均值±标准差，无量纲", "reported_values_and_units": "K从32增至512：均值平移0.880±0.024→0.980±0.027；重尾0.210±0.012→0.524±0.028，仍显著低估。", "information_and_compute": "每分布10,000样本，10次独立重复；均为作者报告。", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p26/§C.2；p27/表3。\n \n"}, {"setting": "d=50的非Gaussian切片实验", "baseline": "已知密度的Monte Carlo原高维散度", "metric_or_guarantee": "d×切片估计/原散度，均值±标准差，无量纲", "reported_values_and_units": "GMM对Gaussian的JS：2.247±0.016；自由度3的Student-t对Gaussian的KL：0.318±0.012。该比例不是纯粹的有限K误差。", "information_and_compute": "K=64、L=128、每分布10,000样本、10次；硬秩总成本O(L[(N+M)d+MlogM+NlogM+NK])。", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p26、29/§C.3、表4；p38/附录E。\n \n"}, {"setting": "MNIST生成器秩预训练后DCGAN微调", "baseline": "DCGAN；更强的MCL-GAN", "metric_or_guarantee": "Precision/Recall，均值±标准差，%", "reported_values_and_units": "KL+DCGAN：96.20±0.46/90.50±0.83；DCGAN：93.85±1.45/75.43±2.56；MCL-GAN：98.20±0.30/98.00±0.40。", "information_and_compute": "batch=128；预训练组20+40 epochs，对照DCGAN为40 epochs，非等训练预算；重复次数未明确。", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p33/§C.6、表5。\n \n"}, {"setting": "two-moons及其非线性升维，d=2/4/10", "baseline": "Sliced Wasserstein；另比较MMD和assignment OT", "metric_or_guarantee": "达到外部classifier-JS阈值的墙钟时间", "reported_values_and_units": "对应阈值0.05/0.15/0.30：Rank为91.3/131.6/59.5秒，SWD为147.0/117.6/120.5秒；d=4时SWD更快。", "information_and_compute": "同3×128生成器；Rank用L=64、K=32、batch=256，上限3000步。软秩每切片另需O(NM+NK)时间/内存。全篇环境为M1 Pro、16GB RAM，按需使用TITAN Xp、12GB显存；未逐实验指明设备。", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p38–40/附录E–F、表6。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "de Frutos, J. M., Olmos, P. M., Lopez, M. A. V., and Míguez, J. Training implicit generative models via an invariant statistical loss. In International Conference on Artificial Intelligence and Statistics, pp. 2026–2034. PMLR, 2024a.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "ISL秩直方图与TV代理", "claimed_difference": "例2.1明确TV特例仅差因子K+1；新增集中于一般f及保证。", "basis": "target_paper_only", "target_locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p3/例2.1；p10/参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "de Frutos, J. M., Vázquez, M. A., Olmos, P., and Míguez, J. Robust training of implicit generative models for multivariate and heavy-tailed distributions with an invariant statistical loss. arXiv preprint arXiv:2410.22381, 2024b.", "identifier_if_present": "arXiv:2410.22381", "relation_candidate": "组件复用", "shared_component": "多变量秩训练及TV预训练缓解mode collapse", "claimed_difference": "将预训练策略扩展至KL、JS、Hellinger等f选择。", "basis": "target_paper_only", "target_locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p10/参考文献；p33/§C.6。\n", "prior_actually_read": false}, {"citation_as_printed": "de Frutos, J. M., Vázquez, M. A., Olmos, P. M., and Míguez, J. Explicit density approximation for neural implicit samplers using a Bernstein-based convex divergence. In Proceedings of The 29th International Conference on Artificial Intelligence and Statistics, Proceedings of Machine Learning Research. PMLR, 2026. To appear.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "Bernstein秩表示与TV散度近似", "claimed_difference": "作者称推广至一般f，并补充定量逼近和统计分析；具体覆盖范围待核读。", "basis": "target_paper_only", "target_locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p9/§5；p10/参考文献；p14/§B。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "一般f的误差率、有限样本界及统计极限构成实质理论增量候选；秩/Bernstein路线已有明确前作，不支持L3判断。", "central_increment": "前作已做TV秩代理（本篇转述）；本作在无原子参考和分位密度比正则条件下推广至一般f并建立统计保证，证据为定理2.3–3.4；尚待排除最近前作的同条件覆盖。", "soundness_observation": "单调下界有Jensen及删样Markov核推导。总体保证与经验估计、软秩训练须分开；未逐式完成独立证明审计或复现实验。", "significance_observation": "提供免训练的散度求值及可替换的学习目标；工程成本仍随K、L增长，尚未展示大规模生成优势。", "main_open_question": "2026年Bernstein前作是否已在可比假设下覆盖本篇一般f框架或关键收敛、统计保证？"}

limitations：[{"text": "有限K产生近似偏差；有限L可能漏掉各向异性、罕见方向或依赖结构，K/L自适应选择和运输收敛理论仍待发展。", "basis": "author_report", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p36–38/附录D"}, {"text": "神经KL对比中，秩方法利用已知乘积分布结构按坐标求和；不足以证明对任意高维分布的优势。d倍缩放并非一般恒等式，Gaussian JS参考还是矩匹配代理。", "basis": "model_inference", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p25/§C.1；p29/§C.3。\n \n"}, {"text": "KL、JS、Hellinger在零点不满足所述全区间Lipschitz/光滑条件，不能直接套用全部有限样本及CLT结论；均值平移和重尾实验亦未统一满足有界正则分位密度比假设。", "basis": "model_inference", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p3–5/定理条件；p26–28/§C.2"}, {"text": "MNIST预训练收益混有额外20 epochs；CIFAR图像不可视。CO-RPT的角向近邻步骤与秩目标贡献未分离，feature-space rank-TV的FID不能当作CO-RPT结果。", "basis": "model_inference", "locator": "TEXT_OR_6dI31vzkqT_3bffc2b3f1e9:p31–33/§C.5–C.6"}]

minimal_check：{"question": "中心理论增量是否超出最近2026年前作？", "control": "取得该前作全文，对照本篇定理2.3、2.5、2.6、3.3、3.4的对象、假设与结论。", "observable_outcome": "形成逐定理覆盖表，区分TV专属结果、一般f直接推广及真正新增速率/统计极限。", "resources": "前作可核对全文与公式；无需训练，核读工时未知。", "failure_or_stop_condition": "同条件保证已被覆盖则下调相应新增判断；未获得前作则停止该检验，不用本篇转述代替核读。"}

missing_fields：["原PDF图像、图中精确功效/运行时间曲线及生成样本质量", "最终出版版本身份、前作全文", "表5中m的明确定义及重复次数；表6计时重复次数", "逐实验设备分配、全篇总运行时间及计算消耗；部分神经基线细节仅引用外部前作"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

一般f的秩代理和统计条件清楚，适合继续对照最近Bernstein前作；使用时先选清总体/切片目标及可适用的f正则条件。

身份与总体秩构造：完整题名、40页当前附件相符。p2明确整个一维章节假设参考nu无原子；K+1格秩律对均匀律求f散度。总体DK≤D(K+1)≤Df与估计器有限样本误差分开，有限K均匀并不单独识别所有分布，原等价陈述要求全部K。TV特例已来自ISL，新增候选是一般f及相应保证。

核查定位：p001 title, p002, standing assumptions/Definition2.1, PDF physical page3, Definition2.2/Theorem2.3/Example2.1；identity_population_construction_and_atomless_condition_confirmed

逼近、有限样本与CLT条件：原Theorem2.5要求分位域密度比连续及f在其值域Lipschitz，Hölder率K^(−alpha/2)、更强条件K^−1。Theorem2.6另需f在[0,K+1]上Lipschitz，误差系数含K+1；KL/JS/Hellinger零点导数条件不能自动满足。原Theorem3.4是已知nu的oracle，要求C²及有界二阶导、sqrtN≪K≪N，不是两组有限样本加有限投影的统一CLT。

核查定位：PDF physical page3, Theorem2.5, p004, Example2.2/Theorem2.6, PDF physical page5, Theorems3.3–3.4；decisive_theorem_conditions_confirmed

高维目标与比较信息：原Theorem3.2极限是sliced Df≤原高维Df；d倍切片没有一般等价性。原表4 d50时GMM/高斯JS比2.247±.016、t3/高斯KL比.318±.012，这含目标差异而非仅K偏差。GaussianJS参考还用矩匹配高斯代替混合分布。神经KL比较利用已知独立坐标将一维KL求和，不能推广为任意高维优势。

核查定位：PDF physical page5, Theorem3.2/Section4.1, PDF physical page29, reference definitions/Table4；sliced_target_proxy_reference_and_factorization_scope_confirmed

一维和生成结果：表3均值平移Delta1的KL估计比从K32 .880±.024到K512 .980±.027，重尾仅.210→.524，仍明显低估。原表5 KL+DCGAN精确率/召回96.20/90.50，对照93.85/75.43，但MCL-GAN98.20/98.00更高；预训练组20+40epochs，对照40epochs，收益混有额外训练。

核查定位：p027, Table3, PDF physical page33, SectionC.6/Table5；empirical_bias_and_training_budget_tradeoff_confirmed

真实计时和求值/训练成本：原图15 Rank在d2/4/10达对应阈值耗时91.3/131.6/59.5秒，SWD147/117.6/120.5，d4后者更快。未达目标的MMD各维及OT d4/10柱高是3000步预算总时，不能当达标耗时。硬秩需排序及NK，软秩每切片还需NM对比矩阵；免优化只指求值。M1Pro16GB与按需TITANXp12GB未逐实验划分。

核查定位：p038, AppendixE, PDF physical page40, Figures15–16/AppendixF；runtime_censoring_and_soft_rank_overhead_confirmed

本地补充/限定：["补看原图15：未达标方法的计时是预算封顶，而非达到相同精度，比较须标注删失。", "p2明确无原子为章节前提，不能因Theorem2.3重复简写而误判任意原子参考也有同一下界性质。"]

核查局限：["未核读2026最近前作，无法最终确认新增定理覆盖；L2仍暂评。", "未重做全部证明、散度实验、生成模型训练或作者代码。", "第1页仅读题名开头，未核验CIFAR图像质量，版本角色未确认。"]


## pro085 · Online Learning and Inference for Cox Proportional Hazards Models Using Renewable Sieve Estimation

论文 OR_TvLOddG9Ay；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6", "source_url": "https://api2.openreview.net/pdf?id=TvLOddG9Ay\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "61b75048b3d665222aa0c5f8aa8d9465463aec4cc48471fbcc32c419445385d8", "source_pdf_sha256": "6da2a9d52da646eba8daa4208121818d190fb365ddc2ef7343f47ce5a8871114"}], "read_ranges": ["TEXT_OR_TvLOddG9Ay_6da2a9d52da6：物理页1–26全部提供文本；正文p1–9、参考文献p9–11、附录A–D p12–26。页标连续，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅有全文转写，未见父PDF和图1–4图像；图2–4曲线点值不可用，部分公式及表格双栏交织。不能据此确认最终出版版本。\n", "未搜索网页、核读前作、执行作者代码或复现实验；下述理论疑点依据所供文本，不是完整证明审计。"]}

问题：右删失生存数据逐批到达、历史原始数据不可保留时，如何联合估计风险系数和基线风险，并进行接近集中式分析的统计推断？

方法：输入(X,Y,Δ)，以Bernstein多项式近似log-baseline hazard，改用逐样本可加全似然。每批将当前score与历史二次型合并求解；active阶数增长时精确提升系数，并从更高阶shadow Hessian提取曲率，再用伪逆升维更新shadow摘要。输出β、基线函数和推断所需曲率。

作者主张：不重访历史数据、不构造全局风险集，同时随累计样本扩大模型复杂度。

论文证据：给出两阶段算法；模拟正文报告逼近Oracle，SRTR与TCGA表格显示较高的一致性，但未提供可读的模拟曲线点值。

模型推断：中心增量不是首次使用全似然，而是将既有renewable更新与增长筛空间衔接；属于实质机制扩展候选。

定位：['TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p12算法1、p13附录B。\n']

作者主张：估计一致、渐近正态，并达到集中式Cox估计的半参数效率。

论文证据：定理4.1给出d(θ̃k,θ₀)=O_p(N_k^{-min(qν,(1−ν)/2)})；定理4.2声称sqrt(N_k)(β̃_k−β₀)⇒N(0,I(β₀)⁻¹)，附录D提供推导。

模型推断：若成立，这是超出经验性能提升的统计保证；但所供证明存在关键不一致，不能按已验证结论收录。

定位：['TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p6定理4.1–4.2、p14–26附录D。\n']

key_results：[{"setting": "混合Weibull模拟；K=6、20、50、200，500次重复；另测试后续批大小100。", "baseline": "Oracle、Meta、Online、SGD、100-epoch离线SGD", "metric_or_guarantee": "Abias、RMSE、95%置信区间覆盖率", "reported_values_and_units": null, "information_and_compute": "正文定性报告COLSA接近Oracle；精确逐设置数值仅见不可读图2–3。", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p6–7§5.1、p13图3。\n"}, {"setting": "表1主模拟K=200；前三批各1500、随后三批各500，余批各500。", "baseline": "Oracle、Online、Meta、SGD、SGD (Offline)", "metric_or_guarantee": "作者报告运行时间与摘要存储复杂度", "reported_values_and_units": "COLSA 28.36秒；Oracle 0.693秒；Online 4.516秒；Meta 1.585秒；SGD 1.606秒；离线SGD 58.14秒。COLSA摘要存储O((d+bar p)²)。", "information_and_compute": "Apple M1 Pro、16GB RAM、RStudio多核；离线SGD训练100 epochs。", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p7表1、p12–13附录B。\n"}, {"setting": "SRTR：N=48,766，49州顺序分批，每批68–5454例；终点为5年DCGF。", "baseline": "集中式Oracle", "metric_or_guarantee": "风险比与Wald显著性一致性", "reported_values_and_units": "作者报告仅Hispanic recipient显著性结论不同：Oracle HR=0.91、Z=−2.22；COLSA HR=0.93、Z=−1.58。", "information_and_compute": "真实数据关联分析，不是有已知真值的风险因素验证；该分析独立耗时未报告。", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p6§5、p8§5.2及表2。\n"}, {"setting": "TCGA：7315名患者、18癌种分批、预选23个基因；显著性阈值|Z|>1.96。", "baseline": "集中式Oracle", "metric_or_guarantee": "Z统计量相关性、平均绝对log-HR差、显著性判断一致性", "reported_values_and_units": "Pearson r=0.997；平均绝对log-HR差0.003；22/23判断一致，唯一分歧为PDCD4。", "information_and_compute": "先用全体受试者单变量筛选，再进行5折交叉验证LASSO选基因，之后按癌种在线估计。", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p8§5.3及表3。\n"}]

prior_work_candidates：[{"citation_as_printed": "Luo, L. and Song, P. X.-K. Renewable estimation and incremental inference in generalized linear models with streaming data sets. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 82(1):69–97, 2020.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "历史曲率摘要与renewable估计方程", "claimed_difference": "由固定维GLM扩展至增长筛空间的Cox联合估计。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p3§3.3、p10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Quan, M. and Lin, Z. Optimal one-pass nonparametric estimation under memory constraint. Journal of the American Statistical Association, 119(545):285–296, 2024.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "预估计未来增长基底的信息", "claimed_difference": "本作引入Bernstein递归投影及Cox统计推断，而非仅单遍非参数点估计。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p3§2、p10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Wu, J., Chen, M.-H., Schifano, E. D., and Yan, J. Online updating of survival analysis. Journal of Computational and Graphical Statistics, 30(4):1209–1223, 2021.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "在线更新基线风险与回归参数", "claimed_difference": "以光滑Bernstein筛和shadow预估计替代文中所述分段常数CUEE方案。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p2§2、p11参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "增长筛空间的在线联合估计与推断是实质机制增量候选，不宜仅因复用组件判为局部改进；但新意判断不等于认可理论正确性。", "central_increment": "前作已支持固定维renewable推断或单遍非参数预估计（本篇转述）；本作新增Cox的active/shadow跨维曲率机制，表2–3提供有限样本支持，尚待排除证明与实现不一致。", "soundness_observation": "按所供文本，存在四处关键问题：p12算法1用R†ᵀHR†升维，p15式(6)却定义RHRᵀ；D.4固定ρ的归一化误差上界含不消失项，尚不足以推出严格oracle等价；p25式(24)将O_p(N^{−(1−ν)/2})并入O_p(N^{−1/2})，不由所示界推出；p26要求qν>1/2，与主定理ν<1/(2q)冲突。需核对原版并补齐论证。\n", "significance_observation": "价值主要在低维流式生存分析的参数推断与不确定性量化；不是预测性能SOTA，也不是比集中式计算更快。", "main_open_question": "按算法1实际伪逆投影、固定ρ=2运行时，能否补齐证明并保留所声称的oracle效率？"}

limitations：[{"text": "作者承认固定协变量维数、数值积分成本较高；仅传摘要尚无正式隐私保证。", "basis": "author_report", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p9§6。\n"}, {"text": "摘要的constant memory表述不严格：bar p随N^ν增长，存储为O((d+bar p)²)。模拟K与总样本量同时变化，小批实验仍保留大首批，不能独立归因于批次数或纯小批处理能力。", "basis": "model_inference", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p1摘要、p7表1、p12附录B。\n"}, {"text": "TCGA全样本选基因后在同数据上作Wald推断，未说明选择后校正；Oracle显著性仅是比较参照，不是生物学真值。", "basis": "model_inference", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p8§5.3。\n"}, {"text": "附录B所印X4条件概率向量(0.1,0.2,0.4,0.5)和为1.2，实际数据生成配置需澄清，未擅自归一化。", "basis": "model_inference", "locator": "TEXT_OR_TvLOddG9Ay_6da2a9d52da6：p12附录B。\n"}]

minimal_check：{"question": "固定ρ=2时，在线更新误差是否随样本增长降至比N^{-1/2}更小？", "control": "同一明确生成配置的合成数据流、相同筛阶与积分精度，对比COLSA和保留历史数据的pooled sieve MLE。", "observable_outcome": "随N增长观察sqrt(N)乘以两者β差异，以及95%区间覆盖率。", "resources": "R、普通CPU及仅供对照保留的模拟数据；可沿用论文500次重复，实际耗时未测。", "failure_or_stop_condition": "标准化差异持续不缩小或覆盖偏离超过Monte Carlo波动，则不支持该设置下的等价性；即使通过，也不能替代修复证明。"}

missing_fields：["图2–4逐设置精度、覆盖率及敏感性曲线数值", "Gaussian Quadrature节点数、积分误差容限和局部求解停止标准", "实际峰值内存、通信字节数及真实数据分析独立耗时", "前作全文、作者实际代码和附录B概率向量对应的真实生成配置"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

增长筛在线摘要的想法可研究，但使用推断与oracle效率前必须澄清C5、实际Hessian映射及渐近余项；当前版本不作为已核实效率保证。

身份、机制与存储范围：完整题名与26页当前附件匹配。active/shadow Bernstein筛阶随累计N增长，摘要Hessian替代历史数据重访；原始数据不保留可成立，存储O((d+pbar)²)、pbar=O(N^nu)并非固定字节的constant memory。目标是固定协变量维数的右删失Cox联合估计与推断，不是高维变量筛选或正式隐私保证。

核查定位：p001 title, p005, stages/hyperparameters, p007, Table1/storage discussion, PDF physical page12, Algorithm1；identity_mechanism_and_growing_memory_scope_confirmed

C5按原文的非零系数障碍：原PDF6 C5条件在给定V=beta0^T X后仍要求所有单位u的条件方差至少eta倍条件二阶矩。取u=beta0/||beta0||时左边0、右边eta V²/||beta0||²，迫使V=0几乎处处，与C3非奇异E[XX^T]及beta0非零矛盾。故原样条件不能覆盖一般非零系数情形；未替作者猜测应如何修改。

核查定位：PDF physical page6, C3/C5, local_check/theory_scope_checks.md；printed_regular_condition_excludes_nonzero_regression_vector

算法与证明的曲率映射：原算法1升维用(Rdagger)^T H Rdagger，证明式6及D.4工作Hessian却用R H R^T。Bernstein1→2、H=I、v=(1,1)时，新方向Rv上的二次型分别2与9/2，不能视作同一操作。原Hessian链式法则本身不受此反例否定；证明需针对实际算法重写。

核查定位：PDF physical page12, line21, PDF physical page15, Eq6–7/LemmaD.3, p016, working Hessian, local_check/theory_scope_checks.md；algorithm_proof_operator_mismatch_confirmed

oracle效率证明的数量级：D.4归一化误差含固定rho^(−1/nu)不消失上界，不能仅因常数小就推o(1)；不代表真实误差必不消失。原p25把较慢O_p(N^−(1−nu)/2)吸收入O_p(N^−1/2)不成立；p26用qnu>.5而主定理nu<1/(2q)，条件冲突。当前证明未完成效率论证，不把实验接近Oracle当渐近证明。

核查定位：p016, TheoremD.4, PDF physical pages25–26, Eq24 and final argument, PDF physical page6, Theorems4.1–4.2；rate_absorption_and_incompatible_conditions_confirmed

实证时间、选变量及真值口径：K200表1 COLSA28.36秒，Oracle .693、Online4.516、离线SGD58.14，优势是流式存储而非比集中式更快。TCGA先在全样本选23基因再按癌种更新，其22/23显著性一致和Z相关.997只是对集中式同数据结果的一致；未说明选择后推断校正。SRTR的Hispanic项HR.91/Z−2.22与.93/−1.58确有差异，不能把Oracle显著项称生物学真值。附录B概率(.1,.2,.4,.5)和1.2，未擅自归一化。

核查定位：p007, Table1, p008, Sections5.2–5.3/Tables2–3, PDF physical page12, simulation setup；empirical_scope_and_generator_ambiguity_confirmed

本地补充/限定：["补充C5+C3对非零beta0不可能同时成立的直接条件化推导。", "原Pro四处理论疑点均核对原PDF；固定rho上界问题限定为证明不足，未声称实际误差必不消失。"]

核查局限：["只做局部代数/条件核查，未重跑生存模拟、真实数据分析或作者代码，未提供临床结论。", "未全面核验所有证明及前作，未读取图2–4精确点值。", "第1页仅读标题开头；附件版本角色未确认。"]


## pro086 · Geometry-Aware Probabilistic Circuits via Voronoi Tessellations

论文 OR_d9LsOCOB9z；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_d9LsOCOB9z_3af0d00b9125", "source_url": "https://api2.openreview.net/pdf?id=d9LsOCOB9z\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "18b8f34f0ed2db6050e522c356abbad973f846d2dd5babfbcf9abc6d835cf09e", "source_pdf_sha256": "3af0d00b912563abadd8814292836e93f3b0d673888e3056a27634e7ffe50618"}], "read_ranges": ["TEXT_OR_d9LsOCOB9z_3af0d00b9125：物理p1–23全部提供文本；p1–9正文，p10–12致谢、影响声明及参考文献，p13–22证明和数据构造，p23数据构造及实现细节。连续页标无缺号。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文文本，未查看原PDF图像，也未核验最终出版版本身份。", "图1–5不可见，不能读取合成任务柱图、学习曲线和几何可视化的具体数值；表1文本可辨。", "双栏文字及部分公式错序；A.15存在未解析的“(??)”交叉引用。"]}

问题：如何让PC按被建模输入的局部几何选择专家，同时保留可计算的归一化、边缘与条件推断？

方法：最近质心硬门控产生未归一化输出f。VT-PC用胞元内外轴对齐盒夹住积分，并可二分细化；HFV-PC使门控与专家按vtree共享分块。质心经k-means初始化，用距离softmax与PC参数联合训练、逆温度退火，测试改用硬门控。

作者主张：形式化Voronoi路由与PC可处理推断的冲突，并给出恢复积分分解的几何对齐条件。

论文证据：Proposition 3.2/A.1展示斜边界导致积分无法逐变量分解；Theorem 3.5/A.4证明区域与专家共享Cartesian分解时积分可因子化。

模型推断：贡献主要是明确建模兼容条件，而非发现新的通用积分原理。

定位：['TEXT_OR_d9LsOCOB9z_3af0d00b9125:p3–4,Proposition 3.2/Theorem 3.5；p13–15,A.1–A.4']

作者主张：为一般VT-PC提供分区函数、边缘与条件概率的认证界，以及单调收紧的anytime算法。

论文证据：Lemma 3.6与Theorems 3.9–3.10给出包含关系、界传播和条件收敛；表1报告未经细化的测试似然区间。

模型推断：将几何表达能力与有证书的近似推断连接起来，属于有价值的方法增量；通用深层实现仍需核验。

定位：['TEXT_OR_d9LsOCOB9z_3af0d00b9125:p4–6,§3.1；p15–18,§A.3；p9,Table 1']

作者主张：HFV恢复精确可处理推断，并通过软门控实现可微训练及软硬转换保证。

论文证据：Theorem 3.14/A.15声称复杂度O(|C|K^m)；Theorem 3.16/A.20证明固定质心下远离边界的门控收敛。

模型推断：潜在中心增量是结构性推断保证，不是softmax本身的新颖性。

定位：['TEXT_OR_d9LsOCOB9z_3af0d00b9125:p6–7,Theorems 3.14/3.16；p19–22,A.15–A.20']

key_results：[{"setting": "UCI密度估计；顺序为power(6D)、gas(8D)、hepmass(21D)、miniboone(43D)，各结果为3次试验均值。", "baseline": "相同基础宽度的EinsumNet与HCLT；均为40个input/sum units。", "metric_or_guarantee": "平均测试log-likelihood，越高越好；VT的LO/UP按作者标注记录，不作为本地认证结果。", "reported_values_and_units": "EinsumNet=[0.56,5.85,-22.35,-32.24]；HFV-EinsumNet=[0.56,5.86,-22.32,-32.18]；VT-EinsumNet LO=[1.73,7.13,-22.98,-32.82]，UP=[3.46,9.76,-4.82,-14.07]。HCLT=[0.55,7.22,-20.36,-25.43]；HFV-HCLT=[0.55,7.07,-20.35,-25.36]；VT-HCLT LO=[5.10,10.57,-19.10,-26.46]，UP=[6.77,13.17,-1.61,-8.95]。原文未明确标注对数底或单位。", "information_and_compute": "单张24GB NVIDIA L4；Adam，学习率0.01，batch=500，100 epochs；逆温度α由1线性升至50；按验证表现选checkpoint，测试硬门控；VT无额外盒细化。", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p9,Table 1/§4.2；p23,§C。\n"}, {"setting": "HFV-PC，电路节点数|C|，最多m个因子，每因子最多K个胞元。", "baseline": "普通平滑可分解PC的递归积分。", "metric_or_guarantee": "作者声称分区函数、边缘及条件推断精确可算。", "reported_values_and_units": "O(|C|K^m)；二叉情形O(|C|K^2)，属于理论操作复杂度而非实测时间。", "information_and_compute": "依赖逐层受限积分可递归、叶积分可算；递归闭包是本次初评的关键待核项。", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p6,Theorem 3.14；p19–20,Theorem A.15"}, {"setting": "固定质心，输入不在Voronoi边界，最近与次近质心的平方距离差γ(u)>0。", "baseline": "有限逆温度α的softmax门控。", "metric_or_guarantee": "软门控趋于硬门控；可积专家下门控加权积分收敛。", "reported_values_and_units": "1-w_nearest(u;α)≤(K-1)exp(-αγ(u))。", "information_and_compute": "这是逐点门控收敛，不是训练优化收敛或全分布统一指数误差保证。", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p7,Theorem 3.16；p21–22,Theorem A.20"}]

prior_work_candidates：[{"citation_as_printed": "Shao, X., Molina, A., Vergari, A., Stelzner, K., Peharz, R., Liebig, T., and Kersting, K. Conditional sum-product networks: Modular probabilistic circuits via gate functions. International Journal of Approximate Reasoning, 2022.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "输入依赖的PC门函数。", "claimed_difference": "CSPN依赖固定的外部观测特征；本作按被建模变量的几何路由，并讨论联合推断。", "basis": "target_paper_only", "target_locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p3,§2；p11,References", "prior_actually_read": false}, {"citation_as_printed": "Rahman, T., Kothalkar, P., and Gogate, V. Cutset networks: A simple, tractable, and scalable approach for improving the accuracy of chow-liu trees. In Joint European conference on machine learning and knowledge discovery in databases, pp. 630–645. Springer, 2014.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "与变量分解兼容的区域划分。", "claimed_difference": "本篇称其轴对齐特例回收cutset式分区，并进一步讨论一般Voronoi几何的认证近似。", "basis": "target_paper_only", "target_locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p4,Theorem 3.5后讨论；p11,References", "prior_actually_read": false}, {"citation_as_printed": "Chen, R. T., Amos, B., and Nickel, M. Semi-discrete normalizing flows through differentiable tessellation. Advances in Neural Information Processing Systems, 35, 2022.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "生成建模中的可微分空间剖分。", "claimed_difference": "本作研究PC内部几何门控与可处理推断的兼容性；未展示对该前作算法的直接继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p1/3；p10,References", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "暂定增量在于几何路由、认证近似与结构性精确推断之间的系统联系，不只是替换门函数；但关键保证存在未闭合环节，不能等同于已验证的新能力。", "central_increment": "前作已有条件门控和轴对齐可积分区（仅本篇转述）；本作对输入几何路由新增VT盒界与HFV对齐方案，证据为§3及表1；尚待排除深层递归与归一化处理缺口。", "soundness_observation": "单层包含界和固定质心软硬收敛较清楚；HFV受限积分闭包、深层VT盒积分及软训练归一化尚未充分说明。新意判断与正确性保留分开。", "significance_observation": "对需要可靠边缘化的局部密度模型有潜在价值；当前是概念验证，HFV似然接近基线，高维VT区间明显变宽。", "main_open_question": "HFV的祖先多维胞元限制能否在后续每次变量拆分下继续可分解，并以O(|C|K^m)处理？"}

limitations：[{"text": "作者承认高维盒界松、细化成本快速增长；HFV不能直接表示跨因子斜边界。A.9的指数形式速率依赖额外正则条件及均匀细化深度，不能当作总计算量界。", "basis": "author_report", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p6,§3.1–3.2；p17,§A.3.2"}, {"text": "软门控输出不自动归一化，Algorithm 3未说明训练所需Z及其梯度如何计算；§3.3承认软门控通常失去精确积分，与附录C的HFV全程精确措辞存在张力。", "basis": "model_inference", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p7,§3.3；p22,Algorithm 3；p23,§C"}, {"text": "p8称使用内盒得到似然下界，但内盒给出Z下界；对p=f/Z，似然下界应使用Z上界。实际实现使用哪一侧需核验，不能据此直接宣布表1错误。", "basis": "model_inference", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p8,§4.1；p9,Table 1。\n"}, {"text": "实验的VT主要为根和节点门控，未验证一般深层界传播；相同基础宽度不等于参数量或时间预算严格匹配，亦未报告误差条和运行耗时。", "basis": "model_inference", "locator": "TEXT_OR_d9LsOCOB9z_3af0d00b9125:p7–9,§4；p23,§C"}]

minimal_check：{"question": "HFV定义允许的多维因子门控是否确实支持所称精确递归？", "control": "构造四维二层vtree，在左侧二维块设置产生x1=x2斜边界的质心；以轴对齐质心为对照，保持专家和权重不变，对比递归Z与误差受控的低维积分。", "observable_outcome": "斜界与对照均在参考误差内一致，且未调用未计入成本的多维积分或指数展开。", "resources": "CPU、低维积分器及待核HFV实现；作者代码未提供，运行时间未知。", "failure_or_stop_condition": "出现超出参考误差的偏差，或必须新增未声明的几何限制才能递归，则原定义下的通用保证不获支持。"}

missing_fields：["图1–5图像及其未文本化数值。", "软训练归一化及梯度算法、每层K与门控配置的完整说明。", "UCI样本划分细节、VT积分域及高斯尾质量处理。", "实际耗时、峰值显存、试验方差和自适应细化实测。", "作者实现、前作全文及候选前作的DOI/arXiv标识。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

几何表达与认证近似的取舍值得研究；采用前先核递归限制、软训练Z计算和似然界方向。

身份和局部几何保证：完整题名和23页附件相符。非负密度在有效内/外包含盒上的积分夹界成立；区域与专家在同一变量块上均作Cartesian乘积分解时，Fubini分解也成立。这是局部构造，深层受限积分还需递归闭包；非分解性本身不等于完整复杂度下界归约。

核查定位：p001 title, p004, Theorem3.5/Lemma3.6, p005, bound algorithm；identity_and_local_containment_factorization_confirmed

HFV的祖先限制闭包：原A.15先把积分拆成各块Voronoi胞元上的子电路积分，p20再称用同一论证递归。仅当前节点按左右块对齐不足以保证祖先胞元在后续拆分仍可分解：四维根分{1,2}/{3,4}，左块可有x1+x2≤0斜界，随后分x1/x2仍受耦合限制。在[-1,1]²独立均匀例中斜半平面质量1/2，不能用两个坐标投影的乘积1替代。若意图要求所有祖先限制也对齐，须明确此更强条件；尚未运行作者算法或否定该受限子类。

核查定位：PDF physical page6, Definition3.13/Theorem3.14, PDF physical pages19–20, A.15/A.17；recursive_closure_gap_identified_not_a_refutation_of_globally_aligned_subclass

归一化界到似然界的方向：对固定精确f及0<Zminus≤Z≤Zplus，logf−logZplus才是似然下界，logf−logZminus是上界。原p8称用inner boxes报告似然下界，图2又明确inner给partition下界，文字口径冲突。未读实现，不能断言表1所有数字算错，但不能把LO标签当本地认证结果。有限Omega若只覆盖数据范围，还需处理域外质量才能界全空间Z。

核查定位：p004, bounded-domain boxes, PDF physical page8, experimental paragraph/Figure2, PDF physical page9, Table1；normalization_inequality_direction_confirmed_implementation_unverified

软训练与硬门控保证：p7明确软门控通常失去HFV精确积分，Algorithm3却只写负logp及反传，未交代训练Z与梯度。即使各pk相同且pi=1/K，输出f=sum pi wk pk=p/K，说明门权重归一不能代替密度归一。固定质心远离边界时1−wnearest≤(K−1)e^(−alpha margin)可成立，但不证明联合训练收敛或全域统一误差；p23的全程精确措辞需限定。

核查定位：p007, Section3.3/Theorem3.16, p022, Algorithm3, p023, implementation；soft_hard_and_density_normalization_scope_confirmed

关键实证与区间宽度：原表1 HFVEinsumNet四集.56/5.86/−22.32/−32.18基本贴近基线.56/5.85/−22.35/−32.24；HFVHCLT在gas7.07低于7.22。VT-EinsumNet高维LO/UP为hepmass[−22.98,−4.82]、miniboone[−32.82,−14.07]，区间很宽。图4也显示高维间隙扩大；三次均值无方差/实际耗时。实验VT主要根节点门控，无额外盒细化；L4 24GB、100epochs同基础宽度并非总参数/算力匹配。

核查定位：PDF physical page9, Figure4/Table1, p007–p008, experiment protocol, p023, implementation；reported_values_and_experiment_scope_confirmed_certification_reserved

本地补充/限定：["用明确四维分块/二维斜界说明递归闭包缺什么条件；不把局部证明缺口误报为全局对齐子类不可能。", "LO/UP只保留作者标签，因归一化方向文字冲突未作本地认证。"]

核查局限：["未执行PC训练、积分实现或作者代码；斜界例只是独立初等积分说明。", "未完整验证所有定理、前作或Gaussian域外尾界，未重算表1。", "第1页仅读标题开头，版本角色未确认。"]


## pro087 · Quantum Algorithms for Triangle Cut Sparsification

论文 OR_u4klflLAX3；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_u4klflLAX3_60eff7ac43b2", "source_url": "https://api2.openreview.net/pdf?id=u4klflLAX3\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_u4klflLAX3_60eff7ac43b2：物理页1–9，正文§1–6。", "TEXT_OR_u4klflLAX3_60eff7ac43b2：物理页10–13，致谢、Impact Statement及参考文献。", "TEXT_OR_u4klflLAX3_60eff7ac43b2：物理页14–31，附录A–G；31个物理页标连续，无可见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文提取文本，未查看原始PDF图像；双栏混排及部分分式、上下标失真，不能核实原始公式排版。", "未提供前作全文或其他版本；未搜索、复现实验或逐项独立证明全部定理。"]}

问题：将非负加权图压缩成重加权子图，同时对每个割保留跨割三角形的权重和至1±ε；三角形权重为三条边权的乘积，不是保留无权三角形个数。

方法：三路枚举算法并行取先完成者：heavy–light分割结合Grover、双层Johnson quantum walk、Grover枚举。量子游走先采样预枚举，再用边不交三角形packing分析标记比例；删边前列出全部关联三角形。随后估计strength、保留关键边、隐式采样重加权，最终搜索恢复输出边。

作者主张：在广泛参数范围内给出triangle listing的首个可证明量子加速。

论文证据：三路算法分别给出复杂度界；Lemma D.6及Proposition D.7通过低最大度证书边与二阶矩，得到标记比例Ω(min{1,νh²/n²})。

模型推断：核心新增是从存在性检测到输出敏感全枚举的分析，不只是黑盒套用Grover。

定位：['TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页5–6 Theorems 3.1、3.4；页19–20 Lemma D.6、Proposition D.7；页25 Theorem D.10。']

作者主张：加速triangle cut sparsifier构造，并用于全局与局部triangle clustering。

论文证据：Algorithms 6–7及Theorem 4.5组合枚举、strength估计与隐式采样；附录F给出聚类归约及推论。

模型推断：稀疏化框架、输出尺寸上界及聚类归约主要继承前作，新增集中于量子执行复杂度。

定位：['TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页7–8 §4；页26–29附录E–F。']

作者主张：证明triangle cut sparsifier需要Ω(n/ε²)条边，使已有尺寸上界近紧。

论文证据：复制Andoni等二分图难例的左部形成三角形，再通过同步割、投影及二倍割值恒等式转移下界。

模型推断：增加了三角形专属的尺寸保证；这不是量子查询或运行时间下界。

定位：['TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页30–31 Lemma G.3、Theorem 5.2。']

key_results：[{"setting": "n点、m边、t≥1个三角形的全枚举。", "baseline": "本文转述的经典枚举算法；Le Gall (2014)处理检测而非全枚举。", "metric_or_guarantee": "高概率输出全部三角形的渐近时间上界。", "reported_values_and_units": "T_q-list=Õ(min{n^(5/4)t^(7/12)+n^(7/6)t^(7/9), m+m^(3/4)t^(1/2), n^(3/2)t^(1/2)})；Õ隐去多对数因子，单位为模型内基本操作、oracle与QRAM操作。", "information_and_compute": "图预存于QRAM，支持degree、neighbor、vertex-pair查询；t未知时使用倍增猜测。附录另给纯查询界，将heavy–light分支的加性m替为n。", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页6 Theorem 1.3证明、页26 Query complexity。\n"}, {"setting": "非负加权图的ε-triangle cut sparsification。", "baseline": "本文转述的经典strength-based管线：T_c-list+Õ(m+t)。", "metric_or_guarantee": "高概率同时保留全部割值至1±ε。", "reported_values_and_units": "输出Õ(n/ε²)条边；时间Õ(T_q-list+√(mn)/ε)。", "information_and_compute": "O(log n)轮；非关键边以p=2^(-1/6)保留并除以p重加权。随机串模拟另需Õ(q)比特QRAM，其中q为被模拟算法时间；非硬件实测。", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页8 Theorem 4.5、Lemma 4.6；页28 Lemma E.7。\n"}, {"setting": "ε∈(1/√n,1)的最坏情形图。", "baseline": "已有Õ(n/ε²)条边的上界。", "metric_or_guarantee": "任意ε-triangle cut sparsifier的尺寸下界。", "reported_values_and_units": "Ω(n/ε²)条边；与上界相差多对数因子。", "information_and_compute": "理论归约，不涉及训练、数据集或实验预算。", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页31 Theorem 5.2。\n"}, {"setting": "2-way triangle spectral clustering。", "baseline": "triangle-weighted graph上的既有谱聚类。", "metric_or_guarantee": "运行时间与输出triangle conductance。", "reported_values_and_units": "时间T_q-list+Õ(√(mn))；输出conductance≤4√(ϕ₂^∆(G))。", "information_and_compute": "由枚举结果构造triangle-weighted graph并接入既有量子谱聚类；属于理论推论。", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页9 Corollary 5.1、页29附录F。\n"}]

prior_work_candidates：[{"citation_as_printed": "Kapralov, M., Makarov, M., Silwal, S., Sohler, C., and Tardos, J. Motif cut sparsifiers. In 2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS), pp. 389–398. IEEE, 2022.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "motif cut定义、strength采样框架及稀疏度保证。", "claimed_difference": "本作新增量子枚举与采样实现及三角形尺寸下界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页7 §4、页11参考文献、页26–28附录E。\n", "prior_actually_read": false}, {"citation_as_printed": "Le Gall, F. Improved quantum algorithm for triangle finding via combinatorial arguments. In 2014 IEEE 55th Annual Symposium on Foundations of Computer Science, pp. 216–225. IEEE, 2014.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "采样好集合与嵌套quantum walk检测。", "claimed_difference": "扩展到全枚举，引入packing标记率分析及避免重复的删边流程。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页5 §3.2、页12参考文献、页18–24附录D。\n", "prior_actually_read": false}, {"citation_as_printed": "Apers, S. and De Wolf, R. Quantum speedup for graph sparsification, cut approximation, and laplacian solving. SIAM Journal on Computing, 51(6):1703–1742, 2022.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "隐式采样、随机串模拟与量子谱聚类。", "claimed_difference": "接入三角形枚举及motif strength框架，而非普通边稀疏化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页8 §4.2、页10参考文献、页29附录F。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "输出敏感量子全枚举及三角形尺寸下界构成实质性新保证候选；并非提出全新稀疏化问题，尚不足判路线级L3。", "central_increment": "前作已有motif sparsification与triangle detection（本篇转述）；本作在QRAM模型下新增全枚举复杂度、构造加速及尺寸下界，支持为Theorems 1.2、1.3、5.2，待排除隐藏实现成本。", "soundness_observation": "下界的复制—投影链条较清晰。主要疑点是外层游走仅隐式存储N(u)∩S，内层却按∆G(H,S)显式已知、成员查询O(1)计时；两种接口如何在所列预算内兼容未充分说明，不能仅凭图查询数接受总时间界。\n", "significance_observation": "潜在价值是可复用的量子枚举原语与近紧尺寸保证，而非已验证的实际机器学习提速；工程实现难度未量化。", "main_open_question": "将隐式集合的成员判断、计数、搜索索引及更新全部计入门数和QRAM操作后，quantum-walk分支还能保持宣称的时间指数吗？"}

limitations：[{"text": "作者承认大规模QRAM物理可实现性仍开放，未提供硬件优势交叉点；理论模型优势不等于现实端到端优势。", "basis": "author_report", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页4 §2、页15 C.1。\n"}, {"text": "加速并非覆盖所有图：稠密且t=Θ(n³)时枚举需Θ(n³)，而正文还列出经典n^ω稀疏化路线，不能只比较经典枚举管线。", "basis": "model_inference", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页2 §1.1。\n"}, {"text": "证据为理论证明与归约，未见数据集、实测或实现评估；更一般motif及非平凡量子查询下界仍列为未来工作。", "basis": "model_inference", "locator": "TEXT_OR_u4klflLAX3_60eff7ac43b2，物理页1–31；页9 §6。"}]

minimal_check：{"question": "核查Lemma D.5的数据结构前提能否由外层游走按声明成本提供。", "control": "固定t=1的参数s=n^(1/2)、h=n^(3/4)，对照显式∆表与仅存N(u)∩S的实现，分别计图查询、QRAM读写和基本操作。", "observable_outcome": "是否能在Õ(sh)初始化、Õ(s)更新预算内，支持后续所需的成员判断、计数与搜索接口。", "resources": "纸笔复杂度审计及数据结构伪代码即可；无需量子硬件。真实实现资源未报告。", "failure_or_stop_condition": "若必须额外构建Θ(h²)表且无法摊还或绕过，或隐式操作提高总时间指数，则该实现尚不能支持所宣称时间界；不能据此自动否定其他分支或尺寸下界。"}

missing_fields：["prior_work_candidates中的identifier_if_present：所选参考文献未印DOI或arXiv编号。", "原始PDF图像及无损公式排版。", "输入装载、完整空间与权重精度依赖、实际硬件资源和运行时间。", "前作全文、其他版本与独立复核结果。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

输出敏感全枚举及尺寸下界值得理论跟进；接受总时间指数前先补齐Delta成员、计数与搜索的相干数据结构成本。

身份及稀疏化对象：完整题名、31页当前附件绑定。三角形权重是三边权乘积，所有割保留跨割三角形权重和；输出原图的重加权子图，而非任意三角形超边集合或无权三角形数。主枚举界假定t≥1，输入已在支持相干degree/neighbor/pair查询的QRAM中。

核查定位：p001 title, p002, Definition1.1/Theorems1.2–1.3, p004, computational model；identity_output_and_oracle_scope_confirmed

枚举增量与标记比例：原主界取三路最小值：n^(5/4)t^(7/12)+n^(7/6)t^(7/9)、m+m^(3/4)t^(1/2)、n^(3/2)t^(1/2)，隐去polylog。局部核查D.6低度证书边选择及D.7二阶矩：相邻边项O(mu^(3/2))可被O(mu+mu²)控制，得到Omega(min(1,nu h²/n²))，不依赖错误的边独立假设。packing只用于分析，未称实际求解最大packing。

核查定位：PDF physical page6, Theorem3.4/combination, PDF physical page19, LemmaD.6/PropositionD.7, p020, second-moment argument；central_bound_and_local_combinatorial_argument_confirmed

查询与总时间接口缺口：外层p18–20仅存每点N(u)交S，称无额外图查询即可重建Delta；内层p21却因Delta显式已知而按O(1)成员判断计时，p22还按O~(1)判集合大小条件。无需新图查询不等于常数门/QRAM操作。t1时s=n^.5、h=n^.75，直接全对表h²=n^1.5超过声明初始化sh=n^1.25；这仅说明朴素补表不在预算内，尚未证明不存在更好相干数据结构，也不否定其余两路。

核查定位：PDF physical page18, implicit representation, p020, data structure/setup/update, p021, explicitly known membership, p022, inner checking cost, PDF physical page6, parameter choice；time_accounting_bridge_unresolved_without_impossibility_claim

尺寸下界与构造代价分列：原Theorem5.2要求epsilon∈(1/sqrt n,1)，给最坏图Omega(n/epsilon²)边，非量子时间/查询下界。同步放置复制顶点后，triangle-weighted图的cut是原二分cut的两倍；投影合并并除2保持割且不增边数，这一局部归约链可核。稀疏化上界时间为Tqlist+O~(sqrt(mn)/epsilon)，随机串模拟还用O~(q)比特QRAM。

核查定位：PDF physical page31, projection/Theorem5.2, PDF physical page8, Theorem4.5/Lemma4.6；size_lower_bound_scope_and_extra_memory_confirmed

优势范围与未测工程成本：t=Theta(n³)时全枚举需Theta(n³)输出时间，正文还列经典n^omega的非枚举稀疏化路线，不能把枚举加速概括成所有图上的最佳稀疏化加速。纯查询heavy-light加性项可为n，而总时间含m，p26明确分列。没有硬件实验、输入装载总账或现实交叉点，全部是所述模型中的理论操作界。

核查定位：p002, classical comparison/extremes, p004, model and hardware discussion, p026, Query complexity；asymptotic_advantage_and_unmeasured_cost_scope_confirmed

本地补充/限定：["核查了packing二阶矩局部论证，正面证据与接口疑点并列。", "h²补表超过预算仅否定朴素实现，不推断一般数据结构或其他分支不可能。"]

核查局限：["未运行量子硬件、模拟器或作者代码；局部复杂度/归约核查不等于31页完整证明验证。", "未核读LeGall或motif sparsifier前作，历史首次仍未知。", "第1页仅读标题开头；当前附件角色未确认。"]


## pro088 · Exact and Approximate Algorithms for Polytree Learning

论文 OR_QIBu6vtRMI；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_QIBu6vtRMI_e0c70a59590e", "source_url": "https://api2.openreview.net/pdf?id=QIBu6vtRMI\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_QIBu6vtRMI_e0c70a59590e：物理页1—10全部提供文本，含§1—6、所附证明及p9—10参考文献；页标连续，未见独立附录。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—6仅有图题及零散标注，不能核验图中结构或紧例。", "双栏文字存在交错，DP分段公式及部分上下标版式受损；表1文字可读。"]}

问题：给定节点及候选父集的局部分数，寻找总分最大的polytree，即无向骨架为森林的有向图；研究入度、可加评分和分量弧数限制如何改变求解难度。

方法：输入候选父集及分数，输出高分或最优polytree。精确算法先转为连通实例，以Q[S,T]记录节点集S上仅T可有非空父集的结构；利用小子树优先DFS的存在性，将差集大小限制为O(k log n)。近似算法分别贪心选择整父集、单条弧或单位弧分数f_v(S)/|S|最高的父集，同时维护相应可行性。

作者主张：将常数入度下的精确求解改进至近2^n时间，并给出SCC条件下近匹配的下界。

论文证据：Lemma 3.2支持仅枚举2^n n^{O(k log n)}个状态。Theorem 3.5声称：SCC下，对每个ε>0存在常数k，使2^{(1−ε)n}|I|^{O(1)}时间不可达。

模型推断：固定入度下指数底数的下降是中心实质增量；下界不能理解为对每个固定k均成立。

定位：['TEXT_OR_QIBu6vtRMI_e0c70a59590e：p4，Lemma 3.2、Theorem 3.3。\n', 'TEXT_OR_QIBu6vtRMI_e0c70a59590e：p5，Theorem 3.5']

作者主张：刻画入度、可加评分及分量大小限制下的近似保证与难近似性。

论文证据：Theorem 4.1—4.3分别给出k+1、2、2q近似；Theorem 5.3及Corollary 5.5在UG下排除O(k/log²k)、O(q/log²q)近似。

模型推断：新增了受限PT的近似保证；可加情形此前已可多项式精确求解，因此2近似是简单算法的保证，而非首次获得可解性。

定位：['TEXT_OR_QIBu6vtRMI_e0c70a59590e：p6—9，Theorems 4.1—4.3、5.3及Corollary 5.5']

key_results：[{"setting": "n个节点，固定最大入度k", "baseline": "Grüttemeier et al. (2021a)：3^n|I|^{O(1)}", "metric_or_guarantee": "精确最优解及最坏情况运行时间", "reported_values_and_units": "(2+ε)^n|I|^{O(1)}，任意固定ε>0；无入度限制时本作仍为3^n|I|^{O(1)}。", "information_and_compute": "基于给定评分输入；非实测运行时间，未报告实际内存。", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p3—4，Theorems 3.1、3.3"}, {"setting": "最大入度k，任意局部分数", "baseline": "最优可行polytree", "metric_or_guarantee": "乘法近似保证", "reported_values_and_units": "f(D)≥OPT/(k+1)", "information_and_compute": "整父集贪心；关于显式输入长度|I|的多项式时间。", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p6，Theorem 4.1。\n"}, {"setting": "最大入度k，可加局部分数", "baseline": "Ganian & Korchemna (2026)已有多项式精确可解性", "metric_or_guarantee": "单弧贪心的近似保证", "reported_values_and_units": "f(D)≥OPT/2；所述紧性针对该贪心算法。", "information_and_compute": "输入O(n²)个弧分数；保持森林和入度约束，多项式时间。", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p6，Theorem 4.2。\n"}, {"setting": "每个连通分量至多q条弧", "baseline": "最优满足分量限制的polytree", "metric_or_guarantee": "单位弧分数父集贪心的近似保证", "reported_values_and_units": "f(D)≥OPT/(2q)", "information_and_compute": "按f_v(S)/|S|选择父集；关于输入长度的多项式时间。", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p7，Theorem 4.3。\n"}]

prior_work_candidates：[{"citation_as_printed": "Grüttemeier, N., Komusiewicz, C., and Morawietz, N. On the parameterized complexity of polytree learning. In Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI 2021), pp. 4221–4227. ijcai.org, 2021a.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "相同PT问题；本篇还复用其Theorem 2的归约。", "claimed_difference": "固定入度下将精确时间由3^n改进到(2+ε)^n。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p3 §3、p8 §5、p10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Ziegler, V. Approximation algorithms for restricted Bayesian network structures. Inf. Process. Lett., 108(2):60–63, 2008.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "反复选择最高分可行父集的贪心思想。", "claimed_difference": "从一般DAG的有向无环约束转为骨架无环约束；本文保证为k+1而非前作的k，问题约束不同。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p1—2 §1、p10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Ganian, R. and Korchemna, V. The complexity of Bayesian Network Learning: Revisiting the superstructure. CoRR, abs/2602.10253, 2026.", "identifier_if_present": "abs/2602.10253", "relation_candidate": "比较基线", "shared_component": "可加评分且有入度限制的PT。", "claimed_difference": "前作Theorem 18已给出多项式精确可解性；本篇分析更简单的逐弧贪心。", "basis": "target_paper_only", "target_locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p2 §1、p6 Theorem 4.2前文、p10参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心是有结构依据的指数时间改进及新的近似保证，超过局部性能优化；未显示路线级新范式。", "central_increment": "前作已达3^n精确求解（本篇转述）；本作在固定入度条件下用小边界状态压缩达到(2+ε)^n，证据为Lemma 3.2及Theorem 3.3。", "soundness_observation": "提供了证明文本，但未独立审计；若干排序、计分及归约规模问题须核原PDF，不能把全部下界视为已验证。", "significance_observation": "指数底数下降有实质理论价值；未报告实验，不能据此判断实际加速或实现难度。", "main_open_question": "归约中的计分和规模问题能否通过原文核对或补充论证解决，从而保住所宣称的近匹配下界？"}

limitations：[{"text": "评分预先给定，并按空父集零分归一化；乘法保证对应这个目标，不直接等于原始概率或未平移分数的相同比例保证。", "basis": "model_inference", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p2，§2评分编码与归一化"}, {"text": "Theorem 4.1文本把f_i按升序排列，却用分块首项给总和上界，方向不一致；可能是笔误或提取问题，不据此直接判定定理错误。", "basis": "model_inference", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p6，Theorem 4.1证明。\n"}, {"text": "Theorem 3.5按供给文本给包含辅助节点p的父集S赋分|S|，却以n′作为覆盖阈值；辅助节点增加的分数未见扣除，条件下界证明需核对。", "basis": "model_inference", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p5，Theorem 3.5证明。\n"}, {"text": "Theorem 5.3声称一般PT无O(n^(1−ε))近似，但构造有|V′|+|E|+1个节点，可能二次膨胀；所给论证未说明如何仍转移该节点数指数。", "basis": "model_inference", "locator": "TEXT_OR_QIBu6vtRMI_e0c70a59590e：p8，Theorem 5.3及证明。\n \n"}]

minimal_check：{"question": "Theorem 5.3的一般PT难近似指数是否经得起归约规模核算？", "control": "分别记独立集节点数N与PT节点数n=N+|E|+1，避免混用。", "observable_outcome": "将PT近似比代回独立集实例，检查是否确实违反所引用的独立集下界。", "resources": "原PDF、所引归约及独立集难近似定理全文；仅需符号推导，不需训练实验。", "failure_or_stop_condition": "若只能推出更弱指数且无补充归约，则将原强指数下界标为未证实，不据此否定精确算法上界。"}

missing_fields：["PDF图像及图中构造的可视核验", "前作全文；部分参考条目未提供唯一标识", "实现、实测运行时间与内存用量；无训练或测试实验报告", "当前附件是否为最终出版版的确认"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

近2^n精确上界是值得阅读的中心增量；近匹配下界及一般难近似指数要在计分/规模修正后才能采信。

身份与评分输入：完整题名与10页附件一致。对象是骨架为森林的DAG，可不连通；候选父集和局部分数预先给定，空父集零分，未指定分数为负无穷。乘法近似对应平移后的分数目标，不直接等同原概率/原始对数分数的相同比率。

核查定位：p001 title, p002, Preliminaries；identity_feasibility_and_score_normalization_confirmed

精确上界的关键条件：小子树优先DFS使仍有未访问父节点的栈位置按子树规模倍增，局部边界O(klogn)，从而状态数2^n n^{O(klogn)}；固定k时为(2+epsilon)^n多项式输入因子，无入度限制仍3^n。预处理增加一个连接节点也将入度界加1；不把它解释成任意增长k下统一近2^n。未逐项实现DP，但关键状态计数可跟踪。

核查定位：p003, connected reduction/DP, PDF physical page4, Lemma3.2/Theorem3.3；upper_bound_mechanism_and_constant_parameter_scope_confirmed

SCC归约计分反例：原PDF5明确父集S含辅助p而赋分|S|。U={a,b,c}、集合{a,b}/{b,c}、t1、epsilon.5无单集合覆盖，但输出PT可取s1父集{p,a,b}，三弧星加孤立c，得分3=n'。原阈值产生假阳性；扣除p计分可能修补，不等于条件下界必为假。图注另将两原集合并入父集的分数写2，与覆盖/基数口径也需统一。

核查定位：PDF physical page5, Theorem3.5/Figure1, local_check/reduction_checks.md；literal_reduction_scoring_counterexample_confirmed

近似算法与证明排版：正文/表1保证为k+1、加性逐弧贪心2、分量至多q弧的单位弧分数贪心2q；加性问题已有多项式精确法。原4.1将f_i升序却用分块首项作总和上界，方向错误；该步应降序，且当前森林最多ki条已加弧、加i个已固定节点，才得到(k+1)i阻塞计数。视为局部修正路径，不凭文字错误否定全部贪心保证。

核查定位：p003, Table1, PDF physical page6, Theorems4.1–4.2, p007, Theorem4.3；approximation_factors_confirmed_local_ordering_gap_scoped

一般难近似指数的归约规模：原5.3从独立集N点M边构造n=N+M+1个PT节点。稠密时n=Theta(N²)，PT的n^(1−epsilon)因子可变为N^(2−2epsilon)，不对全部epsilon>0违反所引独立集下界。该构造直接只给n^(1/2−delta)型较弱节点数指数；需额外规模控制才能得原强表述。最大度d→入度d+1的UG参数下界另行保留，不能因节点数问题一并否定。

核查定位：PDF physical page8, Theorem5.3/construction, local_check/reduction_checks.md；node_count_exponent_transfer_gap_confirmed

本地补充/限定：["将辅助节点计分疑点落实为五节点反例；原样逆向归约不成立但可考虑修正分数。", "明确一般节点数下界与入度参数下界受不同规模因素影响。"]

核查局限：["未运行DP或贪心、未复核SCC/UG及引用前作证明；只有局部图构造和规模算术。", "未证明修正后的完整下界，也未测运行时间和内存。", "第1页仅读标题开头，正文所列页已核查；版本角色未确认。"]


## pro089 · Euclean: Automated Geometry Problem Formalization with Unified Verification in Lean

论文 OR_OUtgFOscnh；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_OUtgFOscnh_1c6cb0035edb", "source_url": "https://api2.openreview.net/pdf?id=OUtgFOscnh\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_OUtgFOscnh_1c6cb0035edb：物理页1–21，含正文§1–7、参考文献及附录A–G；连续页标齐全。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–2仅有提取文字，未观察图形。", "双栏混排影响部分公式与代码，尤其附录G；主要实验表数值可辨，但不能据此确认源码完整可编译。", "未核读前作、仓库或其他版本，未执行代码、复现实验或逐条验证证明。"]}

问题：把纯文本平面几何题转成语义忠实、可编译且兼容原生Mathlib的Lean定理陈述，供通用证明器使用。

方法：DeepSeek-V3依次显式化约束、生成非形式化证明草图以锚定构型、检索并映射Mathlib构造，再用Lean编译错误迭代修复；平面表示为EuclideanSpace R (Fin 2)。输出主要是定理陈述，并非自动获得完整证明。

作者主张：通过显式约束、构型锚定和原生Mathlib映射，实现可统一验证的几何自动形式化。

论文证据：累加式消融显著提高编译通过数；锚定降低编译率，但30题人工配对评测出现7胜3负。

模型推断：增量在几何专用约束处理与流程组合，不是新逻辑基础；尚未建立自动补充条件保持原题语义的保证。

定位：['TEXT_OR_OUtgFOscnh_1c6cb0035edb：p3–6，§3、§5.1；p7表3。']

作者主张：构建最大规模Lean几何形式化数据，并验证对通用神经证明器的训练价值。

论文证据：保留768及177,597道至少有一个可编译陈述的问题；人工检查和留出OMNI测试提供质量及下游用途证据。

模型推断：形成了可接入标准证明器的大规模几何候选资源；规模不等于正确定理数量，历史最大性未外核。

定位：['TEXT_OR_OUtgFOscnh_1c6cb0035edb：p5–8，§4–5；p11–12附录D。']

key_results：[{"setting": "两套数据的生成与编译筛选", "baseline": "OMNI初始780题；Numina初始183,796题", "metric_or_guarantee": "至少有一个可编译陈述的问题保留率，不是证明成功率", "reported_values_and_units": "OMNI：768题、98.5%；Numina：177,597题、96.6%。", "information_and_compute": "生成器DeepSeek-V3；OMNI每题32候选；Numina每题候选预算未明确报告。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p5 §4、p6表2。\n"}, {"setting": "30道OMNI题，每配置每题32次生成，共960候选", "baseline": "基础提示125/960，13.0%", "metric_or_guarantee": "编译通过数；另做人工Pass@3配对评测", "reported_values_and_units": "依次加入概念映射、修复、约束映射、锚定：254、465、500、480个通过，分别26.5%、48.4%、52.1%、50.0%。锚定对无锚定：7题胜、3题负、10题均正确、10题均错误。", "information_and_compute": "顺序累加式消融；统一token及修复预算未报告。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p6 §5.1、p7表3。\n"}, {"setting": "OMNI难度≥4.0的180题，每题检查5个已编译候选", "baseline": null, "metric_or_guarantee": "人工语义一致性；TOP1检查首个，TOP5检查是否至少一个正确", "reported_values_and_units": "TOP1：88/180，48.89%；TOP5：132/180，73.33%。", "information_and_compute": "评审为有形式数学及Lean经验的研究生；这是编译后候选上的条件性结果。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p6–7 §5.2、表4。\n"}, {"setting": "Goedel v2在完整Numina-Geometry上生成训练数据，并在同一语料评测", "baseline": "Goedel v2 8B：Pass@1 13.6%", "metric_or_guarantee": "形式陈述的单次证明成功率", "reported_values_and_units": "SFT后15.1%；DPO后15.0%。", "information_and_compute": "SFT每题采样1次，DPO采样2次、形成7,148偏好对；各用8张A100-40GB训练1轮，有效批量256；耗时未报告。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p7–8 §5.3、表5；p10–11附录C–D、表10。\n"}, {"setting": "作者报告未用于训练的OMNI-Geometry留出评测", "baseline": "Goedel v2：Pass@1 6.90%，Pass@2 8.33%", "metric_or_guarantee": "跨数据集证明成功率", "reported_values_and_units": "SFT：Pass@1 7.68%、Pass@2 9.11%；DPO：7.81%、8.59%。", "information_and_compute": "使用Numina训练后的模型；跨来源去重流程未说明。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p11附录D、表11。\n"}, {"setting": "DeepSeek-Prover-V2-7B在随机一半Numina上采集成功轨迹、训练并在该半集评测", "baseline": "Pass@1 13.4%", "metric_or_guarantee": "跨证明器的训练效用", "reported_values_and_units": "SFT后Pass@1 15.0%。", "information_and_compute": "训练2轮，其余沿用SFT设置；不是独立留出测试。", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p11–12附录D、表12。\n"}]

prior_work_candidates：[{"citation_as_printed": "Murphy, L., Yang, K., Sun, J., Li, Z., Anandkumar, A., and Si, X. Autoformalizing Euclidean geometry. In International Conference on Machine Learning (ICML), 2024.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "自然语言几何的Lean形式化", "claimed_difference": "本篇转述LeanEuclid使用System E及SMT，本作使用原生Mathlib；未给同题等预算直接性能比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p2 §2、p9参考文献、p12附录F。", "prior_actually_read": false}, {"citation_as_printed": "Song, C., Wang, Z., Pu, F., Wang, H., Lin, X., Liu, J., Li, J., and Liu, Z. Leangeo: Formalizing competitional geometry problems in lean, 2025.", "identifier_if_present": "arXiv:2508.14644", "relation_candidate": "比较基线", "shared_component": "竞赛几何的Lean表达与证明资源", "claimed_difference": "本篇称LeanGeo扩展System E；本作强调标准库互通与自动生成规模。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p2 §2、p9参考文献、p12表13–14。", "prior_actually_read": false}, {"citation_as_printed": "Ying, H., Wu, Z., Geng, Y., Wang, J., Lin, D., and Chen, K. Lean workbook: A large-scale Lean problem set formalized from natural language math problems. In Advances in Neural Information Processing Systems (NeurIPS), 2024.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "大规模自然语言数学形式化语料", "claimed_difference": "本作面向几何约束和数据缺口；文中未充分建立具体算法继承关系。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p1–2 §1–2、p10参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心价值是把几何专用流程与标准库连接，形成有人工及下游证据支持的大规模候选资源；超出单项提示优化，但不足以判路线级首创。", "central_increment": "前作已提供几何Lean形式化及大规模数学语料（本篇转述）；本作新增原生Mathlib几何候选库与约束处理流程，支持证据包括人工评测和留出集增益；尚待排除过强假设造成的虚假质量。", "soundness_observation": "陈述编译、形式证明正确、自然语言语义忠实是三回事；示例含sorry，附录证明未本地执行。作者也承认遗漏约束未必触发编译失败。", "significance_observation": "有助于复用通用证明器，数据工程价值明确；实测提升较小，不能据此认定几何自动形式化已经可靠。", "main_open_question": "177,597条候选中，有多少在排除遗漏、过强及矛盾假设后仍真正保留原题语义？"}

limitations：[{"text": "作者明确将Numina视为候选语料而非真值；仅处理文字，受Mathlib覆盖限制，补充条件可能过弱或过强。", "basis": "author_report", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p8 §6。\n"}, {"text": "表1把线段位置映为严格Sbtw，可能排除合法端点；这属于语义收缩风险，不能仅以可编译或可证明消除。", "basis": "model_inference", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p4 §3.2.1、p6表1。"}, {"text": "人工样本仅覆盖OMNI难度≥4的编译后候选，不能直接外推Numina质量；主训练结果及跨证明器结果均含训练语料内评测，留出OMNI缓解但未完全排除来源重复。", "basis": "model_inference", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p6–7 §5.2–5.3、p11附录D。"}, {"text": "Aristotle的100题检查在排除部分错误案例后报告25题获证、19题未决；获证不自动等于忠实，未决也不等于正确，因此不能视为总体语义正确率的严格下界。", "basis": "model_inference", "locator": "TEXT_OR_OUtgFOscnh_1c6cb0035edb：p8 §5.3、p13附录G。"}]

minimal_check：{"question": "构型锚定是否以排除合法情况换取表面正确性？", "control": "抽30道Numina题，完整流程与去锚定流程各取3候选，固定总生成及修复预算，盲审原文与陈述。", "observable_outcome": "配对语义Pass@3，以及过强、遗漏和矛盾假设的数量。", "resources": "原题、生成提示词与候选、匹配Lean环境及有Lean经验的评审；调用费用和耗时未知。", "failure_or_stop_condition": "语义净增益不为正，或收益主要来自缩窄原题，则不支持锚定机制主张；题意无法确定者单列未决。"}

missing_fields：["Mathlib精确提交版本、完整提示词及检索配置。", "Numina候选数、修复轮数、生成token与总耗时。", "人工标注人数、独立一致性和分歧裁决细节。", "跨数据源去重说明、总体语义审计及完整证明验收规则。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

原生Mathlib几何候选库及留出证明增益有用途；继续阅读应优先核查新增、遗漏和矛盾假设的总体语义质量及生成成本。

身份与形式化产物：Euclean题名及21页附件相符；中心是DeepSeek-V3约束显式化、prove-first构型锚定、Mathlib映射和编译反馈修复。原PDF4示例以sorry结束，证明的是陈述可编译，不代表取得完整证明或保持原自然语言语义。

核查定位：p001 title, PDF physical page4, Figure1, p005, pipeline；identity_and_statement_only_scope_confirmed

编译率与语义审查分母：780→768及183796→177597指至少一个陈述编译通过的问题。30题各32候选的通过数125/254/465/500/480；锚定500→480降低编译率，但人工Pass@3为7胜3负、10均正确10均错误，即17/30对13/30。180道OMNI难度≥4题每题5个已编译候选，TOP1 88/180、TOP5 132/180，不能外推177597条Numina候选总体正确率。

核查定位：PDF physical page6, Tables1–2/section5.1, PDF physical page7, Tables3–4；counts_and_conditioned_denominators_confirmed

严格线段约束的具体语义收缩：图1和表1将on segment映为Sbtw。令A=(0,1),B=(-1,0),C=(1,0),P=B，是等腰直角三角形合法端点；P到AB垂足D=B，到AC垂足E=A，C到AB垂足H=A。因此PD+PE=0+sqrt2=CH，原面积恒等式在该端点成立，而Sbtw B P C为假。排除端点不是该恒等式普遍必需条件；这只反驳此例严格条件的必要性，不否定内点定理或证明整个候选库错误。

核查定位：PDF physical page4, Figure1/caption, PDF physical page6, Table1；elementary_endpoint_counterexample_to_necessity_confirmed

训练用途与留出证据：Goedel8B同一完整Numina采轨迹训练后在该语料评测13.6→15.1/15.0；DeepSeek-Prover在同一随机半集训练和评测13.4→15.0。作者声明留出OMNI结果Pass1 6.90→7.68/7.81、Pass2 8.33→9.11/8.59，跨来源重复未核实。7148个DPO偏好对、8A100一轮有效batch256不包含全生成和修复成本。

核查定位：p007–008, section5.3/Table5, PDF physical page11, Tables10–11, p012, Table12；training_set_vs_holdout_and_cost_scope_confirmed

证明器额外验证：Aristotle100题检查先排除显式错误/平凡/反例例子，再报告25获证、19未决未反驳；19不能计正确，25形式获证也不自动保证忠实于原题。原PDF13展示的证明例未在本地Lean编译，不能改称内核验证通过的本地证据。

核查定位：p008, section5.3, PDF physical page13, AppendixG；proof_success_not_semantic_lower_bound_confirmed

本地补充/限定：["将严格Sbtw可能排除端点的风险落实为与文中等腰示例匹配的解析端点构型；不推断其他候选错误。", "保留资源贡献L2作为模型暂定等级，不将177597条候选称为已验证正确定理。"]

核查局限：["未运行Lean、证明器或作者代码，未复核前作；仅核对来源及纸面端点构型。", "第1页仅标题开头；第7–8页提取文字有少量输出截断，关键表由已查看的第7页图像补核；未逐条审查附录全部证明。", "当前附件版本角色未确认；人工语义标注及跨来源去重未独立复验。"]


## pro090 · MathlibLemma: Folklore Lemma Generation and Benchmark for Formal Mathematics

论文 OR_2WfRsrQxpC；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db", "source_url": "https://api2.openreview.net/pdf?id=2WfRsrQxpC\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "source_pdf_sha256": "a9c541b7b8dbd60b8a534841d60882fe31ce0e9594f538973ee765ff3cfb5fef"}], "read_ranges": ["TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页1—20全部提供文本，包括正文、参考文献和附录A—F；连续页标完整，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；双栏交错，公式和代码符号可能失真。表1—5关键数据可辨；图3—5仅有散落文本，不据此补录各轮曲线数值。", "未提供前作全文、完整数据集或运行代码；未搜索、运行证明器或核验上游PR。"]}

问题：从Mathlib种子文件主动发现、形式化并证明缺失的可复用常用引理，而不只解决给定定理。

方法：种子全文→Discovery生成含sorry的候选→Judge忽略语法判断数学合理性→Formalizer借Lean报错修复类型→Prover生成并修复证明。最终代码须通过Lean及proof-bypass筛查，禁止占位证明和新增axiom、constant、opaque等声明。

作者主张：提出首个专为自动folklore挖掘设计的模块化LLM流水线。

论文证据：完整给出四阶段实现、提示词和配置，产出1506条通过所述验证的证明，并报告3条经人工整理后合入Mathlib。

模型推断：新增主要在任务专用化和产物组织；不是新证明算法。已有库种子猜想生成近邻，首创边界尚未确立。

定位：['TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页3，§2.1；物理页8—9，§6。\n', 'TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页9，§6.2。\n']

作者主张：提供4028条非平凡、类型检查通过的Lean命题及可复用证明库，揭示日常形式化能力缺口。

论文证据：报告多模型Success@2、两批未解题人工审计，以及8B模型Pass@16补充实验。

模型推断：提供了有价值的场景资源；但类型检查不等于命题为真，aesop未解也不等于相对全库具有语义新颖性。

定位：['TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页5—8，§4—5。\n']

key_results：[{"setting": "GPT-5.1构建基准，109个Mathlib种子", "baseline": null, "metric_or_guarantee": "候选筛选与类型检查规模", "reported_values_and_units": "表1分域数加总：9148候选→6150被Judge接受→4317可编译；剔除289条aesop直接可解命题，保留4028条。", "information_and_compute": "作者估算前三阶段约$200，证明约$500；全流程摊销约$0.46/已证引理，不含本地模型服务、人工整理及维护者审查。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页6，表1；物理页9，§6.3。\n \n"}, {"setting": "4028题，闭卷证明；初次生成后最多修复2轮", "baseline": "GPT-5.1 none/low、Goedel-Prover-V2-32B、Kimina及其他开放权重模型", "metric_or_guarantee": "Success@2；不是两个独立样本的Pass@2", "reported_values_and_units": "GPT-low总成功率19.39%，Goedel 17.70%，GPT-none 15.69%；七配置并集37.39%，对应1506题。Goedel/GPT-low在基础域为27.42%/22.44%，抽象域为8.24%/18.61%。", "information_and_compute": "默认每次生成上限50000 tokens；Formalizer最多10次试验；Lean v4.25.0-rc2。上限不是实际消耗，未微调。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页8，表3；物理页12—13，附录A.2。\n \n"}, {"setting": "模型均未解残余的种子分层人工审计", "baseline": "模型闭卷未解；人类可查全库、使用AI和外部搜索", "metric_or_guarantee": "样本内人工证明比例", "reported_values_and_units": "主审计107/138，约78%；独立五种子检查79/94，84.0%，不与主样本合并。主审计剩余31条中25条缺假设、5条按原陈述错误、1条技术形式化困难。", "information_and_compute": "人工工时未报告；不能解释为同条件人机对照或全基准78%有效。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页7，表2、§4.3；物理页18，附录D。\n \n"}, {"setting": "人工选择并整理6条已证引理的上游试点", "baseline": null, "metric_or_guarantee": "作者报告的Mathlib接纳情况", "reported_values_and_units": "3条合入、1条因冗余被拒、2条未继续推进；合入PR为#31985、#32167、#32170。", "information_and_compute": "选择性小样本，不代表1506条证明的整体接纳率。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页9，§6.2；物理页19，表5。\n \n"}, {"setting": "Goedel-Prover-V2-8B，4028题，每题16次独立尝试", "baseline": null, "metric_or_guarantee": "Pass@16", "reported_values_and_units": "13/4028，0.32%。", "information_and_compute": "无修复反馈；模型规模和采样协议均不同，不能直接与主表32B的Success@2比较。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页17—18，附录C.3、表4。\n"}, {"setting": "Discovery先显式列必要假设的小规模提示词消融", "baseline": "同规模旧提示词", "metric_or_guarantee": "编译与人工审查结果", "reported_values_and_units": "新旧均123/160可编译；未解决数分别6和7条，真正缺假设案例均为2条。", "information_and_compute": "未展示实质减少缺假设错误；重复试验与运行成本未报告。", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页19—20，附录F。\n"}]

prior_work_candidates：[{"citation_as_printed": "Onda, N., Kasaura, K., Oriike, Y., Taniguchi, M., Sannai, A., and Sonoda, S. LeanConjecturer: Automatic generation of mathematical conjectures for theorem proving. arXiv Preprint, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "从已有库上下文生成Lean猜想，并用自动策略筛选。", "claimed_difference": "本作强调缺失folklore，而非一般合理猜想；未直接比较效果。", "basis": "target_paper_only", "target_locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页3，§2.1；物理页11，参考文献。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Alhessi, Y., Einarsd´ottir, S. H., Granberry, G., First, E., Johansson, M., Lerner, S., and Smallbone, N. Lemmanaid: Neuro-symbolic lemma conjecturing. arXiv Preprint, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "LLM引理生成、类型有效性与库新颖性筛选。", "claimed_difference": "前作面向Isabelle/HOL并结合符号引擎；本作面向Lean/Mathlib的folklore工作流，不能由引用推出继承关系。", "basis": "target_paper_only", "target_locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页3，§2.1；物理页10，参考文献。\n \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "有明确的场景、工程和资源增量；中心机制是已有库种子生成、语义筛选及编译反馈修复的专用化。现有证据不足以确立新的库扩展机制，但也没有依据判为被前作覆盖的L0。", "central_increment": "按本篇转述，前作已能生成库相关猜想；本作新增folklore导向流程和持续保存的基准/证明产物，少量入库支持实际价值，尚待排除大范围语义冗余。", "soundness_observation": "验证协议支持最终形式化代码的条件性正确性，不保证原始数学意图保持；本轮未复核代码、证明目标一致性或运行结果。", "significance_observation": "可能补充日常形式化API，但尚无受控下游实验量化节省的证明工作。", "main_open_question": "1506条已证产物中，真正非冗余且具有可复用价值的库缺口占多少？"}

limitations：[{"text": "作者承认发现过程依赖GPT-5.1且局限于单个种子文件；53条被拒候选审计中46%实际有效，这不是全部真命题的漏判率。", "basis": "author_report", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页6，§4.2。\n \n"}, {"text": "轻量去重不能排除语义等价；语法修复可能改变数学意图；固定库快照需要维护，已证产物仍需人工整理。", "basis": "author_report", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页9，§7。\n"}, {"text": "模型并集使用更多推理资源，不能据此断言多样性优于同预算扩模；不同模型训练背景与环境配置也妨碍因果归因。", "basis": "model_inference", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页8，§5.2；物理页13，附录A.2。\n \n"}, {"text": "约86%可解比例只是作者对分层残余审计的诊断性外推；不能充当全库真值或精确性能上限。", "basis": "author_report", "locator": "TEXT_OR_2WfRsrQxpC_a9c541b7b8db：物理页8，§5.2。\n"}]

minimal_check：{"question": "已证库是否主要填补真实缺口，而非重复现有事实？", "control": "在原固定Mathlib快照上，按三域分层随机抽查30条已证引理，用全库检索和专家判断寻找等价现有声明。", "observable_outcome": "记录非冗余且可复用、等价重复、无法判定的数量，并保存对应旧声明或缺口证据。", "resources": "原始产物、固定Mathlib快照及Lean形式化专家；工时与检索成本未知。", "failure_or_stop_condition": "若多数样本已有直接等价声明，则削弱缺口挖掘主张；拿不到原快照或声明上下文时停止新颖性判断。"}

missing_fields：["未提供确切Mathlib revision标识、实际token消耗、GPU配置、总运行时间和人工工时。", "未提供前作全文或其具体预印本编号；identifier_if_present为null。", "未提供全库语义去重结果、同预算构建基线及受控下游收益。", "图像及图3—5各轮数值的可靠对应关系不可用。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得按全库等价检索与下游复用收益核查1506条产物；日常数学API补全有价值，但当前不足以优先投入全部证明细节。

身份、目标及验证链：MathlibLemma完整题名和20页附件相符。109种子文件全文经Discovery、Judge、Formalizer、Prover；前三阶段GPT-5.1，不微调。陈述以sorry通过类型检查，最终证明另经Lean和去占位/新增axiom等proof-bypass筛查；后者不等于已经排除全库语义冗余。算法1检查生成完整文件P，注释要求证明S，但精确目标一致性实现未随本文验证，不能单凭筛词声称已独立验证。

核查定位：p001 title, p004–005, section3.2, PDF physical page12, Algorithm1, p013, configuration；identity_and_conditional_verification_scope_confirmed

规模与模型结果：表1三域9148→6150→4317，去除78+80+131=289条aesop直接解后4028。Success@2为初次生成加最多两轮顺序修复，非两独立样本。GPT-low19.39%、Goedel17.70%、GPT-none15.69%，七配置并集37.39%=1506题；并集多用预算，不能证明多样性优于同预算单模型。8B Pass@16 13/4028采用另一模型和无修复协议，不可归因为采样劣于反馈。

核查定位：PDF physical page6, Table1, PDF physical page8, Table3, p013, prover settings, p018, Table4；funnel_and_inference_budget_denominators_confirmed

未解残余审计和外推：人类可查库、AI及外部搜索，主分层残余107/138获证，剩余25缺条件、5原陈述错误、1技术困难；另一五种子79/94不得与主样本合并。闭卷模型与开卷人工是不同信息条件。86%总体可解仅诊断性外推；53个Judge拒绝样本中46%有效，是拒绝集合内比例，不是所有真命题的漏判率。

核查定位：PDF physical page7, Table2/section4.3, p006, Judge audit, p008, remaining gap, p018, AppendixD；residual_conditioning_and_information_asymmetry_confirmed

实际使用、成本和提示消融：作者选择整理6条后报告3合入、1冗余拒绝、2未推进；PDF19表5及具体声明相符，但未联网核验PR或运行Lean。约200美元生成+500美元证明/1506≈.46美元，不含本地开放模型服务、人工整理和维护者审查，不能换成每合入引理价格。新旧必要条件提示均123/160编译、未解6对7、真正缺条件均2，未显示稳定消除缺条件。

核查定位：p009, sections6.2–6.3, PDF physical page19, Table5/Listings1–3, p019–020, AppendixF；selected_upstream_evidence_and_partial_cost_scope_confirmed

本地补充/限定：["补充算法1的目标一致性属于须检查的实现条件，未运行代码不能据文字认定存在或已排除绕过。", "保留原L1暂定判断；没有同预算近邻比较和全库语义查重，不能确证首创或总体入库率。"]

核查局限：["未运行Lean/作者代码、访问上游PR、检索现有引理或核读前作；所有入库说法仅来自目标论文。", "第6页部分文本输出截断已由实际PDF图像补核；图3–5各轮曲线未逐点提取。", "未独立统计全库正确率或创新比例；当前附件版本角色未确认。"]

