# 单轮全文初评与有界本地核对 51–60

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro051 · Floating-Point Networks with Automatic Differentiation Can Represent Almost All Floating-Point Functions and Their Gradients

论文 OR_g89qqA6qmD；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b", "source_url": "https://api2.openreview.net/pdf?id=g89qqA6qmD\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "066b68af8c482d82fe9d26e856a869138ee5d80ad9c73d0fbf37062a2ecd73c8", "source_pdf_sha256": "4e9ea06c2c0b163883ba313e8f0a0c2046913f5bc9a165bf92e043c74b7d9d56"}], "read_ranges": ["TEXT_OR_g89qqA6qmD_4e9ea06c2c0b：物理页1–33连续全文；包括正文§§1–5、参考文献、附录A–C及Tables 1–4的提取文本。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["页标连续，未发现缺页；仅阅读文本，未查看PDF图像。双栏串行、公式上下标和表格对齐有损，不能据此确认所有证明细节。\n", "前作全文和作者代码未提供；未搜索、运行代码或复现实验，未确认最终出版版身份。"]}

问题：有限精度网络能否同时精确表示任意目标函数值与输入梯度，并让同一网络针对不同上游梯度产生预定响应？这里的梯度是AD程序输出，不是离散函数的经典导数。

方法：把网络分成表示目标值但反向为零的f1，以及前向为零但产生目标梯度的f2，再按指定顺序拼接。利用逐点指示函数、顺序加法、梯度消除和浮点乘法转移控制两条通路；可变上游梯度情形另构造梯度阈值指示器。

作者主张：给定目标值f*、上游梯度h及目标输入梯度g，浮点网络能同时精确表示前两者要求的前向与反向结果。

论文证据：Theorem 3.1给出至少7层的存在性保证；Theorem 3.6以一般激活条件推广，证明由值通路与梯度通路的构造组合得到。

模型推断：相对仅表示函数值，新增的是计算图层面的独立梯度表达保证，不只是逼近精度改进。

定位：['TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.5 Theorem 3.1；p.7 Theorem 3.6；pp.24–25 Appendix C.1。\n']

作者主张：同一网络可随上游梯度y变化，实现任意满足g*(x,−y)=−g*(x,y)的目标响应，同时保持f=f*。

论文证据：Theorem 3.2及一般形式Theorem 3.8；Lemma 3.7和Appendix B.4利用梯度阈值构造完成扩展。

模型推断：中心增量是反向映射不再必须正比于上游梯度；这是浮点逐步舍入带来的机制差异，而非增加训练损失。

定位：['TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.5 Theorem 3.2；p.7 Theorem 3.8；pp.15–18 Appendix B.4。\n']

