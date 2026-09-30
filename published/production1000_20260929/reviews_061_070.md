# 单轮全文初评与有界本地核对 61–70

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro061 · Equilibrium Pricing in Oligopolistic Data Markets

论文 OR_TAqejOfEAJ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_TAqejOfEAJ_6ac38b561348", "source_url": "https://api2.openreview.net/pdf?id=TAqejOfEAJ\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "6ac38b56134809adf17928f16dff6b8059b809422333d330743b32e377f610e2"}], "read_ranges": ["TEXT_OR_TAqejOfEAJ_6ac38b561348：物理页1–10全部连续文本，包括§1–6、证明概要、Impact Statement及References；未见缺页，所供版本没有附录。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅见全文文本，未看过PDF图像；双栏交错、公式上下标和图中文字抽取可能失真，Figure 1的曲线及逐点数值不可核。", "多项完整证明转引至未提供的Chaudhury et al., 2026b；不能将本附件的连续完整页码等同于已读该完整版。"]}

问题：非竞争性、可分数据的卖家面对预算受限买家策略定价时，纯Nash equilibrium是否存在，何种放松能保证稳定？

方法：输入预算b、估值τ及有限正价格集P，买家按价值/价格贪心购买每份数据至多一个完整副本。输出分片长度ℓ，形成确定性PLC价格。辅助收益仅随机化本卖家的统一价格、对手保持PLC；以固定点和实际收益至少为辅助收益一半，推出受限偏离保证。仿真另用惯性响应更新。

作者主张：统一定价下，纯NE甚至1.363近似NE都可能不存在。

论文证据：Example 3.1给出两卖家、贫富两类买家的参数族；Theorem 3.2及证明概要给出收益偏离倍率下界。

模型推断：说明在该非竞争性预算模型中，竞争均衡的稳定性不能直接迁移到策略定价。

定位：['TEXT_OR_TAqejOfEAJ_6ac38b561348：p004，Example 3.1、Theorem 3.2；p005证明概要。\n']

作者主张：存在PLC策略组合，使任一卖家改用统一价格所获收益不超过当前的2倍。

论文证据：Theorem 4.1通过Lemma 4.2的辅助收益固定点与Lemma 4.3的半收益界推出。

模型推断：这是对给定价格网格内线性偏离的存在性保证，不是允许任意PLC偏离的2近似NE，也不是高效求解或动态收敛定理。

定位：['TEXT_OR_TAqejOfEAJ_6ac38b561348：p006，Theorem 4.1、Lemmas 4.2–4.3。\n']

作者主张：固定其他卖家的策略后，存在至多n个正长度分片的PLC最佳响应。

论文证据：Lemma 6.1以两类不降收益的分片合并变换给出证明。

模型推断：提供单卖家最佳响应的表示复杂度界；不能据此断言均衡策略也至多有n个分片。

定位：['TEXT_OR_TAqejOfEAJ_6ac38b561348：p008–p009，§6、Lemma 6.1。\n']

