# 单轮全文初评与有界本地核对 91–100

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro091 · Towards Solving the Gilbert-Pollak Conjecture via Large Language Models

论文 OR_Cqq3HGRIuM；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_Cqq3HGRIuM_a6795dae94df", "source_url": "https://api2.openreview.net/pdf?id=Cqq3HGRIuM\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "a6795dae94df7a0555434a622f8e8add10a81f6f4cffbdb98d71614c5f437827"}], "read_ranges": ["TEXT_OR_Cqq3HGRIuM_a6795dae94df：物理页1–57全部已提供文本，含正文、参考文献、目录及附录A–H；页标连续，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅阅读文本，未查看PDF图像；图内几何关系及部分示例代码不可见。", "双栏正文存在交错，根号、分式及部分约束组排版受损，尤其p30、34、54–55；数值轨迹采用可读表3而非图9。", "最终机器证书及完整实现仅给外链，未随材料提供；前作全文未提供，版本角色未核实。本轮未搜索、执行代码或复现实验。"]}

问题：为任意有限平面点集的SMT/MST长度比建立更强统一下界，而非直接证明猜想值√3/2。

方法：将归纳剪枝写为Fτ=ρLt*+LS+−LS−的minimax充分条件。LLM接收几何规则及未认证区域，生成两类引理和条件化代码；经Mathematica与人工核查后转为verification functions。利用逐坐标单谷性质在盒顶点验证、单调性处理无界尾部，再以分支定界和二分搜索提高下界。这里的reward model是验证算法，并非训练出的评分网络。

作者主张：将Steiner ratio的一般下界从前作0.824提高到0.8559。

论文证据：附录E给出逐步引理，F给出验证算法，H.4声明最终全域覆盖证书成立；最终证书文件本身不在附件内。

模型推断：若证书及其数学前提成立，这是实质性的新全局保证；不是已经解决Gilbert-Pollak猜想，也不能将全部增量归因于LLM。

定位：['TEXT_OR_Cqq3HGRIuM_a6795dae94df：p29–36，附录E；p55–57，H.4–H.5。\n']

作者主张：通过受规则约束的引理生成、可认证奖励和瓶颈反思，使LLM参与开放数学问题研究。

论文证据：Definition 5、Theorem 6与20给出验证函数及构造路径；提供完整提示词、生成引理和去除瓶颈反馈的消融。

模型推断：形成了任务专用的搜索—验证接口，但Theorem 20展示的是两条充分构造路径，并未证明任意verification function都可等价分解为这两类引理。

定位：['TEXT_OR_Cqq3HGRIuM_a6795dae94df：p5–8，§3；p21–22，C.2；p41–47，附录G。\n']

key_results：[{"setting": "覆盖四种局部结构/参数情形的全域计算辅助证明", "baseline": "Chung & Graham (1985)的0.824，仅据本篇转述", "metric_or_guarantee": "Steiner ratio统一下界", "reported_values_and_units": "作者报告ρSteiner≥0.8559；较0.824提高0.0319，均为无量纲比值。", "information_and_compute": "不是数据集平均表现；依赖几何引理和全域覆盖认证，最终证书仅提供外链。", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p2，§1；p56–57，H.4–H.5。\n"}, {"setting": "代表性轨迹：D为regular point，f=d；表3共9阶段，包含初始基线", "baseline": "经典引理加扩大局部拓扑和计算枚举，初始下界0.8282；该阶段不是LLM生成", "metric_or_guarantee": "各阶段可认证下界", "reported_values_and_units": "0.8282→0.8500→0.8502→0.8519→0.8536→0.8540→0.8542→0.8558→0.8559；相对系统基线增加0.0277，后者为本轮差值计算。", "information_and_compute": "典型轨迹约0.5M tokens、4.6小时LLM推理、11.7小时reward model计算；全研究仅称数千调用、数百dollars，具体计费口径未详述。", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p27，D.1；p29，表3；p9，§4。\n \n"}, {"setting": "引理质量统计及两个LLM骨干实验", "baseline": null, "metric_or_guarantee": "引理有效率及达到报告下界的迭代轮数", "reported_values_and_units": "约100轮实验中，超过80%的所提引理被称为有效，即正确且帮助当步提高下界；GPT-5与Gemini 3 Pro均约十余轮到≈0.8559。", "information_and_compute": "未报告逐骨干样本数、方差、模型精确版本或新增训练。", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p8，§4。\n"}, {"setting": "移除瓶颈区域反馈的消融", "baseline": "保留瓶颈反馈的完整系统", "metric_or_guarantee": "下界是否继续提高", "reported_values_and_units": "移除反馈后10轮未提高下界；未列出重复试验分布。", "information_and_compute": "起点、token预算、验证预算及人工介入是否严格匹配未详述。", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p8，Reflection Ablation。\n"}]