key_results：[{"setting": "Theorem 3.1：Σ包括ReLU、ELU、GELU、Swish、Sigmoid、tanh的舍入版本；X=[−Mσ,Mσ]^d_F。", "baseline": "本篇转述的仅函数值浮点表示定理；不是实验基线。", "metric_or_guarantee": "所有x∈X满足f(x)=f*(x)，D_f,x(h*(x))=g*(x)。", "reported_values_and_units": "L≥7层。前四种激活Mσ=2^(e_max−2)、Hσ=Ω；Sigmoid/tanh的Mσ=2^(e_max−1)，Hσ分别为2^(M−1)、2^(M−2)。Ω为最大有限浮点数，|h*|≤Hσ。", "information_and_compute": "构造使用目标值及梯度，并枚举X；未量化宽度、参数量、时间或内存。无训练获得性保证。", "locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.5正式常数定义与Theorem 3.1。\n"}, {"setting": "Theorem 3.2：同一X和激活条件；对所有|y|≤Hσ同时成立，目标g关于y为奇函数。", "baseline": "精确算术中D_f,x(y)必须正比于y。", "metric_or_guarantee": "固定一个网络，同时满足f=f及D_f,x(y)=g*(x,y)。", "reported_values_and_units": "L≥2^(E+1)+2M+9层；为精确表示保证，不是实测误差。", "information_and_compute": "额外枚举梯度阈值；未报告可变上游梯度构造的实验配置或计算预算。", "locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.5 Theorem 3.2；p.25 Appendix C.2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Hwang, G., Park, Y., Lee, W., and Park, S. Floating-point neural networks can represent almost all floating-point functions. In Forty-second International Conference on Machine Learning, 2025b.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "可区分性、顺序加法和浮点指示网络。", "claimed_difference": "本作增加AD梯度控制及联合表达定理。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.10 References；p.11 A.3；p.14 B.2。\n", "prior_actually_read": false}, {"citation_as_printed": "Park, Y., Hwang, G., Lee, W., and Park, S. Expressive power of ReLU and step networks under floating-point operations. Neural Networks, 175:106297, 2024.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "浮点网络的函数值表达能力问题。", "claimed_difference": "本篇转述前作覆盖ReLU/step的函数值，本作处理函数值与AD输出。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b pp.1–2 §1；p.10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Park, S., Park, Y., and Hwang, G. On the expressive power of floating-point transformers. arXiv preprint arXiv:2601.16450, 2026.", "identifier_if_present": "arXiv:2601.16450", "relation_candidate": "组件复用", "shared_component": "前作Lemma 17作为本篇Lemma B.7，支持浮点乘法转移。", "claimed_difference": "复用的是数值引理，不是Transformer架构；本作研究前向值与反向响应的联合表达。", "basis": "target_paper_only", "target_locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b p.10 References；p.18 Lemma B.7。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "在已有浮点函数值表示基础上，新增独立AD梯度及非线性上游梯度响应的构造性保证，属于实质理论增量；尚不足以确认为路线级首创。", "central_increment": "前作已表示函数值（本篇转述），本作在规定浮点语义下新增联合值—梯度表达；证据为Theorems 3.1–3.8，待排除关键证明及实现语义问题。", "soundness_observation": "有详细证明文本但未完成证明审计。Lemma B.8按所给文本允许g0=0却输出非零g1，与AD零输入保持零冲突，疑似变量或条件误写；不能据此直接否定条件更严格的主定理。", "significance_observation": "有助于区分数值函数与计算图反向行为；未证明实际训练收益、效率或梯度攻击防护效果。", "main_open_question": "Appendix B.4的梯度阈值拼接能否在逐步舍入、左结合且无溢出的条件下，严格实现任意允许的奇映射？"}

limitations：[{"text": "作者明确限定有限浮点数、舍入和计算顺序，构造中避免非有限中间值；不能直接推广到重排、融合或不同精度的实现。", "basis": "author_report", "locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b pp.3–5 §§2.2–2.4"}, {"text": "“Almost all”由具体输入域、梯度范围及兼容条件落实，不是随机函数覆盖概率。逐点枚举与深度界不意味着实际网络可承受；作者只称实现了ReLU的Lemmas 3.4–3.5，未给系统评测。", "basis": "model_inference", "locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b pp.5、7–9。\n"}, {"text": "材料内部有未消解差异：p.2的Sigmoid梯度范围与p.5正式定义不同；pp.25–26低指数位格式的层数口径不一致。本记录采用正式主定理，不合并低精度层数；B.8的零输入问题也需核对原版。", "basis": "model_inference", "locator": "TEXT_OR_g89qqA6qmD_4e9ea06c2c0b pp.2、5、19、25–26。\n \n \n"}]

minimal_check：{"question": "梯度阈值组合能否实现最小的非单调奇映射？", "control": "用M=2、E=4的逐步舍入模拟器、ReLU和X={0}；令前向恒零，目标反向仅在y=±1输出±1，其余为零，按B.4构造并与目标查表对照。", "observable_outcome": "穷举全部有限y，检查前向恒零、AD逐值完全匹配且中间无Inf/NaN。", "resources": "CPU、对应浮点模拟器及独立实现的B.4构造；运行时间和内存未知。", "failure_or_stop_condition": "满足规定语义仍出现反例则该构造失败；若文本歧义使构造无法确定，停止并记录歧义，不据此判定主定理错误。"}

missing_fields：["实际宽度、参数量及硬件、时间、内存预算未报告", "作者实现检查的测试配置、覆盖范围与误差统计未报告", "PDF原版面、代码正文和前作全文未提供"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

计算图反向响应与离散前向函数分离的机制值得继续理解；先沿值通路/梯度通路核查关键引理修正，再考虑与真实AD后端语义的关系。

身份与梯度对象：33页官方当前附件及输入返回绑定一致。梯度指按局部AD规则进行的浮点反向程序输出，不是有限离散函数的经典导数。前向与反向均采用逐步舍入、平局取偶、左结合顺序，并要求构造中无Inf/NaN；改变融合或归约顺序后不能直接套用。

核查定位：text_delivery_manifest.json, structured/pro051.json, p003–p004, §2.2–2.4；source_and_arithmetic_semantics_confirmed

中心联合表达结论的条件：原PDF第5页Theorem3.1要求E>=6及基础M范围，允许L>=7，且h*(x)=0必须g*(x)=0。Theorem3.2对同一网络的可变上游y要求g*(x,−y)=−g*(x,y)，层数为2^(E+1)+2M+9。输入范围Mσ及梯度范围Hσ依激活而异；Almost all不是已测随机函数覆盖概率，不能删去域和奇对称条件。

核查定位：PDF physical page 5, constants and Theorems3.1–3.2, p004, Assumption1；decisive_theorem_conditions_confirmed

构造机制及规模：一条通路表示目标值但反向为零，另一条前向恒零而反向给目标梯度，按固定顺序组合。第5、8页明确枚举X内全部输入，层数少不代表参数量或运行资源少。第7页仅称实现验证ReLU的Lemmas3.4–3.5，未给可变上游任意奇映射的系统评测、训练获得性或可承受宽度。

核查定位：PDF physical page 5, §3.1, p008, §4.1–4.2, p007:L0043-L0045；mechanism_and_existential_scope_confirmed

LemmaB.8零输入条件错误：原PDF第19页B.8只约束g1非零，却未排除g0=0，并声称Df(g0)=g1。按第4页局部AD规则，零上游乘有限权重、有限激活导数并相加始终为零，因此该陈述按字面不成立。第9页主Lemma4.4正确地要求输入y非零，显示可能是B.8变量/条件误写；本地不将该局部错误当成主定理已被反驳。

核查定位：PDF physical page 19, LemmaB.8, p004:L0035-L0061, p009, Lemma4.4；literal_lemma_conflict_confirmed_with_main_lemma_qualification

低指数位层数口径：第25页C.3先称E4全部激活比7层多1层，又给Sigmoid的τ=9、其他8；第26页CorollaryC.5则给E4 Sigmoid13、其他10等不同阈值。部分较大阈值可以只是较松充分条件，不能仅凭不同数值判为数学矛盾；但所称所需层数及改进来源未统一，不能合并为一个已确认最小深度。主7层结果保留E>=6条件，E5的float16应查附录分支。

核查定位：PDF physical page 25, C.3, p026, CorollariesC.5–C.6, PDF physical page 5, E>=6 discussion；low_exponent_depth_claims_kept_separate

本地补充/限定：["原PDF确认B.8的零上游遗漏，并与主Lemma4.4非零输入条件对照，限定问题范围。", "低指数位不同充分层数不必相互矛盾；本地将其表述为口径未统一及最小层数未确认，不扩大为已证伪主结论。"]

核查局限：["未逐式核验B.4的任意奇映射拼接，也未运行作者模拟器或训练实验。", "未独立核读前作，L2仍是暂评；没有认定构造的历史首创。", "未审计全部辅助引理及非有限值边界；原文其他疑点未全部确认。", "Pro只读全文文本，本地观察三页原PDF。"]


## pro052 · Frequentist Consistency of Prior-Data Fitted Networks for Causal Inference

论文 OR_p1GwEz0pix；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_p1GwEz0pix_f84c1dce3c82", "source_url": "https://api2.openreview.net/pdf?id=p1GwEz0pix\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "2a997c92c410caf36d3b299772a4815e1a3a1f2c03a891c5b294747047b53e25", "source_pdf_sha256": "f84c1dce3c82d5082cafe0220132675e3d4701fb02b77d55e3204fe432d625ed"}], "read_ranges": ["TEXT_OR_p1GwEz0pix_f84c1dce3c82：物理页1–31全部所供文本；包括正文1–9页、参考文献10–12页、附录A–G第13–31页。题名匹配，连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–15仅有图题、坐标及正文说明，不能读取曲线数值。", "表1–2部分行列串接；公式上下标、帽号及双栏顺序可能失真。表3–5所引用行可辨。", "图14的实际耗时、显存数值及图15的ATE位置和区间不可读。"]}

问题：PFN生成的ATE后验能否随样本增加，与半参数有效A-IPTW的不确定性对齐，而不只是点估计一致？

方法：输入观测数据(X,A,Y)。从TabPFN取得结局及处理分配PPD，用Gaussian和beta–Bernoulli copula的MP更新构造μ0、μ1、π函数后验样本，再以Bayesian bootstrap加权未中心化有效影响函数，输出校正ATE后验；不重训骨干。

作者主张：现有PFN可能受到prior-induced confounding bias影响，妨碍频率学一致性。

论文证据：对三类PFN的训练先验分别采样512份、每份10000条数据，正文报告混杂量Δ集中于零附近；作者承认实际后验偏差难以解析。

模型推断：支持风险诊断，不构成所有PFN渐近不一致的定理。

定位：['TEXT_OR_p1GwEz0pix_f84c1dce3c82：p5–6，§5.1、图2文字。\n']

作者主张：MP-OSPC无需重训即可改善PFN的ATE后验校准。

论文证据：实现TabPFN+copula及CausalPFN/TabPFN组合，并比较独立、平行、平滑耦合；默认N=100步、B=100次后验抽样。

模型推断：主要增量是补齐点态PPD到可校正ATE后验的接口，而非重新发明OSPC。

定位：['TEXT_OR_p1GwEz0pix_f84c1dce3c82：p7 §5.3、p20–21附录D。\n']

作者主张：OSPC满足半参数BvM；不同MP耦合仅改变更高阶方差贡献。

论文证据：定理1明确基于Yiu等的定理4；命题1分解bootstrap和干扰函数后验方差。

模型推断：这是条件化理论迁移及方差分析，未证明实际预训练PFN满足全部条件。

定位：['TEXT_OR_p1GwEz0pix_f84c1dce3c82：p6定理1、p15–16附录A.3、p17–19命题1。\n']

key_results：[{"setting": "合成数据，dx=25；TabPFN+copula smooth，ρ=0.25；40次运行。", "baseline": "相同结局后验的MP-plug-in，对比MP-OSPC。", "metric_or_guarantee": "ATE后验PIT的经验dKS；无量纲，越低越好，不是覆盖率。", "reported_values_and_units": "作者报告：ntrain=500时0.680→0.355；5000时0.455→0.810；10000时0.255→0.845。箭头表示基线→校正。", "information_and_compute": "训练/测试分开，默认N=B=100；非本地复现。", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p26表3。\n"}, {"setting": "IHDP，训练672、测试75、dx=25，100个分割；TabPFN+copula smooth。", "baseline": "相同ρ的MP-plug-in，对比MP-OSPC。", "metric_or_guarantee": "dTV与dKS，均无量纲、越低越好；±为标准误。", "reported_values_and_units": "ρ=0.25：dTV由0.279±0.014变为0.271±0.014，dKS由0.08变为0.06。ρ=0.5：dTV由0.281±0.014变为0.314±0.014，dKS由0.04变为0.07。", "information_and_compute": "默认N=B=100；半合成参考方差中的倾向由TabPFN估计。", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p22 §E.2、p27表5。\n"}, {"setting": "ACIC 2016：77个数据生成过程，每个10次运行；n=4802、dx=82。", "baseline": "TabPFN+copula smooth、ρ=0.5的MP-plug-in，对比MP-OSPC。", "metric_or_guarantee": "同一骨干方案组内，按dTV或dKS获胜的比例，越高越好。", "reported_values_and_units": "%TV由14.29%变为37.66%；%KS均为22.73%。不是跨全部方法的准确率或覆盖率。", "information_and_compute": "默认N=B=100；因耗时过长排除了TabPFN-only MP。", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p9表2、§6.2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Yiu, A., Fong, E., Holmes, C., and Rousseau, J. Semi-parametric posterior corrections. Journal of the Royal Statistical Society Series B: Statistical Methodology, 87(4):1025–1054, 2025.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "OSPC及其BvM理论", "claimed_difference": "本篇通过MP使PFN输出满足校正流程所需的函数后验接口。", "basis": "target_paper_only", "target_locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p6定理1、p12参考文献、p15–16附录A.3。", "prior_actually_read": false}, {"citation_as_printed": "Nagler, T. and Rügamer, D. Uncertainty quantification for prior-data fitted networks using martingale posteriors. arXiv preprint arXiv:2505.11325, 2025.", "identifier_if_present": "arXiv:2505.11325", "relation_candidate": "方法继承", "shared_component": "PFN初始化与copula后续更新", "claimed_difference": "从点态MP扩展到因果干扰函数的联合后验，并结合ATE校正。", "basis": "target_paper_only", "target_locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p3 §2.2、p7 §5.3、p11参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Balazadeh, V., Kamkari, H., Thomas, V., Li, B., Ma, J., Cresswell, J. C., and Krishnan, R. G. CausalPFN: Amortized causal effect estimation via in-context learning. In Advances in Neural Information Processing Systems, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "条件结局均值后验；亦用于组合方案", "claimed_difference": "加入TabPFN倾向后验和OSPC，而非仅使用naïve plug-in。", "basis": "target_paper_only", "target_locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p5 §4、p10参考文献、p13–14附录A.1。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "联合函数后验与因果校正的整合具有实质方法价值；但不能把中等样本改善等同于已证明现有PFN频率学一致。", "central_increment": "据本文转述，前作已有OSPC及点态PFN-MP；本篇在结局和倾向输出可用时补齐联合后验接口，以构造、方差分析及实验支持，尚待验证实际PFN的收缩前提。", "soundness_observation": "文本式(6)/(23)以ψ中心，而式(25)及证明结尾以ψ̂中心；证明展示弱收敛，结论却写TV收敛，需核对原PDF。附录C末另用了oP(1/n)后验尾概率，强于仅要求后验质量趋1。未完成证明审计。\n", "significance_observation": "无需重训即可研究和改善ATE不确定性；实际优势依赖骨干、样本量和重叠程度，不是通用于CATE的新保证。", "main_open_question": "实际PFN与有限步MP构造能否满足BvM前提，而非仅在中等样本区间暂时校准？"}

limitations：[{"text": "作者承认R2在大样本时反升，当前PFN缺正式渐近保证；MP完整收敛有时需约300步，默认仅100步。", "basis": "author_report", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p9 §6.1及结论、p23 §F.1–F.2。"}, {"text": "表3在ntrain=5000的结果与§F.3.2所称≤5000总能改善不符；表5也显示校正并非普遍获益。相对改善不等于绝对良好校准。", "basis": "model_inference", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p25 §F.3.2、p26表3、p27表5。"}, {"text": "半合成参考方差借助TabPFN估计倾向，且参考方差与OSPC均截断π<0.05，非独立oracle参照；合成高斯噪声也不满足按字面陈述的残差一致有界条件。", "basis": "model_inference", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p8脚注5、p21 §D.2、p22 §E.1。\n"}, {"text": "附录G另有264条跨国疫情观测、5折交叉拟合案例，但无因果真值；与A-IPTW对齐不能验证i.i.d.、无未测混杂或真实覆盖率。", "basis": "model_inference", "locator": "TEXT_OR_p1GwEz0pix_f84c1dce3c82：p31附录G、图15文字。"}]

minimal_check：{"question": "表3的大样本退化是否主要来自倾向后验？", "control": "固定合成数据、结局后验、ρ=0.25和N=B=100，仅将TabPFN倾向替换为真倾向，保持相同截断规则。", "observable_outcome": "比较ntrain=500、5000、10000下dKS、95%区间覆盖率和宽度，检查oracle倾向是否消除退化。", "resources": "需要生成器及模型checkpoint；图14参考环境为AMD EPYC 9455 48-Core CPU和1张H200，最低需求与耗时未知。", "failure_or_stop_condition": "真倾向仍不能消除退化，则主要归因于倾向模型的解释不足；缺可运行模型或数据时停止，不报告复现成功。"}

missing_fields：["全部图形及其精确读数缺失；耗时和显存仅有不可见曲线，不能当成未做资源实验。", "PFN具体收缩率、预训练成本和总GPU时数未报告。", "前作全文未提供；Yiu与Balazadeh参考文献未列可回传的DOI或arXiv标识。", "未搜索外部资料、核读代码、复现实验或完成独立证明审计。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

从点态PPD到可作ATE校正的联合函数后验具有实质接口价值；继续阅读先厘清BvM陈述与全部收缩条件，再判断有限样本校正在哪些重叠/样本区间有收益。

身份、因果对象与机制：31页官方当前附件及全文返回绑定一致。目标为ATE，需i.i.d.观测、处理一致性、无未测混杂和强重叠。点态PPD不能唯一确定跨输入函数后验；copula/MP的不同耦合是新增建模选择，再接既有OSPC与Bayesian bootstrap，不能称原PFN函数后验被唯一恢复。CATE仍是另一个问题。

核查定位：text_delivery_manifest.json, structured/pro052.json, PDF physical page 4, Figure1 and causal assumptions, p005–p007, §4–5.3；source_and_causal_scope_confirmed

BvM的中心与收敛模式：原PDF第4页式6和第15页式23确实以真ψ为中心，式25及第16页证明结尾则以估计量ψhat为中心。条件后验以真值中心的随机平移不能一般忽略；需要统一陈述。此外证明草图展示弱收敛箭头，未单独给升级到声明TV收敛的步骤。被引用前作未独立核读，不能据草图确认完整TV保证。

核查定位：PDF physical page 4, Definition1 and Eq6, PDF physical page 15, Eq23–25, p016, Eq26–29 and conclusion；centering_and_proof_mode_mismatch_confirmed

乘积速率与完整条件不可互代：按所印式11/22单独理解(a)，误差乘积趋零不推出第16页式29的影响函数L2收敛。例如μ完全正确为0、真实π=1/4而后验π恒1/2，Y为独立±1噪声时乘积为0，但影响函数差的平方L2为4/3，候选/有效方差分别4和16/3。若标题L2 concentration隐含两个干扰函数各自一致性，应明确补入；该例不反驳补足后条件。附录第19页又使用后验尾概率oP(1/n)，强于仅质量趋1的陈述。

核查定位：p006, Theorem1 Eq11, PDF physical page 15, Eq22, p016:L0014-L0017, p019:L0042-L0044, local_check/product_rate_scope_argument.json；literal_product_condition_insufficient_qualified

校正并非随样本量普遍改善：原PDF第26页表3确认TabPFN+copula smooth ρ=.25的dKS：ntrain500时.680→.355，5000时.455→.810，10000时.255→.845，后两者明显更差。第27页表5在IHDP的ρ=.25时dTV .279±.014→.271±.014、dKS .08→.06，而ρ=.5时.281±.014→.314±.014、.04→.07。dKS是PIT分布距离，不是覆盖率或准确率；改善也不代表绝对校准良好。

核查定位：PDF physical page 26, Table3, PDF physical page 27, Table5, p009, evaluation metrics；decisive_results_and_metric_denominators_confirmed

实际PFN、有限MP及参照的边界：作者未证明实际PFN的收缩率，并观察大样本逆倾向误差反升。默认MP步数N=100、抽样B=100；第23页称部分后验标准差到250–300步或更久才趋平。半合成参考方差亦用TabPFN倾向估计，参考与OSPC都截断π<.05，因而不是完全独立oracle参照。ACIC表2百分比在相同PFN组内计最佳，非全方法准确率。存在资源图14，不能误写成完全没有资源评测。

核查定位：p007, implementation, p008, footnote5, p009, Table2 and §6–7, p021, D.2, p023, F.1–F.2, p027, F.4；implementation_and_reference_scope_qualified

本地补充/限定：["原PDF确认BvM中心不一致与两张数值表；新增乘积速率不足以推出影响函数L2收敛的限定性代数例，明确与可能隐含的各自一致性条件区分。", "没有证明真实PFN一定不一致，也未把弱收敛草图缺少TV步骤直接当成所引用前作错误。"]

核查局限：["局部反例是有限分布的解析计算，未运行PFN、模拟数据或训练。", "未核读Yiu等前作，也未全面审计MP耦合及方差证明。", "图14精确时间/显存未取数；未验证真实数据的因果识别条件。", "Pro读全部文本，本地观察四页PDF；L2仍为暂评。"]


## pro053 · Many Experiments, Few Repetitions, Unpaired Data, and Sparse Effects: Is Causal Inference Possible?

论文 OR_gqa99Ev4C4；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_gqa99Ev4C4_0cf51b599868", "source_url": "https://api2.openreview.net/pdf?id=gqa99Ev4C4\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_gqa99Ev4C4_0cf51b599868：物理页1—37连续，已读全部提供文本，包括正文§1—6、参考文献、附录A—L及证明；未发现缺失页标。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—15只有提取出的图题、标签等文字，不能读取曲线数值或误差条。", "双栏顺序、公式上下标、矩阵排版及部分不等号失真；表1—2主要文字可读，但未核对原始版面。", "未提供前作全文、可执行代码或原始实验数据；未搜索、复现或比较其他版本。"]}

问题：存在隐藏混杂、只能分别观察(I,Y)和(Ĩ,X̃)时，能否通过增加实验环境数量，而非增加每环境重复次数，一致估计线性因果效应β*？

方法：令B为工具—协变量样本矩、a为工具—结果样本矩。将X侧分成K折，以CXX=m/[K(K−1)]∑h≠k BhᵀBk替代mBᵀB，保留CXY=mBᵀa，最小化加权矩残差。稀疏版加入ℓ1惩罚并重拟合；解析版通过扣除自内积计算无限次分折平均。

作者主张：SPLITUP在环境数增加、每环境观测量保持常数时消除传统双样本IV的渐近偏差。

论文证据：引理4.3给出标量TS-IV的非真值概率极限；定理4.5证明交叉矩估计一致，附录L.8展开并控制折间及跨样本误差项。

模型推断：中心增量是明确特定渐近机制的失败原因并恢复一致性，不是首次使用IV或样本拆分；也不意味着最终系数估计有限样本无偏。

定位：['TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页6—7，引理4.3、定理4.5；物理页33—36，附录L.7—L.8。']

作者主张：在稀疏因果效应下给出识别、估计与选择后推断保证，允许工具矩阵秩小于d。

论文证据：定理3.2/3.4给出受限零空间识别条件；4.2/4.6给出ℓ1估计误差率和阈值支持恢复；E.1给出固定m下重拟合的渐近区间。

模型推断：是既有稀疏IV/GMM理论在当前矩条件下的扩展；本文明确固定d，不能视为d随样本增长的统一保证。

定位：['TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页4—7，定理3.2—4.6；物理页17，定理E.1。']

key_results：[{"setting": "标量d=1、β非零；m→∞、ñ/m→r̃，Q>0且tr(ΣIX)→b>0。", "baseline": "TS-IV", "metric_or_guarantee": "概率极限与一致性", "reported_values_and_units": "作者证明TS-IV→βQ/(Q+b/r̃)≠β*；满足假设4时SPLITUP→β*。", "information_and_compute": "需要独立双样本和相应矩界；属于理论结果，并非本地实测。", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页6—7，引理4.3、定理4.5。\n"}, {"setting": "固定d、s*=||β*||0；有限m使用N=n+ñ，多工具情形使用m作为渐近尺度。", "baseline": "不利用稀疏性的矩估计", "metric_or_guarantee": "ℓ2估计误差与支持恢复", "reported_values_and_units": "UP-GMM(ℓ1)：Op(√(s*/N))；SPLITUP(ℓ1)：Op(√(s*/m))。惩罚分别同阶于N^(-1/2)、m^(-1/2)；beta-min下阈值选集恢复真支持。", "information_and_compute": "须满足假设3或5；这些是作者定理，不是对任意调参或非零选集的保证。", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页5—7，定理4.2、4.6。\n"}, {"setting": "合成分类工具：Setting 2为d=2；Setting 3为d=100、低秩k=60、s*=10；两侧样本均衡，n/m取4、8、16、32。", "baseline": "TS-IV、UP-GMM；连续工具补充实验另含TS-2SLS", "metric_or_guarantee": "MAE(ℓ1)；正文报告SPLITUP误差随样本增加下降，基线保留偏差。", "reported_values_and_units": null, "information_and_compute": "主要实验50次独立运行；分折实现K=2、H=10，随后主要展示解析版。曲线精确误差不可读，硬件与耗时未报告。", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页7—8，§5.1；物理页19、23，附录G、H.3。\n"}, {"setting": "Causal Chambers Light Tunnel；每环境r=8，原始配对数据人为删除X或Y形成非配对样本。", "baseline": "TS-IV、UP-GMM；评估目标由完整配对数据调整已记录的U获得。", "metric_or_guarantee": "系数误差及模型诊断", "reported_values_and_units": "具体MAE不可读。作者报告加入X²后ΔR²=0.000172163，加入I后X回归系数变化3%。", "information_and_compute": "50次重采样；M:=0.0625X是控制器设置，不是已知的X→Y总效应数值。上述诊断不能单独证明工具有效。", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页8—9，§5.2；物理页25—26，H.4。\n"}]

prior_work_candidates：[{"citation_as_printed": "Joshua D Angrist and Alan B Krueger. Split-sample instrumental variables estimates of the return to schooling. Journal of Business & Economic Statistics, 13(2):225–235, 1995.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "用样本拆分处理IV估计偏差。", "claimed_difference": "本篇将自身修正定位为双样本分母测量误差去偏，并区别于前作处理内生性偏差后出现的衰减。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页6，§4.2；物理页9，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Atsushi Inoue and Gary Solon. Two-sample instrumental variables estimators. The Review of Economics and Statistics, 92(3):557–561, 2010.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "组合独立样本中的工具—暴露与工具—结果信息。", "claimed_difference": "本篇重点分析m与样本量同阶增长时传统插件估计的不一致，并提出修正。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页10，参考文献；物理页12，附录A。\n", "prior_actually_read": false}, {"citation_as_printed": "Shimeng Huang, Niklas Pfister, and Jack Bowden. Sparse causal effect estimation using two-sample summary statistics in the presence of unmeasured confounding. arXiv preprint arXiv:2410.12300, 2024.", "identifier_if_present": "arXiv:2410.12300", "relation_candidate": "理论扩展", "shared_component": "稀疏双样本IV问题；不据引用认定算法直接继承。", "claimed_difference": "本篇称前作要求Var(I)可逆且未给一致性或渐近正态保证；本作补充稀疏估计及多工具一致性理论。", "basis": "target_paper_only", "target_locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页10，参考文献；物理页12，附录A。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献包含明确的失败机制及修正后的一致性保证，超出单纯场景性能改进；但不足以认定路线级框架或历史首创。", "central_increment": "前作已有双样本IV、样本拆分和稀疏估计（本篇转述）；本作在固定d、工具数与样本量同阶增长时新增交叉矩去偏保证，核心证据为引理4.3及定理4.5—4.6。", "soundness_observation": "主要交叉矩误差消失的证明结构可追踪，未完成逐式核证。高维SPLITUP的渐近正态性未见对应定理；附录E/K的推断保证针对固定m。", "significance_observation": "为多实验、少重复的数据设计提供有意义的统计依据；应用验证仍以合成数据及受控光学装置为主，未展示生物数据实证。", "main_open_question": "与既有split-sample IV相比，相同双样本、多工具条件下的分母修正和一致性保证究竟新增了哪些内容？"}

limitations：[{"text": "依赖线性结构效应、矩不变与外生性；估计理论另要求两样本独立。识别模型允许样本相关，不等于估计保证也覆盖相关样本；高维不确定性量化仍列为未来工作。", "basis": "author_report", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页3、5、9，§2.1、4、6。\n"}, {"text": "L.9由score=Op(m^(-1/2))及同阶λ推出控制事件概率趋1，论证需补强；定理按c/2阈值选集，算法却按非零系数重拟合，实际支持恢复保证不能直接沿用。此为待核证明与实现衔接问题，不据此断言全部结论错误。", "basis": "model_inference", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页7、20、22、37，定理4.6、算法3/5、L.9。\n"}, {"text": "图11的一致性比较剔除了0.1%最大差异点；d=1000实验手调惩罚且仅5次运行。主比较中UP-GMM估计最优权重、SPLITUP使用单位权重，有限样本差距并非完全隔离去偏机制。", "basis": "model_inference", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页9、26—28，§5.2、图11、I.4、图14。\n"}, {"text": "分类工具的分层解析构造仅保留X侧重复数至少为2的环境；不能据此承诺每环境只有一次X测量时仍有同样保证。", "basis": "model_inference", "locator": "TEXT_OR_gqa99Ev4C4_0cf51b599868，物理页18，附录F。\n"}]

minimal_check：{"question": "核心分母修正是否已被Angrist–Krueger（1995）的结果覆盖？", "control": "核读该前作，将两法统一为独立双样本、固定d、m与n同阶的矩阵表达。", "observable_outcome": "对照是否存在相同折间乘积或自内积扣除，以及是否已有同条件一致性保证。", "resources": "需要该前作全文及逐式假设对照；本轮未提供，不需先运行大规模实验。", "failure_or_stop_condition": "若公式和保证均被覆盖，下调C01新意判断；若假设不能对齐，不作覆盖结论。"}

missing_fields：["图中逐方法MAE、误差条数值及置信区间水平。", "硬件、运行时间、内存及总计算预算。", "Bootstrap重复数B、显著性水平α和惩罚网格的具体配置。", "光学装置调整后目标系数的数值。", "前作全文、部分前作唯一标识符及附件最终出版版本身份。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

多工具、少重复下分母测量误差和交叉矩修正的机制清楚，值得继续读；稀疏部分需另核调参和选择后推断，历史增量需与既有split-sample IV逐式比较。

身份及识别前提：37页官方当前附件与全文输入返回绑定一致。线性结构效应、跨样本Cov(I,X)不变及E[ε|I]=0是核心，不能把少重复和不配对视为无需结构假设。识别部分允许两样本相关，估计§4另加两样本独立。d固定、m增长才是这里的多工具渐近，不能当d随n增长的一般稀疏理论。

核查定位：text_delivery_manifest.json, structured/pro053.json, p003, Assumption1, p004, §3 introductory scope, p005, §4；source_and_identification_conditions_confirmed

中心交叉矩修正及一致性：原PDF第6页确认CXX用独立折之间BhᵀBk的平均替代自身平方，CXY仍用两独立样本的交叉矩。标量TS-IV极限为β*Q/(Q+b/rtilde)。第35–36页关键证明依赖协方差算子范数O(1/m)、固定d/K和跨样本/折独立，使折间噪声内积均值0、方差O(1/m)，继而CXX→Q、CXY→Qβ*。这是一致性论证，不是最终系数有限样本无偏或无需强度条件。

核查定位：PDF physical page 6, Lemma4.3 and Assumption4, p007, Theorem4.5, p035–p036, L.8；main_failure_mechanism_and_proof_step_checked

解析形式与最少重复数：原PDF第18页给出带1/m归一化的矩阵形式：总交叉积减各样本自内积，Algorithm6保留完整d×d矩阵。分类工具的分层实现明确只保留X侧re>=2环境；不能承诺每环境恰一次X观测亦能直接使用该实现。固定平均重复数与逐环境最低重复数是不同条件。

核查定位：PDF physical page 18, F closed form and categorical restriction, p023, Algorithm6；analytic_implementation_and_repeat_scope_confirmed

稀疏识别、估计与推断分开：稀疏识别用ker(A)∩Σ2s={0}，L1估计另需RE锥条件；支持恢复要求beta-min并按c/2阈值选集。Algorithm5却用非零系数集重拟合，不能直接沿用阈值选集保证。第17页E.1依赖固定m的Assumption3/Theorem4.2，高维工具下的不确定性仍在第9页列作未来工作。

核查定位：p004, Theorem3.2, p005–p007, Assumptions3/5 and Theorems4.2/4.6, p017, E.1, p022, Algorithm5 line22, p009, §6；identification_estimation_and_inference_scope_qualified

稀疏速率证明的概率步骤：原PDF第37页由score=Op(m^-1/2)、λm同阶便断言score<=λm/2概率趋1，该推断单靠Op阶不充分：若score=|Z|/√m、λ=c/√m，事件概率一般固定而不趋1。应补更强尾界/调参条件或采用另一概率论证；本地不据此判定最终Op速率或阈值支持恢复定理必错。

核查定位：PDF physical page 37, L.9 final paragraph, p007, λm specification；specific_proof_inference_gap_confirmed

应用与对照范围：主要实验为合成分类/连续工具及受控光学装置。光学数据先配对，再人工删除X或Y；参考目标使用实验者已记录U调整，M=.0625X是控制器设置而非已知总效应系数。UP-GMM与SPLITUP权重估计不同，作者明确其有限样本差距部分源于权重不稳定。未从不可见误差曲线补写MAE数值。

核查定位：p007–p008, §5.1, p008–p009, §5.2, p009:L0021-L0032；experimental_evidence_boundary_confirmed

本地补充/限定：["核对主一致性证明中的独立折方差控制及解析矩阵实现，保留该机制的正面理论价值。", "把L.9问题限定为Op阶到概率趋1的推导缺口，未把它升级成所有估计保证失败。"]

核查局限：["未核读Angrist–Krueger等前作或运行作者代码，L2暂评不等于历史首创认证。", "未完成全部稀疏证明、原始光学数据及工具有效性的独立审计。", "没有补写图中精确MAE、置信水平、运行时间或硬件成本。", "Pro读全部文本，本地观察三页PDF。"]


## pro054 · Relational Structural Causal Models

论文 OR_WTBaZHtIra；暂定 L3；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_WTBaZHtIra_420c5d593505", "source_url": "https://api2.openreview.net/pdf?id=WTBaZHtIra\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "03d3314451c7bc7244c665d6e992b2f3f43b5caecd29126457374ba4eaf7b1b9", "source_pdf_sha256": "420c5d5935052321d03d4d2da75336e043c36326746632855ace258cad0e6601"}], "read_ranges": ["TEXT_OR_WTBaZHtIra_420c5d593505：物理页1–53全部文本；正文1–9、致谢与参考文献10–18、目录及附录A–F 19–53。页标连续，未见缺页；不认定为最终出版版。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图3、4及附录实验曲线的精确数值不可读，不能据坐标文字推测。", "双栏、公式和表格存在错位及符号损失；表E.4.1的c3行与正文不一致，§E.8.2与图E.8.2图注的聚合器条件冲突，未自行修正。"]}

问题：在同一关系schema下，如何用若干对象组合的观测或干预数据，识别对象数量、关系拓扑不同的目标组合上的观测、干预及反事实查询？

方法：按属性类型共享结构函数与外生噪声分布，用一阶关系约束选择多重集父项，可附聚合器；在具体骨架上实例化为SCM。给定关系因果图与源数据，RNCM共享网络拟合源分布，并对目标查询分别最小化、最大化；极值一致时判为可识别。

作者主张：建立RSCM，统一可变对象组合中的因果语义，并刻画学习的不可能性。

论文证据：Def.3.1给出共享机制模板；Thm.3.3–3.4构造源观测相同但目标观测或干预不同的模型。

模型推断：中心增量是跨骨架因果建模与识别问题，而非参数共享本身。

定位：['TEXT_OR_WTBaZHtIra_420c5d593505：p3–5，Def.3.1、Thm.3.3–3.4；p34–35，§D.1']

作者主张：通过关系因果图给出观测迁移及因果识别判据，允许隐混杂。

论文证据：Thm.4.3转移无混杂条件机制；Cor.D.4恢复Markovian目标联合分布；Props.4.4–4.5给出同骨架充分条件与实例内查询必要条件。

模型推断：提供实质性识别边界，但并非所有跨骨架查询的完整符号算法。

定位：['TEXT_OR_WTBaZHtIra_420c5d593505：p5–7，§4；p36–40，§D.2']

作者主张：RNCM具有反事实表达能力，神经识别方法sound且complete。

论文证据：Thm.5.2给出表达性；Cor.D.7把精确约束下查询极值一致与数据依赖的可识别性联系起来。

模型推断：是NCM的关系化扩展；不等于有限样本梯度训练能可靠认证可识别性。

定位：['TEXT_OR_WTBaZHtIra_420c5d593505：p7–8，§5；p40–43，§D.3–D.4。\n \n']

key_results：[{"setting": "§6.1：分别用ρA、ρB、ρC或ρA+ρB训练，在ρC估计行人被干预为横穿时车辆刹车概率。", "baseline": "NCM-X、NCM-J、REL-MLP、REL-MLP+DEG；另有直接用目标数据和ground图训练的NCM*。", "metric_or_guarantee": "相对真值的MSE，图中展示log(MSE)。", "reported_values_and_units": "作者称可识别设置常有约100倍误差优势；ρA→c1为不可识别失败例。精确分组数值不可见。", "information_and_compute": "每源10⁴观测样本、10个种子；共享模块2层×128，200 epochs，batch=1000，学习率10⁻³；通用配置为单H100。", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p8–9，§6.1；p43–44，§E.1–E.3。\n"}, {"setting": "§6.2：2车源骨架迁移到3车目标；bow与IV关系图，majority聚合。", "baseline": "理论可识别的不同车查询与不可识别的同车查询。", "metric_or_guarantee": "最大、最小查询估计之差。", "reported_values_and_units": "作者报告不同车查询差距趋近0，同车查询保持较大差距；10个种子，精确差距不可读。", "information_and_compute": "值得注意：附录证明不同车查询无有向因果路径，干预可被删除，不是非零跨车效应案例。", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p9，§6.2；p47–48，Props.E.3–E.4。\n"}, {"setting": "§E.5：跨骨架front-door估计；正文将查询写为P(c1.B=1|do(c1.X=1))。", "baseline": "生成模型真值；未报告额外比较模型。", "metric_or_guarantee": "概率估计MSE，无量纲。", "reported_values_and_units": "5次试验：0.00082 ± 0.0018；±的统计含义未说明。", "information_and_compute": "采用前门调整的可识别查询；独立耗时及采样预算未报告。", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p46，§E.5。\n"}, {"setting": "§E.7：源10–50个对象，目标同规模或1.5倍、最多75个；改变拓扑而保持类似局部邻域。", "baseline": null, "metric_or_guarantee": "平均干预查询的MSE及训练时间；作者称误差稳定、时间温和增长。", "reported_values_and_units": null, "information_and_compute": "每源5000样本；正文称每源3次试验，图注称10次，无法消解。数值与秒数仅见不可读曲线。", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p48–50，§E.7、Fig.E.7.2。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Salimi, B., Parikh, H., Kayali, M., Getoor, L., Roy, S., and Suciu, D. Causal relational learning. SIGMOD ’20, pp. 241–256, 2020.", "identifier_if_present": "10.1145/3318464.3389759", "relation_candidate": "理论扩展", "shared_component": "关系域因果规则及后门识别。", "claimed_difference": "本篇称前作限同骨架、无隐混杂，未给机制级反事实语义。", "basis": "target_paper_only", "target_locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p16参考文献；p24，§A.5。\n", "prior_actually_read": false}, {"citation_as_printed": "Xia, K. M., Pan, Y., and Bareinboim, E. Neural causal models for counterfactual identification and estimation. The Eleventh International Conference on Learning Representations, 2023.", "identifier_if_present": "OpenReview:vouQcZS8KfW", "relation_candidate": "方法继承", "shared_component": "NCM表达性证明、查询极值优化、MLE架构及代码基础。", "claimed_difference": "加入类型级共享、排列不变关系父输入和跨骨架目标。", "basis": "target_paper_only", "target_locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p17参考文献；p40–44，§D.3、§E.1–E.3", "prior_actually_read": false}, {"citation_as_printed": "Heckerman, D., Meek, C., and Koller, D. Probabilistic models for relational data. Technical Report MSR-TR-2004-30, March 2004.", "identifier_if_present": "MSR-TR-2004-30", "relation_candidate": "组件复用", "shared_component": "DAPER框架的一阶关系约束；Def.B.1明确称修改自其Def.6。", "claimed_difference": "从关系概率依赖扩展到结构机制、干预和反事实。", "basis": "target_paper_only", "target_locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p13参考文献；p22，§A.2；p25，Def.B.1", "prior_actually_read": false}]

assessment：{"ai_verdict": "L3", "confidence": "medium", "reason": "跨骨架查询的统一建模与识别接口符合框架级候选，而非单点性能改良；不等于已证明历史首创。", "central_increment": "前作已做关系域后门推断和固定图NCM识别（本篇转述）；本作在共享机制、已知关系结构下新增跨骨架识别语义、判据与神经实现，支持来自§3–5；仍需排除前作覆盖及图编码遗漏。", "soundness_observation": "未逐条核证证明。Def.4.1的文字规则疑似遗漏同一外生变量一端作为非关系父、另一端作为关系父的混杂边；这可能影响Lemma D.3的一般性，但不直接否定ρ-Markovian神经结果。", "significance_observation": "具有基础理论价值；不是从像素自动学习关系与因果图的世界模型，实证仍限合成结构化数据。", "main_open_question": "Def.4.1及Lemma D.3是否完整覆盖非关系—关系外生父的混合共享？"}

limitations：[{"text": "识别要求schema、骨架和关系因果图已知；连续变量的神经保证留待未来，高维直方图也可能昂贵。", "basis": "author_report", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p52–53，FAQ Q6、Q9–Q10"}, {"text": "扁平NCM丢失关系信息，REL-MLP以条件概率代替干预；缺少同结构、正确因果调整的关系基线，约100倍优势不能单独归因于RNCM架构。", "basis": "model_inference", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p45–46，§E.4"}, {"text": "§6.2的可识别正例是无因果路径查询；扩展实验最多75变量且局部邻域类似，尚不足以证明复杂跨对象效应或大邻域外推能力。", "basis": "model_inference", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p48–50，§E.6–E.7"}, {"text": "错设实验显示缺失特定因果边、用majority压缩真实count机制会损害估计；并无普遍的错设稳健性保证。", "basis": "author_report", "locator": "TEXT_OR_WTBaZHtIra_420c5d593505：p50–51，§E.8正文"}]

minimal_check：{"question": "检查混合外生父共享是否在关系图实例化中丢失混杂边。", "control": "取二值噪声o.U，令o.A←o.U、t.B通过关系R(o,t)访问同一o.U；比较Def.4.1/B.6所得图与直接按ground SCM共享噪声构造的图。", "observable_outcome": "两者都应包含o.A↔t.B；若模板规则缺边，Lemma D.3及依赖它的一般识别结论需补充规则。", "resources": "纸笔或小规模二值枚举；无需训练或作者代码。", "failure_or_stop_condition": "若定义已有明确自身份关系约定覆盖该情况，则撤销遗漏疑点；否则保留反例，不外推否定受限神经模型。"}

missing_fields：["所有图像及主要误差、极值差距、运行时间曲线的精确值。", "前门实验±的含义；扩展实验3次与10次试验数冲突。", "总GPU小时、查询积分或采样预算、完整优化判定阈值。", "前作全文、独立证明核验及实验复现；本轮均未进行。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

跨骨架因果语义与识别接口有框架级潜力，值得带图编码完整性问题继续；先澄清混合噪声规则及受限神经保证，再比较前作覆盖和实用扩展。

身份与框架中心增量：53页官方当前附件及全文返回绑定一致。共享属性类型机制和外生分布，按关系约束形成多重集父项，在具体骨架上实例化SCM；问题是同schema不同对象组合之间的观测、干预及反事实识别。它是已知schema/骨架/因果结构下的框架候选，非从像素自动学图的世界模型；L3仅保留为Pro暂定层级。

核查定位：text_delivery_manifest.json, structured/pro054.json, p003–p007, Definitions3.1–4.2 and Algorithm1；source_and_framework_scope_confirmed

通用图编码遗漏混合共享噪声：原PDF第5页Def4.1和第37页D.3跨实例证明只处理两端都为关系外生父的共享。构造o.A=o.U、t.B经R(o,t)读取同一o.U并异或独立t.V：ground SCM需要o.A↔t.B，但o.A的关系外生父集为空，所印模板两条规则都不会产生该边。所查B.1/B.4/B.6未给把非关系父自动改写为identity关系父的规则。另存严格正的2×2联合表说明该缺口不依赖退化分布。需补混合规则/归一化，不直接否定排除此情况的ρ-Markovian神经结果。

核查定位：PDF physical page 5, Definition4.1, p025–p026, DefinitionsB.1/B.4/B.6–B.7, PDF physical page 37, LemmaD.3 cross-instance implication, local_check/mixed_exogenous_parent_argument.json；literal_mixed_parent_graph_gap_confirmed

跨骨架不可能性和可迁移机制条件：Theorem3.3字面未写目标非同构于所有源；若目标就是源或仅重命名，观察分布显然已知，正文第6页的cross-skeleton定义及第34页构造表明应保留非同构限定。Theorem4.3的正面迁移还需源/目标相应变量无混杂、父项域支持包含；共享机制本身不足以任意外推到新邻域。

核查定位：p004, Theorem3.3, p006, cross-skeleton definition and Theorem4.3, p034, Theorem3.3 proof idea；negative_and_positive_scope_qualified

神经表达性与识别算法的适用条件：§5明确有限离散属性、关系多重集统一有界和ρ-Markovian，允许实例内隐混杂、排除实例间隐混杂。第42–43页sound/complete依赖精确源分布约束和全局极值相等；实际第44页使用MLE及衰减惩罚、200epoch优化，不能将有限训练的极值接近直接当形式识别证书。

核查定位：p007, Assumptions and Algorithm1, p042, Theorem5.2 and CorollaryD.7, p043–p044, implementation and training；neural_theory_vs_optimization_boundary_confirmed

跨对象识别实验的真正对象：原PDF第48页图E.6.1和证明确认c2.X到c3.Y没有有向路径，正例把do删除后变成目标边际查询；不能当非零跨车效应的识别展示。扩大骨架实验保持类似局部邻域，最多75个对象/属性变量，非任意新邻域规模外推。第48页写每源3次试验，第50页图注写10次，保留未消解差异。

核查定位：PDF physical page 48, FigureE.6.1 and E.7 setup, p050, FigureE.7.2 caption；empirical_identification_and_scaling_scope_confirmed

本地补充/限定：["混合外生父共享疑点经所印定义和D.3证明核对后，给出带独立附加噪声的正概率解析实例；明确其不属于ρ-Markovian神经模型范围。", "框架级价值与一般图编码缺口并列保留；未认证历史首创，也未将神经优化收敛当识别完备性证明。"]

核查局限：["未核读关系因果学习和NCM前作，L3是候选判断而非历史首创认证。", "没有训练RNCM、执行识别算法或进行数据实验；新增例为纸笔图规则及概率核算。", "未完整审计全部符号判据、神经表示证明和正文约100倍误差说法。", "Pro为全文文本阅读，本地观察三页PDF；图中误差和耗时不补造精确值。"]


## pro055 · Set-Preserving Calibration from Conformal P-Values to E-Values

论文 OR_jNv4sl4YZH；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e", "source_url": "https://api2.openreview.net/pdf?id=jNv4sl4YZH\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "f4076e7cd57e5e53e2191724faffa262d3d527ed72da7505c708295475fe8721"}], "read_ranges": ["TEXT_OR_jNv4sl4YZH_f4076e7cd57e：物理页1–26连续全文；正文页1–9、参考文献页9–11、附录A–G页12–26。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未见物理页标缺失，但仅提供文本，未看过原PDF图像；图1–4不可见，尤其图2主要实验箱线图无法提取数值。", "双栏文字与部分公式存在串行混排；表1–11主要数值可辨。当前附件不自动认定为最终出版版。材料限制见清单。\n"]}

问题：如何把conformal p-values转成便于合并的e-values，同时不膨胀原来的预测集合？

方法：输入p、校准样本量n和固定α，构造F(p)=[1+exp(C(α−s))]/[α(1+exp(C(p−s)))]；选C使离散秩网格上的平均F恰为1。ECCP逐折转换后平均，以独立U/α为阈值；WECA在分离的调参数据上优化权重，再用推断校准集生成最终e-values。

作者主张：刻画经典校准器的保集限制，并构造兼具保集、exactness、严格正性及光滑可逆性的P2E。

论文证据：命题2.3给出经典左连续校准器中的AoN唯一性；命题2.4–2.5和定理2.6给出存在性、向AoN收敛及逐点支配，附录B提供证明。

模型推断：中心增量是利用conformal p值的离散分布设计校准，而非发明一般p-to-e转换；不能把该映射直接推广为适用于任意p-variable的通用校准器。

定位：['TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页4–5 §2、页15–19附录B']

作者主张：用P2E改善CCP与模型聚合，在1−α覆盖保证下提高集合效率。

论文证据：命题4.1–4.2给出覆盖结论；表1–3和6–11报告回归实验、校准器替换及参数敏感性。

模型推断：应用层增量是把新校准接入已有合并工具；均值合并与随机化本身来自前作，不能全部归为本作创新。

定位：['TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页6命题4.1–4.2、页7–8 §5、页21–25附录D–F']

key_results：[{"setting": "定理2.6的离散均匀conformal p值设置", "baseline": "FAoN(p)=1{p≤α}/α", "metric_or_guarantee": "exact e-variable、单集等价与聚合集包含关系", "reported_values_and_units": "E[F(Pn)]=1；{Pn>α}={F(Pn)<1/α}；F≥FAoN，故相同权重与阈值下P2E聚合集不大于AoN聚合集。无数值单位。", "information_and_compute": "利用n、α和p值；C满足一维离散平均方程，数值求解成本未报告。", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页5定理2.6及式(10)、页18–19 §B.3。\n"}, {"setting": "Boston，RF，K=15，100随机种子；1−α组，沿§5的α=0.1设置", "baseline": "ECCP(FAoN)", "metric_or_guarantee": "平均预测集合长度、经验覆盖", "reported_values_and_units": "ECCP：长度10.126±0.616，覆盖0.899±0.032；AoN：12.662±1.153、0.922±0.027。均为均值±种子间标准差；长度具体单位未注明，覆盖为比例。", "information_and_compute": "15折RF；训练硬件、时间及候选响应网格分辨率未报告。", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页21表6。\n"}, {"setting": "OpenML 361244，α=0.05，7个回归器，20随机种子", "baseline": "COLA-S", "metric_or_guarantee": "平均集合长度、经验覆盖", "reported_values_and_units": "WECA：5.09±2.06、0.96±0.02；UR-WECA：4.93±1.86、0.96±0.02；COLA-S：5.23±1.48、0.97±0.02。均值±标准差；长度单位未注明。", "information_and_compute": "训练/校准/测试为50%/35%/15%；各模型取公共校准池60%–100%的随机子集；另行调权与推断划分的比例、搜索预算未报告。", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页8表2、页23–25附录F。\n"}]

prior_work_candidates：[{"citation_as_printed": "Vovk, V. and Wang, R. E-values: Calibration, combination and applications. The Annals of Statistics, 49(3):1736–1754, 2021.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "p-to-e校准、AoN、e-value合并", "claimed_difference": "本作限定conformal离散p分布，加入n依赖以同时保集、exact且严格正。", "basis": "target_paper_only", "target_locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页3 §1.3/§2.1、页10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Bickel, D. R. A small-sample bayesian information criterion that does not overstate the evidence, with an application to calibrating p-values from likelihood-ratio tests. Statistical Papers, 66(3):1–17, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "样本量依赖的p值映射", "claimed_difference": "作者称其可能最接近P2E，但前作映射至Bayes factors，并非conformal保集问题；未确认方法继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页5 §3、页9参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Gasparin, M. and Ramdas, A. Improving the statistical efficiency of cross-conformal prediction. Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, pp. 18848–18867, 2025.", "identifier_if_present": "PMLR 267:18848–18867", "relation_candidate": "方法继承、比较基线", "shared_component": "CCP及交换性聚合、实验设计", "claimed_difference": "本篇转述前作变体保证1−2α；本作转为e-values后构造1−α有效方法。", "basis": "target_paper_only", "target_locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页6 §4、页9参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献有明确的受限分布校准机制与配套保证，不只是替换经验函数；已有e-CP和合并理论又使其不足以直接判为路线级首创。", "central_increment": "前作已有p→e与AoN保集工具（本篇转述）；本作在无并列、非整数秩阈值条件下新增正、光滑、exact的保集映射，证据是定理2.6及聚合实验；尚待排除收益主要来自补足AoN的有限样本保守性。", "soundness_observation": "核心存在性构造可理解，未做形式化验证。F.1将权重与推断e值的期望直接因式分解；仅数据不相交并不自动给出独立性，在交换性/共享训练模型设置下需补充条件交换性或条件期望论证，不能据此直接断言方法无效。\n", "significance_observation": "价值在保留单个SCP决策的同时接入e-value工具；对强基线COLA-S的数值优势较小，不能推广为所有数据集严格更优。", "main_open_question": "与同一离散p分布下已经归一化为exact的AoN相比，P2E是否仍有稳定、同覆盖的集合效率优势？"}

limitations：[{"text": "严格exactness依赖无并列；整数α(n+1)被排除，作者建议增删校准点。此时改变了n，不能宣称仍保持原校准配置的集合。", "basis": "model_inference", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页2 §1.1、页16 Remark B.4、页22 §E.1"}, {"text": "长度在有限响应网格上近似；部分经典校准器的真实集合可能无界，表中有限长度不是其完整集合长度。", "basis": "author_report", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页8脚注5、页24附录F。\n"}, {"text": "同理论保证不等于同实测覆盖，部分缩短来自减少过覆盖。表2的361237上WECA长度1.65而COLA-S为1.64；未报告配对显著性检验。", "basis": "model_inference", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页8表2、页21表6。\n"}, {"text": "按α=0.1实验上下文，表8 Parkinsons/RF的ECCP(2α)覆盖0.772±0.010、ECCP覆盖0.890±0.009，低于相应0.80/0.90目标；交换性、并列、网格或实现原因未解释，不能把实验整体描述为已验证保证。", "basis": "model_inference", "locator": "TEXT_OR_jNv4sl4YZH_f4076e7cd57e：页22表8。\n"}]

minimal_check：{"question": "平滑P2E的效率收益能否超出对AoN进行离散exact归一化？", "control": "固定Boston/RF的折划分、逐折p值、U和响应网格；比较P2E与A*n(p)=(n+1)/floor(α(n+1))·1{p≤α}，保留原AoN作参照。该对照由本篇离散均匀条件推导，并非声称已有前作。", "observable_outcome": "逐种子比较长度、覆盖及平均e值，检查P2E优势是否仍存在。", "resources": "需原逐折p值或可重建的实验记录，当前未提供；可用普通CPU计算，实际耗时未知。", "failure_or_stop_condition": "若exact AoN消除主要长度差距，或剩余差距仅对应更低覆盖，则不能将主要效率收益归因于平滑、严格正性。"}

missing_fields：["原PDF图像、图2及图4的可核读数值", "模型超参数、主实验s取值、C求解算法与容差", "WECA调参/推断细分比例、权重搜索预算、网格具体边界与分辨率", "硬件、运行时间、内存和独立复现实测", "前作全文；部分前作未列独立标识；当前附件的最终版本身份"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

保留单集并进入e值聚合的接口值得读；继续阅读应优先比较离散exact对照、校验实际覆盖及WECA的条件有效性实现。

身份及离散分布条件：26页官方当前附件与输入返回绑定一致。P2E依赖n和固定α，利用交换性且无并列时的离散均匀秩网格；不属于适用于任意p-variable的通用校准器。Theorem2.6要求α(n+1)>1且非整数、α<s<ceil(α(n+1))/(n+1)，并令网格均值为1。整数情形通过增删校准点处理会改变n，不能继续声称保留原配置集合。

核查定位：text_delivery_manifest.json, structured/pro055.json, p002, Eq3 and no-ties assumption, PDF physical page 5, Theorem2.6, PDF physical page 22, E.1；source_and_exactness_conditions_confirmed

保集与聚合保证的对象：严格递减且F(α)=1/α使单个非随机SCP集合相同；与未归一化AoN的逐点支配则推出相同权重/阈值下聚合集包含关系。这不说明随机化ECCP与原SCP逐样本相同，也不适用于不同选择权重的无条件大小比较。普通ECCP允许折间依赖，Exch变体另需折间交换性，U需独立。

核查定位：p004, Definition2.2 and Eq7, PDF physical page 5, Eq9–10, p006, Eq15–17 and Proposition4.1；central_set_and_aggregation_scope_confirmed

exact归一化与光滑性增量分开：在同一离散网格，AoN期望为floor(α(n+1))/(α(n+1))。乘以其倒数得到A*n=(n+1)/floor(α(n+1))·1{p<=α}，同样exact并保留单集，但仍有零值、不光滑。它是由当前公式推出的有意义对照，未在本地运行或声称已有前作；现有对未归一化AoN的优势尚不能隔离光滑严格正性与消除保守性的各自贡献。

核查定位：p002, rank grid, p004, exactness footnote3, PDF physical page 5, domination result；baseline_normalization_scope_derived

WECA权重有效性的条件论证：F.1先对公共索引池作调参/推断全局划分，再与各模型子集相交，第25页以独立性直接分解E[ωE]。单凭数据不相交或每模型边际交换性不够，但在共同交换样本、与数据取值无关的划分、固定训练/调参信息后剩余校准与测试仍交换的标准设置，可用E[Ek|训练、调参、划分]<=1证明加权e值有效，无需无条件独立。应把这些条件写明；未核代码，不能据该草图缺口宣称方法无效。

核查定位：p006, Proposition4.2, p024–p025, F.1；conditional_validity_repair_distinguished_from_invalidity

长度、覆盖及有限网格：原表6确认Boston/RF/K15：ECCP长度10.126±.616、覆盖.899±.032；AoN12.662±1.153、.922±.027，部分长度收益伴随减少过覆盖。原表8Parkinsons/RF：ECCP(2α)覆盖.772±.010，ECCP .890±.009；按α=.1均低于所对应标称值，原因未说明，不能把实验整体写成已验证覆盖保证。作者明确长度只在有限响应网格计算，替代校准器真实集合可能无界，因此表中有限长度不是完整无界集合长度。

核查定位：PDF physical page 21, Table6, PDF physical page 22, Table8, p007, α=.1 experiment setting, p008, footnote5, p024, evaluation grid；decisive_empirical_numbers_and_measurement_scope_confirmed

强聚合基线的实际差距：表2 α=.05、20种子，361244的WECA/UR-WECA/COLA-S长度5.09/4.93/5.23，覆盖.96/.96/.97；361237则1.65/1.64/1.64。不能概括为每数据集严格优于COLA-S；未给配对显著性，也未报告完整调权搜索和求C数值预算。

核查定位：p008, Table2, p024–p025, weight tuning；strong_baseline_comparison_qualified

本地补充/限定：["补充WECA可通过条件交换性/条件e值期望修复证明的标准路径；不将无条件独立性因式分解的不足等同为算法失效。", "将exact AoN列为解析对照问题，保留P2E严格正性和光滑性的独立形式属性，不把尚未实验比较当成无增量证据。"]

核查局限：["未运行校准器求根、模型训练、数据网格或权重优化；归一化对照仅解析推导。", "未核读e-value与CCP前作，也未完整形式验证所有存在性及渐近证明。", "未确定低覆盖来源，不据有限实验点直接推翻条件定理。", "Pro读全文文本，本地观察三页PDF；L2暂评。"]


## pro056 · CITEGUARD: Conformal False-Discovery Control for Faithful Retrieval-Augmented Generation

论文 OR_IXV8eAZsKc；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_IXV8eAZsKc_99ef34b1d847", "source_url": "https://api2.openreview.net/pdf?id=IXV8eAZsKc\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页1–31全部已提供文本，含正文、参考文献及附录A–E；连续页标无缺口。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–5仅有提取文字，不能核看曲线、误差条及布局。", "部分双栏顺序、公式和表格排版有损；未提供原始数据、运行记录及前作全文。"]}

问题：在用户指定风险α下，从RAG答案中尽量保留有证据支持的主张，并控制保留集合的预期错误发现比例。

方法：先生成草稿并拆分主张，以DeBERTa蕴含logit对检索证据评分、跨段取最大值。用n个无支持校准样本构造p_i=(1+#{a_j^(0)≥a_i})/(n+1)，按BH阈值kα/m或BY阈值kα/(mH_m)保留主张及引用，其余弃答；可选自适应切换和连贯性过滤。实际是生成后的选择层。

作者主张：把引用忠实性转化为多重检验，用用户可调α选择主张，而非固定置信度阈值。

论文证据：算法1给出校准、逐主张打分、BH/BY选择和引用拼装；表1、12报告风险与弃答权衡。

模型推断：新增主要是已有统计工具在RAG输出筛选中的场景化接口，而非新的生成器或检验程序。

定位：['TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页3–4，§4、算法1；物理页18，表12。']

作者主张：交换性下获得有限样本FDR≤α：BY允许任意主张依赖，BH要求PRDS。

论文证据：引理5.2给出空假设p值超均匀性；定理5.3和附录E直接调用经典BH/BY结果。

模型推断：属于场景化推论。保证针对选择集合的E[FDP]，不是每个答案的硬性错误上限，也不自动覆盖合并统计、自适应切换或后处理。

定位：['TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页4–5，§5；物理页31，附录E。\n']

key_results：[{"setting": "FEVER dev，α=0.10，表1所述金标评测。", "baseline": "Vanilla RAG：FDR=0.284。", "metric_or_guarantee": "作者报告的合并FDR、弃答率、支持主张召回率。", "reported_values_and_units": "BH：0.097±0.006、26.8%、92.3%；BY：0.073±0.005、33.6%、86.0%。", "information_and_compute": "默认2000个负校准样本、5次随机校准划分。全研究报告约120 GPU-hours；验证器训练为4×A100、2小时，单查询推理约0.8秒，均未复测。", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页8，表1；物理页14，§B.5。\n"}, {"setting": "NQ，FiD-large+DPR，α=0.10；主评测为500条分层抽样、人类核验主张。", "baseline": "Vanilla RAG FDR=0.306；Self-RAG=0.204。", "metric_or_guarantee": "合并FDR、逐答案平均FDP、覆盖与条件性任务效用。", "reported_values_and_units": "BY合并FDR=0.094，95% CI=[0.082,0.106]；逐答案平均FDP=0.089；弃答37.2%，支持召回86.4%，EM@Acc=50.8%。附录扩展至800条后FDR=0.091，CI=[0.081,0.101]。", "information_and_compute": "2000个负校准样本；EM@Acc仅对非空输出检查金答案子串，不是对全部查询计算的普通准确率。上述区间均不能确认95%置信达标。", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页7–8，指标及表1；物理页22，表19、§C.16。\n"}, {"setting": "FEVER的匹配弃答比较，以及另行校准到目标FDR的基线比较。", "baseline": "调阈值后的Self-RAG；RCPS-FDR。", "metric_or_guarantee": "风险与弃答权衡。", "reported_values_and_units": "约27%弃答时，CiteGuard-BH FDR=0.097、Self-RAG=0.128，作者报告相对降低24%。表29中RCPS-FDR为0.101/26.2%弃答，CiteGuard为0.097/26.8%，差距较小。", "information_and_compute": "均为作者报告；未提供逐例配对结果以核验显著性和基线调参过程。", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页18，表12；物理页29，表29。\n"}, {"setting": "NQ更强生成器补充实验，α=0.10。", "baseline": "Vanilla GPT-4o：FDR=0.126。", "metric_or_guarantee": "BY筛选后的风险与覆盖。", "reported_values_and_units": "GPT-4o+BY：FDR=0.074，95% CI=[0.058,0.090]；弃答15.8%，支持召回96.0%。", "information_and_compute": "每种新增生成器人工标注250条主张，负校准样本1000；API费用与该实验独立算力未报告。", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页24–25，§C.20、表26。\n"}]

prior_work_candidates：[{"citation_as_printed": "Vovk, V., Gammerman, A., and Shafer, G. Algorithmic Learning in a Random World. Springer, 2005.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "交换性下的共形秩校准。", "claimed_difference": "本篇将其用于无支持主张的空假设评分。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页3，§4.2；物理页12，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Benjamini, Y. and Yekutieli, D. The control of the false discovery rate in multiple testing under dependency. The Annals of Statistics, 29(4):1165–1188, 2001.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "任意依赖下的BY校正。", "claimed_difference": "改变检验对象为RAG主张，未修改BY程序。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页4，定理5.3；物理页10，参考文献；物理页31，附录E。", "prior_actually_read": false}, {"citation_as_printed": "Bates, S., Angelopoulos, A., Lei, L., Malik, J., and Jordan, M. Distribution-free, risk-controlling prediction sets. Journal of the ACM, 68(6):1–34, 2021.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "校准数据驱动的风险约束。", "claimed_difference": "作者强调多主张FDR目标；但附录承认目标不同，调成RCPS-FDR后结果接近。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页7、10、28–29，RCPS说明、参考文献及§C.24。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心增量清晰，但主要是成熟校准与多重检验工具的RAG场景整合，未展示新的统计机制或非平凡理论扩展。", "central_increment": "前作已提供秩校准和BY控制（本篇转述）；本作在匹配校准协议下增加逐主张保留/弃答接口，证据为算法1及实验表；尚待排除检验族和评测口径不一致。", "soundness_observation": "核心条件性归约可理解，但实验内部冲突、置信区间解读和附录推导问题明显，不能据此认可全部实证与保证主张。", "significance_observation": "风险预算接口有实用价值，但保证是证据协议相对的，并伴随弃答及连贯性成本。", "main_open_question": "实际检验族究竟是单个答案还是跨答案集合？FEVER若每答只有一条主张，BH/BY为何产生不同结果？"}

limitations：[{"text": "作者明示交换性、标注协议和主张粒度限制；自适应切换及连贯性过滤不在主定理覆盖内。实体错位压力测试中BY仍报告FDR=0.112，高于0.10。", "basis": "author_report", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页4–5，§5；物理页26，表27。"}, {"text": "FEVER被明确设为每答m=1，此时H_1=1，同p值下BH与BY应完全相同；表1却不同，且表16、30报告其答内主张相关性，设置未自洽。", "basis": "model_inference", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页14，表4；物理页8、21、30，表1、16、30。\n"}, {"text": "定理的E[FDP]与主表ΣV/ΣR并非同一目标。B.4按总体分箱比例加权箱内FDR，按所写公式未计接受率差异；此外验证器标签校准不自动保证人类标签下的FDR。", "basis": "model_inference", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页2–3，§3、4.2；物理页14，§B.4；物理页23–24，§C.18。\n"}, {"text": "表1将BY标为95%置信满足α，但区间上界0.106超过0.10；800条扩展的上界0.101也仍超过目标。点估计达标不能替代置信认证。", "basis": "model_inference", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页8，表1；物理页22，§C.16。"}, {"text": "按D.1可读指数界，即令依赖修正为0，ε=0.02、δ=0.05也需m≥4612，而非文中456。证明草图未交代充分依赖条件及随机接受数分母的控制；D.2亦未充分论证阈值网格误差如何推出整体FDR距α的界。", "basis": "model_inference", "locator": "TEXT_OR_IXV8eAZsKc_99ef34b1d847：物理页30–31，命题D.1、D.2及附录E。\n"}]

minimal_check：{"question": "核对FEVER的检验族及BH/BY差异是否可重建。", "control": "固定同一校准划分、逐例p值与α，只切换BH/BY；显式记录每个答案的m。", "observable_outcome": "m=1时接受集合必须逐例一致；检查实际输出能否重建表1。", "resources": "需要答案ID、p值、校准划分和实际选择记录；CPU即可比较，无需重新生成。资料与核验工时未知。", "failure_or_stop_condition": "m=1仍出现差异则实现或表格需修正；实际跨答案组检验则须重述保证范围；无逐例记录时停止数值认证。"}

missing_fields：["所选前作条目未列唯一标识，且未提供前作全文。", "未提供原始逐例记录、完整证明和可运行附件，未核验代码发布状态。", "现代生成器独立算力、API费用及完整标注成本未报告。"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

保留已有统计工具作为RAG筛选接口的工程想法；核心检验族、指标及置信解读存在未消解冲突，在取得原始p值和选择记录前不继续依赖其强实证保证。

身份、方法与保证条件：31页官方当前附件及输入返回绑定一致。方法为生成后逐主张打分、以无支持校准样本形成上尾秩p值，再BH/BY筛选；依赖匹配的生成、检索和标注协议。BY的任意依赖保证仍要求有效空假设p值，不能修复分布漂移；BH需PRDS，弱相关系数本身不是PRDS证明。作者明确排除自适应切换及连贯性后过滤的形式保证。

核查定位：text_delivery_manifest.json, structured/pro056.json, p003–p005, §4–5, p031, classical proof sketch；source_and_conditional_guarantee_confirmed

检验族与FEVER内部冲突：第6页明确FEVER为single-claim-per-instance，第14页表4为每答1.0条。m=1时H1=1，同p值、校准及α下BH/BY均等价p1<=α，但原表1报告FDR .097/.073及弃答26.8/33.6%，第21页表16和第30页表30又给FEVER答内相关性。实际若跨答案组检验、另用不同输入或校准，必须重述设置；目前材料不能重建该差异，不能将其当BY对答内依赖更稳的验证。

核查定位：p006:L0019-L0031, PDF physical page 14, Table4, PDF physical page 8, Table1, p021, Table16, PDF physical page 30, Table30, local_check/risk_scope_arithmetic.json；testing_family_inconsistency_confirmed

期望FDP与合并错误率不同：第2页定义按答案控制E[V/(R∨1)]，第7页主表却使用ΣV/ΣR。两者一般不相同：每答案只有一个且全为空假设时，有效均匀p值可使前者=α，但一旦有接受项，全部接受项都是假发现，合并比例为1。不能由逐答定理直接认证主表合并指标。B.4按总体箱比例加权箱内FDR；若箱内率是接受后错误率，还需按接受率重新归一化权重。

核查定位：p002, FDR definition, p007:L0033-L0038, PDF physical page 14, B.4, local_check/risk_scope_arithmetic.json；risk_estimands_and_weighting_qualified

置信认证及任务效用分母：原PDF第8页表1给NQ BY点估计.094、95%CI[.082,.106]却加注95%置信FDR<=.10；上界超过目标，注释不被该区间支持。EM@Acc排除全弃答，并在拼接的保留文本中找金答案子串，不是所有查询上的普通准确率。弃答、支持召回和该条件效用需一并展示。

核查定位：PDF physical page 8, Table1 note and BY row, p007:L0040-L0061；confidence_and_utility_scope_confirmed

附录样本量算术与推导边界：按原PDF第30页指数界，即将依赖修正设0、ε=.02、δ=.05，也需ceil(log(40)/(2*.02²))=4612条，不能得到所报456或612。第31页仅以弱依赖分块草图援引Hoeffding，未明确足以控制随机接受数分母的条件；仅由p值网格步长也不足直接推出整个FDR距α为O(α/n)。不把这些问题外推为经典BH/BY本身失效。

核查定位：PDF physical page 30, D.1–D.2, p031, D.1–D.2 proof sketches, local_check/risk_scope_arithmetic.json；sample_size_arithmetic_conflict_confirmed

实际资源与标签协议：原PDF第14页明确默认2000负校准样本、验证器4A100约2小时、每查询含检索生成评分约.8秒、全实验约120GPU小时，均为作者报告未复测。NQ校准使用验证器标签而主评测用分层人类标签，两种标签协议不能自动共用同一空假设有效性。

核查定位：p003, calibration protocol, p013, B.1–B.2, PDF physical page 14, B.4–B.5；resources_and_label_scope_confirmed

本地补充/限定：["增加单假设全为空的解析例，明确逐答案FDR控制不能直接推导主表合并接受错误率保证。", "FEVER问题依据明确single-claim设置而非仅由平均值1.0推断；如实际采用另一检验族，应先更正设置，未猜测真实实现。"]

核查局限：["未运行RAG生成、人工标注、选择程序或原始数据重加权。", "局部算术和反例只检查所印公式/指标关系，不是对全部实验的复现或作者动机判断。", "未核读前作，L1为暂评；未认证所有补充实验和代码发布状态。", "Pro只读全文文本，本地观察三页PDF。"]


## pro057 · Learning Unanimously Acceptable Lotteries via Queries

论文 OR_daiccpXZfU；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_daiccpXZfU_ac65f24ba688", "source_url": "https://api2.openreview.net/pdf?id=daiccpXZfU\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_daiccpXZfU_ac65f24ba688：物理页1–43，含正文§1–6、参考文献及附录A–E.6；所供页标连续。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文文本，图1–2不可见；双栏次序、公式上下标及组合数部分失真。", "未对照原PDF确认抽取完整性；当前附件的版本角色未经核实，不认定为最终出版版。"]}

问题：面对n名主体、m个选项，仅查询某主体是否接受一个概率分布，寻找满足全部未知期望效用阈值的彩票，或正确报告不可行。

方法：先查询单纯形顶点，再沿至多m−1条边二分定位接受阈值；利用分母≤1/ε及有理重建精确恢复等价半空间。确定性算法只学习拒绝当前字典序最优候选的主体；随机算法抽样学习并缓存约束、全体核验、加倍违反者权重。预测用于调整扫描顺序、初始权重或边搜索起点。

作者主张：精确恢复单主体接受区域，并自适应求解多主体一致可行性。

论文证据：Lemmas 3.1–3.2及Theorem 3.3给出恢复正确性、查询界和终止论证。

模型推断：有限精度使近似二分能升级为精确恢复；自适应性节省部分实例的征询，但确定性最坏界不优于完整征询。

定位：['TEXT_OR_daiccpXZfU_ac65f24ba688：p5–6；p19–24附录C.1–C.5。']

作者主张：随机化降低需学习的半空间数量，并建立查询复杂度下界。

论文证据：Theorem 3.4通过小见证、加权抽样和势函数分析给出期望界；Theorems 4.1–4.2提供计数及不可区分性下界。

模型推断：中心增量是分离便宜的候选核验与昂贵的约束恢复；仍须向全体主体获取反馈，且上下界尚未完全匹配。

定位：['TEXT_OR_daiccpXZfU_ac65f24ba688：p6–7；p24–34附录C.6–D.2。']

作者主张：利用排序或彩票预测改善征询复杂度，同时保留无预测时的最坏保证。

论文证据：Theorems 5.1–5.3给出随R、E及边投影误差变化的界；Proposition 5.4补充误差相关下界。

模型推断：建议只指导搜索，并未学习新的效用模型；边投影误差不是预测彩票到可行域的距离。

定位：['TEXT_OR_daiccpXZfU_ac65f24ba688：p7–9；p34–43附录E。']

key_results：[{"setting": "ε∈(0,1/2]，1/ε为整数；量化、无噪声接受模型。", "baseline": "完整征询：O(nm log(1/ε))次查询。", "metric_or_guarantee": "精确恢复接受区域；输出可行彩票或NULL。", "reported_values_and_units": "单主体O(m log(1/ε))次；确定性多主体O(n²+nm log(1/ε))次。", "information_and_compute": "oracle不提供效用值；查询界不包含离线LP及有理重建时间。", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p5 Lemmas 3.1–3.2；p6 Theorem 3.3。"}, {"setting": "n,m≥2；相同量化模型；随机抽样与缓存。", "baseline": "完整征询学习全部n个半空间。", "metric_or_guarantee": "作者报告始终正确及期望查询上界；期望复杂度证明待补核。", "reported_values_and_units": "O(nm log n+min{n,m³ log n}·m log(1/ε))次查询；期望学习O(min{n,m³ log n})个半空间。", "information_and_compute": "每轮抽取至多16(m−1)²个带权副本，核验至多n名主体。", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p25算法3；p30附录C.6。\n"}, {"setting": "二元效用；始终正确的确定性或随机算法。第一项计数界的证明另用m≤(1/ε)^(1−η)，固定η>0。", "baseline": null, "metric_or_guarantee": "最坏情形查询下界；随机算法计期望。", "reported_values_and_units": "令d=min{n,m}，下界为Ω((n−d)+(d−1)log(1/ε))次；另有n=1时Ω(m)次，后者无需上述增长限制。", "information_and_compute": "由唯一可行彩票族及二值决策树论证；并非实验测量。", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p7 Theorems 4.1–4.2；p31–34附录D。增长限制见\n"}, {"setting": "外部排序σ̂或彩票x̂建议；其余假设不变。", "baseline": "无建议的算法2、算法3及LearnHyperplane。", "metric_or_guarantee": "预测敏感查询界与最坏情形稳健性。", "reported_values_and_units": "排序确定性：O((n+m log(1/ε))R)次，R≥1；R=0时n次。排序随机性：O(nmμ+min{n,m³μ}·m log(1/ε))次，μ=log E+log log n。彩票建议的单主体恢复：O(m+m log(1+δmax/ε²))次。", "information_and_compute": "E为包含一个有效见证集的最短排序前缀长度；δmax为所搜边的最大转折点投影误差。若x̂已被全体接受，核验n次即可终止。", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p8–9 Theorems 5.1–5.3。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Clarkson, K. L. Las vegas algorithms for linear and integer programming when the dimension is small. Journal of the ACM, 42(2):488–499, 1995.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "低维LP抽样与重加权。", "claimed_difference": "本作需通过二值反馈付费恢复并缓存约束。", "basis": "target_paper_only", "target_locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p6；p11参考文献；p14附录A。", "prior_actually_read": false}, {"citation_as_printed": "Bshouty, N. H., Goldberg, P. W., Goldman, S. A., and Mathias, H. D. Exact learning of discretized geometric concepts. SIAM Journal on Computing, 28(2):674–699, 1998a.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "离散几何概念的精确查询学习。", "claimed_difference": "本作目标是多主体半空间交集可行性，而非完整识别单一概念。", "basis": "target_paper_only", "target_locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p3 §1.2；p11参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Blum, A., Jackson, J., Sandholm, T., and Zinkevich, M. Preference elicitation and query learning. Journal of Machine Learning Research, 5:649–667, 2004.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "为决策而征询，不必完整恢复偏好。", "claimed_difference": "本作采用单纯形上的二值接受查询，并显式分析精度依赖。", "basis": "target_paper_only", "target_locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p2 §1.2；p10参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "弱oracle下的精确可行性与信息复杂度保证具有实质增量；大量继承经典几何算法，尚不足以判路线级L3。", "central_increment": "前作已利用小基集解决低维LP（本篇转述）；本作在量化参数、仅二值主体查询下新增选择性约束征询及预测敏感保证；支持证据为§3–5及附录C–E，尚待核查前作覆盖和随机证明修复。", "soundness_observation": "按提供文本，C.4将1[t<T]放在F_{t−1}条件期望外，但T是终止轮，{t<T}依赖本轮样本，通常仅F_t可测。当前常数漂移推导不成立，并传递至E.2；这不直接反证算法或最终复杂度界。定位：TEXT_OR_daiccpXZfU_ac65f24ba688，p28–29。\n \n", "significance_observation": "意义在征询信息成本，不是模型训练能力；适合小选项集、大主体池。未提供实现或实际部署结果，工程收益尚无实证。", "main_open_question": "能否正确处理终止轮，并保留Theorems 3.4和5.2所依赖的期望迭代界？"}

limitations：[{"text": "噪声、情境变化、非期望效用及尾部风险准则不在保证内；策略性报告亦被抽象掉。", "basis": "author_report", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p9–10 §6及Impact Statement；p14附录A。"}, {"text": "量化解对连续原问题仅有阈值±2ε的转移保证，不能当作有噪声条件下的严格一致接受。", "basis": "model_inference", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p16 Lemma B.2。"}, {"text": "少学习半空间不自动意味着总查询少于完整征询，还需比较全体核验开销；查询复杂度也不等于运行时间，C.1示例重建需枚举分母至1/ε。", "basis": "model_inference", "locator": "TEXT_OR_daiccpXZfU_ac65f24ba688：p5–6；p20 C.1；p30 C.6。"}]

minimal_check：{"question": "检验Lemma C.4原式能否通过首轮精确核算。", "control": "模型构造：m=2、n=17、ε=1/2；仅一名主体要求x2≥1/2，其余ACCEPTALL。算法3首轮从17个主体中均匀抽取16个。", "observable_outcome": "漏抽关键主体概率为1/17，势函数由1/17变为1/9；原式左侧为log(17/9)/17，而漏抽事件上右侧为log 2−1/4，可直接比较。", "resources": "纸笔枚举17种等概率首轮样本即可；不需数据集或GPU，未运行作者代码。", "failure_or_stop_condition": "若原式不成立，停止将该漂移证明视为完备，要求补充终止处理；不能据此宣布算法错误。"}

missing_fields：["图像与原PDF版面未提供，部分公式排版不能视觉核验。", "前作全文未提供；所列候选条目未印DOI或arXiv标识，identifier_if_present为null。", "全文为理论分析，未提供实证评测、预测器训练或生成成本、运行时间及硬件资源。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

弱oracle下分离昂贵约束恢复与便宜候选核验具有可迁移思路；重点读量化精确重建与查询成本分解，并带着停止证明修补及真实反馈噪声边界继续。

身份、oracle和精确性条件：43页官方当前附件与全文返回绑定一致。每次询问一个主体是否接受概率向量，效用/阈值静态、无噪声且按ε量化。目标是找到全体接受的彩票或证明不可行，不是最大化接受人数、真实人类满意度或带尾部风险的决策保证。

核查定位：text_delivery_manifest.json, structured/pro057.json, p004, problem and finite precision, p009, limitations；source_and_oracle_scope_confirmed

恢复半空间的关键算术：第20页转折点(t−a)/(b−a)的约分分母<=1/ε，不同候选间距至少ε²，因此二分到宽度<ε²/2可精确有理重建；最多m−1条边加顶点查询给O(m log(1/ε))。恢复的是等价接受半空间而非唯一真实效用。示例重建枚举分母至1/ε不增加oracle查询，却可能增加离线时间。

核查定位：p004–p005, Algorithm1 and Lemmas3.1–3.2, p020, Eq3–4 and ExactThreshold；central_reconstruction_condition_checked

查询成本与实际运行成本：完整征询O(nm log(1/ε))；确定性自适应最坏还多O(n²)核验，不能普遍称更快。随机界为O(nm log n+min(n,m³log n)m log(1/ε))的期望查询数，通过少学约束交换全体核验成本，主要适合小m大n。离线LP、预测取得成本及墙钟不包含其中；没有实证部署结果。

核查定位：p005, full elicitation and Select, p006, Theorems3.3–3.4, p007–p009, advice and future work；complexity_and_resource_scope_confirmed

停止事件错误的明确实例：原PDF第29页C.4中T为终止轮，{t<T}依赖本轮抽样，不能按第28页F_(t−1)提出条件期望。m2、n17、ε=.5，16个ACCEPTALL及一个x2>=.5约束，首轮无放回抽16人。漏抽概率1/17，Phi从1/17到1/9；原式左侧log(17/9)/17≈.03741，而漏抽事件上右侧log2−.25≈.44315。原不等式确实失败；这不是算法失败例。

核查定位：p024, WeightedSample and lexicographic maximum, PDF physical page 25, Algorithm3, p028, filtration, PDF physical page 29, LemmaC.4, local_check/stopping_event_check.json；literal_drift_inequality_counterexample_confirmed

有条件的局部证明修补：接受C.2/C.3为前提时，可把终止后的分析势设为2并计入终止轮，改用F_(t−1)可测的{t<=T}。终止轮增量至少log2，非终止轮沿原界，Jensen后得到正漂移，求和给ET<=(log2+b log n)/(log2−1/4)。因此同阶O(m log n)可通过此局部改写恢复；细节另存，未声称全部前置引理已形式化核证。

核查定位：PDF physical page 25, LemmaC.2, p028, LemmaC.3, local_check/stopped_potential_repair.md；conditional_local_repair_supplied

预测参数与下界范围：R是给定排序下实际学习的主体数，不是排序误差的外部统计；E是包含有效见证集的最短前缀。彩票建议的δ是所搜边转折点投影误差，不是到可行域距离。若预测本身已全体接受需n次核验；计数下界另有m与ε增长限制，不能把上下界称完全匹配。

核查定位：p004, lower-bound growth restriction, p007–p009, Theorems4.1–5.3 and definitions；advice_and_lower_bound_scope_qualified

本地补充/限定：["用正确的字典序最大Select及无放回抽样确认17主体例。", "补充停止后人工势函数的条件性修补，说明原C.4错误并不要求放弃所称同阶期望复杂度；原始Pro记录保留。"]

核查局限：["未运行作者代码或现实征询实验；局部实例及修补均为纸笔与标量算术。", "未核读Clarkson及精确概念学习前作，L2暂评。", "未逐式审计全部几何采样引理、预测增强证明和下界归约。", "Pro为全文文本阅读，本地观察两页原PDF。"]


## pro058 · Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity

论文 OR_8LVv9hyMII；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_8LVv9hyMII_669f9d534e73", "source_url": "https://api2.openreview.net/pdf?id=8LVv9hyMII\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "c3b0ecea67ed9f1c40fa53e9b557da3ce8a55587c3da5a86474c1ad4ada69d49", "source_pdf_sha256": "669f9d534e73dee3f0f905a5ea47eeb460f12cfd37e464706f1fd1cf9b99ec19"}], "read_ranges": ["TEXT_OR_8LVv9hyMII_669f9d534e73：物理页1–28全部提供文本，页标连续；含正文§1–8、参考文献及附录A–D。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像，图1–5不可见；表1–2主要文字可读，部分列对齐、指数及公式符号失真。", "版本角色未验证，不能认定为最终出版版；前作全文、代码及原始实验数据未提供。本轮未搜索或复现。"]}

问题：在无限时域折扣MDP中最大化整条轨迹回报的static CVaR，同时获得可计算的历史依赖策略。

方法：沿用预算更新z'=(r+z)/γ，将价值改写为v̄*(s,z)=maxπ E[−(R+z)⁻+z⁻]，逐步奖励改为r̃=z⁻−(r+z)⁻。在有限区间投影预算并向下/向上取整，进行VI或Q-learning；每条环境转移同时更新全部预算点。训练后对每个α优化初始z，输出相应预算条件策略。

作者主张：通过奖励重分配保持static CVaR目标，同时消除原表述造成的终端反馈和受限初始化问题。

论文证据：Proposition 4.1与Theorem 4.2给出有界性、L∞收缩、唯一正确不动点及预算区间外常值性质。

模型推断：增量在于使既有增广问题可用标准有界价值迭代处理，不是首次提出状态增广；新奖励仍可能为零，并非每步必有非零反馈。

定位：['TEXT_OR_8LVv9hyMII_669f9d534e73，p4 §4、p14–16 B.4–B.5']

作者主张：提出上下界近似VI与块更新Q-learning，一次训练支持多个风险水平，并给出误差及收敛保证。

论文证据：Theorems 5.3–5.4给出离散化界；Theorem 6.2在Robbins–Monro步长及所有名义状态动作对无限访问下证明Q表几乎必然收敛。

模型推断：收敛对象是离散增广MDP；有限网格和实际外层网格搜索不能直接称为原问题全风险水平精确最优。

定位：['TEXT_OR_8LVv9hyMII_669f9d534e73，p5–7 Theorems 5.3–6.2、p19–26 B.7–B.11。\n']

key_results：[{"setting": "有界奖励、无限时域折扣MDP，连续预算z。", "baseline": "原增广算子在L∞中的零不动点。", "metric_or_guarantee": "新算子为sup-norm下γ收缩，唯一不动点对应正确内层优化。", "reported_values_and_units": "||v̄*||∞≤rmax/(1−γ)；令rγ=rmax/(1−γ)，投影z至[−rγ,rγ]不改变v̄*。", "information_and_compute": "理论结果；不要求奖励非正，也不等于神经网络训练收敛保证。", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p4 Proposition 4.1/Theorem 4.2。\n"}, {"setting": "r≤0、均匀网格间距Δ、精确离散固定点及定理中的外层优化。", "baseline": "原问题最优static CVaR，记为Ψ*。", "metric_or_guarantee": "上下值界及下界算子所诱导策略的性能保证。", "reported_values_and_units": "令b=γΔ/[α(1−γ)]，则Ψ*−b≤Ψˡ≤CVaRα(πˡ)≤Ψ*≤Ψᵘ≤Ψ*+b。", "information_and_compute": "VI需转移模型；Q-learning使用转移样本。每条样本更新全部预算点，样本数不能等同于TD更新数。", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p5–6 Theorem 5.4及均匀网格推论。\n"}, {"setting": "4×5 Crater Walk，γ=0.9、动作噪声ω=0.25，预算区间[−110,110]、5000 bins。", "baseline": "risk-neutral策略，以及本篇Q-VI与Q-learning之间的比较。", "metric_or_guarantee": "经验CVaR、回报分布、折扣入坑次数及Q值收敛。", "reported_values_and_units": "正文称约50,000训练迭代后Q-learning收敛，低α时优于risk-neutral；图形不可见，无法提取效应量。\n", "information_and_compute": "10个种子；Q-learning训练75,000 episodes；VI停止容差1e−4；每α评测10,000 rollouts，测试至多150步。硬件、墙钟时间及训练总转移数未报告。", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p7–8 §7、p27–28 D.1–D.4/Table 2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Bäuerle, N. and Ott, J. Markov decision processes with average-value-at-risk criteria. Mathematical Methods of Operations Research, 74(3):361–379, 2011.", "identifier_if_present": null, "relation_candidate": "方法继承；理论扩展", "shared_component": "连续预算增广与static CVaR动态规划。", "claimed_difference": "本作平移价值并重分配奖励，使正确固定点落入L∞。", "basis": "target_paper_only", "target_locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p4 §3.3–4、p9 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Ávila Pires, B., Rowland, M., Borsa, D., Guo, Z. D., Khetarpal, K., Barreto, A., Abel, D., Munos, R., and Dabney, W. Optimizing return distributions with distributional dynamic programming. Journal of Machine Learning Research, 26(185):1–90, 2025.", "identifier_if_present": "http://jmlr.org/papers/v26/25-0210.html\n", "relation_candidate": "背景引用", "shared_component": "状态增广下包含static risks的动态规划。", "claimed_difference": "本篇仅称其覆盖更广问题；未展示与本作算子的逐项等价性比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p3 §2、p9 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Kim, J.-H. and Min, S. Predictive CVar q-learning. In The Fourteenth International Conference on Learning Representations, 2026.", "identifier_if_present": "https://openreview.net/forum?id=B4SCegRJOA\n", "relation_candidate": "背景引用", "shared_component": "static CVaR的Bellman式递推。", "claimed_difference": "本篇称其需tail value与tail probability两个预测量且限有限时域；本作使用单一有界价值函数处理折扣无限时域。", "basis": "target_paper_only", "target_locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p2–3 §2、p10 References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "改变可用函数空间并建立误差、算法收敛链条，超过局部性能改进；仍属于既有状态增广路线。", "central_increment": "前作已用增广求解static CVaR（本篇转述）；本作在有界折扣奖励下新增L∞正确不动点及可控离散化，证据为Theorems 4.2/5.4；尚待排除近邻前作已有同等保证。", "soundness_observation": "核心代数变换与收缩论证可辨；未完成逐条证明审计，部分附录符号及索引需原PDF核对。理论条件与实验实现之间存在明确缺口。", "significance_observation": "为static CVaR接入表格TD方法提供理论基础；尚未证明大规模或真实安全任务中的优势。", "main_open_question": "定理中连续外层优化的保证，如何覆盖实际网格搜索与有限训练共同产生的总误差？"}

limitations：[{"text": "作者明确实验仅限表格设置；函数逼近扩展属于后续方向。", "basis": "author_report", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p9 §8。\n"}, {"text": "缺少与正确配置的原增广方法进行匹配预算对照，无法隔离奖励重分配的效率收益；图4所谓Ψ*来自10,000预算格Q-VI，非独立精确真值。", "basis": "model_inference", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p7–8 §7/Figures 3–4。\n"}, {"text": "实验步长设正下限κmin=1e−4，渐近上不满足平方可和条件，不能直接套用Theorem 6.2的几乎必然收敛结论。", "basis": "model_inference", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p7 Theorem 6.2、p28 D.4/Table 2。\n"}, {"text": "Algorithm 3及实验列入α=0，却使用1/α，未交代边界处理；正文与D.1对−10处罚发生于入坑还是脱离坑的描述也不一致。", "basis": "model_inference", "locator": "TEXT_OR_8LVv9hyMII_669f9d534e73，p7 §7、p27 Algorithm 3/D.1、p28 D.3。\n"}]

minimal_check：{"question": "外层仅搜索预算网格会增加多少误差？", "control": "在有限步后吸收的小型MDP中枚举历史策略获得精确CVaR；固定内层求解精度，比较连续外层优化与Algorithm 3，并逐次减半Δ。", "observable_outcome": "各α下实际策略CVaR、上下界顺序及网格外层搜索的附加误差。", "resources": "小型MDP、独立策略枚举器和表格VI实现；硬件及耗时未知。", "failure_or_stop_condition": "连续外层版本若违反Theorem 5.4界，停止扩大实验并核查实现或证明；仅网格版本偏离时须单列外层近似误差。"}

missing_fields：["图3–4的具体CVaR、入坑次数、误差及方差数值不可读。", "硬件、墙钟时间、训练总环境步数和超参数搜索成本未报告。", "α=0处理及离散回报的经验CVaR估计细节未说明。", "Bäuerle–Ott参考条目未印独立标识符；所有前作均未实际核读。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

有界价值平移和奖励重分配使既有增广目标接入标准表格Bellman/TD分析，机制清楚值得继续；实用比较应匹配预算并补足外层搜索及有限训练误差。

身份与目标：28页官方当前附件与全文返回绑定一致。研究整条折扣回报的static lower-tail CVaR，非逐步嵌套风险；增广状态可实现原空间历史依赖策略。按算法取0<γ<1，变分目标需0<α<=1，奖励有界。前作增广由本篇承接，未独立核验历史优先性。

核查定位：text_delivery_manifest.json, structured/pro058.json, p003, §3 and Eq1–3, p013, B.1–B.2；source_and_objective_scope_confirmed

奖励重分配的核心代数：原PDF第4页rtilde=z^-−(r+z)^-且z_next=(r+z)/γ。对未投影轨迹，折扣求和望远镜相消为z0^-−(R+z0)^-，因此保持内层目标。负部函数1-Lipschitz给|vbar|<=rmax/(1−γ)，有界奖励Bellman算子按sup范数γ收缩；旧零奖励算子在有界函数空间唯一为0并不否定其在适当无界函数类的原结果。新奖励仍可能为0，不是每步都非零。

核查定位：PDF physical page 4, Proposition4.1 and Theorem4.2, p012, reward illustration, p013, B.2–B.3；central_identity_and_function_space_checked

离散误差与实现外层优化：Theorem5.3–5.4的上下包络及策略保证用非正奖励条件，均匀格误差b=γΔ/[α(1−γ)]；精确离散固定点和定理规定的外层优化是前提。第6页已区分模型已知时连续z求值与模型无关时格点近似；Algorithm3仅搜预算格，有限训练、离散内层和外层搜索的误差应分列，不能说一次有限训练即原MDP全风险水平精确最优。

核查定位：p005, Assumption5.1 and Theorems5.3–5.4, p006, Proposition5.5 and §6, p027, Algorithm3；approximation_guarantee_conditions_confirmed

收敛定理与实验步长不一致：Theorem6.2要求步长和发散、平方和收敛及所有名义(s,a)无限访问。原PDF第28页实验步长为max(1e-4,1/(1+.01N(s,a)))，正下限令平方和最终发散，不能直接套用几乎必然收敛定理。每个环境转移更新全部5000预算点，环境样本数与TD更新数、墙钟成本不可混同。

核查定位：p006–p007, Theorem6.2 and Algorithm2, PDF physical page 28, D.4 and Table2；asymptotic_vs_finite_training_scope_confirmed

图中基准和训练计数：原PDF第8页Fig3d横轴明确为Episodes(x1000)，因此正文所谓约50k迭代应按图解释为episode尺度，不能当50k环境步或TD更新。Fig4的Ψ*由10000预算点Q-VI计算，并非独立精确真值。曲线支持网格加密后上下近似靠拢，但未提供与正确初始化原增广算法的同预算实测对照。

核查定位：PDF physical page 8, Figures3–4 and accompanying text, PDF physical page 28, 75000 episodes；empirical_reference_and_counting_corrected

边界参数与环境说明：正文和Fig3列的是从.01至1的12个正α；附录D.3却称12个并列出含0的13项，Algorithm3仍使用1/α且无0分支，不能据此确认实际运行了除零，只能记录边界处理未说明。附录训练窗口/测试协议为4×5、γ=.9、动作噪声.25、[-110,110]预算格、10种子、每α10000rollouts、测试最多150步。正文入坑处罚与D.1为脱坑额外燃料的描述也需实现澄清。

核查定位：p007, §7, p027, Algorithms3–4 and D.1–D.2, PDF physical page 28, D.3–D.4；boundary_and_environment_ambiguities_preserved

本地补充/限定：["本地原图确认收敛横轴是episode，不将50k迭代误读为环境步。", "α=0问题限定为附录列表/算法未说明，正文和图为正α，未宣称已证实程序除零。"]

核查局限：["未核读Bäuerle–Ott等前作，L2是暂评。", "未完整审计全部离散化证明或执行任何MDP、训练、最小实验。", "未从图估计精确CVaR/方差，硬件、墙钟和总环境步仍未知。", "离散回报的经验CVaR边界质量处理未确认；理论按变分定义理解。", "Pro读全文文本，本地观察三页PDF。"]


## pro059 · Human-AI Collaborative Uncertainty Quantification

论文 OR_FzP6XZGG4d；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_FzP6XZGG4d_2550810f706b", "version_role": "current_attachment_unverified_role", "material_form": "full_text"}], "read_ranges": ["TEXT_OR_FzP6XZGG4d_2550810f706b：物理页1–24，含正文、参考文献及附录A–C.4；页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–9图像未提供；不读取图中曲线数值。表1–5文字基本可辨，双栏阅读顺序及部分公式符号存在抽取损失；未核对PDF图像。"]}

问题：将人类提出的集合H裁剪、补全为尽可能小的C，同时限制人类已覆盖真值时的误删率，并保证人类漏标时的补回率。

方法：输入x、H(x)及固定非一致性分数；候选标签在H内用阈值b，H外用a。离线按真值是否属于H分组，分别取加入∞后的1−ε、1−δ分位数。在线揭晓真值后，仅更新所属组阈值：η×(漏覆盖指示−目标误差率)。分类采用1−p̂；回归用两对分位数构造H内外不同的CQR分数。

作者主张：HACO总体最小尺寸解具有单一后验分数、两个阈值的结构。

论文证据：定理2.1给出C*={y:1−p(y|x)≤a1[y∉H]+b1[y∈H]}；B.1用线性松弛及拉格朗日推导。

模型推断：将协作表述为可分别控制的保留与补全问题有实质价值；但所写纯阈值最优性存在并列概率边界问题。

定位：['TEXT_OR_FzP6XZGG4d_2550810f706b：p002 HACO；p003 定理2.1；p015–p016 B.1。']

作者主张：CUP在离线交换数据和任意在线序列中同时控制两类风险。

论文证据：命题4.1给出两组覆盖下界1−ε、1−δ。命题4.2给出|组内经验漏标率−q|≤[1+ηmax(q,1−q)]/[ηN_g(T)]，其中q分别为ε、δ。

模型推断：实质是两组分位数校准与两条标量反馈的组合扩展；保证不依赖总体最优性成立，但不等于逐例安全或有限样本尺寸最优。

定位：['TEXT_OR_FzP6XZGG4d_2550810f706b：p004–p005 命题4.1–4.2；p016–p019 B.2–B.3。']

key_results：[{"setting": "ImageNet-16H，ω=125，聚合top-2人类集合；表1标注(ε,δ)=(0.05,0.70)。", "baseline": "Human Alone；AI Alone共形预测。", "metric_or_guarantee": "覆盖率/平均标签数，10次划分的均值±标准差。", "reported_values_and_units": "Human：0.8008±0.0090 / 2.00±0.00；CUP：0.9022±0.0083 / 1.49±0.04；AI：0.9072±0.0138 / 1.65±0.07。", "information_and_compute": "数据含1,200张图、32,431条人类预测；VGG19微调10轮。硬件与时长未报。", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p006 §5.1；p007 表1。"}, {"setting": "DDXPlus合成病历，规则诊断列表top-2作为人类代理；GPT-5；表2标注(ε,δ)=(0.02,0.45)。", "baseline": "Human Alone；GPT-5 AI Alone。", "metric_or_guarantee": "覆盖率/平均诊断标签数。", "reported_values_and_units": "Human：0.87/1.95；CUP：0.93/1.65；AI：0.93/1.95。", "information_and_compute": "非真实医生试验；LLM调用、采样和费用预算未报。", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p007 §5.2；p008 表2。"}, {"setting": "Communities & Crime，Human B；表3标注(ε,1−δ)=(0.05,0.90)。", "baseline": "模拟人类区间；AI Alone CQR。", "metric_or_guarantee": "覆盖率/区间长度，长度按论文目标尺度。", "reported_values_and_units": "Human：0.872/0.618；CUP：0.948/0.528；AI：0.948/0.608。", "information_and_compute": "H由真值加高斯噪声生成；两个双输出头MLP用pinball loss训练，资源未报。", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p008 §5.3及表3。"}, {"setting": "真人几何图形计数，Gemini 2.5 Flash-Lite；在线(ε,δ)=(0.2,0.5)。", "baseline": "Human Alone；覆盖率匹配的AI Alone。", "metric_or_guarantee": "累计覆盖率、平均集合标签数。", "reported_values_and_units": "正文报告CUP覆盖率64.35%，Human为48.8%；集合大小CUP为2.72、AI为3.22。非从图5读取。", "information_and_compute": "50名Prolific参与者，每人20例；报酬12美元/小时，中位完成时间约5分钟；AI成本未报。", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p020 C.1；p021:L0018–L0023。"}]

prior_work_candidates：[{"citation_as_printed": "Straitouri, E., Thejaswi, S., and Rodriguez, M. G. Controlling counterfactual harm in decision support systems based on prediction sets. Advances in Neural Information Processing Systems, volume 37, pp. 129443–129479, 2024.", "identifier_if_present": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e9e3e5bdb017bbc887271c6f6de5353f-Paper-Conference.pdf\n", "relation_candidate": "背景引用", "shared_component": "预测集协作中的counterfactual harm问题。", "claimed_difference": "前作分析AI建议对人类后续判断的因果伤害；本作控制人类初始集合被修订后的条件漏覆盖。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p012 参考文献；p014–p015 附录A。", "prior_actually_read": false}, {"citation_as_printed": "Kiyani, S., Pappas, G., and Hassani, H. Length optimization in conformal prediction, 2024.", "identifier_if_present": "arXiv:2406.18814", "relation_candidate": "理论扩展", "shared_component": "最小预测集尺寸的阈值刻画。", "claimed_difference": "由单阈值扩展到人类集合内外分别控制的双阈值。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p003 §2；p010 参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Angelopoulos, A. N., Candes, E. J., and Tibshirani, R. J. Conformal pid control for time series prediction, 2023.", "identifier_if_present": "arXiv:2307.16895", "relation_candidate": "理论扩展", "shared_component": "在线误差反馈与累计校准保证。", "claimed_difference": "从边际错误率控制扩展到误删、漏补两组同时控制。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p005 命题4.2后讨论；p009 参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是带双条件风险控制的协作接口，而非单场景调参；校准算子本身较直接，不足以认定路线级首创。", "central_increment": "前作已有集合建议、最小尺寸与在线校准（本篇转述）；本作在先给H、再修订C的条件下联合控制保留与补回，支持为理论推导和跨任务实验；尚待排除总体最优性边界漏洞。", "soundness_observation": "未逐一定理验算。B.1由点态最优直接断言松弛紧，纯阈值表达在并列概率上存在反例风险；B.2的a/b与正文互换。两组校准思路可独立于总体最优性评估。", "significance_observation": "提供可操作的集合协作机制；工程主体为双阈值维护，但端到端成本未报，临床效用、信任及真人长期适应均未得到验证。", "main_open_question": "总体最优性需要补充哪些边界选择或分布条件，修订后是否仍覆盖所声称的分类场景？"}

limitations：[{"text": "离线交换性会被分布变化、人类适应破坏；较大η提高响应速度，也增加阈值和集合大小波动。", "basis": "author_report", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p004 §4.1；p005 §4.2。"}, {"text": "在线保证是累计分组误差，不保证逐时刻或个体无害；主要人类输入为聚合标注、规则列表或真值加噪声，脚本策略切换不等于真实互动适应。", "basis": "model_inference", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p005 命题4.2；p006–p008 §5；p020 C.1。"}, {"text": "AI基线按CUP已实现覆盖率回配，在线甚至使用全流覆盖率，属于事后效率比较；缺少同样访问H的联合模型对照。", "basis": "model_inference", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p006:L0051–L0063；p007:L0045–L0052。"}, {"text": "正文补回目标为1−δ，B.1却写δ；表4的(ε,1−δ)表头与结果趋势疑似倒置。表5写GPT-5-mini，正文称GPT-5。不能默认记号及模型身份一致。", "basis": "model_inference", "locator": "TEXT_OR_FzP6XZGG4d_2550810f706b：p002 式(2)；p015 B.1；p021 表4；p022–p023 C.3及表5。"}]

minimal_check：{"question": "定理2.1的纯双阈值形式在离散并列概率下是否仍为最小可行集合？", "control": "构造单一x，p=(0.4,0.4,0.2)，H={1,2}，ε=0.6、δ=0.5；枚举8个子集，与定理所写双阈值族比较。", "observable_outcome": "纸笔推断：C={1,3}的误删率0.5、补回率1、尺寸2；纯阈值必须同时保留等分数的标签1、2，再加入3，尺寸3。核对是否需要显式边界选择。", "resources": "纸笔或CPU枚举，无需训练；本轮未运行代码。", "failure_or_stop_condition": "若确认最小尺寸为2而纯阈值可行集最小为3，停止无条件最优性解读，要求补充并列处理或适用条件。"}

missing_fields：["图像证据及未被正文明确记录的曲线数值。", "训练/校准/测试样本划分规模、实验η与初始化、回归分数裁剪及目标尺度说明。", "参数搜索预算、硬件时长、LLM提示与概率提取方式、调用和采样成本；除表1外多数结果缺少不确定性估计。", "δ含义、附录阈值命名及GPT-5/GPT-5-mini身份冲突未解决；前作全文与最终出版版本身份未核读。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

保留与补回分开控制的协作接口有价值；继续阅读先补总体最优性边界、统一δ记号，并用同样可访问H的联合模型作对照。

身份、投递与双条件目标：24页官方当前PDF与返回绑定一致；成功输入为仅压缩横向空白的revision2内联全文，助手返回从response_only边界独立保存解析，未把输入模板当返回。HACO控制Y已在人类H内时被C漏掉的概率，以及Y不在H时被C补回的概率；这是集合修订风险，非真实人类决策因果伤害或临床结果保证。

核查定位：text_delivery_manifest.json, browser/pro059_conversation.json, structured/pro059.json, p002, Eq1–2 and HACO；source_delivery_and_target_scope_confirmed

总体纯阈值最优性反例：原PDF第3页Theorem2.1没有并列处理，原第16页由点态符号选择直接断言松弛紧。固定一个x、p=(.4,.4,.2)、H={1,2}、ε=.6、δ=.5，精确枚举8个集合：C={1,3}或{2,3}尺寸2、误删.5<.6、补回1；同分数纯双阈值不能只取1或2，唯一可行阈值集为三标签全集，尺寸3。因此所印无条件纯阈值最优性不成立，应增加边界选择/随机化或分布条件；这不反驳两组校准方法的覆盖保证。

核查定位：PDF physical page 3, Theorem2.1, p015 and PDF physical page 16, B.1, local_check/tied_posterior_check.json；literal_population_optimality_counterexample_confirmed

离线和在线保证应分开：离线固定分数后按Y是否属于H分组取带∞的分位数，依赖三元组交换性。在线每轮揭晓真Y、仅更新所属组阈值，界控制累计分组漏标率，分母为该组出现次数N_g；需N_g>0、分数[0,1]及适当初值。它不保证每轮、每个人或未来新群体无害，也不保证有限样本集合最小。回归分数需另作缩放裁剪。

核查定位：p004, Proposition4.1, p005, updates and Proposition4.2；finite_sample_guarantee_scope_confirmed

ImageNet数值与匹配覆盖的比较：原PDF第7页表1确认ω125、top2：Human覆盖.8008±.0090/尺寸2；CUP .9022±.0083/1.49±.04；AI .9072±.0138/1.65±.07。人类集合由多份标注聚合为top-k，并非单个专家的实时建议。AI基线按CUP实际覆盖率回配，在线还使用整段流的实际覆盖率，属于事后同覆盖效率比较而非预先可部署的调参策略。

核查定位：PDF physical page 7, Table1, p006:L0028-L0063, p007:L0045-L0052；decisive_table_and_comparison_scope_confirmed

模拟与真人证据层级：DDXPlus是合成病历，所谓human集合来自规则诊断列表；回归H由真值加噪声生成。真人补充实验是50名Prolific参与者的几何图形计数，每人20例，AI为Gemini2.5Flash-Lite；第21页正文报告在线覆盖64.35%对48.8%，集合2.72对3.22。图5trial轴超过1400而50×20为1000，实际汇总流构成未说明，不能自行补成更多参与者或独立样本。它也不验证医生协作或长期真实互动适应。

核查定位：p007–p008, §5.2–5.3, p020, C.1, PDF physical page 21, online results and Figure5；human_evidence_and_counting_limits_confirmed

参数记号不能自动统一：正文补回目标为1−δ，第15页B.1却用δ。原第21页表4表头写(ε,1−δ)，但固定ε=.05时后列从.60降至.40而CUP覆盖从.698升至.809，趋势更像δ而非1−δ；没有原始参数记录不能自动改表。该不一致与总体最优性反例分开保存。

核查定位：p002, Eq2, p015, B.1 constraints, PDF physical page 21, Table4；parameter_label_inconsistency_preserved

本地补充/限定：["用精确有理数穷举确认并列概率下纯双阈值的最优性反例；明确独立于CUP有限样本覆盖保证。", "新增真人实验文字例数与图5时间轴的未解释差异，不猜测实际样本数。"]

核查局限：["未运行训练、在线实验或招募标注；8集合计算是定理的有限逻辑核查。", "未完整审计在线/离线证明及全部附录符号，也未核读前作；L2暂评。", "未解决GPT-5/GPT-5-mini的原始Pro待核身份问题，不将其列为本地确认事实。", "Pro为全文文本阅读，本地观察四页PDF，临床或长期协作价值未验证。"]


## pro060 · Keeping a Secret Requires a Good Memory: Unconditional Streaming Lower-Bounds for Differentially Private Algorithms

论文 OR_JiB2eXY8fT；暂定 L3；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d", "source_url": "https://api2.openreview.net/pdf?id=JiB2eXY8fT\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_JiB2eXY8fT_4f3fe3ce983d：物理页1—13全部；正文§1—4、参考文献及附录A.1—A.4。题名匹配，页标连续，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供全文文本，未见PDF图像；双栏交错、分式和上下标存在提取失真，尤其部分证明公式须核对原版。"]}

问题：连续发布用户级DP下，利用多数用户更新次数受限的promise获得较小误差，是否必然需要多项式工作空间？

方法：构造共享k名重用户C、每阶段独有轻用户S_i的随机插删流。假设存在准确低空间算法，将其输出与用户输入的相关分数随机舍入为集合Y_i；各玩家仅向下一玩家传递算法的M位状态。准确性要求集合足够大，隐私限制重用户反复入选，通信下界遂转为空间下界。

作者主张：提出不依赖密码假设、可用于自然统计任务的私有流算法空间下界框架。

论文证据：Lemma 3.1给出通信下界，Lemma 3.2与Corollary 3.3连接DP算法、舍入集合与状态通信。

模型推断：新增的是隐私约束到通信空间复杂度的证明接口；不等于证明算法必须显式执行某种贡献截断。

定位：['TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，pp.6—9，§3.1—3.3；p.12，A.3。\n']

作者主张：在CountDistinct的promise版本上得到接近T^(1/3)的无条件空间下界，并与非私有算法形成指数级空间分离。

论文证据：Theorem 2.1给出空间—误差关系，Corollary 2.2给出接近1/3指数的实例。

模型推断：若证明成立，则排除了绕过现有重用户处理策略的同精度低空间替代方案；近紧性仅限所列参数区域。

定位：['TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.5，Theorem 2.1、Corollary 2.2。\n']

作者主张：框架扩展至MaxSelect和Quantile。

论文证据：Theorem 2.3及附录A.4借用strong fingerprinting lemma，给出两个二元构造；额外对数平方损失被渐近记号隐藏。

模型推断：展示了跨任务迁移，不足以推出任意连续统计任务均有同样下界。

定位：['TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.5，Theorem 2.3；p.13，A.4。\n']

key_results：[{"setting": "T充分大；w=T^γw、k=T^γk、h=T^γh；各指数属于(0,1)，γw/2≤γk≤γh<γw且3γh<1。最多k名用户超过w次更新。", "baseline": "Cummings et al. (2025)的私有上界可达到tildeO(√w+k)加性误差，均为本文转述。", "metric_or_guarantee": "ε=0.5、δ=T^(-2)；对每个固定流，以至少1−T^(-2)概率，所有时刻同时满足τ=0.1、η=h的近似保证。", "reported_values_and_units": "文中定理：M≥tildeΩ(kw/h²)=tildeΩ(T^(γw+γk−2γh)) bits。", "information_and_compute": "邻接流移除单个用户全部更新；即使每名用户当前频率仅为0或1仍成立。不限制算法运行时间，无训练或实验。", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，pp.3—5，§2、Theorem 2.1。\n"}, {"setting": "Corollary 2.2：0<α<1/9；w=T^(2/3−4α)、k=T^(1/3−2α)、η=T^(1/3−α)；隐私、乘性误差与成功率同上。", "baseline": "本文称Cummings et al.可用T^(1/3+O(α)) bits达到tildeO(T^(1/3−2α))误差；非私有对照为多对数空间。", "metric_or_guarantee": "promise流上的空间分离与近紧性", "reported_values_and_units": "M≥tildeΩ(T^(1/3−4α)) bits；正多项式指数需α<1/12，接近1/3指数须取充分小α。", "information_and_compute": "作者渐近理论比较，不是本地实测。", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.5，Corollary 2.2及后文。\n"}, {"setting": "MaxSelect的d≥2或Quantile的U≥2；其他条件同Theorem 2.1。", "baseline": "§2转述的非私有低空间算法及私有多项式空间算法。", "metric_or_guarantee": "工作空间下界", "reported_values_and_units": "M≥tildeΩ(T^(γw+γk−2γh)) bits。", "information_and_compute": "strong fingerprinting带来额外log²(n)损失，n=3h+k；不提供实测运行成本。", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.5，Theorem 2.3；p.13，A.4。\n"}]

prior_work_candidates：[{"citation_as_printed": "Cummings, R., Epasto, A., Mao, J., Mukherjee, T., Ou, T., and Zhong, P. Differentially private space-efficient algorithms for counting distinct elements in the turnstile model. In ICML, 2025.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "CountDistinct、occurrency promise与重用户处理", "claimed_difference": "前作提供上界；本作试图证明特定区域的空间开销不可避免。", "basis": "target_paper_only", "target_locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，pp.4—5，§2.1—2.2；p.9，References", "prior_actually_read": false}, {"citation_as_printed": "Dinur, I., Stemmer, U., Woodruff, D. P., and Zhou, S. On differential privacy and adaptive data analysis with bounded space. In EUROCRYPT, pp. 35–65, 2023.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "隐私与非隐私流算法的空间分离", "claimed_difference": "从依赖密码假设的特制任务转向自然任务的信息论下界；未声称继承前作构造。", "basis": "target_paper_only", "target_locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，pp.1—2，§1；p.9，References", "prior_actually_read": false}, {"citation_as_printed": "Bun, M., Ullman, J. R., and Vadhan, S. P. Fingerprinting codes and the price of approximate differential privacy. SIAM J. Comput., 47(5):1888–1938, 2018.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "fingerprinting lemma", "claimed_difference": "前作工具连接准确性与输入相关性；本作另以通信博弈将其转为空间下界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.8，Lemma 3.4；p.9，References", "prior_actually_read": false}]

assessment：{"ai_verdict": "L3", "confidence": "medium", "reason": "中心增量是可迁移的通信博弈与DP归约框架，而不只是单任务常数改进，暂列框架级候选；不确认历史首创或全部证明正确。", "central_increment": "前作已有私有上界及条件性空间分离；本作在用户级、连续发布和occurrency条件下新增无条件空间下界框架，证据为主定理与两类扩展，尚待排除关键证明步骤的问题。", "soundness_observation": "正文与附录给出完整论证路线，但可见Lemma 3.4常数与简单核算冲突，A.5的随机映射熵步骤也需修正；不能将定理陈述当成本轮独立验证。", "significance_observation": "若成立，可解释自然统计任务中隐私带来的内存代价；不提供新的实用算法或部署性能证据。", "main_open_question": "Lemma 3.4的可见常数是否源于提取错误；若原版一致，修正后能否保留核心归约与空间下界？"}

limitations：[{"text": "一般occurrency参数下的空间—误差关系未必紧；固定ε、δ，未研究其完整依赖。", "basis": "author_report", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.5，§2.2及脚注4"}, {"text": "按可见Lemma 3.4，误差≤2/5应推出相关期望≥1/10；但线性估计器可给出1/30。须先核对原PDF，不据此直接否定整篇主定理。", "basis": "model_inference", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.8，Lemma 3.4、式(3)。\n"}, {"text": "A.5对随机B=f(m)使用H(B)≤H(m)，一般不成立；可能改用互信息的数据处理不等式修复，未完成修补验证。", "basis": "model_inference", "locator": "TEXT_OR_JiB2eXY8fT_4f3fe3ce983d，p.12，Proof of Lemma A.5。\n"}]

minimal_check：{"question": "核对Lemma 3.4的原版常数及其对后续证明的影响。", "control": "取f(x)=2/5+(1/5)mean(x)，保持文中p均匀取自[0,1]、x服从Ber(p)^n的设置。", "observable_outcome": "模型直接核算：逐输入误差≤2/5，但E[f(x)Σ(x_i−p)]=1/30，小于可见式所述1/10。", "resources": "原PDF公式与纸笔或符号积分；不需要训练或GPU，人工核读用时未知。", "failure_or_stop_condition": "原版公式不同则撤回文本层反例；若一致，则须修正引理及下游证明后才能确认保证。"}

missing_fields：["未提供原PDF图像，关键公式与常数未完成原版核对。", "前作全文及所列三篇前作的DOI或arXiv标识未提供。", "无实验、训练预算或硬件实测；本文为理论下界研究。", "附件版本角色未经确认，不能认定为最终出版版。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

从DP输出相关性到多人通信再到自然流任务空间的接口值得关注，L3仍为框架候选；在引用具体下界前必须先修复fingerprinting引理及下游调用。

身份及隐私/准确性范围：13页官方当前附件与输入返回绑定一致。研究用户级DP下连续发布的整个T步输出，邻接流删除同一用户全部更新并以空更新替代；不同于单事件隐私或只发布最后结果。CountDistinct可限制当前频率0/1，promise最多k名用户超过w次更新；要求对每个固定流，所有时刻同时以至少1−T^-2概率满足乘性.1及加性h误差。

核查定位：text_delivery_manifest.json, structured/pro060.json, p003–p004, §2, PDF physical page 5, Theorem2.1；source_and_privacy_model_confirmed

中心框架和下界参数：共享重用户C与阶段独有轻用户S_i构造流，相关分数随机舍入为集合，M位算法状态成为相邻玩家消息；只限制消息长度，不限制玩家的内部运算资源。原定理给tildeΩ(kw/h²) bits，前提γw/2<=γk<=γh<γw及3γh<1。Cor2.2的1/3−4α要正需α<1/12，接近1/3需充分小α，不能将整个(0,1/9)区间都称正多项式下界。

核查定位：PDF physical page 5, Theorem2.1 and Corollary2.2, p006–p007, AvoidHeavyHitters and reduction；claimed_bound_and_resource_model_located

fingerprinting常数及更强反例：原PDF第8页确认Lemma3.4的前提是逐输入误差<=2/5、p在[0,1]均匀，结论相关期望>=1/10。f=.4+.2mean(x)给1/30，已与常数冲突。进一步取n=5，按1的数量k=0..5令f=(.4,.6,.8,.2,.4,.6)，仍逐输入误差2/5且值在[0,1]，精确积分为−1/210。因此所印条件甚至不保证普遍正下界，不能仅将1/10换成更小正常数修复。该例针对引理，不是流空间下界本身的反例；其归约必须补有效前提或另一引理。

核查定位：PDF physical page 8, Lemma3.4 and Eq3, local_check/fingerprinting_checks.json；literal_fingerprinting_lemma_refuted

随机映射熵的局部修补：原PDF第12页明确允许B=f(m)随机，却用H(B)<=H(m)。额外随机性可增大H(B)，该步不成立。给定原Markov链，可改为I(A;B)<=I(A;m)<=M，并用H(A|B)<=H(C|B)恢复M+H(C|B)>=H(A)。I=|A∩B|的安全熵界为log(k+1)。另存修补，仅处理编码中间步骤，不消除fingerprinting问题。

核查定位：PDF physical page 12, LemmaA.5 proof, local_check/entropy_step_repair.md；local_entropy_error_and_conditional_repair_confirmed

扩展及新颖性边界：第13页MaxSelect与Quantile扩展使用不同先验的strong fingerprinting和二元构造，额外log²损失由tilde记号吸收；不能因Lemma3.4局部错误直接宣布所有分支均被反证。中心游戏提供框架级候选价值，但前作上界、历史首次无条件分离及完整归约未独立核验。本篇无实验或部署成本报告，意义是信息论工作空间限制。

核查定位：p013, A.4, p004–p005, prior upper-bound discussion；extensions_and_novelty_kept_provisional

本地补充/限定：["原PDF排除了2/5及1/10仅由文本抽取导致的可能；新增负相关有限例，说明需要修复引理条件或归约而非仅调常数。", "给出A.5互信息修补及log(k+1)修正，保留其同阶编码思路，不混同两个独立证明问题。"]

核查局限：["未运行流算法、模拟实验或核读被引用fingerprinting/通信前作；本地仅精确有限积分和信息论中间式。", "未完整验证所有概率集中、常数和跨任务归约，也未证明主空间下界错误。", "L3是Pro暂评，历史首创及完整证明正确性未认证。", "Pro只读全文文本，本地观察三页PDF。"]