key_results：[{"setting": "Example 3.1：n−1名买家预算1、估值(α,1)；另一买家预算β、估值(1,0)。取α=0.733(n−1)、β=0.860(n−1)，n→∞。", "baseline": "所有统一价格组合(p,q)", "metric_or_guarantee": "近似NE非存在性", "reported_values_and_units": "不存在1.363近似NE；1.363为无量纲收益倍率，非有限样本实验结果。", "information_and_compute": "理论参数族；所供材料未给有限n阈值。", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p004–p005，Example 3.1、Theorem 3.2。"}, {"setting": "给定有限价格集P_j、顺序平局处理的PLC定价市场。", "baseline": "同一价格集内任一统一价格的单边偏离", "metric_or_guarantee": "存在ℓ满足max_k r_j(e(k),ℓ_{−j})≤2r_j(ℓ*)", "reported_values_and_units": "收益倍率上界2；转换引理保证r_j(ℓ)≥r̂_j(ℓ)/2。", "information_and_compute": "存在性证明，未给计算复杂度或迭代次数保证。", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p006，Theorem 4.1、Lemma 4.3。"}, {"setting": "StockNews新闻—股价方向数据构造的仿真；词频特征加logistic regression，预测误差方差用于推断τ。买家数{5,10,15,20}，卖家数{5,10,15,20,25}。", "baseline": null, "metric_or_guarantee": "终止轮数、线性偏离incentive ratio、平均正长度分片数", "reported_values_and_units": "作者报告全部设置incentive ratio=1、最多137轮终止、平均分片数至多2；均非本地复现实测。\n", "information_and_compute": "全部预算1，学习率0.1，均匀正初始化，策略变化∞范数≤10^-4时停止；正文称五分片及十个候选斜率{k/10:k∈[10]}，对应关系未说明。硬件和耗时未报告。", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p006–p008，§5；图像未提供，仅采用正文明确数值。"}]

prior_work_candidates：[{"citation_as_printed": "Chaudhury, B. R., Garg, J., Murhekar, A., and Song, J. Data pricing via competitive equilibrium. In Proceedings of the ACM on Web Conference (WWW), 2026a.", "identifier_if_present": "http://jugal.ise.illinois.edu/papers/www26.pdf\n", "relation_candidate": "理论扩展", "shared_component": "预算约束、精度增益估值及非竞争性数据市场模型", "claimed_difference": "前作研究competitive equilibrium；本作研究卖家策略定价和单边偏离稳定性。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p001–p002，§1；p009，References。\n", "prior_actually_read": false}, {"citation_as_printed": "Chaudhury, B. R., Garg, J., Sharma, E., and Song, J. Revenue-optimal pricing for budget-constrained buyers in data markets, 2025.", "identifier_if_present": "http://jugal.ise.illinois.edu/papers/data-rev.pdf\n", "relation_candidate": "组件复用", "shared_component": "面向预算受限买家的PLC价格函数", "claimed_difference": "前作研究垄断者收入最优定价；本作研究寡头竞争中的近似稳定性。", "basis": "target_paper_only", "target_locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p005，§4；p009，References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是明确的非存在界及受限偏离的常数存在性保证，属于实质理论知识，而非仅换场景跑实验；不足以判路线级创新。", "central_increment": "前作已研究CE或垄断PLC定价（仅本篇转述）；本作在预算约束寡头市场新增1.363非存在界与受限2倍保证，证据为Theorems 3.2、4.1，尚待补核关键证明。", "soundness_observation": "证明框架可辨认，但主要细节外置；两项倍率针对不同策略/偏离空间，不能直接当作同一博弈的上下界。数值终止及线性incentive ratio=1不构成完整PLC精确NE认证。", "significance_observation": "揭示非竞争性数据定价的稳定性边界；不等于通用数据估值方法或可高效部署的均衡求解器。", "main_open_question": "Lemma 4.3的半收益界能否在全部允许预算、估值和顺序平局规则下严格成立？附件没有完整证明。"}

limitations：[{"text": "PLC精确NE可能不存在、PLC最佳响应NP-hard均为作者报告，证明在未提供的2026b；均衡支持集大小界也仍开放。", "basis": "author_report", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p005，§4.2；p008，§6。"}, {"text": "可加估值及其递增变换不覆盖一般数据互补或冗余；单一新闻代理任务、单位预算、小规模仿真不足以推出一般真实市场稳定性。", "basis": "model_inference", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p003，Beyond Linear Utilities；p006–p007，§5。"}, {"text": "按披露的正初始化及ℓ^t=0.9ℓ^{t−1}+0.1ℓ*，有限轮所有初始分片仍严格为正。因此“严格正”分片平均至多2，需要未说明的判零阈值、剪枝或实现差异解释。", "basis": "model_inference", "locator": "TEXT_OR_TAqejOfEAJ_6ac38b561348：p007，§5 Dynamics与Sparsity of the PLC Strategies。\n"}]

minimal_check：{"question": "小规模合法实例是否出现违反Lemma 4.3半收益界的反例？", "control": "固定预算、估值、对手PLC及平局顺序，将目标卖家的确定PLC与按相同分片长度随机选择统一价格比较。", "observable_outcome": "精确计算r_j与r̂_j，检验r_j≥r̂_j/2；未发现反例不能代替证明。", "resources": "两卖家、少量买家和价格点的精确算术枚举脚本；无需新闻模型训练，实际运行成本未测。", "failure_or_stop_condition": "找到满足假设而r_j<r̂_j/2的实例即否定该界；若平局或公式含义无法确定，则停止作正确性结论。"}

missing_fields：["外置完整版及关键完整证明", "Figure 1可视内容与逐点数值", "数据规模、分割比例、由误差方差计算τ的明确公式", "分片与斜率配置、稀疏判零规则、重复次数和不确定性统计", "实证比较基线、硬件、墙钟时间及任意PLC偏离检验"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

非竞争性预算市场的稳定性边界有理论价值；继续阅读先补半收益引理的完整证明和数值稀疏判定协议，再判断可计算性及更一般偏离空间。

身份及材料边界：10页官方当前附件与全文返回绑定一致，所供正文完整但关键证明明确转引2026b full version；本阶段该外置版本未读取。记录全部所供文本初评完成，不把它等同于关键完整证明已核验。模型是非竞争性、可分数据、预算约束买家与可加估值，递增变换不引入一般数据互补性。

核查定位：text_delivery_manifest.json, structured/pro061.json, p003–p005, model and proof references, p009, full-version reference；source_and_missing_proof_scope_confirmed

两个倍率不是同一博弈的匹配上下界：Theorem3.2在两卖家、n−1名预算1买家和一名富买家、α=.733(n−1)、β=.860(n−1)、n趋无穷下，声称统一价格不存在1.363近似NE。原第6页Theorem4.1则允许确定PLC策略，但只限制给定有限价格集内的统一价单边偏离，收益最多2倍；它不是任意PLC偏离下的2近似NE，也不是求解或动态收敛保证。

核查定位：p004, Example3.1 and Theorem3.2, p005, §4.1–4.2, PDF physical page 6, Theorem4.1；central_guarantee_strategy_spaces_confirmed

辅助随机收益与证明链：rhat_j只随机化当前卖家的统一价格，其余卖家仍固定PLC；它不是所有卖家独立混合价格博弈的收益。Lemma4.2固定点与Lemma4.3 r_j>=rhat_j/2结合推出受限2倍保证，两项完整证明均不在附件。Lemma6.1的至多n分片只针对固定对手后的某个最佳响应，均衡支持大小仍列为开放问题。

核查定位：PDF physical page 6, randomized revenue and Lemmas4.2–4.3, PDF physical page 8, §6 and Lemma6.1, p009, proof conclusion；mechanism_and_unverified_proof_boundary_confirmed

数值收敛与稀疏性不一致：原第7页从所有坐标1/m_j开始，采用l_t=.9l_(t−1)+.1lstar，lstar>=0。故每坐标l_t>=(.9)^t/m_j>0；137轮后五分片时下界约1.08e-7，非浮点下溢。所报严格正分片平均至多2不能由该更新直接得到，需未说明的判零阈值、剪枝或实现差异。Fig1b卖家轴1–10，而正文/图a是5–25，实验范围也需澄清。

核查定位：PDF physical page 7, dynamics and sparsity definition, PDF physical page 8, Figure1, local_check/inertial_support_check.json；literal_positive_support_conflict_confirmed

经验均衡认证范围：正文报告最多137轮、incentive ratio=1，但ratio只测试统一价偏离，策略变化<=1e-4也不等于精确均衡认证。仿真采用单一StockNews代理任务、单位预算、词频logistic预测误差推估值；五分片与十个斜率的对应关系、重复数、具体估值公式及运行资源未充分给出，不能推出一般真实市场稳定性。

核查定位：p006–p007, empirical setup, PDF physical page 7, incentive ratio and termination, PDF physical page 8, Figure1；simulation_and_equilibrium_scope_qualified

本地补充/限定：["原PDF确认严格正支持与惯性更新的不一致，并补充有限轮正下界量级；没有假定作者实际采用哪个阈值。", "将有限网格、受限统一价偏离和缺失完整证明分别标明，不把1.363与2当同一策略空间的上下界。"]

核查局限：["未核读外置full version及前作，不对关键完整证明作认证，L2暂评。", "未做定价枚举、仿真、新闻模型训练或部署测试；仅局部更新式算术。", "未推断错误产生原因或作者动机；参数和图轴冲突保留待澄清。", "Pro读全部所供文本，本地观察三页PDF。"]


## pro062 · Local-Minima-Preserving Polynomial Relaxation of Ising Problems

论文 OR_EBTMJ3MXt0；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47", "source_url": "https://api2.openreview.net/pdf?id=EBTMJ3MXt0\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "7c5cdd8d99fac69b8793b9992843ad5cac907528c0e0ce64424df637dafd8e03", "source_pdf_sha256": "ea22d3afbc47622b6dfa48d34f88012911ff29a1f6a3d12350772c25ae021521"}], "read_ranges": ["TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页1–22，连续页标完整；包括正文§1–6、参考文献、附录A–F及跨页表4。\n"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅有全文提取文本，未见PDF页面图像；图1–7的曲线、直方图及颜色编码不可核读。", "双栏文本存在交错，公式上下标和表格可能失真；表1部分基线单元格明显可疑，未擅自修正。", "未提供前作全文、作者代码或运行日志；未搜索、复现或核验其他版本。"]}

问题：如何让Ising问题的光滑连续松弛保留离散单翻转局部最优性，同时使用GPU梯度优化求解SK、MAX-CUT和NPP？

方法：输入耦合矩阵J，在盒域内优化H(x)=−xᵀJx/2+Σfθ(xi)。实用版本取fθ(x)=βx⁴/4−αx²/2，以投影ADAM迭代、角点梯度检查和高斯扰动进行搜索，输出被接收候选中能量最低的符号向量；无需训练标签。

作者主张：连续松弛局部极小值与Ising单翻转局部极小值存在一一对应。

论文证据：Lemma 3.7排除非角点局部极小值，Lemmas 3.9、3.11分别证明两个包含关系，Theorem 3.13得到loc(H)={λs:s∈loc(E)}。

模型推断：前作pCQO-MIS已建立特定MIS对应关系（仅本篇转述）；本作在可容许吸引子条件下扩展至一般齐次Ising，是实质性的保证扩展，但不是全局最优或优化器收敛保证。

定位：['TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页4–5，§3.3；物理页13–16，附录B。\n']

作者主张：构建可扩展梯度求解器，在多类困难实例上取得优于先进基线的结果。

论文证据：表1中SK最佳能量次于FEM，K2000和NPP最佳目标值优于所列基线；表2提供小规模调参向较大实例迁移的实验。

模型推断：跨任务实用价值有报告支持，但优势依赖任务和比较口径，不能概括为全面领先。

定位：['TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页6–8，§4、表1–3。\n']

key_results：[{"setting": "齐次零对角Ising，盒约束四次松弛。", "baseline": "原离散问题的单翻转局部极小值集合。", "metric_or_guarantee": "局部极小值集合精确对应。", "reported_values_and_units": "充分条件：3βλ²<α<βλ²+γ(J)；loc(H)={λs:s∈loc(E)}。", "information_and_compute": "精确计算γ通常组合困难；明确量化步长可给出下界γ0。无全局质量或有限迭代收敛保证。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页4–5，Proposition 3.4、Theorem 3.13、式(28)。\n"}, {"setting": "表1：1000-spin SK，非对角耦合服从标准正态，100次运行。", "baseline": "FEM。", "metric_or_guarantee": "无量纲Ising能量，越低越好。", "reported_values_and_units": "MiP最佳/均值−16689.49/−16491.62；FEM为−16814.75/−16593.16。表列Runtime分别0.21/0.01秒。", "information_and_compute": "上述工作站；运行时间排除调参，未明确其跨运行汇总口径。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页7，表1。\n"}, {"setting": "表1：K2000完全图，边权随机±1，100次运行。", "baseline": "FEM。", "metric_or_guarantee": "Cut Value，越高越好。", "reported_values_and_units": "MiP最佳34137、均值33473.33，表列Runtime 0.24秒；FEM最佳34038、Runtime 0.01秒。", "information_and_compute": "调参时间排除；FEM均值单元格可疑，未修正或用于比较。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页7，表1及MAX-CUT段。\n"}, {"setting": "表1：NPP，1000个U[0,1]数，100次运行。", "baseline": "D-WAVE标记的基线。", "metric_or_guarantee": "分区差值Disc，越低越好。", "reported_values_and_units": "MiP最佳/均值0.0015/0.014，Runtime 0.21秒；D-WAVE为0.00957/1.191、1.073秒。", "information_and_compute": "均为作者报告；D-WAVE具体后端未清楚交代，不能据此认定真实量子硬件对比。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页7，表1。\n"}, {"setting": "表2：1000-spin GOE；非对角方差1/n，对角方差2/n，100个实例。", "baseline": "按模型调优的IAMP。", "metric_or_guarantee": "平均Ising能量、平均sync及时间。", "reported_values_and_units": "MiP/IAMP：能量−728.27/−643.85；sync 1.000/0.943；时间0.137/0.179秒。", "information_and_compute": "J量化至五位小数；MiP仅在100-spin实例调参后固定。表内非零对角与理论假设的衔接未说明。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页8，表2。\n"}, {"setting": "表3：G-set MAX-CUT。", "baseline": "文中列出的best-known值及D-WAVE。", "metric_or_guarantee": "Cut Value及相对best-known差距。", "reported_values_and_units": "G49：MiP=6000，匹配best-known；G55：MiP=10173，best-known=10299，误差1.22%，D-WAVE=10259。", "information_and_compute": "F.1设R=10轮、K=200、T=10、σ=10⁻³；每维网格3–5点，总调参耗时未完整报告。", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页8，表3；物理页19，附录E、F.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Alkhouri, I., Le Denmat, C., Li, Y., Yu, C., Liu, J., Wang, R., and Velasquez, A. Differentiable quadratic optimization for the maximum independent set problem. In Forty-second International Conference on Machine Learning, 2025.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "连续二次目标的局部极小值与maximal independent sets对应。", "claimed_difference": "本篇声称推广至一般Ising的单翻转局部极小值，并给出吸引子充分条件。", "basis": "target_paper_only", "target_locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页2，§1；物理页9，References。\n", "prior_actually_read": false}, {"citation_as_printed": "Goto, H. Quantum computation based on quantum adiabatic bifurcations of kerr-nonlinear parametric oscillators. Journal of the Physical Society of Japan, 2018.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "KPO有效Hamiltonian中的四次势。", "claimed_difference": "本篇在静态化势函数上增加盒约束、可容许条件和局部极小值对应分析，不把四次势本身当作全新组件。", "basis": "target_paper_only", "target_locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页9，References；物理页17–18，附录D.1。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是有明确假设的一般齐次Ising局部极小值保持保证，不只是更换优化器；但理论与实验实现存在重要未解释之处。", "central_increment": "将特定离散问题的连续局部最优对应，扩展为可由吸引子条件检验的Ising松弛保证。", "soundness_observation": "附录B给出负曲率排除非角点及角点一阶条件的证明链；未做形式化核证。附录E的参数规则和实验认证指标不能直接与该证明衔接。", "significance_observation": "有潜力提供通用离散优化的局部最优证书；不代表解决全局搜索难度。工程部分主要依赖矩阵运算、现成优化器和调参。", "main_open_question": "实际实验实现是否真正满足可容许条件，并按统一的零场、精度与接收规则返回严格单翻转局部极小值？"}

limitations：[{"text": "按附录E现有文本，λ=√(γ/(2β))使式(63)两端同时等于3γ/2，α的严格可行区间为空，与保证所有配置可容许的说法冲突；需核原公式及实现，不能据此直接否定条件定理。", "basis": "model_inference", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页19，附录E。\n"}, {"text": "表1的MiP平均sync为0.999、0.998、0.994；表4则报告常小于n的整数。它们不足以确认所有输出均通过严格认证，且可能涉及零局部场符号约定、归一化或实现差异。", "basis": "model_inference", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页4–5，式(18)、(29)；物理页7、19–20，表1、4。\n"}, {"text": "附录A仅证明外场增广保持全局最优，不能据此推出原模型单翻转局部极小值的一一对应；表2 GOE含非零对角，是否先去除也未说明。", "basis": "model_inference", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页12，Proposition A.1；物理页8，表2。\n"}, {"text": "正文关于G-set全部在1%内及G55超过D-WAVE的概括与表3不符；G22在表3/4分别为13326/13226，未解释差异。计时排除调参，不能直接代表端到端等预算优势。", "basis": "model_inference", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页7–8，§4、表1、3；物理页20，表4。\n"}, {"text": "作者报告λ过大时性能崩溃，学习率影响最终目标值；可扩展性仍依赖合适参数窗口。本轮仅核读消融文字，未核读图中曲线。", "basis": "author_report", "locator": "TEXT_OR_EBTMJ3MXt0_ea22d3afbc47：物理页21–22，附录F.2。\n"}]

minimal_check：{"question": "实际参数生成和输出认证是否兑现定理条件？", "control": "在同一小型量化、对称零对角J上，以精确枚举得到的γ及逐单翻转能量差，独立对照实际参数和Algorithm 1接收结果。", "observable_outcome": "参数存在非空可行区间；每个被认证输出均满足所有单翻转能量差非负，且sync口径一致。", "resources": "实际参数生成实现与输出日志目前未提供；小规模精确核验可用普通CPU，具体耗时未测。", "failure_or_stop_condition": "若参数区间为空，或任何被认证输出存在下降翻转，则停止将该实验实现宣称为兑现局部最优保证；这不自动反驳满足假设时的定理。"}

missing_fields：["原PDF页面图像及图1–7的可核读图形。", "完整实例参数、数值精度、零场处理、认证容差及输出日志。", "表1–2完整搜索预算、各基线具体后端、计时汇总口径和调参总成本。", "前作全文、独立复现实验及附件出版版本身份核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

局部极小值保持条件有理论价值；优先核查可执行的参数生成、零对角处理与逐翻转认证，再依赖其工程效率及严格证书主张。

身份及中心定理对象：22页官方当前附件与全文返回绑定一致。中心正确对应对象是对称零对角、无外场Ising的单翻转局部极小值与盒角点λs上的连续局部极小值集合。偶函数、内点负曲率和−λγ<f'(λ)<0给充分条件；γ是全部违反配置的最小非零场幅度，通常难精确求。它不保证全局最优、任意软向量取sign都有效或ADAM有限步收敛。

核查定位：text_delivery_manifest.json, structured/pro062.json, p002, homogeneous model, p004–p005, Definition3.6 and Theorem3.13；source_and_local_equivalence_conditions_confirmed

可容许参数公式区间为空：原PDF第19页确实同时写λ=sqrt(γ/(2β))和3βλ²<α<βλ²+γ。按同一个γ代入，两端都为3γ/2，严格区间为空，不能由该参数化保证全部配置可容许。实际代码若使用更小λ、不同margin或舍入规则，须另行给出；这个矛盾不反驳选择合法参数时的条件定理。

核查定位：PDF physical page 19, Eq63 and parameterization, p005, Eq28, local_check/bounded_parameter_checks.json；printed_parameterization_conflict_confirmed

局部证书与sync口径：Algorithm1只接收角点梯度条件通过者；第4页理论对零场明确约定sign((Js)i)=si。原表1的MiP平均sync却为.999/.998/.994，表4又用未归一化整数且常小于节点数。尤其按文中K2000完全图±1权、零对角设定，每行1999项之和非零，该项不能单靠零场约定解释。需明确表格是否对应最终接收输出、认证容差和实际参数，不能将near-perfect称为严格一翻转证书。

核查定位：p004, zero-field convention, p005, Eq29, p006, Algorithm1, PDF physical page 7, Table1 and K2000 setup, p019–p020, Table4；certification_vs_reported_metric_gap_confirmed

外场归约只保持全局最优：附录A.1仅证明加辅助自旋后的全局最优可映回原外场问题，不能推出所有原单翻转局部最优一一对应。局部两自旋例E=−s1s2+(s1+s2)/2中，++能量0、单翻转后1，故是原局部最优；增广后仅翻辅助t即可降到−2。此例只否定不加限定的局部推广，不否定齐次定理。表2GOE又含非零对角，是否先去对角后认证未说明。

核查定位：p012, PropositionA.1, PDF physical page 8, Table2 caption, local_check/bounded_parameter_checks.json；field_and_diagonal_scope_qualified

主表性能与计时：原表1确认SK上MiP最佳/均值−16689.49/−16491.62，FEM−16814.75/−16593.16，MiP均不占优；K2000最佳34137优于FEM34038，但时间.24秒对.01秒。NPP最佳/均值.0015/.014优于所列D-WAVE .00957/1.191，具体D-WAVE后端未证。全部计时排除调参；附录又有10轮、每轮K200/T10、每维3–5点搜索，不能作为完整等预算墙钟优势。

核查定位：PDF physical page 7, Table1 and caption, PDF physical page 19, F.1；decisive_performance_and_cost_scope_confirmed

G-set概括与表格不符：原表3中G55误差1.22%，MiP10173低于D-WAVE10259，不支持全部1%内及G55超过D-WAVE的正文概括；G14则与D-WAVE同为3056。G22表3为13326、表4为13226，差异未解释，不替作者统一。

核查定位：PDF physical page 7, MAX-CUT paragraph, PDF physical page 8, Table3, p020, Table4 G22；result_summary_conflicts_confirmed

本地补充/限定：["原PDF确认参数区间为空，并给出两自旋例限定外场归约能保留的局部结构。", "区分理论零场约定与实际sync口径；对完全±1 K2000补充非零局部场判断，不直接推断未提供代码的具体故障。"]

核查局限：["未运行优化器或代码、未重做基准；参数与外场例仅精确代数核查。", "未完整形式验证全部局部极小值证明，未核读前作；L2暂评。", "未校正可疑基线单元格或猜测D-WAVE实际后端。", "Pro读全文文本，本地观察三页原PDF。"]


## pro063 · Instance-Specific Approximation Ratios for Correlation Clustering and Max-Cut

论文 OR_s3atUwqKHs；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_s3atUwqKHs_c481f60e7f00", "source_url": "https://api2.openreview.net/pdf?id=s3atUwqKHs\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "8c397457843f0ef224cefe0b23c9216f0563ac880eeb3b330411ba307281453f", "source_pdf_sha256": "c481f60e7f009b7f2a9fc65001a95811f7f629af97bcebba3431ad1eaf6fdeb8"}], "read_ranges": ["TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页1–19连续全文，包括正文§1–5、参考文献、附录A–C.5；未见页标缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供文本，未查看原PDF图像；图1、图2曲线不可见。", "双栏串读、公式上下标错位及表2–3部分行粘连；不恢复无法可靠对应的单元格。", "版本角色未核实，不根据会议页脚认定为最终出版版。"]}

问题：如何在大规模图上快速计算可验证的界，判断既有CC和Max-Cut启发式解离最优有多远？

方法：对CC枚举坏三角形，对Max-Cut枚举全部三角形。以分数triangle packing构造MINETCOVER下界LB：ρ=3的oracle按边权和排序，在预算内批量选取边不交三角形，累计MWU更新并按最大边负载归一化。CC-dis证书为ALG/LB；CC-ag和Max-Cut为ALG/(m−LB)。

作者主张：以批量MWU高效近似triangle packing，并推广到列稀疏packing。

论文证据：定理2陈述LB≥(OPT_ITP−2)/(1+ε)；定理9推广为整数基准(OPTint−ρ+1)/(1+ε)。

模型推断：新增在oracle及分析，不是新LP；上述定理并未保证普遍逼近分数LP最优。

定位：['TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页4–5算法1、定理2；页14–16附录B、定理9。']

作者主张：增加排序即可改善简单greedy下界。

论文证据：Cluster Editing七图、PIVOT取50次最佳解，平均证书由Veldt的2.326降至GreedyPacking的2.263。

模型推断：有价值的局部排序改进，未提高已有最坏情况3近似保证。

定位：['TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页17表5、页18§C.3。\n']

作者主张：大图上的实用启发式可以获得明显优于悲观最坏界的实例证书。

论文证据：七个CC图、九个无符号图的证书及运行时间，具体设置见key_results。

模型推断：支持这些实例上的质量界；不是改进最坏情况保证，也不是与SDP算法直接比较后的胜出。

定位：['TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页6–8§4、表1–3；页17§C.1。']

key_results：[{"setting": "无权triangle packing对偶，ρ=3", "baseline": "OPT_ITP是最大整数边不交三角形packing值，不是分数LP最优值", "metric_or_guarantee": "作者陈述的可行下界及复杂度", "reported_values_and_units": "LB≥(OPT_ITP−2)/(1+ε)；时间O(αmρlog²(n)/ε²)。", "information_and_compute": "枚举指定三角形集T；MWU空间O(m+|T|)，非仅O(m)。", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页5定理2、页19§C.5。\n"}, {"setting": "七个signed CC图，共用SCMLEVO解", "baseline": "GreedyPacking、MWU及其他下界方法", "metric_or_guarantee": "CC-dis上界/CC-ag下界，均无量纲", "reported_values_and_units": "GreedyPacking均值1.976/0.941；MWU ε=0.05均值1.992/0.941。wikiConflict有2,014,053条边，其MWU ε=0.05证书为1.146/0.992。", "information_and_compute": "每算法2小时超时；SCMLEVO内部运行预算未详述。", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页6表1、页7表2、页17§C.1。\n"}, {"setting": "九个无符号图上的Max-Cut及MINETCOVER", "baseline": "GreedyPacking证书、平凡界", "metric_or_guarantee": "实例近似比，无量纲", "reported_values_and_units": "MWU ε=0.05：Max-Cut平均0.891，GreedyPacking为0.874、平凡界为0.738；MINETCOVER平均1.179，GreedyPacking为1.263。", "information_and_compute": "Max-Cut取LOCALSEARCH、DUARTE、FESTA三者最好解，其中LOCALSEARCH取10次最佳；MINETCOVER解由SETCOVERGREEDY产生。", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页7§4、页8表3、页17§C.1。\n"}, {"setting": "flickr：2,316,948条边、107,987,357个三角形", "baseline": "Gurobi及MWU-SU ε=0.5在2小时截止时未完成", "metric_or_guarantee": "下界计算时间，非整个启发式求解流程时间", "reported_values_and_units": "MWU ε=0.1约6分钟；ε=0.5为23秒，均为正文报告而非读取图中曲线。", "information_and_compute": "两颗16核AMD EPYC 9124、512 GB RAM；实际线程配置未报告。", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页6表1及实验设置、页8Running Time。\n"}]

prior_work_candidates：[{"citation_as_printed": "Nick Fischer, Evangelos Kipouridis, Jonas Klausen, and Mikkel Thorup. 2025. A Faster Algorithm for Constrained Correlation Clustering. In STACS (LIPIcs, Vol. 327). 32:1–32:18.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "同一对偶LP、MWU", "claimed_difference": "前作逐三角形更新；本作整批更新，文中称渐近时间相同但实际更快。", "basis": "target_paper_only", "target_locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页5§3.1、页10参考文献、页18§C.4。", "prior_actually_read": false}, {"citation_as_printed": "Nate Veldt. 2022. Correlation Clustering via Strong Triadic Closure Labeling: Fast Approximation Algorithms and Practical Lower Bounds. In ICML (Proceedings of Machine Learning Research, Vol. 162). PMLR, 22060–22083.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "LP型下界及无排序greedy packing", "claimed_difference": "本作增加预排序，并以批量MWU计算下界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页5–6§3.2、页11参考文献、页17表5。", "prior_actually_read": false}, {"citation_as_printed": "Serge A. Plotkin, David B. Shmoys, and Éva Tardos. 1995. Fast Approximation Algorithms for Fractional Packing and Covering Problems. Math. Oper. Res. 20, 2 (1995), 257–301.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "bounded-width oracle与MWU框架", "claimed_difference": "构造适配packing的批量oracle及分析，无需猜测最优目标值。", "basis": "target_paper_only", "target_locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页5§3.1、页10参考文献、页12–16证明。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "批量oracle及列稀疏推广属于既有LP/MWU路线中的实质机制增量，不是路线首创；印刷伪码的正确性另有疑点。", "central_increment": "前作已有同一LP、近线性MWU和实例下界（本篇转述）；本作新增整批packing更新，以定理陈述和大图实验支持更实用的认证能力；尚待排除伪码与实际实现不一致。", "soundness_observation": "必须区分对偶可行性、整数基准保证和分数LP近优性。归一化可产生可行证书，但按可见伪码，非零初始化会破坏所述固定轮数保证，见minimal_check；不能将定理视为已验证。", "significance_observation": "价值在为既有启发式补上可扩展质量证书；工程负担主要是大量三角形的枚举、排序、权重和内存管理。", "main_open_question": "实验实现是否采用与证明一致的初始化及精度参数，从而使理论保证确实对应所测算法？"}

limitations：[{"text": "如何利用整数间隙获得超过当前LP对偶的界，仍是作者提出的开放问题。", "basis": "author_report", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页9结论。"}, {"text": "算法1将x初始化为全1，但A.2.2的权重递推未计入该初始负载；证明最后的ε/4重标定也未同步写入算法1。", "basis": "model_inference", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页4算法1、页13–14附录A.2.2。\n"}, {"text": "三角形结构决定界的强弱及成本；统一证书精度下的实现优化、线程和数值容差公平性仍需核查，不能只比较相同ε标签。", "basis": "model_inference", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页3§2、页5Early Termination、页18§C.4。"}, {"text": "正文称MWU ε=0.5使CC-dis平均证书小于2，但表2为2.061；本次数值依据表格，不沿用该句。", "basis": "model_inference", "locator": "TEXT_OR_s3atUwqKHs_c481f60e7f00：物理页7表2及比较段。"}]

minimal_check：{"question": "可见算法1的非零初值是否与定理2固定轮数保证兼容？", "control": "构造10000个共用一条边的三角形，再加4个独立三角形：m=20013、OPT_ITP=5。取ε=0.5、至多238轮，仅对照x初值为1和0。", "observable_outcome": "模型计数推导、未运行：原伪码初始最大边负载至少10000，每轮至多增加15的目标值，故返回值≤(10004+238×15)/10000=1.3574；定理声称的下界则为(5−2)/1.5=2。", "resources": "构造图与两种初始化的CPU实现；无需训练或精确优化求解器，实际耗时和内存未测。", "failure_or_stop_condition": "若原PDF确认相同伪码，该例即否定其字面固定轮数保证；若源码采用不同初始化，不把此反例直接外推到实验实现。"}

missing_fields：["原PDF图像、图1–2曲线及部分公式的可靠排版。", "前作原文及所选三篇前作的DOI/arXiv标识。", "代码实际初始化、停止规则、线程、数值容差、部分启发式预算及绝对峰值内存。", "最终出版版本身份、独立证明核验和实验复现结果。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

快速实例证书有实际用途；先核实正确初始化、内部ε与停止规则，并验证实际对偶可行性，再依赖其质量和时间保证。

身份、问题与证书方向：19页官方当前附件与全文返回绑定一致。目标是给已有启发式解计算实例质量证书，非提出新的Max-Cut解法。任何非负三角形packing经最大边负载归一化即满足对偶容量约束，LB用于CC-dis的ALG/LB上界，以及CC-ag/Max-Cut的ALG/(m−LB)下界；这些方向不能混换，也不是最坏情况近似比改进。

核查定位：text_delivery_manifest.json, structured/pro063.json, p003, Lemma1 and instance-specific ratios, PDF physical page 4, dual LP and normalization；source_and_certificate_scope_confirmed

批量oracle的保证基准：ρ=3的oracle每轮选边不交三角形并赋值ρ，目标保证相对整数packing最优OPT_ITP，Theorem2为(OPT_ITP−2)/(1+ε)。它不直接保证以1+ε逼近分数LP最优。列稀疏推广所用矩阵为二元、单位目标权重；不同表述不能等同为任意packing LP近优算法。

核查定位：PDF physical page 4, Algorithm1, p005, Theorem2 and Lemmas3–4, p014, generalized LP setup；oracle_and_integer_benchmark_confirmed

非零初始化的固定轮数反例：原PDF第4页明确x_t初始化为1、边权为1，循环2ρ ln(m)/ε²轮。取10000个共用一边的book三角形加4个独立三角形，m=20013、|T|=10004、OPT_ITP=5。ε=.5至多238轮，每轮目标最多增加15，而最大边负载始终至少10000，故最终目标<=1.3574；定理下界却为2。此为计数反例，未实际构建或运行大图。归一化仍给可行LB，错误在所印固定轮数质量保证，不自动否定所有实验证书。

核查定位：PDF physical page 4, initialization and iteration count, p005, Theorem2, local_check/book_graph_counting_check.json；literal_fixed_round_quality_guarantee_counterexample_confirmed

证明和实际停止规则需对齐：A.2.2的边权递推从新增oracle负载开始，未计x=1初始负载；第14页还将ε替换为ε/4以取得声明倍率，伪码未同步。正文实际采用可行原始/对偶gap提前停止，未说明是否存在与伪码不同的初始化或额外轮数。需要实际代码协议，不能把同ε标签自动当成相同证书精度。

核查定位：p013–p014, proof of Lemma4, p005, Early Termination；proof_implementation_alignment_gap_confirmed

表格证书与正文概括：原表2确认CC-dis平均GreedyPacking1.976、MWU ε=.05为1.992，均优于ε=.5的2.061；正文称ε=.5平均小于2不符。CC-ag二者约.941。原表3Max-Cut平均MWU ε=.05为.891、Greedy .874、平凡界.738；这是九个实例中对三种启发式最好解的证书均值，非普遍超过SDP或新最坏比保证。

核查定位：PDF physical page 7, Table2 and comparison paragraph, PDF physical page 8, Table3, p017, C.1 heuristics；decisive_table_values_and_averaging_scope_confirmed

规模和计时口径：flickr为2316948边、107987357三角形，正文报MWU ε=.1约6分钟、ε=.5为23秒；服务器两颗16核EPYC9124及512GB RAM。时间只计下界计算，非完整启发式求解；空间为O(m+|T|)，近线性边数时间还依赖低arboricity。第19页内存比较仅给相对倍数，不能把机器容量当实测峰值。

核查定位：p006, Table1 and experimental setup, PDF physical page 8, Running Time, p019, C.5；runtime_and_memory_scope_confirmed

本地补充/限定：["原PDF确认x=1及自然对数轮数，计数核查得到1.3574<2；明确只是所印固定轮数质量保证失效，返回对偶可行性可独立成立。", "关键实验均按原表读取，不沿用ε=.5平均小于2的正文句。"]

核查局限：["未运行图算法、读作者源码或核读前作；反例仅组合计数，L2暂评。", "未全面形式验证oracle及列稀疏推广证明，未重建实验中的实际数值容差。", "不从图拟合线猜测逐点时间或峰值内存。", "Pro读全部文本，本地观察三页原PDF。"]


## pro064 · Tight Stability Bounds for Robust Distributed Learning: Byzantine Failures Hurt Generalization More than Data Poisoning

论文 OR_lWyXszYR58；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_lWyXszYR58_d7edc4836de7", "source_url": "https://api2.openreview.net/pdf?id=lWyXszYR58\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_lWyXszYR58_d7edc4836de7：物理页1–41全部提供文本；正文1–9页，参考文献9–11页，附录A–I为12–41页。连续页标完整，题名与清单一致。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；Figure 1曲线和示意图不可见，不能由坐标刻度推断结果。", "部分公式的根号、分式、量词及双栏顺序失真；关键推导疑点仍需原PDF核对。", "版本角色未核实；未提供前作全文。"]}

问题：当部分工作节点恶意失效时，任意篡改通信与预先固定的数据投毒，是否对有限训练集上的泛化造成不同阶的损害？

方法：服务器以鲁棒聚合梯度执行GD/SGD。SMEA选择协方差最大特征值最小的n−f个梯度并求均值。比较仅替换一个诚实样本的两条轨迹：Byzantine情形借助诚实均值中间项；投毒情形利用两次入选集合的交集及梯度正则性。再构造子集切换下界和双点分布连接泛化。

作者主张：给出鲁棒分布式学习的紧稳定性分析，证明数据投毒的附加不稳定性小于Byzantine失效。

论文证据：Theorems 3.1–3.4给出上下界；Appendix C.3补充小f弱下界，E/G/H补充非凸、异质性/方差细化和高概率结果。

模型推断：增量是对已有SMEA的实质性机制与保证分析，不是提出新聚合算法；投毒梯度仍受损失正则性约束是关键区别。

定位：['TEXT_OR_lWyXszYR58_d7edc4836de7，p4 Theorems 3.1–3.2、p5–6 Theorems 3.3–3.4。\n \n']

作者主张：首次建立两种威胁模型之间的根本泛化差距。

论文证据：Lemma 4.1在m=1的特殊分布上连接稳定性与泛化；Theorem 4.2据此报告SMEA的分离比，并给出小规模数值说明。

模型推断：属于特定算法与最坏情形分布上的存在性分离，不是所有分布、聚合器或测试准确率上的普遍排序。

定位：['TEXT_OR_lWyXszYR58_d7edc4836de7，p6–7 Lemma 4.1/Theorem 4.2、p34–35 Appendix F.1。\n']

key_results：[{"setting": "C-Lipschitz、L-smooth凸损失，γ≤1/L，T步；Byzantine上界适用于任意(f,κ)-robust聚合，所列下界及投毒紧界针对SMEA。", "baseline": "无恶意节点时的均值聚合稳定性界2γC²T/(nm)。", "metric_or_guarantee": "uniform stability ε，单位为损失差；以下均为作者理论结果。", "reported_values_and_units": "Byzantine：ε≤2γC²T[√κ+1/((n−f)m)]；n/3≤f<n/2时，ε≥Ω(γC²T[√(f/(n−2f))+1+1/((n−f)m)])。数据投毒：ε=Θ(γC²T[f/(n−f)+1/((n−f)m)])，下界对应GD或projected-SGD。", "information_and_compute": "GD每步使用本地全量梯度，SGD每节点抽一个样本；随机算法的上述下界要求T=Ω(m)。", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p4–6 Theorems 3.1–3.4、p16–19 Appendix C.3、p28–32 Appendix D.3。"}, {"setting": "另加μ-强凸，γ≤1/L；有界参数域及必要投影。", "baseline": "两种威胁模型及SMEA投毒上下界。", "metric_or_guarantee": "不随T增长的稳定性上界。", "reported_values_and_units": "Byzantine：ε≤(2C²/μ)[√κ+1/((n−f)m)]。投毒：ε≤(2C²/μ)[f/(n−2f)+1/((n−2f)m)]；GD下界为Ω((C²/μ)[f/(n−f)+1/((n−f)m)])。", "information_and_compute": "投毒GD下界要求T≥ln(1−c)/ln(1−γμ)，0<c<1。", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p4–6 式(4)、(7)、(11)，p13 Definition B.1，p26–28 Theorem D.5。"}, {"setting": "m=1、SMEA、n/3≤f<n/2，构造性凸线性损失与诚实节点分布。", "baseline": "同一理论设置下任意数据投毒攻击。", "metric_or_guarantee": "期望泛化差E[R_H(A(S))−R̂_H(A(S))]的威胁模型分离。", "reported_values_and_units": "作者报告E_gen^byz/E_gen^pois∈Ω((n−f)/√(f(n−2f)))；该因子接近失效阈值f=n/2时发散。", "information_and_compute": "m=1时GD与SGD的本地梯度抽样无差别；不涉及真实数据集训练。", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p7 Theorem 4.2、p35 式(28)–(29)。"}, {"setting": "一维线性损失，GD+SMEA；C=γ=1，T=5，n=15，m=1，f=1至7。", "baseline": "作者称最坏数据投毒、投毒理论上界及Theorem 3.2的Byzantine下界。", "metric_or_guarantee": "泛化差；作者称投毒曲线贴近上界，定制Byzantine攻击更差，包括f<n/3。", "reported_values_and_units": null, "information_and_compute": "攻击数值搜索可入选的极端更新，Algorithm 3使用边界偏移ε=10⁻³；搜索次数、硬件及耗时未报告。", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p7–8 Figure 1、p35–36 Appendix F.2。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Allouah, Y., Guerraoui, R., Gupta, N., Pinot, R., and Stephan, J. On the privacy-robustness-utility trilemma in distributed learning. In ICML, 2023b.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "SMEA及其鲁棒性保证。", "claimed_difference": "从既有优化保证转向稳定性与泛化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p3 Definition 2.3、p9 References。", "prior_actually_read": false}, {"citation_as_printed": "Farhadkhani, S., Guerraoui, R., Gupta, N., and Pinot, R. On the relevance of byzantine robust optimization against data poisoning. arXiv preprint arXiv:2405.00491, 2024b.", "identifier_if_present": "arXiv:2405.00491", "relation_candidate": "理论扩展", "shared_component": "两类威胁模型及鲁棒优化误差分析。", "claimed_difference": "本篇强调预先固定训练集的泛化，而非流式新样本下的风险结论；并非直接推翻相同设置的结论。", "basis": "target_paper_only", "target_locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p8 §5、p10 References、p38 Appendix H。", "prior_actually_read": false}, {"citation_as_printed": "Ye, H. and Ling, Q. Generalization error matters in decentralized learning under byzantine attacks. IEEE Transactions on Signal Processing, 73:843–857, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "Byzantine学习的uniform stability分析。", "claimed_difference": "本篇采用协方差型鲁棒性及中心服务器，并比较数据投毒；称前作直径型定义依赖较差。", "basis": "target_paper_only", "target_locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p8–9 §5、p11 References。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是已有鲁棒算法的新稳定性刻画与条件性泛化分离，超过局部性能改进；不构成新学习路线，历史首创未外核。", "central_increment": "前作已给出SMEA及优化保证（本篇转述）；本作在有限、异质训练集条件下新增威胁模型敏感的稳定性界及分离构造。", "soundness_observation": "未逐项验证全部证明。可见文本中式(28)是有符号的C·E[θ_T^(−C)−θ_T^(0)]/[4(n−f)]，而随后sup_z表达取该输出差的绝对值；Lemma 4.1声称适用于任意A，需补方向条件或核对原式。这不自动否定满足方向条件的SMEA构造。\n", "significance_observation": "解释优化鲁棒性为何不充分刻画泛化；价值主要在理论，未展示可扩展新算法或实际训练收益。", "main_open_question": "核实或修正Lemma 4.1的符号条件后，Theorem 4.2的具体SMEA构造是否完整满足该条件？"}

limitations：[{"text": "f<n/3已有Ω(γC²T·f/(n−2f))弱下界，但与投毒界仅差常数，紧性及更强阶分离未解决。", "basis": "author_report", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p16–19 Appendix C.3、p39 Appendix I。"}, {"text": "强凸投毒上下界分别含n−2f和n−f，接近半数失效时并非一致紧；非凸附录比较的是上界，不能单独证明严格分离。", "basis": "model_inference", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p5–6 式(7)/(11)、p32–34 Appendix E。"}, {"text": "下界针对SMEA；其他聚合器、动量、多步本地更新及定向攻击留待扩展。ZKP仅为理论动机，未实现。", "basis": "author_report", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p39–41 Appendix I。"}, {"text": "泛化分离依赖m=1及特制异质分布；数值攻击按f调整恶意节点身份并定制更新，不足以建立现实任务的普遍收益。", "basis": "model_inference", "locator": "TEXT_OR_lWyXszYR58_d7edc4836de7，p35–36 Appendix F。"}]

minimal_check：{"question": "Lemma 4.1的符号处理是否足以支持中心分离定理？", "control": "固定F.1的双点分布，分别考虑输出差期望为正与负，直接比较式(28)和sup_z表达。", "observable_outcome": "确认是否需改为绝对泛化差或附加方向条件，再检查Theorem 4.2攻击是否满足修正条件。", "resources": "p34–35原PDF或LaTeX及代数核算，无需训练。", "failure_or_stop_condition": "若具体分离构造无法满足修正条件，暂停接受Theorem 4.2；若仅引理表述过宽，则保留修正后的条件性结论。"}

missing_fields：["Figure 1逐点实验数值不可读，故对应reported_values_and_units为null。", "数值搜索范围、次数、运行硬件、耗时及可执行实现未提供。", "最终出版版本身份、前作覆盖关系及公式排版疑点未独立核实。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

威胁模型如何改变泛化而非仅优化误差是可继续研究的明确增量；按有限样本、SMEA、参数区间理解结果，并校正随机算法引理表述。

身份、版本与威胁模型：题名、41页文本、结构化材料哈希与单一当前附件绑定；没有camera-ready确认。中心贡献是既有SMEA在预先固定的有限异质数据上的稳定性/泛化分析。Byzantine可观察通信后任意发送，投毒者预先固定数据并遵循梯度规则；这与流式采样下的既有结果不是同一假设。

核查定位：p002, setting and threat models, PDF physical page3, Definitions2.2–2.4, p008, Related Work；identity_and_increment_scope_confirmed

主界及紧性边界：凸情形Byzantine一般上界含sqrt(kappa)，SMEA下界需要n/3≤f<n/2；投毒附加项f/(n−f)。强凸投毒上界分母n−2f而下界n−f，不能称接近半数失效时一致紧。强凸Lipschitz条件依有界域/投影。泛化分离是m=1构造性存在结论，固定f/n且离1/2有常数距离时分离因子是常数量级。

核查定位：p004–p007, Theorems3.1–4.2, p013, DefinitionB.1；theorem_conditions_and_nonuniform_tightness_confirmed

撤回Pro的有符号等式质疑：原PDF第6页式12及第35页式28后的等式左边均有绝对值。式28本身先计算有符号差，再取绝对值，故不能以负输出差作为Pro所述反例。原始Pro保留，派生解释明确纠正。

核查定位：PDF physical page6, Lemma4.1, PDF physical page35, Eq28 and following equality, local_check/page_035_equation.png；pro_formula_suspicion_retracted_after_visual_check

一般随机算法仍需区分期望与绝对值顺序：第3页Definition2.4采用sup|E lossdiff|；Lemma4.1及第35页所印右边却为sup E|lossdiff|。在同一随机种子R=±1等概率下取A(S^−C)=R、A(S^0)=0，线性损失zθ、m=1枢纽分布保持不变，左边|Egen|=0，所印右边C/[4(n−f)]>0。此为任意随机A表述的简单代数检查；改用sup|E lossdiff|即可与式28一致。Theorem4.2指定GD和m=1，不受这个随机化反例直接否定。

核查定位：PDF physical page3, Definition2.4, PDF physical page6, Eq12, PDF physical page35, following Eq28；random_algorithm_expectation_order_gap_identified_with_narrow_scope

数值证据的实际规模：原Figure1确认特制Byzantine曲线高于投毒，投毒靠近其上界；未读取逐点精确数值。实验仅一维线性损失，C=gamma=1、T=5、n=15、m=1、f=1…7，非真实数据训练。小f曲线不代替主下界对n/3的限制。D.4中SMEA子集切换给出确定性输出分离，未全面验证所有组合子集论证。

核查定位：PDF physical page8, Figure1, p023–p024, D.2.1, p035–p036, F.2；visual_direction_and_experiment_scope_confirmed

本地补充/限定：["Lemma4.1左边原PDF带绝对值；撤回Pro关于有符号等式及负输出差的疑点。", "一般随机算法的真实问题是sup E|diff|与sup|E diff|顺序；不扩展为确定性GD分离定理失效。"]

核查局限：["未全面核验SMEA各下界构造、所有定理证明或前作全文。", "未复现算法或攻击搜索，图仅验证可见趋势。", "Pro读取41页文本，本地只核查所列页和图；仍为有限模型复核，L2暂评。"]


## pro065 · Best-of-Both-Worlds for Heavy-Tailed Markov Decision Processes

论文 OR_j6gXeiPJ3z；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_j6gXeiPJ3z_434bda96e400", "source_url": "https://api2.openreview.net/pdf?id=j6gXeiPJ3z\n", "version_role": "current_attachment_unverified_role", "version_note": "当前附件的版本角色未经核验，不认定为最终出版版。"}], "read_ranges": [{"source_id": "TEXT_OR_j6gXeiPJ3z_434bda96e400", "physical_pages": "1–48，连续页标齐全", "sections": "正文§1–6；参考文献pp.9–11；附录A pp.12–13、B pp.14–31、C pp.32–48。"}], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文提取文本，未查看PDF页图；双栏混排及部分分式、上下标、绝对值符号失真，复杂公式的排版细节不能完全核验。", "未提供前作全文、其他版本或实验材料；本轮未搜索、复现实验或逐条独立证明全部定理。"]}

问题：有限时域表格MDP中，仅观察轨迹上的逐步重尾损失，能否在不知道环境类型时，同时取得对抗环境的最坏情形遗憾保证和正间隙随机环境的对数级遗憾？

方法：输入已知尾参数α、σ，以占用测度FTRL输出策略π_t。已知P时，按τ_t=Cσt^(1/α)x_t^(1/α)跳过极端损失，作重要性加权并减去截断偏差补偿。未知P时在倍增epoch内使用经验模型、UOB重要性分母及HσB_i转移补偿，并重置FTRL。

作者主张：HT-FTRL-OM首次在已知转移重尾MDP中实现BoBW，且不要求损失非负。

论文证据：给出定理4.1/B.1及附录B推导；Lemma B.2–B.3控制shifted-loss幅度与二阶矩，B.8以次优动作质量控制状态占用差异正部。

模型推断：实质增量是将重尾bandit与有界损失MDP的BoBW技术接通，处理占用约束和跨层依赖，而非提出全新的FTRL范式。

定位：['TEXT_OR_j6gXeiPJ3z_434bda96e400:p14 Theorem B.1；pp.17–21 Lemmas B.2–B.3；p25 Lemma B.8。\n']

作者主张：HT-FTRL-UOB在未知转移下实现对抗次线性、随机log²T级遗憾。

论文证据：算法2、定理5.2/C.1及附录C；将转移误差、FTRL估计误差、截断误差和pessimism误差分开，C.9控制UOB引入的额外偏差。

模型推断：新增保证超出简单替换损失估计器，但适用范围受截断非负性限制，经验占用到真实占用的自约束转换是关键证明环节。

定位：['TEXT_OR_j6gXeiPJ3z_434bda96e400:p6 Assumption 5.1；p32 Theorem C.1；pp.39–40 Lemma C.9；pp.47–48 Lemma C.16。\n']

key_results：[{"setting": "已知转移；对抗损失分布可依赖过去历史。随机特例取C_sb=0。记ω_r=Σ_{(s,a):a≠π*(s)}Δ(s,a)^(-1/(r−1))。", "baseline": "本文引用的重尾MAB下界及有界损失BoBW-MDP保证；不是实验基线。", "metric_or_guarantee": "相对固定确定性策略的期望累积遗憾；以下固定α并省略poly(H,S,A)因子。", "reported_values_and_units": "对抗：O(σ[T^(1/α)+log T])；随机：O([σ^(α/(α−1))ω_α+σ]log T)。一般自约束界另含O(C_sb^(1/α)W^((α−1)/α))，W=σ^(α/(α−1))ω_α log T。", "information_and_compute": "T个H步在线回合，每回合求解占用多面体上的凸优化；作者称多项式时间，未报告实际运行资源。", "locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p14 Theorem B.1，Eqs.(11)、(15)；pp.28–31证明。\n"}, {"setting": "未知固定转移且满足Assumption 5.1；随机界取C_sb=0，ι=HSAT/δ，ω_r同上。", "baseline": "本文转述Zhuang & Sui (2021)的重尾MDP下界与Jin et al. (2021)的有界损失BoBW结果。", "metric_or_guarantee": "期望累积遗憾；按附录C.1概括，省略poly(H,S,A)及固定α相关因子。", "reported_values_and_units": "对抗：Õ(σ[T^(1/α)+√T])；随机：O((σ+σ²)log²ι+σ²[ω_2+Δ_min^(-1)]logι+σ^(α/(α−1))ω_α log²T)。保留附录额外的σ²log²ι项，不只摘录正文的主导项简式。", "information_and_compute": "逐步观察损失与转移，每回合求解FTRL及UOB；O(SA log T)个倍增epoch。无数据集、硬件或墙钟时间报告。", "locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p32 Theorem C.1；pp.43–46证明；p7 §5.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Jin, T., Huang, L., and Luo, H. The best of both worlds: stochastic and adversarial episodic mdps with unknown transition. Advances in Neural Information Processing Systems, 34:20491–20502, 2021.", "identifier_if_present": null, "relation_candidate": "方法继承、理论扩展", "shared_component": "占用FTRL、loss shifting、转移误差与自约束分析", "claimed_difference": "从有界损失扩展到重尾反馈，加入截断偏差控制。", "basis": "target_paper_only", "target_locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p10 References；pp.12–13 A.2；附录B、C。\n", "prior_actually_read": false}, {"citation_as_printed": "Huang, J., Dai, Y., and Huang, L. Adaptive Best-of-Both-Worlds Algorithm for Heavy-Tailed Multi-Armed Bandits. In Proceedings of the 39th International Conference on Machine Learning, pp. 9173–9200. PMLR, June 2022.", "identifier_if_present": null, "relation_candidate": "组件复用、理论扩展", "shared_component": "重尾损失跳过、Tsallis正则与BoBW分析", "claimed_difference": "从单步bandit扩展到受转移耦合的多步MDP。", "basis": "target_paper_only", "target_locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p10 References；p5 §4.2；p13 A.3。\n", "prior_actually_read": false}, {"citation_as_printed": "Zhuang, V. and Sui, Y. No-Regret Reinforcement Learning with Heavy-Tailed Rewards. In Proceedings of The 24th International Conference on Artificial Intelligence and Statistics, pp. 3385–3393. PMLR, March 2021.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "表格重尾MDP、矩条件及最坏情形遗憾", "claimed_difference": "新增环境自适应与对数级随机实例保证，不仅处理随机环境的最坏情形界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p11 References；p12 A.1.2。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是重尾MDP中新的联合遗憾保证，有针对占用约束的非平凡分析；属于既有路线的实质扩展，而非仅换组件或路线级范式创造。", "central_increment": "前作已有重尾bandit BoBW与有界损失MDP BoBW（均为本文转述）；本作在矩条件及未知转移附加符号条件下接通二者，以B.1/C.1支持。", "soundness_observation": "证明链已提供，但C.16式(72)将前文H³σ级余项写入H⁴σ²级余项，对任意σ>0的吸收理由需补核；这是证明完整性疑点，尚不能据此判定主定理错误。\n", "significance_observation": "理论价值在于环境自适应和随机情形T依赖改善；最优性仅针对指定参数、允许状态动作时域多项式损失，实际工程收益未展示。", "main_open_question": "未知转移自约束证明中，Lemma C.16的经验—真实占用转换及余项吸收，能否覆盖全部声明的σ>0范围？"}

limitations：[{"text": "作者明确承认H、S、A因子待收紧，未知转移的截断非负条件待放宽，尚未扩展到函数逼近。", "basis": "author_report", "locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p9 §6。\n"}, {"text": "不是参数自由算法；损失可对抗变化但转移固定。随机对数界若存在非参考零间隙动作会变为空泛界。", "basis": "model_inference", "locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:p3 §3.1；p5、p7 Algorithms 1–2；p14、p32定理中的逆间隙项。"}, {"text": "全文为理论结果，未见实验或实际算力评测；不能推出有限样本性能优势。前作未核读，无法独立确认首次性与完整可比性。", "basis": "model_inference", "locator": "TEXT_OR_j6gXeiPJ3z_434bda96e400:pp.1–48。"}]

minimal_check：{"question": "Lemma C.16式(71)至(72)的σ依赖是否完整？", "control": "保留吸收前的H³σ余项，与式(72)及最终C.1逐项比较；同步缩放损失、σ和间隙，覆盖Hσ<1。", "observable_outcome": "给出适用于全部声明参数的吸收不等式，或定位必须保留的余项、附加条件及其对最终界的影响。", "resources": "需原PDF或LaTeX确认公式，并核读被引用的占用残差引理；以符号推导为主，计算预算未报告。", "failure_or_stop_condition": "若吸收仅在未声明参数下界下成立，且其他已列项不能覆盖余项，则该证明环节未通过；不自动否定另一设置下的结果。"}

missing_fields：["PDF页图与无损公式排版", "实验数据、实现、硬件、运行时间及实际优化成本", "三篇候选前作全文及参考条目未印出的DOI/arXiv标识", "版本角色的独立核验"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得沿未知转移的经验占用转换继续读，但须保留完整sigma/H/S/A依赖并修复或解释式72余项。

身份与中心增量：首行完整题名与48页当前附件匹配。新保证接通重尾bandit和占用FTRL的BoBW-MDP分析；非新的FTRL范式，也非已演示工程加速。复用Tsallis正则、loss shifting、UOB和倍增epoch；中心新分析处理跨状态损失与截断偏差。

核查定位：p001 title, p004–p007, Algorithms1–2 and technical insights；identity_and_mechanism_confirmed

核心适用条件和遗憾量：固定分层表格转移P，逐轨迹损失反馈，alpha∈(1,2]且sigma>0均为输入；对抗可依历史选损失分布，非对抗转移。已知P不限制损失符号；未知P要求所有M>0下E[loss 1{|loss|≤M}]≥0，正均值本身不足保证此条件。随机对数界依正的非参考动作间隙；零间隙使所列逆间隙界空泛。

核查定位：p003–p004, setting and Definition3.1, PDF physical page6, Assumption5.1, p005/p007, inputs；assumptions_and_observation_budget_confirmed

决定性定理的阶和隐藏成本：B.1已知P给sigma T^(1/alpha)对抗阶及sigma^(alpha/(alpha−1))乘逆间隙和logT的随机阶，并有sigma logT余项。原C.1未知P随机界确含H^4 sigma² S³ A² log²iota，主项还含H^6 sigma² S²逆间隙logiota，不能只报log²T而隐藏状态/动作/时域因子。最优性表述仅限所比较参数并允许poly(H,S,A)损失。

核查定位：p014, TheoremB.1, PDF physical page32, TheoremC.1, p009, stated limitations；formal_bound_and_comparison_scope_confirmed

C.16余项缩放的有限核查：原PDF48页先得H³ sigma S³ A² log²iota，乘gamma′≤1后式72写成H^4 sigma² S³ A² log²iota。若仅用gamma′≤1和S≥1，这项逐项吸收不对任意sigma>0成立：固定H、sigma趋0，前后比1/(H sigma)无界。需要保留线性sigma余项或说明其他逆间隙项如何吸收；尚未证明最终C.1无法由其他项覆盖。补回此余项不改变固定参数下的log²T阶。第48页占用差确有绝对值，未据提取文本误判符号。

核查定位：PDF physical page48, before Eq72 and Eq72, p047, normalized gap assumption, PDF physical page32, total theorem terms；isolated_absorption_gap_confirmed_total_bound_not_refuted

实际证据类型：正文结论和算法给理论及多项式时间求解说明，没有有限样本实验和实测硬件时间。每回合凸优化、未知P的UOB计算与epoch重置是成本；不可由遗憾阶推出现实训练速度。

核查定位：p004, convex optimization, p007, Comp-UOB, p009, Conclusion；theory_only_cost_scope_confirmed

本地补充/限定：["将C.16疑点限定为所示逐项吸收缺依据；未声称整个最终界或已知转移结果错误。", "条件是所有阈值的截断非负性，不能用正均值替代。"]

核查局限：["未核读被引用占用残差前作，未完成全部48页证明独立验算。", "没有运行MDP、训练或作者源码。", "第1页仅读题名及开头；Pro读完整文本，本地读所列定理/算法段落与三页原PDF。", "当前附件版本角色未确认，L2为模型暂评。"]


## pro066 · FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates

论文 OR_1KRpajnd6u；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_1KRpajnd6u_57319dd40a00", "source_url": "https://api2.openreview.net/pdf?id=1KRpajnd6u\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "1c0c9d963bc7b55205869902753af9922ca13d3442a179bb4cf48ea65e784364", "source_pdf_sha256": "57319dd40a00d91cdfe5a7921bb1c1c3f536bdc47530638fc7e90ca69e160481"}], "read_ranges": ["TEXT_OR_1KRpajnd6u_57319dd40a00：物理页1–30，页标连续；包括正文、参考文献、附录A–E，以及全部已提供图题和坐标文字。题名与清单一致。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–17的曲线、场图及示意图不可见，不能独立核查视觉结论。", "双栏文字存在交错，公式上下标和表格排版可能失真；主要更新公式及表1–9数值基本可辨。", "前作全文、源码和实验产物未提供；未联网、未复现，以下数值均为作者报告。"]}

问题：如何学习守恒PDE的自回归演化，在较大预测步长下兼顾离散守恒、物理取值边界与预测精度？

方法：输入当前场u及可选外场ξ，预测邻格间整个模型时间步的累计输运F，以u'=u−ΣFout+ΣFin更新。L/U分别将可转出余量/可接收容量乘以sigmoid比例和softmax方向分配；D平均两分支状态增量，并用DCL惩罚增量不一致。以状态轨迹MSE监督，通常加入停止梯度的pushforward训练。

作者主张：以可插拔容量约束输运头实现结构性守恒、L/U单边保界及D头近零双边越界。

论文证据：命题1–3给出守恒与单侧边界论证；表3、4、7、9提供跨骨干结果及头部消融。DCL降低部分越界率，但牺牲点预测精度。

模型推断：中心增量是可复用的受限输运参数化，而非守恒抵消本身。L/U可支持非严格边界不变性；D不具双边硬保证。

定位：['TEXT_OR_1KRpajnd6u_57319dd40a00：p4–5，§3.3–3.5、表1；p12–13，附录A。\n', 'TEXT_OR_1KRpajnd6u_57319dd40a00：p7–8，表3–4；p16–17，表7、9。']

作者主张：累计输运无需显式积分，消除CFL约束；扩大邻域支持大步长，ghost cells扩展到非周期边界。

论文证据：表5报告50Δt下优于所实现的FluxGNN；表6报告相场模型最高17.3×推理加速。开放域满足内部质量变化等于净边界输运。

模型推断：支持特定设置的大步长可用性，不构成任意步长稳定或准确性定理；开放域不是内部总质量恒定。

定位：['TEXT_OR_1KRpajnd6u_57319dd40a00：p3，Remark 1；p5，§3.6；p8–9，表5–6；p18–20，附录D.3、E。']

key_results：[{"setting": "周期1D对流扩散，表2标T=1。", "baseline": "FluxNet-N、FluxNet-P", "metric_or_guarantee": "rollout MAE、Econs", "reported_values_and_units": "L/P/N的MAE分别为(1.36±0.41)/(1.51±0.45)/(16.73±24.22)×10^-3；L的Econs=2.46×10^-8。", "information_and_compute": "32格；训练/验证/测试100/10/10条；300 epochs，单步训练，5个训练种子。", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p6表2；p13–14附录B。\n"}, {"setting": "周期2D浅水，2×时域外推；附录2.4→4.8，表3标T=2。", "baseline": "同ResNet骨干的Box+Mass Projection", "metric_or_guarantee": "水深MAE、越界率、各场Econs", "reported_values_and_units": "LAP水深MAE=(1.75±0.11)×10^-3，对照(9.41±4.81)×10^-3；两者水深越界率均0%。LAP的h/mx/my守恒误差为3.1×10^-8/6.1×10^-6/3.8×10^-6。", "information_and_compute": "64²格；50/20/50条；300 epochs，pushforward长度5，5个种子。", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p7表3；p15附录C.1–2。\n"}, {"setting": "周期LWR交通流，训练至4.0、测试至8.0；表4、9标T=2。", "baseline": "ResNet-AR、D头去除DCL", "metric_or_guarantee": "密度MAE、下/上界越界率", "reported_values_and_units": "ResNet-AR、D、去DCL的MAE分别为(8.09±0.91)/(2.79±0.79)/(1.52±0.14)×10^-3。D的下/上越界率0.59%/0.01%，去DCL为2.26%/0.41%。", "information_and_compute": "256格；100/50/100条；R=5，γ=1，300 epochs，pushforward长度5，5个种子。", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p8表4；p16–17附录D.2、表9。\n \n"}, {"setting": "Dirichlet交通流，测试至8.0；Δt=0.016。", "baseline": "FluxGNN、FluxGNN-D", "metric_or_guarantee": "密度MAE", "reported_values_and_units": "10Δt时FluxNet-D/FluxGNN/FluxGNN-D为(11.7±0.23)/(3.54±1.08)/(2.73±0.95)×10^-4；50Δt时FluxNet-D/FluxGNN为(50.1±4.85)/(1150±87.9)×10^-4。", "information_and_compute": "256格；50/50/50条；FluxNet半径5→7；各方法300 epochs、5种子，称参数规模近似匹配，但未列具体数量。", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p8表5；p17–18附录D.3。\n"}, {"setting": "Cahn–Hilliard单轨迹学习，2×时域外推；准确率对应E.2的128²网格，计时另在1024²网格。", "baseline": "不同步长FluxNet-D；同GPU相场求解器", "metric_or_guarantee": "浓度MAE、推理加速比", "reported_values_and_units": "10/100/1000Δt的MAE为2.76/2.16/8.39×10^-2；完成50000Δt的加速比分别0.55×/3.8×/17.3×。", "information_and_compute": "单条轨迹训练100 epochs，每种配置仅一次训练；R=1/2/4且骨干同时变化。计时使用同一NVIDIA A800；绝对耗时图不可读。", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p9表6；p19–20附录E.2–3、E.7；p30图17图题。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Horie, M. and Mitsume, N. Graph neural PDE solvers with conservation and similarity-equivariance. In Proceedings of the International Conference on Machine Learning, pp. 18785–18814. PMLR, 2024.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "守恒通量更新；其骨干用于FluxGNN-D。", "claimed_difference": "由瞬时通量率改为容量受限累计输运。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p2，§2.2；p10参考文献；p18，D.3.4。", "prior_actually_read": false}, {"citation_as_printed": "Praditia, T., Karlbauer, M., Otte, S., Oladyshkin, S., Butz, M. V., and Nowak, W. Finite volume neural network: Modeling subsurface contaminant transport. arXiv preprint arXiv:2104.06010, 2021.", "identifier_if_present": "arXiv:2104.06010", "relation_candidate": "背景引用", "shared_component": "有限体积启发的可学习单元界面通量。", "claimed_difference": "本文强调累计输运、可扩邻域及容量限制；直接方法继承尚未核实。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p2–3，§2.2；p11参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Lan, Z., Zeng, Q., Ma, W., Liang, X., Li, Y., Chen, Y., Chen, Y., Hu, X., Li, J., Wang, L., et al. Scalable data-driven modeling of microstructure evolution by learning local dependency and spatiotemporal translation invariance rules in phase field simulation. arXiv preprint arXiv:2511.10171, 2025.", "identifier_if_present": "arXiv:2511.10171", "relation_candidate": "背景引用", "shared_component": "局部依赖、时空平移不变性与相场单轨迹学习。", "claimed_difference": "本文将该数据效率动机结合守恒、容量约束输运；与此自引前作的具体重叠待核读。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p8，§4.4；p10参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "可复用容量参数化带来明确的结构约束能力，并有多任务和消融支持；并非仅报告性能增益，但不足以确立路线级首创。", "central_increment": "FVM类前作已结构守恒（仅本文转述）；本作新增容量约束累计输运接口，支持证据为命题及表3–9；尚待排除重参数化、邻域变化和基线步进设置的影响。", "soundness_observation": "守恒抵消论证成立，但命题2/3的严格不等式过强：全场恰为下界/上界时容量全零，状态保持边界值，只能普遍保证≥/≤。此外，更新中无Δt因子不能单独推出任意步长稳定性。\n \n", "significance_observation": "对有物理边界的守恒场预测有实用价值；多头、多骨干和边界适配体现工程整合，但不等于通用PDE求解保证。", "main_open_question": "等骨干、等邻域并允许稳定子步进后，大步长优势是否仍来自累计输运机制本身？"}

limitations：[{"text": "D头无双边硬保证；邻域需随步长选择，固定stencil不保留FNO式分辨率不变性；仅处理无源项方程，非周期验证限1D Dirichlet。", "basis": "author_report", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p9，§5；p13，A.3。"}, {"text": "保界改善并非普遍：FNO-D下/上越界率2.47%/1.02%，反高于FNO-AR的1.36%/0.50%。", "basis": "model_inference", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p8，表4。\n"}, {"text": "大步长对照同时改变输运邻域，未给等时延或稳定子步进比较；浅水投影基线是否同时约束两动量也未说明，不能把全部优势归因于容量限制。", "basis": "model_inference", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p5–7，基线说明及表3；p18，D.3.3–4。"}, {"text": "相场报告口径待澄清：E.2称训练/评估128²，E.7却称训练分辨率1024²；E.2测试20条，图3统计100条，未说明是否不同集合。不可将速度与精度视为同网格联合结果。", "basis": "model_inference", "locator": "TEXT_OR_1KRpajnd6u_57319dd40a00：p9图3图题；p19 E.2；p20 E.7。\n \n \n"}]

minimal_check：{"question": "大步长优势能否在控制邻域与步进成本后保留？", "control": "用同一Dirichlet数据、骨干和R=7，对照累计输运头与同容量约束的通量率参数化F=Δt·f；另让原FluxGNN采用稳定子步进，统一报告成本。", "observable_outcome": "比较50Δt输出间隔下的MAE、越界率、守恒误差与总推理时延；区分参数重标度等价性和实际效率优势。", "resources": "需原数据与实现；原设256格、300 epochs、5种子。训练硬件及所需运行时间未报告，本轮未执行。", "failure_or_stop_condition": "等成本后优势消失，则不支持范式独有优势；无法复现原基线或对齐邻域、步进时，停止因果归因。"}

missing_fields：["原PDF图像、前作全文及版本身份核验。", "训练GPU、训练耗时、显存、确切参数量和超参数搜索预算。", "Econs归一化细节；表中T=2与附录物理终时的统一换算说明。", "Dirichlet及相场的完整越界统计；相场训练分辨率、测试集合数量冲突的解释。", "图示统计曲线和绝对计时数值的可核查材料。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可复用容量输运头值得研究；先对齐相场分辨率与计时协议，并以同邻域、稳定子步进对照判断大步长收益。

题名版本与机制：完整题名、30页当前附件及全文哈希一致。更新逐对抵消保证周期网格总量守恒；创新候选是容量限制的累计输运头，非抵消恒等式本身。开放边界需记净边界通量，不能宣称内部总量恒定。

核查定位：p001 title, p003, Eq2/Proposition1, p012, A.1, p018, ghost cells；identity_and_structural_conservation_confirmed

单边与双边保证：原命题2/3从u≥lower或u≤upper推出严格不等式过强。全场恰在同一边界时所有可用容量为0，所有相应输运为0，仍停留边界。可保留非严格单边不变性；有限精度sigmoid也不能提供普遍严格缓冲。D头平均两种单边更新，没有双边硬保证，A.3与结论承认这一点。

核查定位：PDF physical page4, Propositions2–3 and Eq3, p012–p013, A.2–A.3；strict_bound_claim_corrected_non_strict_invariance_retained

表4/9的保界与精度取舍：原表4确认ResNet-D MAE2.79e−3、越界.59%/.01%；FNO-D虽MAE3.17e−3优于FNO-AR7.30e−3，其越界2.47%/1.02%却高于1.36%/.50%。表9去DCL误差降至1.52e−3但越界升至2.26%/.41%。不能概括为所有骨干在所有指标同时改善。

核查定位：PDF physical page8, Table4, p017, Table9；tradeoff_and_counterexample_to_uniform_empirical_gain_confirmed

大步长因果归因：原表5在10dt下FluxNet-D误差11.7e−4，逊于FluxGNN3.54e−4和FluxGNN-D2.73e−4；50dt下则50.1e−4优于1150e−4。FluxNet半径从5增至7，各步长分别训练，未报告允许稳定子步进且等时延的比较。没有显式dt乘子不足以单独证明任意步长准确/稳定。

核查定位：p003, Remark1, PDF physical page8, Table5, p018, D.3.3–D.3.4；large_step_results_confirmed_attribution_limited

相场加速、精度及图注冲突：原表6确认10/100/1000dt分别.55/3.8/17.3倍，加速最大时MAE8.39e−2，100dt为2.16e−2；邻域及骨干也同时变化。原图17纵轴是完成50000dt的毫秒墙钟，粗步长曲线更快，但图注把17.3倍写给100dt，与表6及E.7的1000dt不一致。E.2写128²训练评估、20测试轨迹，E.7称训练分辨率1024²、图3称100轨迹；未解释数据/计时集合关系，不能将速度与精度视为同一网格联合结果。

核查定位：PDF physical page9, Table6/Figure3, p019, E.2–E.3, p020, E.7, PDF physical page30, Figure17/caption；speed_accuracy_scope_and_reporting_conflicts_confirmed

本地补充/限定：["补看原图17：时间单位为毫秒，图注把17.3倍标给100dt，与正文/表6对应1000dt冲突。", "单边严格不等式错误不否定非严格保界及守恒；D头经验效果单列。"]

核查局限：["未运行PDE、作者代码或训练实验，最小对照仅为建议。", "未核读FluxGNN等前作；没有确认camera-ready或历史首创。", "局部阅读所列页和四页原图，不做全场景稳定性证明；第1页仅读标题开头。"]


## pro067 · Mesh Field Theory: Port–Hamiltonian Formulation of Mesh-Based Physics

论文 OR_MgIvtHk5wm；暂定 L2；low。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_MgIvtHk5wm_05a076bf685e", "source_url": "https://api2.openreview.net/pdf?id=MgIvtHk5wm\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_MgIvtHk5wm_05a076bf685e：物理页1–29，页标连续；包括正文、参考文献及附录A–D.10。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文文本，未见PDF图像；图1–7不可核读，部分公式与双栏表格排版错位。", "未提供前作正文、代码或其他版本；清单版本角色未核实，不认定为最终出版版。"]}

问题：如何在不使用已知PDE残差监督的网格动力学学习中，区分必须固定的拓扑耦合与可学习的本构、耗散？

方法：以相邻阶cochain及能量变量e=∇H描述状态，提出Jacobian分解∂F/∂z=(J−R)G。主实现固定关联矩阵接线J，局部MLP学习SPD度量G和PSD耗散R；实验常用(q,p)及K=DᵀWD实现，以KDK/Strang、CFL子步预测下一状态，采用一步监督。

作者主张：从局部性、置换等变、定向协变和能量条件推出局部port–Hamiltonian分解；拓扑固定接线，正对角增益可依赖状态，常增益可归一化。

论文证据：Theorem 3.3、Corollary 3.4及附录B给出证明链；能量假设还明确要求两点增量无功/耗散，而不只是轨迹能量不增。

模型推断：潜在增量是接线限制的原则化刻画，不是首次提出DEC或pH；但当前证明存在具体逻辑问题，尚不能视为已成立的新保证。

定位：['TEXT_OR_MgIvtHk5wm_05a076bf685e：p4/Assumption 3.2、Theorem 3.3；p14–16/附录B \n']

作者主张：固定拓扑、只学习度量与耗散，可获得稳定、数据高效且能外推的模拟器。

论文证据：提供波动、异质弹性、非线性晶格和消融实验。表7中完整模型动量变化为2.67e−7，破坏拓扑接线后为1.26e−2。

模型推断：支持指定基准下的结构归纳偏置价值；不能由这些实验反推定理必要性，也不能概括为所有任务最优或离散步严格守恒。

定位：['TEXT_OR_MgIvtHk5wm_05a076bf685e：p6–9/§5；p9/Table 7；p27/附录D.8 \n']

key_results：[{"setting": "32×32周期解析平面波；Δt=0.002，200步rollout，表2为5种子均值。", "baseline": "MGN、HNN", "metric_or_guarantee": "一步MSE、TSMSE、归一化能量漂移；均为作者报告。", "reported_values_and_units": "依次为：MeshFT-Net 1.3e−9、9.6e−5、1.3e−4；MGN 1.6e−7、0.13、25.9；HNN 3.5e−8、0.003、0.01。漂移无量纲，MSE未给物理单位。", "information_and_compute": "2000训练对、256验证对，10 epochs，batch 8；该实验总训练耗时未报告。", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p6/Table 2；p18–19/附录D.1 \n"}, {"setting": "分辨率32×32→64×64，以及波速1.0→1.4；Δt=0.004，200步，3种子均值。", "baseline": "GraphCON、MGN-HP", "metric_or_guarantee": "OOD TSMSE与归一化能量漂移。", "reported_values_and_units": "分辨率外推：MeshFT-Net为0.051/0.0029，GraphCON为0.32/0.71。波速外推：MeshFT-Net为0.71/0.17；MGN-HP的TSMSE为0.59，优于MeshFT-Net。", "information_and_compute": "4000训练对、512测试对，10 epochs，batch 16。", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p21/附录D.4；p22/Table 11 \n"}, {"setting": "32×32非线性晶格OOD，256步，Δt=0.002，3种子均值。", "baseline": "HNN、GraphCON", "metric_or_guarantee": "TSMSE、相对能量MAE及能量单调性违反率。", "reported_values_and_units": "阻尼ϕ4：MeshFT-Net为2.54e−4/8.70e−3/0.325，GraphCON为9.19e−4/1.98e−2/0.354。FPU任务TSMSE：MeshFT-Net 0.0304，HNN 0.00905；并非全面领先。", "information_and_compute": "32训练、8域内验证、8 OOD轨迹；10 epochs，batch 8；参考轨迹使用8内部子步。", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p24/附录D.6.2；p25/Table 13 \n"}, {"setting": "表15独立计算成本实验：128×128解析波，单NVIDIA H100，3种子均值。", "baseline": "MGN", "metric_or_guarantee": "推理/训练计时、峰值训练CUDA内存、参数量。", "reported_values_and_units": "MeshFT-Net：2.70/3.82 ms、262.8 MB、642参数；MGN：13.8/40.7 ms、2379 MB、108930参数。", "information_and_compute": "作者说明计时受实现及内核差异影响；不与表2误差拼接成同一运行配置。", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p28/Table 15；p29/附录D.10 \n"}]

prior_work_candidates：[{"citation_as_printed": "Trask, N., Huang, A., and Hu, X. Enforcing exact physics in scientific machine learning: A data-driven exterior calculus on graphs. Journal of Computational Physics, 456:110969, 2022.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "固定incidence、学习Hodge的拓扑–度量分离；仅为概念层面候选关系。", "claimed_difference": "本文主张从物理原则约化Jacobian，而非从离散算子学习设置出发。", "basis": "target_paper_only", "target_locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p2/§2；p11/参考文献 \n", "prior_actually_read": false}, {"citation_as_printed": "Desai, S. A., Mattheakis, M., Sondak, D., Protopapas, P., and Roberts, S. J. Port-hamiltonian neural networks for learning explicit time-dependent dynamical systems. Physical Review E, 104:034312, 2021.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "port–Hamiltonian能量及耗散建模。", "claimed_difference": "本文声称推导局部结构，而非预设全局pH模板。", "basis": "target_paper_only", "target_locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p2/§2；p10/参考文献 \n", "prior_actually_read": false}, {"citation_as_printed": "Pfaff, T., Fortunato, M., Sanchez-Gonzalez, A., and Battaglia, P. Learning mesh-based simulation with graph networks. In International Conference on Learning Representations, 2021.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "网格上的局部、置换等变动力学预测。", "claimed_difference": "增加定向及能量结构约束，缩小可学习耦合空间。", "basis": "target_paper_only", "target_locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p2/§2；p11/参考文献 \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "low", "reason": "按中心新意暂列理论/机制层面的L2候选，而非新路线；此判断不表示认可定理正确性，已支持的架构及性能增量更接近L1。", "central_increment": "前作已固定incidence并学习Hodge（本篇转述）；本作在更强能量条件下主张从原则推出接线限制，并用于动态学习；证据是约化证明及实验，尚待排除关键推理缺口。", "soundness_observation": "按式(1)，恒等映射T(x)=x满足T(ρx)=ρT(x)，但B.2却据定向协变排除恒等项。该反例直接动摇此引理及现有拓扑证明链，不等于否定所有可修订的约化结论。TEXT_OR_MgIvtHk5wm_05a076bf685e：p14/B.2 \n", "significance_observation": "固定结构确有长时预测及资源效率潜力；实证优势主要限于所测系统，不能提升为普遍物理保证。", "main_open_question": "修正定向协变论证后，能否仍从明确假设推出所声称的incidence接线限制，而不是额外假定该结构？"}

limitations：[{"text": "定理只涉及局部Jacobian，作者明确不保证单一全局pH表示；固定J另需状态无关增益。", "basis": "author_report", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p4–5/§3.2"}, {"text": "增量(E)强于普通能量不增；PSD的状态相关R不自动验证增量耗散。§4固定G与D.6.2使用状态特征的非线性实现也未充分对齐。", "basis": "model_inference", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p4–5/§3–4；p24/附录D.6.2"}, {"text": "不是容量与结构先验匹配对照，MGN未获显式阻尼；No-Orientation同时破坏反对称性，不能单独归因于定向约束。", "basis": "model_inference", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p19/附录D.2；p28/Table 15；p29/附录D.9"}, {"text": "The Well仅有快照及定性叙述，未见数值基线表；图不可见，无法核实该部分视觉效果及数据效率曲线。", "basis": "model_inference", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p8/§5.4；p21–22/附录D.5"}, {"text": "表9题注称规则网格而正文称Delaunay；表8称相对能量漂移而D.7定义绝对差，相关口径未擅自统一。", "basis": "model_inference", "locator": "TEXT_OR_MgIvtHk5wm_05a076bf685e：p9/Table 8；p19/Table 9；p26/附录D.7"}]

minimal_check：{"question": "B.2排除同阶恒等项是否确实遵循式(1)？", "control": "在单边复形上取T=I，按式(1)检验局部性、置换等变与定向协变，并对照B.2使用的额外负号。", "observable_outcome": "若I通过原协变定义，则a=0不能由该定义推出，现有证明需补假设或改结论。", "resources": "原始PDF用于排除文本提取错误；纸笔或小型矩阵运算，无需模型训练。", "failure_or_stop_condition": "若只能通过新增反协变或禁止同阶项的假设排除I，停止把原四原则视为该接线结论的充分依据。"}

missing_fields：["候选前作的DOI/arXiv标识未提供。", "训练总GPU时、完整调参预算及The Well定量对照未报告。", "PDF图像、前作全文及代码未提供；本轮未外查、执行代码或复现实验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

固定结构的经验收益可借鉴；依赖其理论前先修补协变引理、增益退化条件和实际非线性实现映射。

身份和理论/实现范围：完整题名与29页附件绑定。Theorem3.3是局部Jacobian分解，非单一全局pH动力学保证；要求两点增量能量条件，明显强于轨迹能量不增。固定J还需状态无关增益。实现采用KDK/Strang及CFL子步，连续时间能量性质不等于离散步严格守恒。

核查定位：p001 title, PDF physical page4, assumptions/Theorem3.3, p005, Corollary3.4/Algorithm1；identity_conditions_and_discretization_scope_confirmed

B.2协变推理：原PDF14页确有额外负号：已乘rho_k^−1补偿输出后仍令结果等于−T。按同页式1的T(rho x)=rho T(x)，T=I局部且置换/定向等变，a=1合法。因此B.2单凭O排除恒等项的证明不成立；不是提取丢失符号。B.3的增量能量代数分解可以独立讨论，不能因B.2错误一并否定。

核查定位：PDF physical page14, Eq1/LemmaB.2, p015, LemmaB.3；orientation_lemma_counterexample_confirmed

主定理严格正增益的零动力学边界：一条边D=[−1,1]，H=||z||²/2，Fcon=Fdiss=0满足L/P/O/E。但DF=0=(J−R)G且G可逆推出J=R；反对称J和对称R只能均0，与CD、C>0非零冲突。原定理需要允许零增益或非退化条件；该退化反例不否定特定固定接线网络的经验用途。完整推导另存。

核查定位：PDF physical page4, Theorem3.3 Ck>0, local_check/zero_dynamics_argument.md；strict_positive_gain_universal_claim_boundary_counterexample

非线性实证并非全指标领先：原表13 FPU TSMSE MeshFT .0304，HNN .00905，后者更优；MeshFT动量变化4.75e−8更好。阻尼phi4 TSMSE2.54e−4、能量相对MAE.00870，单调违反率.325仍非零，不能称离散能量单调保证。每组32训练、8验证、8OOD轨迹，3种子、10epochs。正文固定G描述与非线性实验使用状态特征需进一步对齐。

核查定位：p024, D.6.2, PDF physical page25, Table13, p005, state-independent G；decisive_empirical_values_and_limits_confirmed

消融与计算预算：No-Orientation同时破坏J反对称性，无法单独归因于定向性质；Scrambled保留反对称性但用共同理论能量评估，故漂移不等于自身Hamiltonian失守。原表15在128²/H100给MeshFT2.70ms推理、3.82ms训练步、262.8MB、642参数，MGN13.8/40.7ms、2379MB、108930参数；为特定实现的每步成本，不是总训练时间或等容量比较。

核查定位：PDF physical page28, Tables14–15, p029, D.9–D.10；cost_scope_and_ablation_confound_confirmed

本地补充/限定：["B.2疑点经原PDF确认；另补严格正C的零动力学反例，限定为原样主定理的退化边界。", "性能增量与未成立的拓扑唯一性证明分开，L2仍为低置信中心新意候选，不是正确性认证。"]

核查局限：["未执行仿真、作者代码、前作复读或完整证明验证。", "只对所列局部恒等式作纸笔核查，未证明修订定理。", "第1页仅读标题开头；未重新评测数据效率曲线和The Well任务。", "当前附件版本身份未确认。"]


## pro068 · Physics from Video: Identifiability of Time-Invariant Second-Order ODEs under Minimal Trajectory Conditions

论文 OR_xrXxqLadvS；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_xrXxqLadvS_228ce6612c5f", "source_url": "https://api2.openreview.net/pdf?id=xrXxqLadvS\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "13a136382e1f6f76accd49f1adb3687dbe2b85199d0f67ba0fc80a8eeb38da38", "source_pdf_sha256": "228ce6612c5f43cdc8c075ad0e3251b11198d71f08303eac362d05ada49ca4af"}], "read_ranges": ["TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页1—45全部所供文本，含正文1—9、参考文献10—11及附录A—F；页标连续，未发现缺页标。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文提取文本，未查看PDF页图；图1—11不可见，不能核读图3曲线或视频示例的视觉内容。", "双栏混排、部分公式上下标及表3单元格错位；仅采用明确可辨或在附表重列的数值。", "附件版本角色未核验，不认定为最终出版版；前作原文、其他版本及实验原始数据未提供。"]}

问题：已知标量齐次二阶LTI方程形式，何时仅凭视频即可唯一恢复阻尼与刚度系数，而非得到另一套坐标下的伪物理参数？

方法：共享逐帧CNN将视频映射为标量潜变量；中心差分估计一、二阶导数，联合学习编码器与ODE系数，最小化物理残差加潜变量标准差下限惩罚。理论以ẑ=f(z)展开链式法则，在同一状态的不同速度处消去关于速度的二次多项式。

作者主张：首次为encoder-only视频物理参数学习建立结构可辨识性保证，并刻画不同阻尼区间的最小轨迹需求。

论文证据：Thm4.2由共同开区间内每个状态至少三种互异速度，推出f局部仿射及参数完全相等；Thm4.3给出严格欠阻尼单轨迹L≥2P的充分条件；Thm4.6证明满足跨轨迹覆盖的三条轨迹足够。

模型推断：中心增量是约束未知视觉坐标，而非新网络。三轨迹已证充分，但未证普遍必要；Thm4.5直接证明的是覆盖证书失败，不能单凭此推出所有识别方法均不可能。

定位：['TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页5—6，Thm4.2—4.6。\n', 'TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页16—22，附录C.1—C.5。\n']

作者主张：给出离散有噪视频参数估计的非渐近误差保证。

论文证据：Thm4.8给出||η̂−γ||₂≤[C1σ√(log(3/δ)/(T−1))+C2σ²+C3Δt²]/ψmin+Eenc；B.3扩展到多片段总样本量N，离散化项使用Δtmax²。

模型推断：这是条件性回归误差分解，不是端到端学习收敛保证。固定噪声存在errors-in-variables偏差底，缩小Δt还会放大差分噪声。

定位：['TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页6，Thm4.8；物理页14—15，B.2—B.3；物理页22—27，证明。\n']

作者主张：variance-floor防止潜变量坍塌、改善条件性并稳定训练。

论文证据：表4中临界和过阻尼条件下优于KL正则；表15测试τ=1、10、100，估计变化较小。

模型推断：属于相对LPFV的局部方法改进；方差下限本身不保证良态设计，D.1还需速度能量与边界控制。

定位：['TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页8，表4；物理页28—30，D.1—D.2；物理页45，表15。\n']

key_results：[{"setting": "合成临界阻尼摆，真值(γ0,γ1)=(4,4)，三轨迹覆盖成立；表11对应初值为(70,−200)、(70,−600)、(70,−1000)，每条2 s。", "baseline": "KL-regu", "metric_or_guarantee": "系数估计均值±标准差；按秒制ODE量纲，γ0为s⁻²、γ1为s⁻¹", "reported_values_and_units": "Var-regu：(4.0218±0.0040，4.0352±0.0017)；KL-regu：(9.2659±1.0532，6.2857±0.4848)。", "information_and_compute": "64×64、20 fps、5随机种子；无需状态标签；训练硬件和耗时未报告。", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页8，表4；物理页32，F.2；物理页43，表11。\n \n"}, {"setting": "真实干净背景摆，绳长0.45、0.90、1.50 m，各5段不同初值视频。", "baseline": "LPFV；另列PAIG和NIRPI。基线数字转引Garcia et al. (2025)，未由本篇统一复跑。", "metric_or_guarantee": "绳长RMSE", "reported_values_and_units": "按上述绳长顺序，OURS为0.050、0.070、0.101 m；LPFV为0.061、0.247、0.201 m。基线RMSE由已发表均值和样本标准差换算。", "information_and_compute": "192×108、30 fps；均值与标准差跨5段视频，不是5随机种子；训练成本未报告。", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页9，表5、§5.2.1；物理页32，F.3。\n \n"}, {"setting": "真实车轮安装手机的物理摆，经裁剪缩放并采用小角度、有效线性阻尼近似。", "baseline": "几何与转动惯量计算的γ0参考值8.26 s⁻²", "metric_or_guarantee": "γ0估计均值±标准差", "reported_values_and_units": "8.998±0.009 s⁻²；γ1没有物理标定真值，不能据此确认阻尼恢复准确。", "information_and_compute": "120×120、10 fps、5随机种子；未报告运行成本。", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页9，§5.2.2；物理页32、34—36，F.3.2。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Garcia, A. C., Warchocki, J., van Gemert, J., Brinks, D., and T¨omen, N. Learning physics from video: Unsupervised physical parameter estimation for continuous dynamical systems. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 27924–27933, 2025.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "encoder-only、潜空间物理约束及抗坍塌训练；也是直接比较基线。", "claimed_difference": "新增结构可辨识性分析，并用中心差分、variance-floor替代其Euler/单侧构造和KL项。", "basis": "target_paper_only", "target_locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页2，§2；物理页10，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Wang, Y., Huang, W., Gong, M., Geng, X., Liu, T., Zhang, K., and Tao, D. Identifiability and asymptotics in learning homogeneous linear ode systems from discrete observations. Journal of Machine Learning Research, 25(154):1–50, 2024b.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "线性ODE可辨识性与离散观测分析。", "claimed_difference": "本篇将从像素学习的未知状态重参数化纳入问题；未证实直接继承该前作的具体定理。", "basis": "target_paper_only", "target_locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页3，§2；物理页11，参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是未知表征下的实质性充分性保证，不只是性能提升；架构与正则改动较局部，也不足据此判为路线级L3。", "central_increment": "LPFV已做到无解码器视频参数学习（本篇转述）；本作在共享平滑状态映射与三斜率覆盖下新增局部仿射性及精确参数恢复保证，证据为Thm4.2/4.6，尚待厘清最小性。", "soundness_observation": "核心二次多项式三根消去逻辑清楚；但C.3只证明覆盖失败，未建立全面的不可辨识性结论。固定潜变量的离散回归唯一性也不等同编码器与参数联合唯一。", "significance_observation": "可指导受控单自由度振动视频的采集与参数估计；不是任意视频或通用世界模型物理理解的保证。", "main_open_question": "能否建立真正的必要条件与最小轨迹数，而不是将三斜率充分证书失败解释为一般不可辨识？"}

limitations：[{"text": "作者限定标量二阶LTI；state consistency难从原始像素验证，真实拍摄依赖相对受控场景。合成覆盖检查使用真实状态轨迹，不等于已实现无真值的视频认证。", "basis": "author_report", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页3，Def3.1、Remark3.2；物理页7，§5.1.1；物理页9，§6。\n"}, {"text": "强动态干扰会破坏恢复；Brightness L3的γ1为0.0386±0.0228，真值0.08。Brightness L2另报告排除失败种子的结果，不能替代全部5种子的表现。", "basis": "author_report", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页36，表6及F.4。\n"}, {"text": "真实基线转引且实现细节不同，不能将全部收益因果归于中心差分或正则；未提供耗时、显存对照，无法量化省算主张。", "basis": "model_inference", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页9，§5.2.1；物理页34，Remark F.1。\n"}, {"text": "附录E允许常数项平衡点平移，但物理常数g仍受潜变量尺度与原点影响，需额外标定；不能泛化为所有物理常数均可直接恢复。", "basis": "author_report", "locator": "TEXT_OR_xrXxqLadvS_228ce6612c5f：物理页31，附录E。\n"}]

minimal_check：{"question": "两条不同振幅的无阻尼轨迹是否已足以识别，从而否定“三条轨迹普遍必要”的强解读？", "control": "保持共同频率与共享f；比较不同振幅A1≠A2和仅相位不同、振幅相同的两条完整周期轨迹。", "observable_outcome": "利用本篇速度公式±ω√(Ai²−u²)，检查共同开区间是否已有至少三种互异速度，再沿式(12)验证f″=0及参数相等。这是由本文公式提出的检验，非已完成的独立审计。", "resources": "本篇物理页16式(12)、物理页19无阻尼解析式；纸笔或符号代数即可，无需训练视频模型，具体耗时未测。", "failure_or_stop_condition": "不能在共同开区间建立互异斜率则不下结论；若消去成功，仅削弱三轨迹必要性，不否定Thm4.6的充分性。"}

missing_fields：["PDF图像及图中独有数值不可核读。", "训练硬件、显存、迭代数、优化器、总耗时及搜索预算未报告。", "真实实验γ1的独立物理标定未提供。", "所选前作条目未给DOI/arXiv编号，原文未核读。", "未外搜、未复现实验、未完成全部定理独立验证或版本比对。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

三斜率消去提供清晰的数据采集充分条件；继续研究更弱覆盖条件与可从视频检验的state consistency，比直接宣称最小轨迹数更有价值。

身份及中心定理条件：题名与45页当前附件匹配。Def3.1要求共享C²状态映射；Thm4.2同时要求真/潜变量精确满足标量齐次LTI方程、同状态三种互异速度、f′不恒零。式12关于速度的二次多项式有三根，故各系数零，f仿射并恢复两系数；核查该核心消去逻辑成立。不是对任意像素视频或训练算法收敛的证明。

核查定位：p001 title, p003, Definition3.1, PDF physical page5, Theorem4.2, p016, Eq12–14；identity_and_central_sufficient_argument_confirmed

三条轨迹不是普遍必要条件：取无阻尼两条完整周期轨迹z1=cos(omega t)、z2=2cos(omega t)。在u∈(−1,1)，联合速度为±omega sqrt(1−u²)、±omega sqrt(4−u²)，四者互异；同一共享f和潜方程下，式12已有三根以上，故同样可辨识。此为纸笔覆盖检查，说明三轨迹充分证书不能读作普遍最小轨迹数；不反驳Thm4.6本身的充分性。单轨迹覆盖失败也不单独证明所有方法不可识别。

核查定位：PDF physical page5, Theorems4.3–4.6, p016, Eq12, p019, undamped slope formula；two_trajectory_sufficiency_example_confirmed_strong_minimality_not_supported

有限样本与variance-floor的范围：原式9除采样项还有sigma²偏差、dt²离散化误差及Eenc；sigma是差分后尺度，dt变小可能放大噪声。D.1额外要求速度能量下限、方差约束实际达到及边界控制，给出的最小特征值下界可能非正，不能只靠软方差惩罚宣布良态设计。

核查定位：PDF physical page6, Theorem4.8, p028, LemmaD.1 and Eq30；noise_floor_and_conditioning_conditions_confirmed

真实视频的数值和比较协议：原表5三种绳长RMSE为.050/.070/.101米，对LPFV .061/.247/.201；基线转引既有结果、并非统一复跑，均值标准差跨5段视频。手机摆gamma0=8.998±.009对几何参考8.26，相对偏差约8.9%，小随机种子离散度不等于物理准确性；gamma1未独立标定。

核查定位：PDF physical page9, Table5/Sections5.2.1–5.2.2；empirical_values_and_baseline_scope_confirmed

观测干扰边界：原表6保留全部5种子，Brightness L2的gamma1为−.5532±1.3890，剔除失败种子后.0680±.0111只能作附注；L3为.0386±.0228，真值.08。MovingClutter L3也明显失败。不能把受控背景成绩扩展到任意动态干扰。

核查定位：PDF physical page36, Table6/caption/F.4；all_seed_failure_cost_and_nuisance_scope_confirmed

本地补充/限定：["已完成Pro建议的两种振幅无阻尼两轨迹纸笔检查：有四种速度，削弱三轨迹普遍必要性强解读，保留三轨迹充分定理。", "补充Brightness L2全部种子结果及手机摆相对偏差，避免只保留稳定或成功结果。"]

核查局限：["未运行视频训练或复现实验；两轨迹例仅解析推导。", "未逐项验证噪声集中证明、前作全文或完整训练协议。", "第1页仅读标题；局部核查不覆盖所有45页，版本角色未确认。"]


## pro069 · High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions

论文 OR_GW3umRqsZZ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955", "source_url": "https://api2.openreview.net/pdf?id=GW3umRqsZZ\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "c8474d7e22a1527ca3c27e65d6fab4968e8dc355899f6521af4b5728957e8815", "source_pdf_sha256": "e7a52f3d0955cb37c1f72e8261bbf20a2a67ec56a590ddb5b97b526652b90fa1"}], "read_ranges": ["TEXT_OR_GW3umRqsZZ_e7a52f3d0955：物理页1–35，连续页标齐全；包括正文§1–6、参考文献、目录及附录A–F。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文文本，未查看原PDF图像；双栏串行、根号作用范围、上下标及部分公式存在抽取损失。", "前作及p001脚注提及的改进arXiv版本未提供；不将当前附件认定为最终出版版。"]}

问题：不访问密度值、仅查询准确或近似的对数密度梯度，能否以polylog(1/δ)查询获得δ精度样本？

方法：将目标写成q(x)exp(w(x))，以随机路径上的梯度内积估计w；截断估计到[−B,B]，抽取J∼Poisson(2B)，用乘积∏(B+Wj)/(2B)接受候选。FORS精确采样的是截断后倾斜分布，再分别控制截断、score估计和初始化误差；用于逐步逆扩散或proximal sampler的RGO。

作者主张：仅凭L2准确score，在最小数据假设下实现高精度扩散采样，相较既有精度依赖获得指数级改善。

论文证据：Theorem 3.1给出随机接受机制；Theorem 4.1及Corollary 4.2给出多对数查询界和加权L2误差控制。

模型推断：实质增量是免密度评估且容忍近似score的高精度保证，而非Bernoulli factory本身。

定位：['TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p004、006，Theorems 3.1、4.1与Corollary 4.2；p018–022，附录C、E.1。']

作者主张：进一步获得次线性环境维度依赖和低维结构适应性。

论文证据：Theorems 4.4、4.7分别利用非均匀Lipschitz条件与覆盖数控制。

模型推断：改善并非免费：score误差系数增大，低维版本还增强了误差分布要求。

定位：['TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p006–007，Assumption 4.3、Definition 4.6、Theorems 4.4、4.7；p023–033，附录E。']

作者主张：通过一阶RGO实现，获得一般对数凹分布的高精度采样。

论文证据：Theorem 3.3控制Gaussian tilt采样误差；Theorem F.1列出LSI、PI及对数凹条件下的结果。

模型推断：明确去掉密度值评估，但所给分析仍借助proximal oracle，不能直接视为纯梯度端到端成本已闭合。

定位：['TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p005、008、034–035，Theorems 3.3、F.1。\n']

key_results：[{"setting": "有限二阶矩；M=d+E||X0||²；S=Σt ηt Ept||st−∇log pt||²。", "baseline": "Li & Yan (2025)：本文转述同类条件下查询复杂度为Õ(d/δ)，未核读前作。", "metric_or_guarantee": "早停分布的KL保证，并转换为原数据分布的bounded Lipschitz保证。", "reported_values_and_units": "Q=O(d log²(M/δ)+log³(M/δ))次score查询；D_BL(pdata,p̂1)²≲δ²+S。", "information_and_compute": "Corollary 4.2给出至少1−δ概率的查询预算；不包含score学习成本，也不是原始任意数据分布的TV保证。", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p002 §1.1；p006，Corollary 4.2及其前后说明。\n"}, {"setting": "Assumption 4.3：Ppt(||∇s⋆t||op>Lδ/σt²)≤δ²/d⁸。", "baseline": "本篇§4.1的一般数据版本。", "metric_or_guarantee": "次线性维度查询界，伴随更大的score误差系数。", "reported_values_and_units": "正文给出Q=O(max{√(dLδ log(d/δ)),Lδ log(d/δ)}log(M/δ²))；D_BL²≲δ²+√(d/Lδ)S。", "information_and_compute": "单位为score查询次数；Lδ可随精度变化，不能默认为固定常数。", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p006–007，Assumption 4.3、Theorem 4.4及后续复杂度式。\n"}, {"setting": "Definition 4.6的d⋆有限；采用shifted score。", "baseline": "本篇§4.1的环境维度d依赖。", "metric_or_guarantee": "覆盖熵适应的查询复杂度。", "reported_values_and_units": "Q=O(d⋆log²(M/δ)+log³(M/δ))；D_BL²≲δ²+(d/d⋆)S+。", "information_and_compute": "S+将各步score均方误差替换为额外高斯方差v∈[0,2ηt]下、分布pt∗N(0,vI)上的最大值；不是原始pt上的普通L2条件。", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p002 §1.1；p007，Definition 4.6、Theorem 4.7。\n"}, {"setting": "f为β1-smooth，µ满足PI；χ0²=Dχ²(µ0∥µ)有限。", "baseline": "Fan et al. (2023)，本文称恢复其相关复杂度而不使用密度值。", "metric_or_guarantee": "Dχ²(µ̂∥µ)≤ε²。", "reported_values_and_units": "期望查询数Õ(CPI β1(√d·log^{1/2}(1/ε)+log(1/ε))log(χ0²/ε²))。", "information_and_compute": "正文明确同时计一阶与proximal oracle查询；仅依赖W2初始化距离的对数凹分支仍为1/ε²级。", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p008 §5；p034，Theorem F.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Huang, X., Zou, D., Dong, H., Zhang, Z., Ma, Y., and Zhang, T. Reverse transition kernel: a flexible framework to accelerate diffusion inference. Advances in Neural Information Processing Systems, 37:95515–95578, 2024a.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "高精度逆向转移核采样。", "claimed_difference": "前作使用额外密度评估及Lipschitz条件；本作一般版本仅需有限二阶矩与L2 score误差。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p002–003 §1.2；p010参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Fan, J., Yuan, B., and Chen, Y. Improved dimension dependence of a proximal algorithm for sampling. Proceedings of Thirty Sixth Conference on Learning Theory, volume 195, pp. 1473–1521. PMLR, 7 2023.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "proximal sampling与Gaussian tilt/RGO实现。", "claimed_difference": "恢复相关维度依赖，同时以随机梯度积分代替密度值评估；proximal求解仍需另行核算。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p005 §3.2、p034附录F；p009参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Gatmiry, K., Chen, S., and Salim, A. High-accuracy and dimension-free sampling with diffusions. arXiv preprint arXiv:2601.10708, 2026.", "identifier_if_present": "arXiv:2601.10708", "relation_candidate": "同期独立工作", "shared_component": "多对数精度依赖的扩散采样。", "claimed_difference": "同期工作要求有界支撑分布的高斯卷积、次指数score误差及估计score的Lipschitz性；其R/σ复杂度与本文维度复杂度不可直接排序。", "basis": "target_paper_only", "target_locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p003 §1.2、p012–013附录A.1；p009参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "经典随机拒绝组件被转化为弱score oracle下新的高精度与鲁棒性保证，明显超出局部调参；主要新增是实质能力及复杂度保证。", "central_increment": "前作已能借助密度值高精度采样（本篇转述）；本作在有限二阶矩和L2误差条件下，以FORS实现仅score查询的多对数精度依赖，证据为Theorem 4.1及Corollary 4.2。", "soundness_observation": "未逐式验证全部证明。E.1的p020:L0037所印截断不等式对a=2B、b=0不成立；改用min{|a−b|,2B}+τB(a)存在候选修补路径，但需核对原PDF并重查常数传播，不能据此直接否定主定理。", "significance_observation": "理论意义在于改变高精度采样所需的oracle条件；没有实测证据证明神经网络推理墙钟加速，工程实现成本仍未验证。", "main_open_question": "修正E.1所印截断分解后，能否仅凭原L2条件维持同阶误差累积与查询保证？"}

limitations：[{"text": "作者明确指出每步多次score调用和保守步长可能影响实用性；全文未报告数据集实验、运行时间或硬件成本。", "basis": "author_report", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p008 §6。\n"}, {"text": "多对数推理查询不等于多对数端到端学习成本；增强维度结果牺牲误差容忍度，对数凹扩展另有proximal oracle与初始化条件。", "basis": "model_inference", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p006–008、034–035。"}, {"text": "E.1截断分解的文本表达有可检验问题；有损抽取下不能确定是原文笔误还是提取失真，亦未完成修补后的完整证明核验。", "basis": "model_inference", "locator": "TEXT_OR_GW3umRqsZZ_e7a52f3d0955:p020:L0031–L0037。\n"}]

minimal_check：{"question": "核验E.1截断分解修正是否只改变常数。", "control": "对照原文分解与|a−ClipB(b)|≤min{|a−b|,2B}+(|a|−B)+，其余算法与假设不变。", "observable_outcome": "重新应用Lemma B.12和Proposition E.1，检查平均单步KL是否仍为O(δ+ηtε²t,score)，且不新增逐点或高阶score误差条件。", "resources": "原PDF用于核对符号；本篇p016–017、020–022的推导。无需训练模型，审计工时未估算。", "failure_or_stop_condition": "若修正仅改变B相关常数，则该疑点不影响量级；若必须增强score假设或改变精度阶数，则中心保证需重新评估。"}

missing_fields：["训练样本量、score网络结构、训练算力及采样墙钟成本未报告。", "原PDF图像、前作全文及作者另述改进版本未提供。", "F.1的完整证明及去除精确proximal oracle后的总成本未在所给材料中展开。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

仅score且弱L2条件下的高精度机制值得继续理解；以修正后的局部推导为入口，重点比较oracle及误差要求，不预设实用加速。

身份与随机接受机制：完整题名及35页当前附件一致。J~Poisson(2B)的乘积接受概率期望为exp(E[W|x]−B)，因此精确采样q exp(EW)，而非无条件精确采样未经截断的目标；梯度路径积分与截断偏差控制承担后者误差。B=Theta(1)是应用查询复杂度的重要条件。

核查定位：p001 title, PDF physical page4, Algorithm1/Theorem3.1, p006, Theorem4.1；mechanism_and_exactness_scope_confirmed

主保证的距离和oracle条件：原Cor4.2先给早停平滑分布KL，转回任意有限二阶矩原分布时给bounded-Lipschitz误差平方≤delta²+加权score均方误差；不是原分布TV保证。多对数精度依赖要求score误差同步变小，不含score训练代价。低维dstar是尺度相关覆盖熵，且Theorem4.7需要额外高斯平滑分布族上的最坏L2误差。

核查定位：PDF physical page6, Corollary4.2 and right column, p007, Definitions4.5–4.6/Theorem4.7；decisive_accuracy_metric_and_error_requirements_confirmed

E.1原式错误与有限修补：原PDF20页确认所印截断不等式对a=2B,b=0失败。正确式为|a−ClipB(b)|≤min{|a−b|,2B}+tauB(a)。以u上限2B应用B.12、以4B²归一化应用E.1(1)，尾项仍只作用于真score；固定B下局部单步KL保持O(eta epsilon_score²+exp(−cK))。同页边缘KL的链等式改成≤即可。详细推导保存，条件性修补不等于整篇证明通过。

核查定位：PDF physical page20, E.1, p016–p017, LemmaB.12, p021, PropositionE.1, local_check/clipping_repair.md；local_error_confirmed_and_same_order_repair_derived_conditionally

对数凹扩展和实际成本：附录F明确假设精确proximal oracle；平滑条件下说明可做凸优化但误差成本未完整展开。PI/LSI分支有初始化散度依赖，仅W2初始化的普通对数凹分支仍有1/epsilon²。全文结论承认每步多次score评估和保守步长，没有墙钟实验，不能把查询阶优势写成已实现推理加速。

核查定位：PDF physical page34, F/TheoremF.1, p008, Section5 and Conclusion；oracle_initialization_and_unmeasured_runtime_scope_confirmed

本地补充/限定：["截断问题已用原PDF确认并保存同阶局部修补；补充KL链等式应为上界，不以两处笔误直接否定主要结果。"]

核查局限：["未跑采样、score训练或前作比较实验。", "局部修补依赖所述引理，并未逐条形式验证35页全部证明。", "未读取作者脚注所指后续版本；第1页仅读题名及摘要开头，版本角色未确认。"]


## pro070 · GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training

论文 OR_cVO0eX8vLQ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5", "source_url": "https://api2.openreview.net/pdf?id=cVO0eX8vLQ\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "7892d4ab5b9f4f710bcde02885c92c027541e299da0da060c4db533e6d3613c4", "source_pdf_sha256": "24c47f25b1a5612197c2be191e8d9ddfdeacaa5569ab6e42e10a6bde77484d70"}], "read_ranges": ["TEXT_OR_cVO0eX8vLQ_24c47f25b1a5：物理页1–9正文，10–12致谢、影响声明及参考文献，13–28附录A–G；连续页标1–28完整。\n"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文提取文本，未查看PDF图像；图1–25的曲线、误差图及相关性可视化不可直接核读。", "双栏公式存在交错和符号损失；主要数值表可辨。仅图中呈现的结果不补写数值。", "未搜索、核读前作、比较其他版本、执行代码或复现实验。"]}

问题：如何仅用无物理标签的3D几何预训练神经模拟器，减少流体、固体等下游模拟所需的求解器标签与微调轮数？

方法：输入查询点、几何及逐点随机恒速向量；构造遇几何边界后粘附的轨迹，回归t=0,1,2三个时刻的vector distance。下游将随机速度替换为流向、光传播方向或冲击条件编码，并用物理标签微调；碰撞条件还采用空间衰减幅值。

作者主张：通过dynamics lifting弥合几何与物理之间的预训练任务差距。

论文证据：表8–12比较静态vector distance预训练、冻结几何条件及从零训练；表4显示该预训练也改善Galerkin Transformer和GNOT。

模型推断：中心增量是监督机制与条件接口，而非新骨干；证据支持可迁移性，但尚未隔离一般方向性几何增强与边界输运的作用。

定位：['TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.21 表4、p.23 表8–12。\n']

作者主张：百万级几何监督支持跨物理任务迁移、模型扩容及20–60%的标签节省。

论文证据：五个工业任务的表6、8–12支持精度、规模与数据效率收益；另有瞬态DTCHull和radiosity扩展。

模型推断：展示了有效的跨任务初始化，而非无需微调的通用物理求解器。

定位：['TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.22 表6、p.23 表8–12。\n']

key_results：[{"setting": "Base模型、8层、200轮微调。依次为DrivAerML、NASA-CRM、AirCraft、DTCHull、Car-Crash；训练/测试数分别为100/20、105/44、100/50、100/20、100/30。", "baseline": "同骨干Transolver从零训练；各骨干比较采用相同任务条件参数化。", "metric_or_guarantee": "relative L2，无量纲，越低越好；均为作者报告。", "reported_values_and_units": "从零训练：[0.0927, 0.0996, 0.1104, 0.1814, 0.1977]；GeoPT：[0.0746, 0.0880, 0.0904, 0.1459, 0.1772]。", "information_and_compute": "13,463几何×100动力学场，共1,346,300样本、约5TB；80个CPU核生成约3天。A100 40GB上B/L/H预训练约144/360/576 GPU小时，微调约3/6/10 GPU小时。预训练200轮，但每轮每几何只抽一个动力学场。\n \n", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.18 表2、p.19 表3、p.20 §E.2、p.22 表6。\n \n"}, {"setting": "上述五任务及顺序；Base模型，固定200轮考察标签节省，固定满训练集考察收敛轮数。", "baseline": "使用全部训练数据、训练200轮的Transolver。", "metric_or_guarantee": "达到不劣于基线的relative L2点估计；不等于端到端加速。", "reported_values_and_units": "GeoPT使用60/84/60/40/60样本分别达0.091/0.094/0.107/0.180/0.194，对应少用40/20/40/60/40%标签。满数据约需100/100/150/50/100轮达到基线，约为2/2/1.33/4/2倍轮数缩减；Car-Crash按表中舍入值持平。", "information_and_compute": "不包含预训练成本；摘要的2倍概述不能替代各任务结果，DTCHull表格支持4倍轮数缩减。", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.23 表8–12。\n"}, {"setting": "瞬态DTCHull采用稳态速度范数的1/5；radiosity为Cornell box内变化的bunny位置、尺度及光照，160训练/40测试。", "baseline": "分别从零训练，不是零样本迁移。", "metric_or_guarantee": "瞬态任务relative L2；radiosity为MAE。", "reported_values_and_units": "瞬态DTCHull：0.06189→0.05402；radiosity：0.097→0.090，MAE单位及归一化未说明。", "information_and_compute": "均需目标任务微调；瞬态滚动长度、时间划分及扩展任务独立算时未充分报告。", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.9 §5.3、p.19 §E.1、p.21 表4(a)。\n \n \n"}]

prior_work_candidates：[{"citation_as_printed": "Zhang, Z., Wu, Y., Zhang, K., and Wang, Y. From cheap geometry to expensive physics: A physics-agnostic pre-training framework for neural operators. In ICLR, 2026.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "利用几何预训练表示辅助物理预测。", "claimed_difference": "本篇称前作使用冻结编码器且几何模型限于3D inductors；GeoPT直接预训练骨干。实际对照以Hunyuan3D替代该编码器，并非原作直接复现。", "basis": "target_paper_only", "target_locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.12参考文献、p.21 §E.4。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Wu, H., Luo, H., Wang, H., Wang, J., and Long, M. Transolver: A fast transformer solver for pdes on general geometries. In ICML, 2024.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "几何通用神经模拟骨干与潜在状态聚合。", "claimed_difference": "新增预训练任务及条件化迁移，而非重新提出Transolver架构。", "basis": "target_paper_only", "target_locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.6 §4.3、p.12参考文献。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Faugeras, O. and Gomes, J. Dynamic shapes of arbitrary dimension: the vector distance functions. In The Mathematics of Surfaces IX: Proceedings of the Ninth IMA Conference on the Mathematics of Surfaces. Springer, 2000.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "vector distance几何特征。", "claimed_difference": "本篇沿合成轨迹预测该特征序列，未声称发明vector distance。", "basis": "target_paper_only", "target_locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.6 §4.3、p.11参考文献。\n \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心是明确且非显然的预训练机制增量，跨任务、跨骨干证据较充分；暂不足以提升为路线级首创判断。", "central_increment": "前作已使用几何表示辅助PDE预测（本篇转述）；本作新增合成动态轨迹监督，直接预训练物理骨干；表4、6、8–12支持迁移，尚待排除一般方向性几何增强的解释。", "soundness_observation": "式(8)仅为零损失下的初始切片一致性；A.1的守恒对象是合成粒子过程。实际回归vector distance并不自动等于估计相空间密度f，Remark A.2声称约束网络守恒的论证存在缺口；A.3也明确不保证普遍泛化。\n", "significance_observation": "有望节省昂贵物理标签；工程代价包括大规模几何处理、存储和预训练，不能把微调轮数收益当作推理或总成本收益。", "main_open_question": "在输入、监督维度和训练预算匹配后，几何边界约束的输运监督是否仍显著优于一般方向性几何增强？"}

limitations：[{"text": "速度场不能无损编码所有材料与模拟条件；复杂边界任务为主，无复杂边界的规则网格湍流仍属未来工作。", "basis": "author_report", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.28 §G。\n"}, {"text": "作者报告5次运行标准差并宣称95%置信区间支持数据节省、等效界0.001，但未列具体区间、逐次结果及检验程序，不能独立核验等效性。", "basis": "model_inference", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.22 表7及Statistical test。\n"}, {"text": "主比较匹配微调策略，不代表总训练算力匹配；Hunyuan3D代理基线也不足以覆盖所有几何预训练方法。", "basis": "model_inference", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.19 表3、p.21 §E.4。\n \n"}, {"text": "DTCHull称生成130个几何，表2只列100训练加20测试，其余10个用途未说明；不能据此擅自认定验证集或数据泄漏。", "basis": "model_inference", "locator": "TEXT_OR_cVO0eX8vLQ_24c47f25b1a5 p.18 表2及§E.1。\n"}]

minimal_check：{"question": "边界粘附是否贡献独立于方向性几何增强的迁移优势？", "control": "固定几何、查询点、速度、三个监督时刻及训练预算，只把碰壁停止替换为无边界自由飞行；两组在同一DrivAerML 60样本划分微调200轮。", "observable_outcome": "比较多种子测试relative L2差值及预先规定的非劣性区间。", "resources": "需对应几何、物理数据、两组预训练及GPU；原文Base的144 GPU小时预训练与约3 GPU小时微调仅供资源参考，复测实际成本未知。", "failure_or_stop_condition": "若自由飞行对照在预注册容忍界内不劣，则该设置不支持边界粘附的必要性；无法保持数据划分和预算一致时停止归因。"}

missing_fields：["PDF图像及仅图中呈现的精确数值", "前作全文及所选参考文献的DOI或arXiv标识", "逐次统计结果、完整置信区间及检验程序", "瞬态评测的滚动长度和时间划分", "Radiosity MAE单位、归一化及独立计算预算", "约30万几何扩展的完整量化结果与资源成本", "DTCHull剩余10个几何的用途"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

跨任务几何动态预训练有可操作的机制和较完整学习曲线；进一步阅读应集中于信息量匹配对照与预训练成本摊销。

身份和学习对象：完整题名及28页当前附件绑定。GeoPT回归随机恒速、遇边界粘附的三个时刻vector distance轨迹，直接预训练骨干，再用目标物理标签微调。不是无标签直接解真实PDE或零样本通用模拟器；任务条件以速度场编码，材料多属性可能丢失区分性。

核查定位：p001 title, p005, Eq6–7, p020, Algorithm1, p028, limitations；identity_and_pretrain_finetune_scope_confirmed

守恒解释不等于网络保证：A.1讨论合成粒子总质量（含边界累积）的守恒，A.2却把vector distance回归视为相空间密度f估计，并进一步称网络输出都守恒。实际监督是几何特征轨迹，不是归一化粒子密度；也无输出硬约束。因此该解释不足以给下游预测提供守恒保证，不能与FluxNet逐对抵消性质混同。

核查定位：p005, Eq6/Remark4.1, PDF physical page13, PropositionA.1/RemarkA.2, p020, VectorDistance targets；structural_guarantee_overinterpretation_not_supported

精度、标签和轮数节省：原表6同8层GeoPT五任务L2=.0746/.0880/.0904/.1459/.1772，对照.0927/.0996/.1104/.1814/.1977。原表8–12在200轮下分别60/84/60/40/60样本达不劣的点估计，即40/20/40/60/40%标签减少；满样本达到基线需100/100/150/50/100轮，Car-Crash按舍入值持平。它们是微调效果/轮数，不是总算力或推理速度。

核查定位：PDF physical page22, Table6, PDF physical page23, Tables8–12；decisive_values_and_savings_denominators_confirmed

完整资源口径：原表3为13463几何×100动态=1346300样本，约5TB；A10040GB预训练B/L/H约144/360/576 GPU小时，200轮微调约3/6/10 GPU小时。每个预训练epoch只从每几何抽一个动态，不能按200遍百万样本推算成本。DrivAerML还分20表面及400体积子集顺序推理，非全任务单次整网格推理。

核查定位：PDF physical page19, Table3, p020, pretraining/fine-tuning paragraphs；pretraining_amortization_and_actual_epoch_scope_confirmed

比较和统计可核验范围：几何条件基线使用Hunyuan3D代理编码器，非Zhang2026原方法直接重跑；骨干对照共享本篇条件参数化。表7有5次标准差并声称95%区间与.001等效界，但未列区间/逐次配对结果，当前仅确认点估计节省。静态与动态监督的维度和信息量不同，尚未隔离边界粘附和一般方向性增强。

核查定位：p021, E.4, PDF physical page22, statistical test/Table7, p020, Algorithm1；baseline_proxy_and_mechanism_attribution_limits_confirmed

本地补充/限定：["补充每epoch仅每几何一个动态的真实计算口径，以及DrivAerML分块推理例外。", "守恒仅是合成粒子过程的性质，未确认网络守恒。"]

核查局限：["未运行5TB数据生成、GPU训练、作者代码或前作复现。", "未重算等效性检验、未确认全部扩展几何曲线。", "第1页仅读标题开头；版本角色未独立核实。"]