prior_work_candidates：[{"citation_as_printed": "Du, D.-Z. and Hwang, F. K. A new bound for the Steiner ratio. Transactions of the American Mathematical Society, 278(1):137–148, 1983.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "归纳剪枝及隐式regular point距离界。", "claimed_difference": "扩大局部拓扑、枚举splits，并以新引理扩充认证覆盖。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p10参考文献；p16 Lemma 14；p26–27 D.1", "prior_actually_read": false}, {"citation_as_printed": "Chung, F. R. and Graham, R. L. A new bound for Euclidean Steiner minimal trees. Annals of the New York Academy of Sciences, 440(1):328–346, 1985.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "同一平面Steiner ratio统一下界问题。", "claimed_difference": "本篇比较其0.824与新报告值0.8559。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p2–3；p10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Du, D. Z., Hwang, F. K., Song, G. D., and Ting, G. Y. Steiner minimal trees on sets of four points. Discrete & Computational Geometry, 2:401–414, 1987.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "四点Steiner拓扑的几何存在条件。", "claimed_difference": "将既有条件转换、简化为满足正交凸性的参数约束，用于新验证函数。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p7 §3.2.2；p10参考文献；p16 Theorem 16", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是新的全局数学保证及可计算证明机制，超出一般场景调参；但当前证据不足以确认通用路线级创新。", "central_increment": "前作已做到归纳几何下界证明（本篇转述）；本作在局部结构全域认证条件下新增规则化引理搜索，报告0.8559；支持见表3及附录C–H，尚待核验最终证书。", "soundness_observation": "提供归纳、顶点最大和单调性论证，并报告CAD及作者人工核查，但不等于本轮独立验证。符号引理验证与提示词中C++ double接口如何衔接为无舍入误判的最终证书，文本未充分交代。", "significance_observation": "若认证成立，数学结果有明确价值；系统工程价值在于把发现过程与正确性检查分离，而非全自主解决猜想。", "main_open_question": "最终证书能否独立确认0.8559，并严密覆盖四种情形、边界及无界尾部？"}

limitations：[{"text": "CAD随变量和代数复杂度增加而难扩展；每个LLM引理仍需人工核查，并非全自主系统。", "basis": "author_report", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p9，§6"}, {"text": "系统基线已达0.8282，不能把相对历史0.824的全部提升归因于LLM；缺少等预算非LLM引理搜索对照。", "basis": "model_inference", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p27，D.1；p8，§4。\n"}, {"text": "预算耗尽返回False只能表示未认证，不能证明候选下界不成立；因此搜索终值还受区域预算限制。", "basis": "model_inference", "locator": "TEXT_OR_Cqq3HGRIuM_a6795dae94df：p37，Algorithm 1。\n"}]

minimal_check：{"question": "固定最终引理后，0.8559的覆盖证书能否独立通过？", "control": "不重新调用LLM；以作者证书和原验证器为对照，用独立精确或保守区间算术检查相同分区。", "observable_outcome": "四情形的覆盖、有限顶点不等式及无界方向单调性均成立，且无未决区域。", "resources": "需取得最终证书、实现和精确算术环境；硬件、内存及运行时间未知。", "failure_or_stop_condition": "发现误接收区域或覆盖缺口则不能确认该证书；证书缺失或精度不足时停止，不据此宣称猜想或下界已被反驳。"}

missing_fields：["最终机器证书、实际验证日志及数值误差控制细节。", "计算硬件、软件精确版本、区域阈值、二分精度和人工核查成本。", "逐骨干重复次数、随机性设置、消融预算匹配及引理有效率的独立基线。", "三篇候选前作的独立标识未提供，identifier_if_present为null；前作未实际核读。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

若最终证书独立通过，统一数学下界是明确中心增量；优先阅读其证书格式、四情形覆盖和保守算术接口，之后才评估LLM发现贡献。

身份与结果对象：题名及57页附件一致，目标是所有有限欧氏平面点集SMT/MST的下界0.8559，仍小于sqrt3/2；论文没有宣称已达到猜想值。历史0.824来自目标论文转述，不是本地核验的最新历史纪录。

核查定位：p001 title/abstract, PDF physical page56, H.4；identity_and_lower_bound_scope_confirmed

连续域验证接口：定义5逐坐标先降后升，子水平集正交凸；引理19以逐维补全面及轴线段证明含盒全部顶点则含整盒，局部推导成立。定理20仅两类充分构造且第一类仍需检查生成函数形状，不支持正文的任意验证函数等价分解措辞。Algorithm1超阈值False是未认证，不能判下界数学上不可行。

核查定位：PDF physical page5, Definition5/Theorem6, p021–022, Lemma19/Theorem20, PDF physical page37, Algorithm1；vertex_argument_confirmed_sufficiency_not_equivalence

四情形及无界尾部：D为regular/Steiner与f≤d/f>d组成四情形；困点引理可移植，四点引理仅在f=d符号验证，按p29用于边界归约后的Case2/4，在可变f≤d的Case1/3排除。p9笼统说在unbounded参数regimes排除，需以细则限定。p38单调性充分条件只覆盖至多三终端或x=f；p56代入f=d后在d方向单调还依赖原函数同时在d和f下降，需最终证书逐分支验证，不能从仅对f的筛选自动推得。未发现实际证书误接收，属于尚未核实接口。

核查定位：p009, limitations, p027, D.2, PDF physical page29, transplantation policy, p038, Proposition37, PDF physical page56, H.5；case_policy_and_extra_monotonicity_obligation_identified

数值轨迹与增量归属：表3九阶段含非LLM基线.8282，后为.8500/.8502/.8519/.8536/.8540/.8542/.8558/.8559。总对历史增加.0319，对系统基线增加.0277。基线已扩大拓扑并枚举splits，不把所有增量归给LLM；表3代表D regular、f=d，最终全域结论还靠其余情形。

核查定位：p027, baseline explanation, PDF physical page29, Table3, p008, experimental claims；trajectory_and_system_baseline_separated

认证证据和资源边界：附录H声明最终证书成立，但p57仅给外部实现/证书链接，没有在57页内给出可逐盒独立核验的完整机器产物。p44/46/47检索显示C++ double接口，正文Mathematica精确引理验证不能自行补足浮点全域覆盖误差控制。典型轨迹约.5M tokens、4.6小时推理与11.7小时验证，人工逐引理检查未计；移除反馈十轮不进步无同预算重复分布，不能确证通用性或全自主。

核查定位：p008–009, experiments/limitations, p044, p046–047, text search for double interfaces, PDF physical page55–57, H.4–H.5；final_certificate_not_independently_verified_and_cost_scope_confirmed

本地补充/限定：["确认顶点最大局部证明可跟踪，保留整体下界为作者报告的待独立证书核验结果。", "补充正文与附录四点引理使用情形差异，以及f=d代入后d方向单调性所需额外条件。"]

核查局限：["未下载或执行外部证书及作者代码，未全核57页引理、历史前作或当前最优纪录；没有宣称反驳0.8559。", "本地只核对列明页及double接口文本定位，未对所有几何图/约束做CAD或区间算术。", "版本角色未确认；历史及模型成本均按本文报告。"]


## pro092 · AutoNumerics-Zero: Automated Discovery of State-of-the-Art Mathematical Functions

论文 OR_n7F2nwPcYB；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a", "source_url": "https://api2.openreview.net/pdf?id=n7F2nwPcYB\n", "version_role": "current_attachment_unverified_role", "physical_pages": 23}], "read_ranges": ["TEXT_OR_n7F2nwPcYB_6e1ee790e75a：物理页1—23全部提供文本，包括正文、参考文献及附录A—D；连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图中程序代码及表1数值有可读文本，但性能曲线、计算图不可见。", "部分双栏、分式和上下标错位；B.2的f/E及B.3的ULP记号需对照原式，不能仅据提取文本完成证明核验。", "未提供前作全文、证明脚本或仓库文件；未搜索、执行代码或复现实验，版本角色未独立核验。"]}

问题：能否自动发现超越函数的短程序，在有限精度目标下减少基本运算，或提高特定硬件上的吞吐量？

方法：从恒等程序出发，外层dNSGA-II按误差—运算数的Pareto前沿异步选择，并随机增删、重连计算图；内层CMA-ES用正确输入输出样本优化系数，再以未见样本评估。默认算子为四则运算，Bessel加入sqrt；硬件版改用float32舍入、ULP误差及实测吞吐量。

作者主张：无预置逼近公式的搜索发现高效新表达式；10次运算的指数程序达到约14位精度，比同长度已知近似改善超过6个数量级。

论文证据：给出可读程序及区间算术误差界；还测试余弦、Airy、Bessel和erf，保留了高精度erf不占优的结果。

模型推断：新增价值是可认证的低成本求值结构，而非新的进化算法；四则运算程序仍属有理函数，优势在表示、复用与求值顺序。

定位：['TEXT_OR_n7F2nwPcYB_6e1ee790e75a p1 Abstract；p5—6 §4.1—4.5；p16—17 B.1—B.2；p20 Figure 11']

作者主张：硬件感知搜索得到误差低于1 ULP、速度超过最佳基线3倍的指数程序。

论文证据：B.3报告误差认证；附录C解释其分裂融合计算、避开并行任务派发开销的HLO机制。

模型推断：证明了搜索可利用编译器行为，但该加速不能直接解释为算术内核普遍更优。

定位：['TEXT_OR_n7F2nwPcYB_6e1ee790e75a p7 §4.6；p17—19 B.3及C；p23 Figure 15。\n']

key_results：[{"setting": "实数运算的2^x逼近，x∈(0,1]；域外通过range reduction扩展。", "baseline": "Taylor、Padé、Chebyshev、 polynomial/rational minimax及多种连分式。", "metric_or_guarantee": "最大相对误差的作者证明上界。", "reported_values_and_units": "10次基本运算：误差≤5.40×10^-15，约14位精度；该计数不含range reduction。", "information_and_compute": "§4.1搜索报告6,000核·天。系数优化样本1,000，评估约10,000，常规最终测试约100万；CMA-ES种群128、最多10,000代并早停。", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p14—15 A.5、A.9—A.10；p17 Table 1。\n"}, {"setting": "Ai(-7x)逼近，正文§4.3采用x∈(0,1]；A.1另写为[0,1]。", "baseline": "§4.2所用基线，包括Chebyshev；比较最佳20运算基线。", "metric_or_guarantee": "a=-log10(最大绝对误差)，采样估计。", "reported_values_and_units": "19运算程序a≈4.2；作者报告最大误差低约两个数量级。", "information_and_compute": "使用共同搜索配置；本任务独立核·天未报告。", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p6 §4.3；p13 A.1；p22 Figure 13。\n"}, {"setting": "I1/2(x)，x∈(0,1]，允许sqrt。", "baseline": "Frobenius及针对该函数手工构造的Chebyshev方案。", "metric_or_guarantee": "a=-log10(最大绝对误差)。", "reported_values_and_units": "进化程序8运算、a≈8.1；手工定制基线9运算、a≈7.8。", "information_and_compute": "本任务独立资源未报告；此处不是全域严格误差证书。", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p6 §4.4；p23 Figure 14。\n"}, {"setting": "硬件感知2^x核心，float32输入位于(0,1]。", "baseline": "同栈下误差低于1 ULP的最快基线；含Sollya优化的多项式minimax。", "metric_or_guarantee": "ULP误差上界及吞吐速度比。", "reported_values_and_units": "B.3报告上界0.654 ULP；正文报告速度超过基线3倍，图8图题报告跨所测架构最差仍快80%。", "information_and_compute": "最佳程序搜索9,600核·天；吞吐测试向量10,000、堆叠深度100、计时重复1,000取最短值，最终速度测试再重复10次。", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p7 §4.6；p15—16 A.7—A.10；p18 B.3。\n"}]

prior_work_candidates：[{"citation_as_printed": "Koza, J. R. Genetic programming: on the programming of computers by means of natural selection. MIT press, 1992.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "遗传编程与程序变异。", "claimed_difference": "本篇将其用于有限精度超越函数求值程序发现。", "basis": "target_paper_only", "target_locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p3—4 §2.3、§3；p11 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Deb, K., Pratap, A., Agarwal, S., and Meyarivan, T. A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE transactions on evolutionary computation, 2002.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "非支配排序与Pareto选择。", "claimed_difference": "dNSGA-II改为分布式抽样、无中心异步更新。", "basis": "target_paper_only", "target_locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p4 Method 1；p13—14 A.3；p10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Schkufza, E., Sharma, R., and Aiken, A. Stochastic optimization of floating-point programs with tunable precision. ACM SIGPLAN Notices, 2014.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "浮点程序的精度—计算成本优化。", "claimed_difference": "据本篇转述，前作改写既有程序并允许牺牲精度；本作从空代码同时搜索两个目标，未给出直接实测对照。", "basis": "target_paper_only", "target_locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p3 §2.3；p12 References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是带误差认证的高效新求值结构，不只是已有优化器的组合或局部跑分快；但材料不足以确认路线级首创。", "central_increment": "前作已能优化固定形式或改写程序（本篇转述）；本作在有界域、有限误差目标下搜索可复用中间值的结构，指数误差界支持实质增量，尚待排除更强同成本基线。", "soundness_observation": "IBEX区间界及Gappa结合穷举构成较强证据；未运行证明，且实数保证、float32保证与完整range reduction实现必须区分。", "significance_observation": "提供可复用的数值程序与较完整工程验证，但搜索成本高，尚无端到端应用收益或成本摊销实测。", "main_open_question": "允许同等中间值复用、复合及重复平方，并统一编译调度后，主要精度—成本优势是否仍成立？"}

limitations：[{"text": "“零知识”限于搜索中的逼近结构；域、监督值、算子及range reduction仍由外部提供，搜索前期算力需求高。", "basis": "author_report", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p9 §5.2。\n"}, {"text": "高精度erf上Padé更好；不能把指数结果推广为所有超越函数上的优势。", "basis": "author_report", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p6 §4.5。\n"}, {"text": "基本运算数未区分除法等成本，3倍加速又受默认编译调度支配；两种结果都不直接证明完整数学库的普遍加速。", "basis": "model_inference", "locator": "TEXT_OR_n7F2nwPcYB_6e1ee790e75a p5 §4.1；p15 A.8；p18—19 C"}]

minimal_check：{"question": "硬件版加速是否主要来自并行派发门槛？", "control": "固定论文编译栈，对进化程序和最佳基线分别测试默认设置及统一并行派发策略。", "observable_outcome": "比较吞吐比、HLO融合与派发路径，并确认两者误差仍低于1 ULP。", "resources": "需Skylake CPU、JAX/Jaxlib 0.4.11、Sollya及已给程序；无需重跑搜索，测试耗时未知。", "failure_or_stop_condition": "若统一派发后优势消失，则只能保留默认编译栈下的加速结论；若误差超阈值，停止同精度速度比较。"}

missing_fields：["图4、6—9逐点数据及消融效应量、重复间波动不可读。", "部分任务独立搜索预算、全项目总成本和应用级收益未报告。", "前作全文、DOI等标识及可执行证明材料未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

短程序、中间复用和分层误差证据具有直接复用价值；优先核对可执行证书和同求值结构/同编译调度基线，保留硬件依赖结论。

身份与新产物：AutoNumerics-Zero题名及23页附件一致。恒等程序起始、计算图变异、分布式Pareto选择和CMA-ES系数搜索；零知识仅不预置逼近形式，仍给定正确函数值、域、算子及外部range reduction。图11的10步实数有理程序确含三次重复平方及中间复用，不是浮点硬件版图15的14步程序。

核查定位：p001 title, p004–005, method, PDF physical page20, Figure11, PDF physical page23, Figure15；identity_and_distinct_real_vs_hardware_artifacts_confirmed

实数误差证据及证明文字修正：表1为10运算5.40e−15相对误差界，运算计数不含range reduction。B.2定义误差E后却继续对f导数/中心值求上界，原PDF17确有变量混用：若f仍是逼近2^x的函数，eta≤微小epsilon不可能是误差证明。可修正为对E及−E做区间包络并用中点m；这是一条局部证明写法修复路径，未运行IBEX，不能独立认证表1。原式导数含绝对值，不能误报其缺失。

核查定位：p016, B.1–B.2, PDF physical page17, B.2/Table1；reported_bound_confirmed_notation_error_and_repair_scoped

float32误差界：B.3将误差分为20阶实数Taylor、x86_80高精度参考舍入、与目标float程序的穷举差，非单靠Gappa证明最终程序。p17的ulp(2^x)≥1应为≥ulp(1)=2^−23，式2用ulp(1)仍是适当方向。p18给7.8e−8绝对误差再写≤.654 ULP；按印出上界乘2^23约.654311，而非严格≤.654，仍小于1。这是末位取整/记号问题，不构成反驳<1ULP；穷举及证明脚本未核验。

核查定位：PDF physical page17, B.3/Eq2–3, PDF physical page18, B.3；less_than_one_ulp_claim_scoped_rounded_constant_corrected

速度适用范围及成本：PDF7图7/8报告Skylake默认栈超过3倍、所测其他CPU最差约1.8倍。附录C明确基线单长fusion触发并行派发，进化程序两短fusion避开派发；不能推成同调度算术内核普遍3倍。JAX/Jaxlib.4.11，10000输入×100堆叠、1000计时取最短，优化吞吐非标量延迟。实数搜索6000核天、硬件9600核天；尚无端到端摊销。

核查定位：PDF physical page7, Figures7–8, p014–015, A.7–A.10, PDF physical page18–19, AppendixC；compiler_dependent_speed_and_search_cost_confirmed

本地补充/限定：["原PDF核实B.2中的f/E混用和B.3的ulp≥1文字错误；提供修复方向而非宣布数值程序失效。", "0.654只能视为印刷近似，按所列7.8e−8可推出约0.654312的保守上界且仍<1。", "目标float程序误差依赖高精度参考加穷举；不要把x86_80参考混作float32目标或宣称仅Gappa已经完成所有检查。"]

核查局限：["未执行作者程序、IBEX、Gappa、穷举或性能基准，也未查前作；仅做源文和纸面数量核对。", "第一次多页文本输出部分截断，关键B.2/B.3/速度页已实际查看PDF，未逐点重取其余函数的性能曲线。", "全部误差和速度结果仍为作者报告，版本角色未确认；当前研究未进行复现实验。"]


## pro093 · FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight

论文 OR_tnsQ23imeD；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_tnsQ23imeD_3f107f6a520b", "source_url": "https://api2.openreview.net/pdf?id=tnsQ23imeD\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "3f107f6a520ba24ea49b0590c4aba54baa9fd724eb89bc4b612959d2f366d239"}], "read_ranges": ["TEXT_OR_tnsQ23imeD_3f107f6a520b：物理页1—30全部已提供文本，包括正文§1—5、参考文献及附录A—D.11；连续页标未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF页图；图1—7的图形、曲线及误差带不可见。双栏文字存在错序，公式和表格仅按可辨文本读取。", "版本身份仍按清单标为未核实，不因附录自称camera-ready而认定出版版本；未核读前作、代码、原始轨迹或其他版本。"]}

问题：事后判断已执行智能体轨迹是否满足用户意图、安全约束和诚实性要求；不验证智能体内部策略，也不等同于执行前阻断。

方法：输入意图与动作—观察轨迹；自顶向下分解约束，先解析结构化事实，再用局部上下文LLM处理语义事实；合成Dafny谓词，经Boogie/Z3组合判定，可将违约事实和规约反馈给智能体重试。

作者主张：用双向Formal-of-Thought将概率语义判断与确定性逻辑组合分离，改善智能体监督。

论文证据：表1三基准×七智能体的21组比较均优于所列五种基线；§3.4明确保证以事实正确、规约忠实为条件。

模型推断：建立了可审计的监督流程，但没有消除自然语言到规约的错误。

定位：['TEXT_OR_tnsQ23imeD_3f107f6a520b：p5 §3.4；p7 表1']

作者主张：7B裁判检测72B智能体欺骗的准确率超过90%。

论文证据：Deceivers采用4×4裁判—智能体配对，每个智能体规模含200欺骗和200非欺骗轨迹；超过90%来自正文陈述，图5具体格点不可见。

模型推断：支持限定故障注入场景的弱到强检测，不构成任意强智能体可监督的保证。

定位：['TEXT_OR_tnsQ23imeD_3f107f6a520b：p7—8 §4.4。\n']

作者主张：形式反馈通过迭代修正带来近线性安全改善。

论文证据：作者报告Claude-4.5-Opus三轮后由70.7%至99.8%；Few-shot和CoT最终为83.5%和85.5%。

模型推断：支持结构化反馈的可用性，三轮结果不足以建立线性改善规律。

定位：['TEXT_OR_tnsQ23imeD_3f107f6a520b：p3贡献列表、p8 §4.5、p26 D.4.4。\n']

key_results：[{"setting": "Claude-4.5-Opus裁判，七智能体平均；依次为Agent-SafetyBench、VitaBench、Deceivers。", "baseline": "LLM；LLM + Python。", "metric_or_guarantee": "参考标签一致率，单位%；均为作者报告，不是本地复现实测。", "reported_values_and_units": "FormalJudge：76.2、74.8、93.7；LLM：59.9、66.2、65.4；Python：66.4、69.8、74.7。", "information_and_compute": "参考标签采用三模型各三轮多数票。VitaBench实际使用100任务切分；Deceivers为200任务双变体；Agent-SafetyBench本体2000例，但主表逐模型有效样本数未列。", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p6 §4.1、p7 表1、p14 表9、p15 B.1、p17 C.1。\n"}, {"setting": "X-Teaming风格补充测试，每目标每条件72情景；评价已完成轨迹。", "baseline": "Python与NL，共享抽取的轨迹事实。", "metric_or_guarantee": "不安全轨迹检测准确率%，不是攻击成功率。", "reported_values_and_units": "按FormalJudge/Python/NL顺序：Claude-4.5-Sonnet目标为98.6/93.3/85.8；GPT-4o目标为88.9/72.2/86.1。", "information_and_compute": "共享事实控制了部分信息差异；不计入三基准主汇总，未充分交代等规约和等调用预算。", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p12 A.2、表5。\n"}, {"setting": "评测harness中的每轨迹中位墙钟延迟。", "baseline": "单次LLM；LLM + Python。", "metric_or_guarantee": "秒及运行时间占比。", "reported_values_and_units": "FormalJudge 14.59秒，LLM 4.83秒，Python 12.32秒；Dafny编译与Z3求解占比小于6%。", "information_and_compute": "Deceivers限制最多10步/300秒，原子上下文3000 tokens、文件1500字符、Dafny超时180秒；未描述额外训练，硬件与总费用未报告。", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p13—14 A.4、表9—10；p21 表18。\n"}]

prior_work_candidates：[{"citation_as_printed": "Pan, L., Albalak, A., Wang, X., and Wang, W. Logic-lm: Empowering large language models with symbolic solvers for faithful logical reasoning. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 3806–3824, 2023.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "语言模型与符号求解器结合。", "claimed_difference": "本篇转向意图约束与智能体轨迹监督；未证明直接实现继承或前作覆盖范围。", "basis": "target_paper_only", "target_locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p3 §2、p11 References。", "prior_actually_read": false}, {"citation_as_printed": "Ma, L., Liu, S., Li, Y., Xie, X., and Bu, L. Specgen: Automated generation of formal program specifications via large language models, 2024.", "identifier_if_present": "arXiv:2401.08807", "relation_candidate": "方法继承", "shared_component": "LLM生成可验证规约的思路。", "claimed_difference": "作者明确称将规约合成思路扩展到智能体轨迹；不据此认定代码复用。", "basis": "target_paper_only", "target_locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p3 §2、p10 References。", "prior_actually_read": false}, {"citation_as_printed": "Guo, D., Liu, Q., Liu, D., Ren, Q., Shao, S., Qiu, T., Li, H., Fung, Y. R., Ba, Z., Dai, J., et al. Are your agents upward deceivers? arXiv preprint arXiv:2512.04864, 2025.", "identifier_if_present": "arXiv:2512.04864", "relation_candidate": "组件复用", "shared_component": "Deceivers任务与向上欺骗评测场景。", "claimed_difference": "本篇新增原子事实提取及Dafny组合检测流程。", "basis": "target_paper_only", "target_locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p10 References、p17—23 附录C。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "最明确的新增是面向轨迹监督的任务化流程、规则组织与反馈接口，具有跨场景性能价值；所示核心仍为既有规约生成与符号组合范式，尚不足支持路线级新机制判断。", "central_increment": "前作已有LLM结合求解器及规约生成（本篇转述）；本作在可信轨迹条件下新增原子监督—判定—反馈流程，表1及补充实验支持有效性，尚待排除规则和预算优势。", "soundness_observation": "条件保证表述合理，但不是端到端意图保证。p4图3的可见文本将“到达当天入住”编码为入住日≥到达日，二者并不等价，显示语义忠实性仍需核查。", "significance_observation": "对具有可信日志和可显式化约束的事后审计有实用意义；不能直接外推在线防御或真实部署事故率。", "main_open_question": "固定相同原子事实、规约和预算后，准确率收益有多少仍可归因于Dafny验证后端？"}

limitations：[{"text": "作者承认意图分解、语义提取和规约合成仍会出错；定性要求只能用代理变量表达，可信工具轨迹被改写时需外部来源证明。", "basis": "author_report", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p5 §3.4、p9 §5、p13 A.3、p14 A.5。"}, {"text": "Oracle仍由LLM组成且包含主裁判Opus；一致率不是独立人工真值，相关误差无法排除。补充实验虽共享事实，但尚非主三基准上的同规约、等预算后端消融。", "basis": "model_inference", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p6 §4.1、p12 A.2。"}, {"text": "摘要的平均提升16.6%缺少明确权重和单位口径；对表1已给21格作等权算术核对，绝对差均值约17.75个百分点，不能直接复得16.6%。", "basis": "model_inference", "locator": "TEXT_OR_tnsQ23imeD_3f107f6a520b：p1 Abstract、p7 表1。\n"}]

minimal_check：{"question": "后端优势是否主要来自不同规则或代码生成，而非形式求值本身？", "control": "冻结Deceivers同一组15个原子事实及同一布尔规约，对比直接Python求值、Dafny和原生成式Python基线。", "observable_outcome": "逐例判决差异、参考标签一致率及错误来源。", "resources": "作者缓存的事实、规约和基线代码，CPU与Dafny/Z3环境；无需重训，产物尚未提供，耗时未知。", "failure_or_stop_condition": "若同规约Python与Dafny一致且共同优于原Python，则优势更可能来自上游规则或生成过程；无法恢复对应产物时停止因果归因。"}

missing_fields：["图4—7逐点结果、完整误差信息及原始逐例预测。", "主实验有效样本分母、置信区间、完整调用和重试预算、硬件及总费用。", "弱到强实验逐阶段骨干、规约及原子模板自动生成与人工设计的边界。", "16.6%聚合口径及迭代99.8%对应的准确率/通过率定义。", "Logic-LM在本篇参考文献中未提供独立标识符。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可信日志的原子事实与可检查反馈有实用价值；关键后续是固定事实和规约比较后端，并检查语义缺口及独立标签，暂不接受端到端安全保证。

身份与保证边界：FormalJudge题名和30页附件一致；事后轨迹分解、提取、Dafny/Boogie/Z3组合。section3.4明确仅在事实正确、规约忠实时保证组合判决；不验证内部策略或保证在线阻断。p4定义原子事实全为bool而图3用成本/日期类型，也需区分原始类型化事实和其上布尔谓词。

核查定位：p001 title, p004–005, sections3.1–3.4；identity_and_conditional_not_end_to_end_guarantee_confirmed

图3语义反例：原PDF4确将must start on arrival day写为checkin≥arrival。把示例入住由Mar15改Mar17，保持Mar16到达与750≤800，所列两条谓词会通过，但仍违反当天入住要求；正确对应为等号。确定性求解器不能自动修复这种规约语义偏差；这不证明主测试全用同一错误模板。

核查定位：PDF physical page4, Figure3；one_day_late_counterexample_to_printed_specification_confirmed

主表收益与参考真值：PDF7表1共21格FormalJudge均为所列最高。对比vanilla差值逐格相加372.70/21≈17.7476个百分点，不能从此等权口径复得摘要16.6%；未报告权重时不擅自替作者定义。参考是含主裁判Opus在内的三模型各三轮多数票，衡量与模型oracle一致率，不是独立人工真值或部署事故率。

核查定位：p001 abstract, p006, Evaluation Protocol, PDF physical page7, Table1, PDF physical page14, Table9；table_dominance_confirmed_aggregation_and_reference_limits

弱到强与反馈实验：PDF8图5b的7B裁判/72B智能体格为对最佳基线+24个百分点；曲线及正文支持所设文件故障场景约91–96%，不等于任意强代理监督。三轮99.8%文中称safety classification accuracy又描述修正行为，终点定义需澄清。PDF26明确迭代实验Opus做分解/规约，因此7B/14B受反馈提升不能称完整弱模型流水线；不能把这条配置未经证据直接套到独立弱到强实验。

核查定位：p007, section4.4 sample200+200, PDF physical page8, Figure5/section4.5, PDF physical page26, D.4.4；observed_figure_and_distinct_experiment_backbones_scoped

对照与成本：补充X-Teaming72情景每目标每条件：Sonnet98.6/93.3/85.8、GPT4o88.9/72.2/86.1为FormalJudge/Python/NL，共享提取事实但不声明完全同布尔规约。主Python是生成自由检查代码，不能据差值归因Dafny后端数学必然优越。中位14.59秒对4.83/12.32，Dafny+Z3<6%，其余主要LLM；保持同规约、同事实的确定性Python应作为未来对照。

核查定位：PDF physical page12, Table5, PDF physical page14, Tables9–10, PDF physical page20, Python baseline；shared_facts_not_identical_specification_and_latency_confirmed

本地补充/限定：["实看PDF确认日期不等号，给出翌日入住的具体误接受例。", "补录图5b可读的7B→72B相对最佳基线+24个百分点，不能从图中倒推出未印出的精确绝对率。", "将迭代试验已知Opus依赖与弱到强实验逐阶段模型未知分开，避免跨实验误推。"]

核查局限：["未运行Dafny/Z3、作者代码或重标轨迹，未核读前作；纸面日期反例不是全基准复现。", "没有据附录自称camera-ready改写来源版本角色；图4曲线未逐点数字化。", "百分比聚合与99.8%终点定义仍需原始数据；不将分类一致率作为绝对安全概率。"]


## pro094 · Graph Neural Networks Are Not Continuous Across Graph Resolutions

论文 OR_powiRLgonD；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_powiRLgonD_1756f3bfc4fa", "source_url": "https://api2.openreview.net/pdf?id=powiRLgonD\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "d75a72f1d47083a19dbed81f5d78099aadb234827db698ee184fb4cf7f717533", "source_pdf_sha256": "1756f3bfc4fab0380a3e612fa40ec8a8cdc5d974fe9d346098abe45d76094348"}], "read_ranges": ["TEXT_OR_powiRLgonD_1756f3bfc4fa：物理页1—53全部提供文本；正文§1—9、参考文献、附录A—I，页标连续，无页标缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF页面图像，图1—26均不可见，不能核验曲线、坐标或图中数值。", "部分公式上下标、粗图横线、范数及积分符号失真；附录F存在重复定理编号；表5的ChebNet与GIN行串联，未采用这些行的数值。"]}

问题：同一对象的细图与粗图在热扩散意义上接近时，GNN为何仍生成不同表征，如何让预测随分辨率变化保持一致？

方法：以自然拉普拉斯L=M⁻¹(D−A)构造Ψ(L)=∫e^(−tL)dν(t)。谱网络以其替换归一化拉普拉斯多项式；MPNN以Ψ的矩阵元素加权消息求和，并先做一次输入扩散。粗图特征取J↓X，图级读出为节点质量加权的逐通道绝对值和。

作者主张：常见GNN跨尺度不连续源于传播结构，而非仅训练不足。

论文证据：附录D分析谱归一化、对称归一化和消息传递的极限；QM7表1—2展示跨分辨率误差及表征差距。

模型推断：提供有实质价值的失效机制；结论针对指定粗化收敛和架构，不是所有GNN、所有扰动下均不连续。

定位：['TEXT_OR_powiRLgonD_1756f3bfc4fa：p3—4，§3—5；p19—28，附录D。']

作者主张：Laplace-transform传播使谱网络和MPNN获得跨尺度连续性。

论文证据：定理7.1及附录E、F给出节点和图级误差界；实例采用正时间指数及正参数resolvent。

模型推断：增量是从已有resolvent谱方法扩展至统一传播与MPNN保证，而非首次使用热核。

定位：['TEXT_OR_powiRLgonD_1756f3bfc4fa：p6，定理7.1；p29—38，附录E—F。']

作者主张：方法在分子、社区图、节点分类和连续流形离散化中保持尺度一致性。

论文证据：QM7与SBM有可读表格；CORA/CITESEER复制节点、环面细化的主要证据为不可见图及正文描述。

模型推断：支持多种受控设置，但节点分类是在各扩展图上分别训练，不等同于固定模型跨分辨率迁移。

定位：['TEXT_OR_powiRLgonD_1756f3bfc4fa：p7—9，§8；p38—46，附录G。']

key_results：[{"setting": "细图向质量守恒粗图的热核收敛。", "baseline": "常见归一化谱传播及邻接消息传播。", "metric_or_guarantee": "图级表征误差的热核积分上界。", "reported_values_and_units": "作者给出∥Fω−F̄∥≤C·max_i∫|ψ̂_i(t)|∥e^(−tLω)−J↑e^(−tL̄)J↓∥dt，并据此主张连续性；不是无条件的任务误差保证。", "information_and_compute": "要求对应输入、质量与读出；常数受网络参数、深度、输入及证明中的有界性条件影响。", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p6，定理7.1；p38，定理F.3。\n"}, {"setting": "QM7共7165分子，随机1500测试、其余训练，5个随机种子；高、低分辨率双向测试。", "baseline": "GCN、GATv2、ChebNet、GIN及多尺度基线。", "metric_or_guarantee": "MAE，单位kcal/mol；均值±标准差。", "reported_values_and_units": "Spectralexp.高→低15.9±1.1、低→高16.0±1.5，分别与对应同尺度结果相同；GCN高→低136.7±6.6、低→高138.1±2.4，同尺度均63.6±1.3。Lanczos高→高9.9±2.5，但高→低938.4±2.5，故本文优势主要是迁移而非全面同尺度最优。", "information_and_compute": "原子电荷one-hot，粗图采用投影后的组成特征；报告两层、宽64及单张RTX8000。基线mean读出，新方法质量加权读出。", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p7，表4；p39—40，G.1。\n"}, {"setting": "SBM：12簇、每簇60节点，p_inter=2/60²；表5比较p_connect=1与粗图。", "baseline": "GCN。", "metric_or_guarantee": "未归一化潜在表征距离，无物理单位。", "reported_values_and_units": "Spectralres.为0.12±0.07；GCN为4.39±2.95，均为作者报告。", "information_and_compute": "随机单位范数节点特征；每个p取100个随机图；单张RTX8000。", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p8，表5；p41，G.3。\n"}, {"setting": "附录I的QM7与大图资源测试；大图表8未区分具体数据集。", "baseline": "ChebNet。", "metric_or_guarantee": "峰值GPU内存与每epoch时间。", "reported_values_and_units": "QM7：Resolvent 184.8±0.1 MiB、0.7±0.1 s，ChebNet 230.8±0.8 MiB、0.8±0.1 s；大图：Resolvent 168.9±0.9 MiB、35.86±0.19 ms，ChebNet 551.0±9.0 MiB、107.14±1.21 ms。", "information_and_compute": "未单列传播矩阵构建时间、完整训练成本及大图稀疏化精度代价。", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p52—53，表6、8。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Koke, C. Limitless stability for graph convolutional networks. ICLR, 2023.", "identifier_if_present": "OpenReview:XqcQhVUr2h0", "relation_candidate": "理论扩展", "shared_component": "resolvent谱滤波及稳定性/迁移分析。", "claimed_difference": "本篇转述其主要处理谱网络；本篇扩展到一般Laplace-transform传播和MPNN。", "basis": "target_paper_only", "target_locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p10，参考文献；p16，附录B。正文小标题将该前作写作Limitless transferability，与参考条目不一致。", "prior_actually_read": false}, {"citation_as_printed": "Koke, C., Saroha, A., Shen, Y., Eisenberger, M., and Cremers, D. Resolvnet: A graph convolutional network with multi-scale consistency. NeurIPS 2023 Workshop on New Frontiers in Graph Learning (GLFrontiers), 2023.", "identifier_if_present": "OpenReview:V5eDwEDfXT", "relation_candidate": "方法继承", "shared_component": "多尺度一致性主题；作者明确列为本研究早期非归档版本。", "claimed_difference": "仅统称早期成果被本篇涵盖和扩展，未逐项说明。", "basis": "target_paper_only", "target_locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p11，参考文献；p16，Previous versions。", "prior_actually_read": false}, {"citation_as_printed": "Koke, C., Rieck, B., Bronstein, M. M., and Cremers, D. Scale continuity in graph learning: Going beyond spectral methods. ICLR 2026 Workshop on Geometry-grounded Representation Learning and Generative Modeling, 2026.", "identifier_if_present": "OpenReview:RYl2VWfIRI", "relation_candidate": "理论扩展", "shared_component": "跨尺度连续性及非谱方法；依据题名和早期版本声明。", "claimed_difference": "本篇未列出相对该工作坊版本的新定理或新实验清单。", "basis": "target_paper_only", "target_locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p11、p16。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是可辨认的失效机制、统一传播构造及条件性保证，超过局部性能修补；但已有同作者resolvent与多份早期版本，不宜据此认定路线首创。", "central_increment": "前作已研究resolvent谱网络迁移（本篇转述）；本篇在热核粗化收敛下扩展到统一谱/消息传播，并提供受控跨尺度实验。", "soundness_observation": "正时间指数与resolvent实例的构造逻辑清楚。由逐点热核收敛推出一般Laplace传播连续性，仍需核对可积支配及t=0原子/恒等项的排除；附录C的允许测度范围未明确这一边界。未完成逐式证明审计。", "significance_observation": "为需要忽略细节、保留粗结构的任务提供架构设计原则；不是普遍提高图辨别力的方案。", "main_open_question": "统一节点质量处理、读出方式和调参预算后，跨尺度预测优势有多少仍可独立归因于传播算子？"}

limitations：[{"text": "尺度连续性并非所有任务都需要；严格区分非同构程序图、电路图时，细结构可能不可忽略。", "basis": "author_report", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p14，附录A。"}, {"text": "基线mean与新方法质量加权绝对值读出同时变化，未隔离传播贡献；不同模型的绝对嵌入距离还受表征幅值影响。", "basis": "model_inference", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p40，G.1。\n"}, {"text": "节点复制实验允许重新训练和额外滤波超参搜索，不能视为固定模型的零样本尺度迁移。", "basis": "model_inference", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p41—42，G.4。"}, {"text": "大量小矩阵元素不自动保证截断误差小；精确算子的连续性保证尚不能直接转给稀疏化实现。大图计时缺少清晰的数据集归属和构建成本。", "basis": "model_inference", "locator": "TEXT_OR_powiRLgonD_1756f3bfc4fa：p51—53，附录I。"}]

minimal_check：{"question": "QM7迁移优势是否主要来自传播，而非读出差异？", "control": "做传播算子GCN/Spectralexp.×读出mean/质量加权的2×2对照，固定电荷输入、两层宽64、分割、5个种子和调参预算。", "observable_outcome": "比较高↔低MAE增量及归一化嵌入差；检查统一读出后传播优势是否保留。", "resources": "QM7和作者实现；硬件可参照论文单张RTX8000，完整运行预算未报告。本轮未执行。", "failure_or_stop_condition": "若仅更换读出即可消除主要预测差距，则任务性能的传播归因不足；若无法统一输入或预算，则不作因果归因。"}

missing_fields：["图形原件及图内定量曲线。", "QM7优化器、学习率、批量、训练总轮数和完整搜索预算。", "传播矩阵构建成本、大图表8所属数据集及截断后的精度与连续性误差。", "前作全文、早期版本逐项差异及当前附件的最终出版版本身份。", "失真公式的PDF核对与独立证明审计。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

热核粗化提供清晰设计原则，正时间实例及迁移结果值得读；需收窄测度类、统一读出对照，并把精确算子保证与稀疏实现分开。

身份和中心机制：题名及53页附件一致；强簇内耦合粗化以自然质量拉普拉斯热核收敛定义尺度接近，非任意图扰动。谱滤波替换为Laplace传播，MPNN另需一次输入预扩散；输入按Jdown投影，读出是质量加权逐通道绝对值和，质量在粗节点相加。

核查定位：p001 title, p005–006, sections6–7, PDF physical page33, DefinitionE.2, PDF physical page38, graph aggregation lemma；identity_and_correspondence_conditions_confirmed

t=0原子边界反例：定义6.1及附录C允许[0,infty)的有限测度/Dirac，未明确排除0。若取nu=delta0，则Psi=I。两单位质量节点以权重omega相连，L=omega[[1,-1],[-1,1]]，每t>0热核趋向二点平均投影；粗图单节点质量2。输入(1,-1)、投影输入0、一层单位权重恒等激活、质量绝对值读出，细图F=2而粗图Fbar=0，对所有omega不收敛。积分误差上界本身可仍成立，错误是从t>0逐点收敛推出含0原子的积分趋0。加有限总变差、无0原子及一致热核界可用支配收敛修复；正时间指数和正参数resolvent实例不受这个反例否定。

核查定位：PDF physical page5, Definition6.1, PDF physical page6, Theorem7.1 following paragraph, PDF physical page17–18, AppendixC, PDF physical page33, readout；literal_generalized_filter_continuity_boundary_counterexample

滤波表示公式：原PDF18确将(-t)^(k−1)exp(-lambda t)的Laplace变换直接写为(z+lambda)^−k，缺符号及阶乘；实际积分是(-1)^(k−1)(k−1)!/(z+lambda)^k。表示正resolvent幂的正确密度为t^(k−1)exp(-lambda t)/(k−1)!。线性可学习系数可吸收固定倍数，但积分表示不应原样引用；该修正不改变已明确定义的正resolvent矩阵。

核查定位：PDF physical page5, resolvent example, PDF physical page18, ExampleC.10；laplace_density_normalization_error_confirmed

数值结果和实验协议：PDF7表4确认Spectralexp高→低15.9±1.1/低→高16.0±1.5与同尺度相同；GCN跨尺度136.7/138.1对应同尺度63.6，Lanczos同尺度9.9却跨尺度938.4。PDF8表5Spectralres.12±.07对GCN4.39±2.95；现在图像可解ChebNet4.67±2.76、GIN24877.22±279.41，但不将绝对嵌入幅值当标准化质量。基线mean读出与新法电荷加权同时改变。节点复制每个k上重新训练，LTF还搜索深度、归一化及lambda，非固定模型零样本迁移。

核查定位：PDF physical page7, Tables3–4/Figure8, PDF physical page8, Table5, p040–042, G.1/G.3/G.4；source_tables_and_readout_training_confound_confirmed

稀疏与吞吐：PDF52/53所列内存和epoch时间与Pro一致，大图表8未分别标注两个数据集。小元素数量本身不能界定截断算子范数：N×N全部1/N每项趋0但谱范数1，逐项固定阈值全删会损失整体传播。该例只说明所用论据不足，不是本文实际resolvent截断误差的测量；应附矩阵构建时间、截断误差与准确率。

核查定位：p006, Scalability, PDF physical page52, Figure26/Table7, PDF physical page53, Table8；reported_resource_values_confirmed_sparsification_guarantee_missing

本地补充/限定：["将t=0原子疑点落实为二点粗化反例；只限制通用测度宣称，不否定正时间指数和resolvent。", "补充resolvent幂的密度阶乘/符号，并由PDF补核原提取串联的SBM表格行。"]

核查局限：["未核读引用前作或早期版本、未逐式审计F节、未运行GNN/截断实验；两个反例仅为纸面边界检查。", "局部反例没有反驳作者已测正时间模型结果；未独立验证完整常数、范数选择和全部公式。", "当前附件角色未核实，结果为作者报告而非本地复现。"]


## pro095 · Fixed Aggregation Features Can Rival GNNs

论文 OR_gSZhNPp103；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_gSZhNPp103_782fb63b38e5", "source_url": "https://api2.openreview.net/pdf?id=gSZhNPp103\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_gSZhNPp103_782fb63b38e5：物理页1–30连续全文；包括正文、参考文献及附录A–G，未发现缺页标。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文文本，未看过PDF图像；图1–6、训练曲线和SHAP图的图形内容不可见。", "双栏文字交错，公式上下标与表格强调格式可能有损；不据图题或残留坐标补推数值。", "版本是否为最终出版版未核；前作全文、代码和运行日志未提供。本轮未搜索、复现或执行作者代码。"]}

问题：含节点属性的图预测任务，是否必须学习逐层邻域聚合，还是固定统计特征加分类器已经足够？

方法：输入图结构与节点特征；各reducer独立递归聚合K轮，拼接原始特征和各跳结果，得到F(1+|R|K)维向量，再用标签训练MLP。FAF4使用mean、sum、max、min；另测std等变体，按验证集选型。免训练仅指特征聚合，不包括分类器。

作者主张：FAF结合精调MLP可在14个标准节点分类基准中的12个媲美或超过GNN。

论文证据：正文实际分为5项领先、5项在误差或1个百分点内、4项落后；Cora和Citeseer也落后，并非只有两个例外。表10–11支持多数任务受益于非线性分类器与跨跳拼接，但并非逐集都更优。

模型推断：证明固定统计在不少现有设置中已经够用；没有区分任务本身不需要学习聚合，还是现有GNN未学好聚合。

定位：['TEXT_OR_gSZhNPp103_782fb63b38e5，物理p7，§5；p8表1；p26表10–11。\n']

作者主张：说明固定无损聚合的理论可能性，并解释常用归约保留的信息及表达力与可学习性的差别。

论文证据：定理4.1讨论正交特征状态上的sum单射；mean另需度数信息。定理4.2明确重述Schmidt-Hieber既有定理。KA实验多数任务较差，Roman-Empire则报告80.33±0.47%准确率。

模型推断：新增主要是图邻域语境下的条件化解释，而非首次建立KA表示定理；实际FAF并不具有普遍无损保证。

定位：['TEXT_OR_gSZhNPp103_782fb63b38e5，物理p5–6定理4.1–4.2；p15附录A.2；p27表12。\n']

key_results：[{"setting": "表1：验证集选出的FAF与重跑经典GNN比较。", "baseline": "各数据集最强的GCN、GAT或GraphSAGE。", "metric_or_guarantee": "准确率%；Minesweeper按表2为ROC-AUC×100，不能沿表1标题统称准确率。", "reported_values_and_units": "Pubmed：FAF 80.96±1.06，GCN 80.00±0.77；Citeseer：70.48±1.24对72.72±0.45；Roman-Empire：78.11±0.38对GCN 91.05±0.15；Minesweeper：90.00±0.39对SAGE 97.72±0.70。", "information_and_compute": "主要设置为全图特征与边可见的传导学习；每数据集3–10个划分取平均，A100、每次2500轮；均为作者报告。", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p8表1；p16表2；p17附录B.2。\n"}, {"setting": "固定2500轮的训练时间比较。", "baseline": "GCN。", "metric_or_guarantee": "平均训练时间，秒。", "reported_values_and_units": "Amazon-Ratings：FAF1 17.33±0.58，GCN 140.30±0.58；Coauthor-Physics：FAF1 532.70±0.58、FAF4 2383.00±0.58，GCN 65.33±0.58。", "information_and_compute": "A100；高维特征可抵消预传播收益。未单列聚合预计算及完整搜索成本，不能解读为统一的端到端加速。", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p17表3。\n"}, {"setting": "GraphLand四个数据集的初步实验，平均10次运行。", "baseline": "转录的ResMLP-NFA、GCN、GAT。", "metric_or_guarantee": "测试准确率%。", "reported_values_and_units": "四集FAF均低于GAT；例如pokec-regions：FAFmean 31.23±0.18，ResMLP-NFA 8.05±0.03，GCN 34.96±0.38，GAT 46.17±0.32。", "information_and_compute": "FAF仅探索mean及mean+std，未完成全量超参数搜索。", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p28–29附录F、表15–16。\n"}, {"setting": "GraphBench的quotes、replies初步实验。", "baseline": "基准已报告的GNN，正文称MPGNN。", "metric_or_guarantee": "测试MAE，越低越好；目标变量单位未说明。", "reported_values_and_units": "quotes：FAFmean 0.661±0.002对0.768±0.002；replies：0.579±0.001对0.694±0.002。", "information_and_compute": "双方未专项调参，FAF移植GraphLand超参数；不是完整基准验证。", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p29附录F、表17。\n"}]

prior_work_candidates：[{"citation_as_printed": "Frasca, F., Rossi, E., Eynard, D., Chamberlain, B., Bronstein, M., and Monti, F. Sign: Scalable inception graph neural networks. In ICML 2020 Workshop on Graph Representation Learning and Beyond, 2020.", "identifier_if_present": null, "relation_candidate": "方法继承（结构相近，直接继承关系待核）", "shared_component": "预计算固定多跳扩散、拼接并后置训练。", "claimed_difference": "FAF加入非线性统计归约，强调基准诊断而非仅可扩展性。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p3 §2；p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Bazhenov, G., Platonov, O., and Prokhorenkova, L. Graphland: Evaluating graph machine learning models on diverse industrial data. In The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2025.", "identifier_if_present": "OpenReview: Gyq8lMgdk5", "relation_candidate": "比较基线", "shared_component": "NFA将一跳邻域统计加入表格预测。", "claimed_difference": "本篇将其视为一跳FAF实例，扩展到多跳与更多归约组合。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p3 §2；p9参考文献；p28–29附录F。", "prior_actually_read": false}, {"citation_as_printed": "Schmidt-Hieber, J. The Kolmogorov–Arnold representation theorem revisited. Neural Networks, 137:119–126, 2021.", "identifier_if_present": "doi:10.1016/j.neunet.2021.01.020", "relation_candidate": "组件复用", "shared_component": "固定不连续编码及连续读出分解。", "claimed_difference": "用于解释图邻域聚合及可学习性；目标论文定理4.2明确沿用该前作定理。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p6定理4.2；p12参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心价值是已有固定传播范式的系统扩展、强基线校准与适用边界梳理；尚不足以确认独立的新机制或一般保证。", "central_increment": "SIGN已能固定传播并拼接，NFA已有邻域表格化（均为本篇转述）；本作在标准节点基准上加入更丰富归约与精调MLP，并用消融定位收益。支持为表1、10–17；尚待排除主要增量来自更强调参。", "soundness_observation": "按可见文本，A.2计数式将正交直接当作正交归一，缺少范数因子；若允许零特征，单射性还需补条件。这是局部证明表述问题，不足以否定实验结果。\n", "significance_observation": "适合作为检验学习消息传递是否必要的强基线。实现机制简单，但高维缓存和搜索成本不可忽略；不能据此宣布GNN普遍无用。", "main_open_question": "与SIGN/NFA在相同分类器容量、数据划分及搜索预算下比较，FAF还保留多少独立增量？"}

limitations：[{"text": "主实验集中于富属性、传导式节点分类；归纳测试需要重算邻域特征，外推到其他图任务尚未充分验证。", "basis": "author_report", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p18附录B.4。"}, {"text": "相似超参数范围不等于相同搜索预算；GNN残差、分类器容量也存在差异。GESN仅移植配置，Transformer结果主要转录前作，不能视为统一充分调优的直接对照。", "basis": "model_inference", "locator": "TEXT_OR_gSZhNPp103_782fb63b38e5，物理p17附录B.2；p28附录E；p29–30附录G。"}]

minimal_check：{"question": "非线性归约是否提供超出固定线性多跳特征的独立收益？", "control": "在Amazon-Ratings上比较FAF4与SIGN式固定线性多跳输入，保持划分、跳数、读出容量和验证搜索预算一致。", "observable_outcome": "测试准确率差及含预计算的时间、峰值显存。", "resources": "数据、划分与两种实现；参照论文使用A100，总运行预算未知。", "failure_or_stop_condition": "若匹配预算后差异消失，则不支持独立归约机制增量；此单集检查不能替代14集结论复核。"}

missing_fields：["图像、可靠公式原版；前作全文及代码日志。", "实际搜索次数、总GPU时、单列预计算成本及±的统计定义。", "B.2列MLP深度为2/3/5，但表5给Minesweeper为12，需核协议。", "GraphBench目标单位与运行次数未明确；SIGN参考条目未列外部标识。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

应把FAF纳入图任务强基线，但独立方法增量需与SIGN/NFA同预算匹配；12/14和免训练的宽口径不宜直接引用。

身份与免训练范围：题名及30页附件相符；各reducer独立递归K跳、拼接原始与逐跳特征，维数F(1+|R|K)，再监督训练MLP。免训练仅指聚合。FAF4是mean/sum/max/min，多变体验证选型，不能把固定聚合称整个系统无需学习。

核查定位：p001 title, p004, Eq1–2, p007, experimental setup；identity_and_trainable_readout_confirmed

一跳正交计数证明：PDF15明确distinct feature states只要求两两内积零。非单位非零向量需n_x=x^T h/||x||²；例如x=(2,0)出现一次内积4非1。加非零条件即可修补单射；若允许0，则{0}与{0,0}同和0而不同多重集，字面原假设不足。一般多重集函数g需作用于全体计数向量，不能只逐计数分量写任意f。此局部修正不否定一热实例或实验。

核查定位：PDF physical page5, Theorem4.1, PDF physical page15, A.2；normalization_repair_and_zero_state_counterexample_confirmed

理论范围与多跳：PDF6承认第二跳后特征不再正交，原一跳无损论证不能逐层沿用；KA定理明确重述Schmidt-Hieber固定维度、不连续编码及连续读出结论，不是实际FAF普遍无损/数值稳定保证。PDF26 KA实现用给定数据顺序处理排序，独立排序不变性及有限精度未本地验证。

核查定位：PDF physical page6, Theorem4.2/information loss, PDF physical page26, KA reducer paragraph；existing_representation_theorem_not_empirical_losslessness

成绩口径及反向结果：正文p7自述5领先+5误差或1点内+4落后，与摘要仅两例外12/14口径不同。PDF8 Citeseer70.48对72.72、Cora82.84对84.38、Roman78.11对91.05、Minesweeper90对97.72。Minesweeper和Questions均应按转录表19的ROC-AUC而非一律accuracy。表10非线性MLP非逐集占优：Chameleon42.96<43.97、Minesweeper90.01<90.45；结论应说多数。

核查定位：p001 abstract, p007, Comparison, PDF physical page8, Table1, PDF physical page26, Table10, p030, Table19 metric row；headline_scope_and_metric_exceptions_confirmed

成本与外部基准：PDF17固定2500轮：RatingsFAF1 17.33秒对GCN140.30，但PhysicsFAF1 532.70/FAF4 2383对65.33，非统一加速；搜索和预计算未单列。PDF29四GraphLand集FAF均低GAT；两个GraphBench MAE .661/.579优于.768/.694，是有限初步移植实验。主配置GNN残差/MLP深度/变体搜索不同，尚需同容量同搜索预算SIGN/NFA对照。

核查定位：PDF physical page17, B.2/Table3, PDF physical page29, Tables15–17, p030, original baseline tables；tradeoffs_and_partial_new_benchmark_scope_confirmed

本地补充/限定：["补充Questions也为ROC-AUC，不能沿主表标题统称准确率。", "把缺范数因子与零特征的真实单射边界分别说明，非零正交情况有直接修复。", "具体指出MLP消融两项反向结果，保持多数有效而非一致优越。"]

核查局限：["未运行模型、检索前作或检查作者排序代码；理论反例仅针对字面有限多重集条件。", "第一次文本输出部分截断，关键公式与表已实看PDF；未取所有SHAP曲线或重新统计显著性。", "作者结果未复现，当前附件出版角色未确认。"]


## pro096 · Do Audio LLMs Listen or Read? Analyzing and Mitigating Paralinguistic Failures with VoxParadox

论文 OR_v7rYbRR9Zw；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8", "source_url": "https://api2.openreview.net/pdf?id=v7rYbRR9Zw\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "5ed71bbaa5d25cea20b1a438a8706ecaa5784ad6d49b7982940c8cb5b2efc746", "source_pdf_sha256": "f298234a9ad885fc02a0df3e07375521d175cf9923c9d1743987e40d86fee4bc", "physical_pages": 28}], "read_ranges": ["TEXT_OR_v7rYbRR9Zw_f298234a9ad8：物理页1–28连续全文，包括正文、参考文献、附录A–E及表1–11；题名与清单一致，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供文本，未见PDF图像或音频；双栏阅读顺序、公式和部分表格排版有损。", "图1–9图像不可见；逐层探针曲线的具体数值无法核读，仅记录正文明确陈述的趋势。", "未提供其他版本或前作全文；未搜索、复现或执行作者代码。"]}

问题：话语内容与声音属性冲突时，Audio LLM能否依据声学线索作答；失败来自表征退化还是决策时未利用？

方法：输入音频、问题和选项。BERT-small→MLP/softmax按问题加权同一编码器第5、15、25、30及最终层的独立投影，送入LLM输出选项。冻结音频编码器，先训练投影器和混合模块，再SFT LLM；最后DPO仅更新LLM，以正确选项对随机错误选项构造偏好。

作者主张：VoxParadox以2000个已验证样例、十项任务直接暴露转写捷径。

论文证据：每任务200题；十二个底座的平均GT为15.33%、ALA为64.34%；全量ASR校验，人工抽查200题。

模型推断：新增跨任务受控失效证据，但不能把压力测试错误率当作自然语音错误率。

定位：['TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p3–5，§3–4.1；p16–17，A.3、表3–4']

作者主张：部分声学信息在深层或投影接口退化，LLM还存在可检索但未利用的差距。

论文证据：正文报告十折线性/MLP探针、跨编码器和VoxCeleb2衍生任务的趋势；CLAP是例外。静态中间层拼接使AF3从17.40%升至19.75%。

模型推断：支持两类瓶颈假说，是既有层分析与利用差距诊断在本场景的扩展，尚非因果证明。

定位：['TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p6，§4.2；p18–21，B.3–B.6、表7']

作者主张：PCLM配合DPO增强声学决策并迁移至MMSU。

论文证据：两底座在VoxParadox上明显超过SFT及SFT+DPO对照，MMSU副语言结果也改善。

模型推断：具有实质能力增量，但尚不能把全部收益归因于prompt条件化本身。

定位：['TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p8，表2；p23，表8、C.3']

key_results：[{"setting": "VoxParadox，2000题、十任务宏平均；以下均为作者报告，非本地复现。", "baseline": "依次为原始底座、SFT、SFT+DPO、PCLM、PCLM+DPO。", "metric_or_guarantee": "GT accuracy与ALA，单位%。", "reported_values_and_units": "AF3的GT依次17.40/34.80/40.30/60.00/65.20；Qwen2-Audio依次14.85/45.70/44.50/68.65/72.30。原始→PCLM+DPO的ALA：AF3为68.50→22.60，Qwen2为70.25→15.95。", "information_and_compute": "文报8×H100 80GB，新增参数不足原模型1%。SFT数据三块分别67K/914小时、1023K/1287小时、177K/1074小时；DPO为20K偏好对。SFT学习率5e-5，DPO为5e-7、β=0.1；GPU时未报告。", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p8表2、p23 C.3；资源见p17 B.1、p22 C.1、p25–26表9–10。\n \n"}, {"setting": "MMSU副语言子集及完整MMSU。", "baseline": "各原始底座与PCLM、PCLM+DPO。", "metric_or_guarantee": "准确率，单位%。", "reported_values_and_units": "副语言子集按原始/PCLM/PCLM+DPO：AF3为37.74/54.06/54.78，Qwen2为34.37/65.18/63.26。完整MMSU原始→PCLM+DPO：AF3为51.43→50.62，Qwen2为50.82→55.43。", "information_and_compute": "评测子集题量及训练—测试音频去重审计未交代；DPO并非对所有指标继续增益。", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p23，表8。\n"}, {"setting": "人工抽查200题，每任务20题；正文称每例由60名标注者独立标注。", "baseline": "构造时指定的声学真值与文本诱导标签。", "metric_or_guarantee": "个人响应准确率/多数票准确率，单位%。", "reported_values_and_units": "GT为80.9/82.1，Adv为88.7/94.4；说话人身份识别的GT多数票准确率仅50.0。", "information_and_compute": "仅覆盖基准10%；人工费用未报告，汇总分母存在待核问题。", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p16–17，A.3、表3。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Chen, J., Guo, Z., Chun, J., Wang, P., Perrault, A., and Elsner, M. Do audio LLMs really LISTEN, or just transcribe? measuring lexical vs. acoustic emotion cues reliance. Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 5848–5877, 2026.", "identifier_if_present": "doi:10.18653/v1/2026.eacl-long.274", "relation_candidate": "背景引用", "shared_component": "分离词汇与声学情绪线索。", "claimed_difference": "本篇由情绪扩展至十类受控冲突任务。", "basis": "target_paper_only", "target_locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p3，§2.1；p10，References", "prior_actually_read": false}, {"citation_as_printed": "Shan, W., Li, Y., Zhang, Y., Luo, Y., Xu, C., Zhao, X., Meng, L., Lu, Y., Zhang, M., Yang, H., Xiao, T., and Zhu, J. Enhancing speech large language models with prompt-aware mixture of audio encoders. Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 19305–19320, 2025.", "identifier_if_present": "doi:10.18653/v1/2025.emnlp-main.974", "relation_candidate": "背景引用", "shared_component": "prompt条件化音频表征混合。", "claimed_difference": "PaM混合多个编码器，本篇混合同一编码器的中间层。", "basis": "target_paper_only", "target_locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p3，§2.2；p12–13，References", "prior_actually_read": false}, {"citation_as_printed": "Diatlova, D., Balagansky, N., Varlamov, A., and Spirin, E. VARAN: Variational inference for self-supervised speech models fine-tuning on downstream tasks, 2025.", "identifier_if_present": "arXiv:2508.12061", "relation_candidate": "背景引用", "shared_component": "输入依赖的编码器层聚合。", "claimed_difference": "本篇以用户prompt控制层权重，并对接Audio LLM副语言问答。", "basis": "target_paper_only", "target_locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p3，§2.2；p11，References", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "跨任务冲突评测及跨底座、跨评测的能力改善构成实质增量；层混合、探针和DPO本身并非新路线。", "central_increment": "前作已解耦情绪线索并研究自适应聚合（本篇转述）；本作新增十任务失效测量及对应接口干预，证据见表1、2、8；尚待排除生成捷径和额外训练预算解释。", "soundness_observation": "SFT对照与外部评测增强证据，但探针可解码性不等于因果利用；随机错误DPO负例也不等于专门的文本诱导负例。", "significance_observation": "对Audio LLM诊断和声学接口改造有实际价值；没有新理论保证，轻量参数增量不等于训练成本低。", "main_open_question": "同层、同参数、同训练预算的静态混合，能否复现PCLM的主要收益？"}

limitations：[{"text": "后置修复存在表征损失上限；合成对抗评测不能替代自然语音评测。", "basis": "author_report", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p9，§6"}, {"text": "二元任务始终设置相反标签时，纯转写后取反也可能命中；未见此类文本捷径对照。信号比较复用同一句脚本生成三段，但答案为排序，唯一对抗选项的映射说明不足。", "basis": "model_inference", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p3，§3；p15–16，A.1"}, {"text": "ASR零WER和TTS元数据不能保证感知真值无歧义。表3的GT响应准确率逐任务等权均值经本轮算术检查为77.22%，不同于所报80.9%；有效样本与汇总分母待核。", "basis": "model_inference", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p4，§3.3；p16–17，A.3、表3"}, {"text": "训练数据与基准共享信号处理及拼接流程，选层又受本基准探针指导；未使用测试样例训练不等于独立于测试进行方法选择。缺少静态混合的等预算对照。", "basis": "model_inference", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p22，C.1；p24，D.1"}, {"text": "Qwen2的MMSU副语言结果加DPO后下降，AF3完整MMSU也低于原始底座；正文关于无退化或一致增益的概括需限定。", "basis": "model_inference", "locator": "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p9，§5.2；p23，表8"}]

minimal_check：{"question": "prompt条件化是否优于静态层混合？", "control": "将PCLM的prompt向量替为固定向量，保持五层、投影器、参数、训练数据与步数一致；两组均不做DPO。", "observable_outcome": "比较VoxParadox的GT/ALA及MMSU准确率，报告配对差值和不确定区间。", "resources": "需作者数据、检查点和训练实现；论文参考配置为8×H100 80GB，实际GPU时未知。", "failure_or_stop_condition": "静态对照追平或差异区间覆盖零，则不能支持prompt路由的独立收益；训练预算无法对齐时停止因果归因。"}

missing_fields：["图中逐层探针数值、原始音频、逐例输出和人工标注记录未提供。", "训练步数/轮数、batch size、随机种子、GPU时、推理延迟及闭源评测快照未报告。", "声学变换强度、探针是否按说话人/脚本隔离、MMSU子集规模及数据去重细节未交代。", "TEXT_OR_v7rYbRR9Zw_f298234a9ad8：p26表10的DPO总时长写96.0小时，但十任务分项合计115.3小时；保留冲突，未替作者校正。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

词汇—声学冲突诊断及接口改善值得保留；优先问人工有效分母、文本取反捷径和同预算静态层混合能解释多少收益。

身份、任务与监督：完整题名及28页附件相符。VoxParadox十任务各200合成多选题，文本标签与声学标签刻意冲突；GT与ALA非互补率，多选还可选两者之外。PCLM选五层、冻结编码器，先对齐投影/混合再训练完整LLM；DPO正确选项对随机错误选项，不是每对都专门含文本诱导负例。

核查定位：p001 title, p003–004, construction/metrics, PDF physical page8, training/DPO, p022, two-stage training；identity_and_training_target_confirmed

数据可靠性和可能捷径：零WER只核对转写，TTS元数据/信号处理并不自动保证人能感知指定标签。PDF16每任务20例、每例60人，PDF17说话人ID多数票仅50%。GT个人响应十项等权均值77.22%而非80.9%；若样本/标注数相同二者应一致。多数票66.7/88.9/77.8又不符合完整20例的5点步长，提示排除/有效分母需说明，不能自行猜缺失数或认定造假。二元标签始终相反时，识别文本后取反可命中，不足以证明声学利用。

核查定位：PDF physical page4, verification, PDF physical page16, A.3, PDF physical page17, Table3；human_validation_denominator_conflicts_and_binary_shortcut_scoped

关键成绩和逆向结果：PDF8 AF3原始/SFT/SFTDPO/PCLM/PCLMDPO GT17.40/34.80/40.30/60/65.20；Qwen14.85/45.70/44.50/68.65/72.30。不是所有任务逐项提高：Qwen speaker count原12.50→PCLM11.50；DPO后AF3 intonation49.50→47。PDF23 Qwen MMSU副语言65.18→63.26、AF3完整MMSU51.43→50.62，均须保留；外部总体转移有价值但非无代价一致改善。

核查定位：PDF physical page8, Table2, PDF physical page23, Table8/C.3；large_main_gains_and_nonuniform_transfer_confirmed

因果解释和资源：探针可解码性不等于因果使用，倒放同时改变韵律时序；当前无同五层同参数同训练的静态混合对照。选择层受本基准探针引导，即便样例不用于训练也非完全独立方法选择。新增参数<1%但第二阶段全LLM微调，8H100训练未给总GPU时。PDF26十任务DPO小时6.3+6.3+23.5+13.2+13.4+13.2+4.3+22.1+9.9+3.1=115.3，与总96.0冲突；不重复加emotion子项。

核查定位：p016, reversed emotion filtering, p017, B.1, p022, layer choice/training, PDF physical page26, Table10；mechanism_attribution_and_training_cost_limits_confirmed

本地补充/限定：["补充多数票百分比与每任务20例的离散分母不一致，以及Qwen speaker-count PCLM反向结果；不能只说十任务均提高。", "明确DPO时长冲突只按十个顶层任务相加，未把情绪子集再次计入。"]

核查局限：["未听原始音频、复核人类标签、训练模型或运行探针；未核读前作。", "只查看所列PDF，未数字化所有探针曲线；不把元数据声称或算术异常当作完整数据质量裁决。", "版本角色未确认，报告值未复现，未新增实验。"]


## pro097 · Joint-Space Empowerment for Dexterous Coordination in Tendon-Driven Hands

论文 OR_qI2eHwfNfh；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a", "source_url": "https://api2.openreview.net/pdf?id=qI2eHwfNfh\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "9bce8045eeba2f7492dc097b8c2a3ae148aaf91715839edfed7e16a0f8b4a41e", "source_pdf_sha256": "46a8d16fec1adc006f025f9df95d620575da853cc9357b1ced6c54b2da1250e9"}], "read_ranges": ["TEXT_OR_qI2eHwfNfh_46a8d16fec1a：物理页1–25全部文本；正文p1–9、参考文献p10–13、附录A–I及实现与补充分析p14–25。连续页标齐全，题名匹配。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文抽取文本，未查看PDF图像；图1–12不可见，不能读取曲线末值、误差带或可视化结构。", "双栏交错，部分公式上下标、矩阵及表1排版有损；表2–7的主要数值可辨，但未经原始版面核验。", "前作全文、代码和实验日志未提供；未搜索、复现或核定最终出版版本。"]}

问题：如何在过驱动腱驱动手中消除执行器动作冗余，同时保留关节运动控制能力，并提高任务学习和跨物体泛化效率？

方法：以潜动作z为发送信号、下一步关节速度y′为接收量，最大化信道容量JoSE。网络学习y′~N(f(s)+G(s)a,Q(s))，按G的行空间构造状态依赖预编码器a=θ(s)z；主设置G≈LR、秩15。动力学以转移数据做最大似然训练，MC dropout采样不同动作子空间；SAC只优化任务潜策略，实际动作另经tanh约束。

作者主张：将动作流形发现表述为JoSE最优预编码问题，并给出闭式最优解。

论文证据：Theorem C.1给出白化矩阵G̃的非零右奇异向量V_r作为预编码器；C.3说明同一子空间的可逆换基可由源协方差补偿。

模型推断：新增主要在控制对象选择及其与动力学协同的连接；闭式解沿用经典高斯信道结构，不保证一般任务回报最优。

定位：['TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p4，Definition 4.1；p16–17，Theorem C.1、Corollaries C.2–C.3。\n']

作者主张：JoSEPi支持同步或解耦学习，提升灵巧性、样本效率、稀疏奖励学习和泛化。

论文证据：提供MyoHand与模拟Adroit实验、Reorient迁移、dropout及秩消融，并加入状态依赖重构基线SD-SAR。

模型推断：动力学监督与任务策略解耦具有实质价值；目标不含奖励，不等于数据采集完全无任务监督。

定位：['TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p7–9，§10；p20，§F.1–F.2；p22–23，§H']

key_results：[{"setting": "同步学习：MyoHand四项接触操作任务；另测稀疏Reorient8及模拟Adroit四任务", "baseline": "MyoHand：SAC、Lattice-SAC、Lattice-rPPO；Adroit：SAC", "metric_or_guarantee": "fraction solved：每回合已解决时间步数除以最大回合长度，并非整回合成功率", "reported_values_and_units": "正文称MyoHand KeyTurn收敛约快2–3倍；其余优势仅能记录作者定性报告，不能从图4、5、7补造数值。", "information_and_compute": "5个随机种子；SAC主体超参数统一，环境交互并行使用20 CPU核；GPU、墙钟时间及推理延迟未报告。", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p7，§9–10.1；p8–9，Figures 4–7；p18，§E。\n"}, {"setting": "MyoHand，训练5M环境步后的输入矩阵秩消融", "baseline": "k=23参数化，对比主设置k=15", "metric_or_guarantee": "fraction solved，均值±标准误，无量纲", "reported_values_and_units": "依次为BaodingBalls、DieReorient、KeyTurn、PenTwirl：k=15为0.611±0.102、0.380±0.031、0.717±0.021、0.624±0.015；k=23为0.572±0.052、0.355±0.023、0.688±0.023、0.609±0.016。", "information_and_compute": "每设置5个种子；亦测试k=9、12、18，结果不支持15维在所有任务均最优。", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p23，Table 7。\n"}, {"setting": "Reorient8获取play数据，固定流形学习Reorient100，再测ReorientID/OOD未见物体", "baseline": "SAR、SD-SAR、SAC", "metric_or_guarantee": "下游fraction solved和零样本泛化；作者报告JoSEPi最好", "reported_values_and_units": null, "information_and_compute": "play为1M环境步；JoSE动力学离线训练1M次迭代，SD-SAR为50K次，两者每迭代20梯度步、批量256；图6计入play环境步，但不是等计算量比较。", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p8，§10.3/Figure 6；p19–21，§E.1.5、F.2。\n \n"}, {"setting": "已训练MyoHand策略的事后动力学分析，按接触切换分组", "baseline": "发生接触切换与未发生切换的转移", "metric_or_guarantee": "逐关节平均预测MSE", "reported_values_and_units": "切换组0.152±0.001，n=148021；非切换组0.149±0.001，n=125499；误差的物理单位或归一化尺度未明确。", "information_and_compute": "每个已训练策略展开100回合，每条转移采样50个dropout模型；仅检验策略访问分布，非固定状态下广泛反事实动作。", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p21–22，§G.1、Table 5。\n"}]

prior_work_candidates：[{"citation_as_printed": "Telatar, E. Capacity of multi-antenna Gaussian channels. European Transactions on Telecommunications, 10(6):585–595, 1999.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "高斯MIMO容量、奇异向量预编码、water-filling", "claimed_difference": "本作将通信结构映射为状态依赖的关节运动控制。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p9，§11；p13，References；p16–17，§C", "prior_actually_read": false}, {"citation_as_printed": "Berniker, M., Jarc, A. M., Bizzi, E., and Tresch, M. C. Simplified and effective motor control based on muscle synergies to exploit musculoskeletal dynamics. Proceedings of the National Academy of Sciences, 106:7601–7606, 2009.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "依据身体动力学发现保留控制能力的低维协同", "claimed_difference": "本篇称前作采用解析确定性控制模型；本作学习随机动力学并以JoSE构造协同。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p3，§2.1；p10，References", "prior_actually_read": false}, {"citation_as_printed": "Berg, C. H., Caggiano, V., and Kumar, V. SAR: Generalization of physiological dexterity via synergistic action representation. In Robotics: Science and Systems, 2023.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "play阶段获取协同，再迁移至下游操作", "claimed_difference": "SAR以ICAPCA重构动作模式；JoSE以转移动力学发现状态依赖子空间。", "basis": "target_paper_only", "target_locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p8，§10.3；p10，References；p20，§F.2", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "不是新高斯容量公式，但关节空间目标、学习动力学协同与不确定性探索形成有实质作用的组合，并有多任务和迁移证据；不足以认定路线级首创。", "central_increment": "前作已有动力学协同、MIMO容量解和play迁移方法（均为本篇转述）；本作新增可在线学习、任务解耦的关节速度预编码机制，支持证据为定理及仿真对照；尚待排除理想信道与实际动作约束的差距。", "soundness_observation": "C.1在所列理想条件下推导连贯，未逐式证明。G节将含Q的混合预测方差称为纯认知不确定性，按所写定义还含条件噪声；总样本数273940与Table 5的273520也不一致，需核对实现和统计口径。", "significance_observation": "为过驱动手提供可复用低维控制接口，工程结构明确；证据仍限仿真，未证明真实刚度控制或普适跨任务能力。", "main_open_question": "有界、单向且经tanh变换的真实动作条件下，JoSE子空间是否仍保留关键可达关节运动？"}

limitations：[{"text": "动作相关接触非线性与信号依赖噪声超出近似；真实腱摩擦、弹性、共收缩和刚度控制仍待研究。", "basis": "author_report", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p9，Limitations and Future Work。\n"}, {"text": "任务无关目标不保证训练数据覆盖无关任务；迁移仍在相近物体重定向任务族内。", "basis": "model_inference", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p8，§10.3；p20–21，§F.2"}, {"text": "SD-SAR与JoSE离线训练预算、监督目标及信息利用不同，优势不能完全归因于JoSE信息论目标；未报告等墙钟比较。", "basis": "model_inference", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p19–21，§E.1.5、F.2.2–F.2.3"}, {"text": "事后预测相关性不能单独证明不确定性校准或全动作空间探索；G节方差定义与样本计数冲突削弱其解释力度。", "basis": "model_inference", "locator": "TEXT_OR_qI2eHwfNfh_46a8d16fec1a:p21–22，§G。\n"}]

minimal_check：{"question": "实际幅值约束下，流形是否丢失重要的一步关节速度可达目标？", "control": "固定同一接触状态和已训练动力学，比较全动作空间与JoSE经tanh映射的动作；目标、幅值范围及多起点优化预算一致。", "observable_outcome": "比较目标速度跟踪误差和动作饱和率。", "resources": "可重置仿真状态、已训练模型及批量动作评估；无需重训策略，具体耗时未知。", "failure_or_stop_condition": "全空间可重复实现而JoSE持续无法实现的目标，否定实际无损控制外推，但不否定理想高斯定理；两侧优化均不收敛则不作判定。"}

missing_fields：["主要性能曲线、泛化柱状图及dropout消融的精确数值", "MSE物理单位或归一化尺度", "GPU配置、墙钟成本、推理延迟", "G节方差实现与样本计数差异解释", "前作全文核读、真实硬件验证、最终版本身份"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

关节速度目标与动态协同接口有实质价值；需先核实际有界动作的可达性、同离线计算对照和不确定性实现再迁移到真实腱手。

身份与控制对象：题名及25页附件相符，JoSE是潜动作到下一关节速度的信道容量，不是完整状态/任务回报目标。MyoHand39动作23关节主秩15，修改Adroit25自由度46腱42执行器仍为仿真，非硬件验证；动力学输入含物体状态。

核查定位：p001 title, p004–006, definitions/method, p018, model input, p020, Adroit abstraction；identity_and_simulation_control_scope_confirmed

理想高斯定理与实际映射：C.1白化G后以非零右奇异向量张成行空间，协方差可优化且只限总发送功率，Hadamard对角化论证可跟踪；换基等价还要相应改变源协方差。r是完整非零模态跨度而非必须激活r个独立功率方向，低功率water-filling可关掉弱模态。真实动作经tanh及单向幅值约束，SAC潜策略也非任意高斯容量源，故不把C.1推广为实际无损可达/奖励最优。

核查定位：PDF physical page16–17, C.1–C.4, p007 tanh paragraph, p020, ai in [-1,0]；conditional_optimality_not_bounded_action_guarantee

性能度量、图像及秩：fraction solved为已解决时间步/最大回合长度，不是整回合成功率。实际PDF8图4–6支持Baoding/PenTwirl及迁移优势，DieReorient后段Lattice-rPPO追近/可超过蓝线，不能说全部终点最优；未伪造精确曲线点。表7主秩15的.611/.380/.717/.624与Pro相符，Baoding秩12 .700、KeyTurn秩18 .750更高，15不是各任务最优。

核查定位：p007 metric definition, PDF physical page8, Figures4–6, PDF physical page23, Table7；metric_and_nonuniform_performance_confirmed

迁移信息及训练成本：play为SAC在Reorient8有任务奖励的1M环境步，目标无奖励不等于采集无任务监督。两方法共享play，但JoSE动力学1M迭代、SD-SAR50K迭代，每次20梯度步batch256，离线更新量相差20倍；图6包含play环境步却未覆盖这个计算差异。20CPU并行未给全墙钟，不能归因全收益于JoSE目标。

核查定位：p018, implementation, p019, E.1.5, p020–021, F.2, PDF physical page8, Figure6；task_data_and_offline_budget_difference_confirmed

不确定性定义与样本数：PDF21先定义50个Gaussian混合再取预测方差，按全方差公式为E[Q]+Var(f+Ga)，含条件噪声，不是纯epistemic。若实现只对均值取方差则可为epistemic，但与印出定义不同，未查代码。Table5 .152/.149和样本148021+125499=273520，区别文中273940，不能自行删420。正相关r.50–.66支持风险排序，非概率校准/全动作空间覆盖证明；已访问确定策略分布不能验证广泛反事实动作的控制仿射性。

核查定位：PDF physical page21, mixture/variance, PDF physical page22, Tables5–6/G.2, PDF physical page23, Figure8；total_variance_mislabelling_and_count_conflict_confirmed

本地补充/限定：["补核图像的DieReorient晚期及rank消融，保留非统一最优。", "补充water-filling可令弱非零模态功率为0，r维表示最优不等于最小必需潜维恒等于r。"]

核查局限：["未运行仿真、作者代码或真实手，未核读前作；只做定理条件、全方差恒等式及统计数量核对。", "第7页仅度量/tanh定位段，其余页为所列来源核对；没有逐点数字化曲线或全证明审计。", "当前版本角色未确认，报告数值不是本地复现。"]


## pro098 · CARD: Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition for Transferable Free Energy Estimation

论文 OR_Kdc1UvnMKk；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9", "source_url": "https://api2.openreview.net/pdf?id=Kdc1UvnMKk\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "6695e29ae79f626b04b69c2e382bcc7aa092fc3cea82138db5137a9dc999a95c", "source_pdf_sha256": "83fc1b9bdaf954136015894a4c110062b58d305243dd8d37d6e411e204e7666e"}], "read_ranges": ["TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9：物理页1–9，正文全部章节", "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9：物理页10–14，影响声明及参考文献", "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9：物理页15–26，附录A–H全部"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["连续26页文本齐全；未提供PDF图像，图1–8的散点、结构及分组分布不可核验。", "双栏、公式和图中文字存在交错；未补写图3水相混排的精确指标，式(24)损失符号及算法1距离输入需原版核对。", "§4.1训练分子数为40,203，附录表7为40,303，保留冲突。", "来源URL与PDF哈希仅为清单元数据，未下载PDF、搜索前作或执行代码；不认定为最终出版版。"]}

问题：如何对未见分子构造可采样、可计算密度的参考分布，绕过炼金中间态估计自由能？

方法：输入原子序数、拓扑和MD参考构象，经PCA对齐与原子排序，将坐标拆为逐层radix离散数字和连续残差。Transformer先生成全体原子的粗坐标再细化，分类头与BMM给出密度；先训NLL，再加中心化能量匹配。以−log q作为零自由能参考，结合模型样本和目标端点MD通过MBAR估计绝对自由能，再求差。

作者主张：通过可逆radix分解兼顾粗到细构象生成与精确似然计算。

论文证据：命题3.1、3.2及附录C给出有界坐标的映射和密度公式；表5提供结构消融。

模型推断：新增主要是坐标分辨率序列化与条件生成的组合；零自由能参考本身不是本篇首创。

定位：['TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p5–6，命题3.1–3.2；p16–18，附录C；p24，表5']

作者主张：无需针对未见系统重训即可估计自由能，并获得约40倍推理加速。

论文证据：70个溶剂化测试分子、18个HiPen系统和27对互变异构体提供迁移证据；表1报告耗时。

模型推断：支持固定条件内、有目标MD上下文的跨拓扑迁移；含端点MD约为5倍加速，不是无采样预测。

定位：['TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p7–8，§4.1–4.3、表1–2；p23，表4']

key_results：[{"setting": "70个中性ZINC测试分子，最大训练集ECFP4相似度≤0.65；真空到隐式甲苯/水。", "baseline": "MFES：11个状态各5 ns MD，再用MBAR估计。", "metric_or_guarantee": "自由能误差及每系统平均耗时", "reported_values_and_units": "甲苯MAE=0.71、RMSE=1.27 kcal/mol，R²=0.92；水相正文报告MAE<1 kcal/mol、R²>0.9。MFES=32,300 s；CARD不含端点MD=770 s，含端点MD=6,650 s。", "information_and_compute": "正文训练40,203分子，各环境MM轨迹10 ns。计时使用单V100 32GB，不含训练。附录H报告每模型Stage I用32张A100约4天，Stage II用16张A100约10天。", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p7，§4.1、表1；p9，表3；p23–24，§F.3；p26，H。\n \n \n"}, {"setting": "18个HiPen分子的OpenFF 2.0.0→ANI-2x端态修正。", "baseline": "MFES参考值", "metric_or_guarantee": "MAE", "reported_values_and_units": "0.90 kcal/mol。", "information_and_compute": "训练7,881、验证100个分子；MM轨迹10 ns，ANI-2x轨迹5 ns。", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p8，§4.2；p18，§D.1。\n"}, {"setting": "经ANI适用性及实验自由能差2.72 kcal/mol阈值筛选的27对水相互变异构体。", "baseline": "DFT、sPhysNet-pre；基线结果引用Pan等(2025)。", "metric_or_guarantee": "MAE/RMSE（kcal/mol）及PCC/SPCC", "reported_values_and_units": "CARD：4.11/5.49/0.64/0.64；DFT：4.62/7.05/0.36/0.42；sPhysNet-pre：4.61/6.95/0.35/0.41。", "information_and_compute": "复用ANI真空与MM溶剂化模型，不用实验自由能标签训练；仍需相关端点模拟。", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p8，§4.3、表2。\n"}, {"setting": "真空→甲苯消融；架构对比均仅Stage I。", "baseline": "无分解的连续自回归模型、无几何注意力偏置模型", "metric_or_guarantee": "MAE", "reported_values_and_units": "完整模型0.81；无分解并改用GMM为1.29；无几何偏置1.17 kcal/mol。完整模型加入Stage II后为0.71 kcal/mol。", "information_and_compute": "去分解对照同时改变残差分布族，不能将差异完全归因于radix；各消融训练成本未单列。", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p9，表3；p24，表5。\n"}, {"setting": "many-peptides-md；CARD重训至4AA；2AA、4AA各30个测试体系，每体系生成10,000个未重采样proposal。", "baseline": "TarFlow、Prose", "metric_or_guarantee": "Torus-W2、TICA-W2，单位未注明", "reported_values_and_units": "2AA Torus-W2：CARD/TarFlow/Prose=0.296/0.178/0.261；4AA为0.832/0.882/0.916；4AA TICA-W2为0.384/0.384/0.546。", "information_and_compute": "CARD仅Stage I，44.5M参数、640 A100小时；Prose为285M、260 H100小时且训练至8AA，硬件和训练范围不同。", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p25，§G.2、表8–9。\n"}]

prior_work_candidates：[{"citation_as_printed": "Ding, X. and Zhang, B. Deepbar: A fast and exact method for binding free energy computation. The Journal of Physical Chemistry Letters, 12(10):2509–2515, 2021.", "identifier_if_present": "10.1021/acs.jpclett.1c00189", "relation_candidate": "方法继承", "shared_component": "归一化模型充当零自由能参考，再用BAR计算自由能。", "claimed_difference": "以跨系统条件自回归模型替代逐系统normalizing flow。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p3，§2.2；p11，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Tan, C., Hassan, M., Klein, L., Syed, S., Beaini, D., Bronstein, M., Tong, A., and Neklyudov, K. Amortized sampling with transferable normalizing flows. In Belgrave, D., Zhang, C., Lin, H., Pascanu, R., Koniusz, P., Ghassemi, M., and Chen, N. (eds.), Advances in Neural Information Processing Systems, volume 38, pp. 94290–94325. Curran Associates, Inc., 2025a.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "跨分子系统的Boltzmann ensemble生成。", "claimed_difference": "CARD采用radix自回归并接入自由能估计；本篇与Prose仅直接比较肽生成和资源，未比较自由能误差。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p13，参考文献；p25，§G.2", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "可计算密度的粗到细坐标建模与跨拓扑自由能迁移构成实质增量；但沿用既有参考分布范式，不宜仅凭作者措辞判为路线级首创。", "central_increment": "DeepBAR已建立零自由能参考思路（本篇转述）；CARD新增跨系统条件radix自回归proposal，并给出迁移及消融证据。", "soundness_observation": "附录C支持有界坐标的radix变换，但未清楚交代PCA去除刚体自由度后，密度测度如何对应物理配分函数；有限MD与重叠也限制对“exact”的解释。", "significance_observation": "可能摊销大量新分子的估计成本，但前期训练重；互变异构体MAE仍为4.11 kcal/mol，不能将溶剂化精度推广至所有任务。", "main_open_question": "PCA对齐后的q与MBAR目标能量是否定义在一致、正确归一化的积分测度上？"}

limitations：[{"text": "作者承认对称构象PCA不稳及蛋白配体扩展待研究；G.4报告静态SDF近退化23/40,403（0.057%），测试集为0%。", "basis": "author_report", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p9，§5；p26，§G.4"}, {"text": "肽实验重训且测试长度未超训练上限，只验证生成分布；不能证明无重训跨域迁移、长度外推或肽自由能准确性。", "basis": "model_inference", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p25，§G.2、表8–9"}, {"text": "四个训练分子的扭转图不足证明所有MD充分采样。G.3已有双向ESS诊断，但图不可见；表6缩短的只是参考构象来源轨迹，不能据此删去目标端点MD。", "basis": "model_inference", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p18，§D.2；p24，表6；p26，§G.3"}, {"text": "互变异构体按实验值筛选且基线未在本轮统一复跑；主要性能表未报告多随机种子置信区间，推广范围和稳定性仍待核验。", "basis": "model_inference", "locator": "TEXT_OR_Kdc1UvnMKk_83fc1b9bdaf9，p8，§4.3；p9、24–25，结果表"}]

minimal_check：{"question": "PCA预处理是否引入未计入的归一化或自由能偏差？", "control": "在配分函数可解析的非对称分子玩具体系中，对比CARD/PCA处理与显式保留或解析积分刚体自由度的计算，使用相同势能及独立样本。", "observable_outcome": "绝对自由能及两势能间自由能差随样本增加收敛至解析值。", "resources": "原始PCA、密度与MBAR实现，以及解析玩具体系；设备、采样量和耗时待定，本轮未执行。", "failure_or_stop_condition": "增加样本后仍有系统性偏差，或实现无法明确所用积分测度，则不能确认绝对自由能的exact主张。"}

missing_fields：["原PDF图像、图中逐点数据及混排水相精确指标", "40,203与40,303训练规模冲突的解释", "PCA后物理测度对应关系", "总训练数据制备成本、超参数搜索总预算及重复实验不确定性", "Prose条目的稳定标识；两篇候选前作全文均未提供"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

可计算密度的跨拓扑proposal及含MD仍约5倍的估计流程值得深入读；首要核查物理测度与参考/目标样本契合，其次评估训练摊销和等分布族消融。

身份和可逆变换范围：CARD完整题名及26页附件相符。在已经PCA对齐的有界坐标上，radix离散数字加[0,a/r^L)残差为分片平移双射，连续残差Jacobian1，BMM rescale密度另乘r^L/a；此数值分解可跟踪。它没有同时证明前置去平移/旋转保持3N维物理配分函数测度。PCA规范化多对一，仍需明确刚体自由度、诱导测度及归一化约定；不能从分解双射直接认定绝对物理自由能exact。

核查定位：p001 title, p004, PCA preprocessing, PDF physical page5–6, Propositions3.1–3.2, p016–017, C.1；radix_change_of_variables_confirmed_physical_measure_unresolved

训练损失的原版核对：PDF6式24明确为中心化能量差的绝对值平均，文本抽取丢失的竖线确实存在；不能误判中心化后有符号和恒等零。归一化proposal可用作零自由能参考，仍需要target端点样本和分布重叠；2000生成构象加去相关MD用于MBAR。

核查定位：PDF physical page6, Eq24/section3.5, p007, evaluation procedure；absolute_value_loss_confirmed_not_zero_sum_bug

精度和加速分母：实际PDF7图3补得水相MAE.70、RMSE1.13、R².98；甲苯.71/1.27/.92。V100每体系MFES32300秒、CARD去MD770/含MD6650，即约41.95倍与4.86倍。不能称零MD或端到端40倍。70测试分子为100候选经最大ECFP4相似度.65筛剩，三个热力学环境各训练模型。

核查定位：PDF physical page7, Figure3/Table1/section4.1, PDF physical page23, Algorithm4/Table4/F.3；previously_unread_water_values_and_full_inference_cost_confirmed

任务、消融及泛化：PDF8互变异构体筛选至27对、CARD MAE4.11/RMSE5.49，对基线略优而非所有任务<1kcal/mol。PDF24 StageI全模型.81、无分解1.29、无几何1.17；无分解同时BMM改GMM。缩短至100ps只改变参考构象来源，不移除MBAR端点MD。PDF25肽重训至4AA，2AA TorusW2 .296劣于.178/.261，4AA .832优于.882/.916；不是跨训练长度外推或肽自由能测量。

核查定位：PDF physical page8, Table2, PDF physical page24, Tables5–6, PDF physical page25, Tables8–9；task_limits_and_multiple_changed_ablation_factors_confirmed

重叠、PCA诊断及训练资源：PDF26双向ESS与绝对误差的Spearman为−.256/−.421/−.412，可作风险线索，非每体系可靠性证书。PCA近退化23/40403按静态SDF检查，不覆盖所有MD帧或物理测度。正文训练40203、附表40303冲突保留。每模型32A100约4天加16A100约10天，约6912 A100 GPU小时，未含数据制备/搜索，远非免费迁移。肽44.5M参数却4AA显存5.35GB高于Prose4.21，参数少不等于全面省资源。

核查定位：PDF physical page25, Tables7/9, PDF physical page26, Figure8/G.4/H；diagnostic_not_guarantee_and_training_cost_scope_confirmed

本地补充/限定：["原PDF确认式24含绝对值，撤除仅由文本失真产生的符号不明。", "补录水相精确图值、ESS相关及含端点MD4.86倍口径。", "PCA物理测度为待明确的重要前提，未据此宣称已证实其自由能估计有偏。"]

核查局限：["未运行MD、MBAR、作者代码、PCA玩具体系或检索前作；只完成有限来源、公式和数字核对。", "未独立验证全部采样充分性及算法1距离输入；没有把图相关性当校准或物理证明。", "当前附件角色未核实，报告值均来自目标论文。"]


## pro099 · Periodic Bayesian Flow Networks with Additive Accuracy

论文 OR_N7hieduZYV；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_N7hieduZYV_18c17e0da693", "source_url": "https://api2.openreview.net/pdf?id=N7hieduZYV\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "2556fb69f74426e3c35b9dc8995384d13f0889651966a1d57b37ae8f949eee89", "source_pdf_sha256": "18c17e0da69366b1052867ea339354a38fc3cbebda00a8f937ab35c74d07176f"}], "read_ranges": ["TEXT_OR_N7hieduZYV_18c17e0da693：物理页1—16全部提供文本，含正文、参考文献及附录A—F；页标连续，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供原PDF图像；图1—3仅有图题及零散提取文字，无法核验视觉效果。", "双栏文字交错，部分公式上下标、复数符号及表格布局可能失真；未用外部材料补齐或核读其他版本。"]}

问题：如何对周期变量进行具有确定、可加精度调度的BFN生成，并消除晶体整体平移及CLF相位多解性造成的训练目标歧义？

方法：将周期标量映射为(cos,sin)，在R²维护高斯信念并执行ρ←ρ+α，网络负责变量间耦合。CSP联合生成晶格与分数坐标，并解析边缘化整体平移；CLF在射线累积相位Px域边缘化二元符号，以强度而非真实相位监督，采用end-back采样。附录(46)的实际损失为重建项加0.01倍RB项。

作者主张：通过二维单位圆嵌入恢复周期BFN的严格可加精度、闭式前向边缘与连续时间训练。

论文证据：给出高斯更新、前向分布(18)及采样算法；MP-20去除二维嵌入后性能下降。

模型推断：增量是改变周期变量的概率建模空间及训练接口，不只是增加位置编码；可加性针对辅助高斯精度。

定位：['TEXT_OR_N7hieduZYV_18c17e0da693，p5 §4.2、p6算法1、p15表6。\n']

作者主张：解析边缘化周期对称性，得到不变目标并保证降低梯度方差。

论文证据：CSP目标使用von Mises一阶矩I1/I0；CLF符号后验得到tanh目标；附录给出推导，CSP有去RB消融。

模型推断：这是针对两种已知对称性的具体闭式构造，而非新的一般Rao–Blackwell定理；未直接测量梯度方差。

定位：['TEXT_OR_N7hieduZYV_18c17e0da693，p7 §4.5、p12—13 A.3—A.4。\n']

作者主张：作者称首次将周期生成建模用于现代裸眼3D显示的CLF相位合成。

论文证据：单场景OOD测试中，PSNR高于EyeReal，但低于共轭梯度；推理慢于EyeReal。

模型推断：展示了有价值的跨域应用与质量—延迟折中，尚不能确认历史首次性或真实显示端的同等增益。

定位：['TEXT_OR_N7hieduZYV_18c17e0da693，p8 §5.2、p15表5。\n']

key_results：[{"setting": "给定原子组成的CSP，多种子mean±std；StructureMatcher阈值stol=0.5、angle_tol=10、ltol=0.3。", "baseline": "CrysBFN", "metric_or_guarantee": "Match rate（%）及RMSE（单位未注明）", "reported_values_and_units": "MP-20：本作70.05±0.04、0.0370±0.0009；基线64.33±0.24、0.0445±0.0010。MPTS-52：本作27.03±0.13、0.1105±0.0024；基线19.71±0.72、0.1112±0.0077。", "information_and_compute": "CSPNet为6层、隐藏维512；本作默认500采样步，MP-20/MPTS-52分别训练5000/3000 epochs。种子数量未报告。", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §5.1、p15表4、p15—16附录C。\n"}, {"setting": "MP-20多种子消融", "baseline": "去除RB、二维嵌入或时间输入", "metric_or_guarantee": "Match rate，mean±std（%）", "reported_values_and_units": "完整模型70.05±0.04；无RB 66.11±0.12；无二维嵌入60.02±0.10；无t输入66.17±0.19。", "information_and_compute": "消融具体替代实现、逐项训练预算及种子数量未充分交代。", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p15表6。\n"}, {"setting": "MP-20固定前向次数比较", "baseline": "CrysBFN；两模型均12.3M参数", "metric_or_guarantee": "Match rate（%）随NFE变化", "reported_values_and_units": "按本作/基线：10次为59.13/60.18；200次69.78/64.35；500次70.06/62.14。低至10次时本作并不占优。", "information_and_compute": "NFE为网络前向次数；主比较表未逐方法明确绑定采样预算。", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p16表8。\n"}, {"setting": "CLF：10000训练双目对、10组OOD测试对；PSNR在360×640评测，延迟在1080×1920评测。", "baseline": "EyeReal及Conjugate Gradient", "metric_or_guarantee": "PSNR（表未标单位）、端到端延迟及FPS，多种子mean±std", "reported_values_and_units": "本作31.40±1.05、35.1±0.22 ms、28.49±0.16 FPS；EyeReal为27.46±1.18、19.4±0.25 ms、51.55±0.53 FPS；共轭梯度PSNR为34.31±1.21。", "information_and_compute": "6000 epochs；随机姿态及文中R∈[30,50] cm；附录称N∈{1,2}并另有最终前向，表中具体N未注明。", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §5.2、p14 A.5、p15表5、p16附录C。\n"}, {"setting": "MP-20运行开销", "baseline": "CrysBFN", "metric_or_guarantee": "参数量、训练步耗时、预热后200步单GPU推理耗时", "reported_values_and_units": "本作/基线：12.3M/12.3M参数；0.047/0.053秒每训练步；74/89秒推理。", "information_and_compute": "GPU型号、批量及推理样本总数未报告，不能换算单样本速度或总GPU时。", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p16表7。\n"}]

prior_work_candidates：[{"citation_as_printed": "Wu, H., Song, Y., Gong, J., Cao, Z., Ouyang, Y., Zhang, J., Zhou, H., Ma, W.-Y., and Liu, J. A periodic bayesian flow for material generation. In The Thirteenth International Conference on Learning Representations, 2025.", "identifier_if_present": "Lz0XW99tE0", "relation_candidate": "方法继承、组件复用、比较基线", "shared_component": "周期晶体BFN与CSP骨干", "claimed_difference": "从直接圆周更新转向二维高斯可加精度，并引入RB目标。", "basis": "target_paper_only", "target_locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §4.6、p11参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Lin, P., Chen, P., Jiao, R., Mo, Q., Jianhuan, C., Huang, W., Liu, Y., Huang, D., and Lu, Y. Equivariant diffusion for crystal structure prediction. Proceedings of the 41st International Conference on Machine Learning, volume 235, pp. 29890–29913. PMLR, 21–27 Jul 2024.", "identifier_if_present": "https://proceedings.mlr.press/v235/lin24b.html\n", "relation_candidate": "理论扩展候选、比较基线", "shared_component": "使晶体去噪目标尊重整体平移等价性", "claimed_difference": "本篇将其类比为等变去噪思想，并利用二维嵌入与von Mises矩进行解析平均；不据此认定代码继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p7 §4.5、p10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Ma, W., Zhao, Z., Zhao, C., Ouyang, W., and Zhong, H.-S. Glasses-free 3d display with ultrawide viewing range using deep learning. Nature, 648(8092):76, 2025.", "identifier_if_present": null, "relation_candidate": "组件复用、比较基线", "shared_component": "EyeReal相位合成U-Net与条件渲染管线", "claimed_difference": "由一次相位回归扩展为周期嵌入、RB监督及迭代生成。", "basis": "target_paper_only", "target_locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §4.6、p10参考文献、p14 A.5。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "二维提升与解析对称边缘化实质改变周期BFN的训练和采样接口，并有晶体消融支持；不只是单一性能调参，但仍建立在已有BFN框架上。", "central_increment": "CrysBFN已实现周期晶体生成（本篇转述）；本作在二维高斯与已知对称性条件下新增确定可加精度和闭式RB目标，支持证据为式(18)/(26)/(31)及表4/6；尚待排除预算差异与CLF物理实现缺口。", "soundness_observation": "高斯精度可加的代数依据清楚，但不等于圆周集中度或生成质量单调改善。命题4.1覆盖范围宽于附录von Mises证明草图；未完成一般定理验证或实验复现。", "significance_observation": "意义在于周期科学数据的统一处理及可观测的CSP收益。工程上复用主干，主要新增周期头、解析目标和CLF双域适配；实际开发成本未报告。", "main_open_question": "CLF所报PSNR是否来自实际可显示的xbase经sin²(Pxbase)渲染，而非含δcos残差的嵌入解码结果？"}

limitations：[{"text": "作者承认迭代CLF推理慢于一次回归器。", "basis": "author_report", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p9结论。"}, {"text": "CLF只验证单场景、10组OOD输入，且画质与延迟使用不同分辨率；不能视作1080p画质与跨场景泛化的联合证明。", "basis": "model_inference", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §5.2。"}, {"text": "式(48)允许δcos改变解码强度，但实际LCD仅显示xbase；物理可实现性可能被残差绕过。正文称加入小重建项，附录(46)却将RB项乘0.01，权重口径也需核对。", "basis": "model_inference", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p8 §4.5.2、p13—14 A.5。\n \n"}, {"text": "种子数量、显著性检验和逐方法预算不全；MPTS-52单次RMSE本作较差，多种子均值差也很小，不能据此确认该指标显著改善。", "basis": "model_inference", "locator": "TEXT_OR_N7hieduZYV_18c17e0da693，p9表1、p15表4、p16附录C/E。"}]

minimal_check：{"question": "CLF增益在实际LCD相位的物理渲染中是否保留？", "control": "固定同一检查点、10组OOD输入和采样设置，分别计算sin²(Pxbase)与(1−vhat_cos)/2，并与相同分辨率EyeReal比较。", "observable_outcome": "两种渲染的PSNR差、强度不一致程度，以及物理渲染相对EyeReal是否仍有增益。", "resources": "作者检查点、相同数据与渲染器及一次推理评测；无需重训，GPU型号、显存和耗时未知。", "failure_or_stop_condition": "若增益仅存在于残差解码结果，显示质量结论需收缩；若检查点或原评测输入不可取得，停止并记录不可检验。"}

missing_fields：["原PDF图像及图1—3的可核验视觉内容。", "前作全文均未提供；EyeReal参考文献未列DOI或URL。", "CSP明确数据拆分、每组成分候选数量及逐方法训练/采样预算。", "多种子数量与种子值、显著性检验细节。", "GPU型号、批量、总训练耗时、表7推理工作量及CLF结果对应的具体N。", "CLF表中PSNR采用的精确渲染路径，以及独立的CLF残差头/RB分项消融。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

CSP二维提升和RB目标的增量有直接支持；CLF应用需先确认实际可显示相位的渲染分数，并补相同NFE/种子预算，才适合投入显示端应用。

身份与可加性的对象：题名及16页附件一致。单位圆嵌入后在R²做Gaussian更新，rho加alpha和闭式前向边缘成立；这是辅助Gaussian精度，不是圆周集中度或生成质量必然单调。命题4.1措辞覆盖任意圆周族，附录A.1–A.2实际只证明von Mises的向量合成集中度依赖夹角，不能据该证明独立确认一般不可能性。

核查定位：p001 title, PDF physical page5, Proposition4.1/Eq16–20, PDF physical page12, A.1–A.2；gaussian_algebra_confirmed_general_no_go_claim_unproven

RB目标推导：CSP均匀整体平移后验的S统计和I1/I0均值、CLF等先验二元符号的logistic/tanh均值可由所列Gaussian似然推出。实际PDF12式36有S复共轭，文本提取丢失，不能误报角度符号错误。Rao–Blackwell在给定模型和条件化信息下减少目标/梯度随机性，不证明物理上每条射线符号独立可实现，也未给实测梯度方差。

核查定位：PDF physical page7, Eq24–31, PDF physical page12–13, Eq35–45；closed_form_local_derivations_and_conjugate_confirmed

CLF物理输出与损失接口：PDF13式46为重建项+0.01 RB，与正文small reconstruction措辞相反。PDF14式48的cos/sin都含加性残差，而显示只取xbase；解码强度=(1−vhatcos)/2可与sin²(Pxbase)不同。单射线代数示例xbase=0、delta_cos=−2b即可完美解码目标b，实际相位渲染仍0；这说明接口无自动物理一致保证，不是实际多射线模型必能任意实现该残差或已学会绕过。p14称强度取嵌入解码，p15又给物理渲染式，表5采用哪条路径仍未消解。

核查定位：p008, hybrid description, PDF physical page13, Eq46, PDF physical page14, Eq48/output, PDF physical page15, Eq49；residual_decoder_vs_displayed_phase_gap_confirmed

CSP数字与预算：表4 MP20 70.05±.04对64.33±.24，MPTS52 27.03±.13对19.71±.72；后者RMSE.1105对.1112差很小，无种子数和检验不能称显著。表6去RB66.11、去2D60.02、去t66.17。固定NFE表8在10次本作59.13<60.18，200次69.78>64.35，500次70.06>62.14，故非所有采样预算均胜。74对89秒为未标样本量的200步工作量，非单样本延迟。

核查定位：PDF physical page15, Tables4/6, PDF physical page16, Tables7–8；source_results_and_budget_dependence_confirmed

CLF结果范围：单LEGO bulldozer场景10000训练双目对、10个不同姿态分布测试对；PSNR在360×640，而时间在1080×1920。表5本作31.40±1.05/35.1ms/28.49FPS；EyeReal27.46/19.4/51.55，共轭梯度34.31/691.2/1.447；是质量—速度折中，非同时最佳或1080p画质证明。N=1或2另有最终前向，表5具体N未标，6000epoch的总GPU时未知。

核查定位：p008, section5.2, PDF physical page14, sampling, PDF physical page15, Table5, p016, training；single_scene_two_resolution_tradeoff_confirmed

本地补充/限定：["确认CSP后验公式的S复共轭存在，避免因抽取丢失而增加假问题。", "将CLF物理渲染疑问绑定到式46/48/49及单射线代数例；不认定未查看的评测代码一定用了错误路径。"]

核查局限：["未执行代码、生成晶体、测试显示或核读前作；单射线例仅检验接口逻辑。", "没有确认一般圆周不可能定理或所有RB/采样条件；本文局部核对不等同完整证明验证。", "16页版本角色仍未确认；原失败发送已恢复且只有一轮有效初评，不追加调用。"]


## pro100 · What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning

论文 OR_5W30WwL8wt；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8", "source_url": "https://api2.openreview.net/pdf?id=5W30WwL8wt\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "4ee77f719e4b602762248096f1f33e897a74be58e78a5e81eb24b2f5d4b461cd", "source_pdf_sha256": "5ae9ba0495c85aedef81bfcfad8589c31e8a15fdde994985b74b31c698fadb49"}], "read_ranges": ["TEXT_OR_5W30WwL8wt_5ae9ba0495c8：物理页1–47全部提供文本，包括主文1–9页、致谢及参考文献10–12页、附录A–H第13–47页；连续页标无缺失，首页题名匹配。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供原PDF图像；图1–15仅有图题、部分标签及收益表文本，不能核验轨迹形状或图5所称混沌程度。", "双栏文本交错，部分公式分数、上下标及括号有损；以下保留可辨认的定理条件，不视为公式排版核验。", "附件版本角色未核实，不认定为最终出版版。"]}

问题：有限正规形博弈中，仅凭纯策略单边偏好的顺序，能否判断连续时间学习的稳定集合？何时必须知道收益大小？

方法：分析分数动力学ẏ=v(Q(y))。club对弱有利单边偏离闭合，s-club仅对严格有利偏离闭合；span(H)是H支持的独立混合策略集合，即面之并而非凸包。以Fenchel gap处理子博弈；定义Φ(β,α)=Σ_i[u_i(α_i,β_-i)−u_i(β)]，对所有β∈H、α∉H要求Φ≤0或<0，分别得到rad、s-rad，并构造局部能量函数证明稳定性。

作者主张：偏好闭包约束动态稳定性；对子博弈，偏好条件可给出等价刻画。

论文证据：定理1：FTRL稳定集合的骨架为s-club；定理2：强连通偏好图排除SD的真子集吸引子；定理3及推论1给出无ties子博弈的club—渐近稳定等价。

模型推断：实质扩展已有RD结果，尤其覆盖non-steep子博弈情形；不是首次建立偏好图与吸引子的联系。

定位：['TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p6定理1–3；p7推论1–3；附录F、G.2。\n', 'TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p7推论1–2。\n']

作者主张：非子博弈club集合的span可在所有本文允许的FTRL下不稳定。

论文证据：命题2构造2×2×2博弈，H=A∖{BLB}为唯一非空真club集合；其三面之并存在任意接近的全支撑初值，轨迹仍逃离固定邻域。

模型推断：增量在FTRL适用范围及全支撑逃离证明，而非首次否定纯序数充分性。

定位：['TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p7命题2；p33–38附录G.3。\n']

作者主张：以收益大小补充偏好信息，为任意人数、任意纯策略集合提供稳定性充分条件。

论文证据：定理4：s-rad集合的span是SD吸引子；定理5：rad且club集合的span是RD吸引子。附录H分别使用指数Fenchel能量与集合外概率质量证明。

模型推断：统一非乘积集合的稳定性保证，是中心理论增量；不是必要充分刻画。

定位：['TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p8定理4。\n', 'TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p9定理5；p38–47附录H。\n']

key_results：[{"setting": "附录G.3的2×2×2反例，混合点x*=(1/2,1/2,1)", "baseline": "纯策略H的club闭包", "metric_or_guarantee": "第三人在混合点存在向H的span外运动的严格收益诱因", "reported_values_and_units": "第三人选择T的收益为1/2，选择B为5/2，差为2个构造收益单位；属于解析构造值，不是实验测量。", "information_and_compute": "使用给定完整收益表；逃离结论另由能量估计证明，非仅凭正收益差。", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p34，G.3。\n"}, {"setting": "可查询显式正规形收益表，n=|N|，A为全部纯策略组合", "baseline": null, "metric_or_guarantee": "rad / s-rad判据的理论计算复杂度", "reported_values_and_units": "给定H的检查为O(n|H||A∖H|)步骤；构建payoff-flux图并寻找相应集合为O(n|A|²)时间。", "information_and_compute": "需收益大小而非仅偏好顺序；这是输入规模上的运算阶数，未报告硬件耗时。", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p8，§6。\n"}, {"setting": "弱无环、无ties博弈；满足E.1的SD", "baseline": "此前势博弈结果[54]，仅据本篇转述", "metric_or_guarantee": "最小吸引子恰为严格Nash均衡", "reported_values_and_units": null, "information_and_compute": "结构性定理，不等于所有初值均收敛到均衡，也不提供统一收敛时间。", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p7推论3；p32–33证明"}]

prior_work_candidates：[{"citation_as_printed": "[8] Biggar, O. and Papadimitriou, C. H. Sink equilibria and the attractors of learning in games. https://arxiv.org/abs/2502.07975\n, 2025.", "identifier_if_present": "arXiv:2502.07975", "relation_candidate": "理论扩展", "shared_component": "sink equilibrium、local source、收益型稳定条件", "claimed_difference": "将RD不稳定性分析扩至一般FTRL和全支撑初值；rad不限制为两人博弈。", "basis": "target_paper_only", "target_locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p3、p10参考文献[8]、p38 Remark G.2", "prior_actually_read": false}, {"citation_as_printed": "[10] Biggar, O. and Shames, I. The replicator dynamic, chain components and the response graph. In ALT ’23: Proceedings of the 34th International Conference on Algorithmic Learning Theory, 2023.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "偏好图强连通性、chain transitivity及吸引子", "claimed_difference": "将RD的图—动力联系推广到满足条件的正则化strategy flow。", "basis": "target_paper_only", "target_locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p6、p10参考文献[10]、p13附录A", "prior_actually_read": false}, {"citation_as_printed": "[14] Cauvin, P.-L., Legacci, D., and Mertikopoulos, P. The impact of uncertainty on regularized learning in games. In ICML ’25: Proceedings of the 42nd International Conference on Machine Learning, 2025.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "club子博弈稳定性与能量函数", "claimed_difference": "据本文，[14]以Bregman能量处理steep随机连续时间FTRL；本作Fenchel gap覆盖确定性连续时间的non-steep情况。", "basis": "target_paper_only", "target_locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p10参考文献[14]；p13附录A", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "在已有偏好图—吸引子研究路线内，给出非平凡的一般性扩展、反例和收益判据，构成实质理论增量；不足以认定路线级首创。", "central_increment": "前作已揭示RD中序数信息的能力与局限（本篇转述）；本作扩展FTRL稳定性联系，并以rad条件为任意集合恢复保证，支持为定理1–5及命题2。", "soundness_observation": "附录F–H提供证明链；必须保留无ties、E.1及rad与club的区别。本轮未逐条复证，不能把定理4扩大到所有non-steep FTRL。", "significance_observation": "价值在可检查的集合稳定性保证，而非预测每条轨迹；工程实现难度和实际MARL收益未评测。", "main_open_question": "与[8]及同期[9]相比，rad判据具体新增哪些不能由已有条件推出的稳定集合？"}

limitations：[{"text": "rad仅为充分条件：附录给出club子博弈虽稳定却不rad，某跨集合payoff flux为2>0。", "basis": "author_report", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p16附录B.2，式B.1。\n"}, {"text": "结论针对有限博弈的连续时间精确收益动力学；未建立离散步长、采样反馈或神经网络MARL的对应保证。", "basis": "model_inference", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p3、p5、p21模型定义"}, {"text": "多项式复杂度相对显式收益表；|A|可随人数指数增长，找到rad集合也不保证得到非平凡真子集，不能等同于高效求混合NE。", "basis": "model_inference", "locator": "TEXT_OR_5W30WwL8wt_5ae9ba0495c8：p3策略空间定义；p8复杂度讨论"}]

minimal_check：{"question": "G.3构造的纯策略闭包与混合点向外偏离是否同时成立？", "control": "固定原收益表，分别检查H的纯顶点出边与x*=(1/2,1/2,1)处的期望收益差。", "observable_outcome": "H无向外弱改进边；前两人无差异，第三人向B偏离增益为2。", "resources": "8个纯策略组合的三人收益表，纸笔或符号计算；无需训练，耗时未估计。", "failure_or_stop_condition": "若出现H出边或收益差不符则停止并复核；通过只支持构造机制，不替代一般FTRL逃离证明。本轮未执行该检验。"}

missing_fields：["原PDF图像、图示轨迹及部分公式精确排版不可见。", "图示仿真的硬件、积分参数、运行预算与重复次数未报告；无实证训练或基准性能结果。", "前作全文及其他版本未提供；最终出版版身份未核实。", "参考文献[10]、[14]未印可回传的独立标识；纯理论定理无实验数值。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

偏好闭包何时足够、何时需收益幅度的边界和反例明确，适合继续读Fenchel gap与rad能量证明；前作覆盖和离散/随机扩展应另核。

身份和稳定性概念：首页完整题名与47页附件一致，内页短标题The Role of Preferences...是同附件页眉。有限正规形连续时间FTRL；span(H)为独立混合支持包含于H的面之并，不是纯点凸包。FTRL初始化限choice map像，SD吸引子允许全部相邻面初始化，两个概念不能互换。

核查定位：p001 title, PDF physical page6, stability distinctions, PDF physical page7, subgame equivalences, p033, EqG.15；identity_and_setwise_not_trajectory_prediction_confirmed

主要条件区分：FTRL稳定→骨架s-club；club子博弈→FTRL渐近稳定，无ties下才得club与该稳定性等价。一般集合s-rad→SD吸引子须E.1，即1/theta''延拓Lipschitz且0点为0，蕴含steep；弱rad+club→吸引子限RD。弱无环无ties的最小吸引子为strict NE，不说明每条轨迹都收敛或给收敛时间。

核查定位：PDF physical page6–9, Theorems1–5/Corollaries1–3, p021, AssumptionE.1/PropositionE.3；nonsteep_subgame_vs_steep_general_set_scope_confirmed

反例构造的有界算术核对：PDF33收益表中BLB=(0,0,0)唯一外顶点。三个相邻H顶点FLB/BRB/BLT向BLB的对应玩家收益分别2→0、1→0、1→0，因此H无向外弱改进边。顶面四点成改进环，FLT→FLB→FRB→BRB→BRT把另外三点接回，支持唯一非空真club。x*=(.5,.5,1)前两人均无差，第三人T均值.5、B均值10/4=2.5、增益2。该点仍是mixed local source，不反驳所引原猜想，只排除pure-source加强及扩展FTRL/全支撑初值。

核查定位：PDF physical page33–34, G.3/payoff table, PDF physical page38, RemarkG.2；eight_profile_construction_mechanism_checked_without_simulation

逃离证明与充分而非必要：G.19切向能量漂移与s=1−r成比例；G.20由强凸界控制前两人偏离，G.28–29约束累计漂移，让第三人s达到固定eta时前两人仍离边界远，从而dist(x,S)=sqrt2 min(1−p,1−q,s)固定正值。这比单凭正收益差更强；中间常数/全47页未逐式审计。PDF16另给稳定club子博弈跨集flux=(−3)+5=2>0，确认rad非必要。

核查定位：PDF physical page34, EqG.19, p035, G.20–22, p037, G.28–29/escape, PDF physical page16, EqB.1；escape_argument_local_chain_and_nonnecessity_confirmed

收益判据与计算口径：flux对单边可比纯点退化为单玩家收益差，H.1成立；在子面上的多线性最大值取纯顶点，支持纯收益判据向混合面的提升。给定H检查O(n|H||A\H|)，全部flux图O(n|A|²)，相对显式收益表而非玩家数多项式。找到集合可能是全A，不保证非平凡真吸引子；图5展示不同轨迹不能单靠可视化证明混沌或真实MARL性能。

核查定位：PDF physical page8, complexity, PDF physical page9, Figure5, PDF physical page38, H.1–H.2, PDF physical page47, theorem5 final scope；cardinal_information_and_explicit_table_complexity_confirmed

本地补充/限定：["按原表实际核对闭包及混合点收益，属于本轮有界来源算术，不是执行额外研究练习或仿真。", "强调唯一club需限定非空真集合；全A始终闭合，文中某处省略proper不改变命题2完整限定。"]

核查局限：["未完整复证定理1–5或核读前作/同期论文；只是关键条件、构造算术和局部能量链。", "未运行轨迹积分、MARL实验或额外研究练习；图像不充当混沌数学证明。", "第一页只核题名；当前附件版本角色未确认，论文没有可报告的训练吞吐实验。"]

