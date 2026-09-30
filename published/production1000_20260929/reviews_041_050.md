# 单轮全文初评与有界本地核对 41–50

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro041 · IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation

论文 OR_z0m3EhzhOH；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5", "source_url": "https://api2.openreview.net/pdf?id=z0m3EhzhOH\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_z0m3EhzhOH_d65ae3a018e5：物理页1–14全部已提供文本，页标连续；正文及实验p1–8，参考文献等p9–10，附录A证明p11–13，附录B实验设置p13–14。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未见PDF图像；图1–3仅有提取文字，不能读取曲线精确数值。", "双栏交错，算法及公式的转置、上下标和指数排版受损；主要实验表格数值可辨。", "未提供前作全文或代码；未搜索、未复现实验，未将附件认定为最终出版版。"]}

问题：能否利用线性层梯度G=(∇YL)Xᵀ的生成结构，减少Adam状态与梯度存储，同时保持训练效果？

方法：分别累计输入平方与输出梯度平方的EMA，置于轮换更新的b列缓冲，以匹配列的外积和构造二阶预条件统计；将梯度矩阵乘法融合进动量更新以免单独保存G。LLM实验仍保存全尺寸一阶矩M，未采用可选的一阶缓冲。另探索满足1/p+1/q=1的Hölder指数调整。

作者主张：不再分解已生成的权重梯度，而是跟踪其输入和输出梯度因子，实现内存高效自适应优化。

论文证据：给出算法、缓冲机制及多任务结果；二阶持久状态由mn降为b(m+n)，但LLM的一阶状态仍为mn。

模型推断：是明确的统计替代与实现设计增量，不能将二阶状态复杂度当成整个优化器或峰值显存复杂度。

定位：['TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p2表1，p3算法2，p4§3.2–3.3，p6§4.1。']

作者主张：IO-Adam二阶矩上界于Adam，并具有同阶O(√T)累计regret。

论文证据：式(15)给出单批平方梯度的Cauchy上界；命题3.1及附录A尝试推广至优化过程。

模型推断：单批不等式不能直接推广为分开EMA后的矩上界；现有证明也未完整落实实际算法所需条件。

定位：['TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p5§3.4.1–3.4.2，p11–13附录A。\n']

key_results：[{"setting": "RoBERTa-Base微调GLUE。", "baseline": "AdamW、Adafactor、Galore。", "metric_or_guarantee": "任务分数；仅CoLA测量峰值allocated memory。", "reported_values_and_units": "IO/AdamW：CoLA为61.59/62.82，SST2为94.04/92.09；显存分别1599.61/2409.89 MB。Adafactor为1133.41 MB，Galore为1768.14 MB。", "information_and_compute": "30 epochs，学习率3e−5，线性调度；batch=16，IO缓冲/Galore rank均为16。表内未逐任务注明分数指标名称。", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p6表2、§4.1，p13§B.1。\n"}, {"setting": "LLaMA-60M/130M/1B在C4预训练。", "baseline": "AdamW、Galore、AdamSNSM；部分值转引前作。", "metric_or_guarantee": "最终评测perplexity，越低越好。", "reported_values_and_units": "IO为29.75/22.40/14.36；AdamW为29.62/22.61/14.51。AdamSNSM的1B结果14.05带星号，属前作转引。", "information_and_compute": "缓冲分别128/256/1024；IO的60M/130M搜索五个学习率，1B因成本固定为0.002，不能视为各规模等预算调参。", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p7表3、§4.2。\n"}, {"setting": "附录所列ViT配置在CIFAR10训练50 epochs。", "baseline": "AdamW及IO不同缓冲大小。", "metric_or_guarantee": "评测准确率、allocated memory。", "reported_values_and_units": "IO b=16：77.63%、68.40 MB；b=1：75.46%、65.47 MB；AdamW：76.06%、112.02 MB。", "information_and_compute": "IO/AdamW学习率为1e−3/5e−4；未报告多随机种子误差。缓冲增大并非每个相邻配置都单调提高准确率。", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p7表4，p14§B.3。\n"}, {"setting": "GPT-2在WikiText-2微调。", "baseline": "AdamW、Adafactor。", "metric_or_guarantee": "Perplexity。", "reported_values_and_units": "IO为22.36，AdamW为22.63，Adafactor为22.72。", "information_and_compute": "IO缓冲为1；主文学习率分别为5e−4、5e−4、5e−5；将GPT-2的等价一维卷积模块改成线性模块。图3仅能记录作者文字称p≈1.8最优，不能读取逐点数值。", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p8表5、§4.4。\n"}, {"setting": "LLaMA-60M在C4上的单步耗时。", "baseline": "AdamW。", "metric_or_guarantee": "平均每步秒数。", "reported_values_and_units": "IO为0.3010 s，AdamW为0.2817 s；作者称约增加7%耗时。", "information_and_compute": "L20Z GPU，batch=64，梯度累积8批；不代表完整训练或调参总成本。以上均为作者报告，非本地复现实测。", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p8表6、§4.5。\n"}]

prior_work_candidates：[{"citation_as_printed": "Shazeer, N. and Stern, M. Adafactor: Adaptive learning rates with sublinear memory cost. In International Conference on Machine Learning, pp. 4596–4604. PMLR, 2018.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "因子化二阶状态。", "claimed_difference": "Adafactor累计平方权重梯度的行列和；本文直接累计输入和输出梯度的统计。", "basis": "target_paper_only", "target_locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p3–4§3.2，p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Zhao, J., Zhang, Z., Chen, B., Wang, Z., Anandkumar, A., and Tian, Y. Galore: Memory-efficient llm training by gradient low-rank projection. arXiv preprint arXiv:2403.03507, 2024.", "identifier_if_present": "arXiv:2403.03507", "relation_candidate": "比较基线", "shared_component": "降低优化器状态存储。", "claimed_difference": "Galore对权重梯度做子空间投影；本文利用梯度生成因子，不依赖该SVD投影步骤。", "basis": "target_paper_only", "target_locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p2§2及表1，p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Lv, K., Yan, H., Guo, Q., Lv, H., and Qiu, X. Adalomo: Low-memory optimization with adaptive learning rate. arXiv preprint arXiv:2310.10195, 2023.", "identifier_if_present": "arXiv:2310.10195", "relation_candidate": "方法继承", "shared_component": "融合反向计算与更新以减少梯度驻留的思路。", "claimed_difference": "本文将类似融合用于一阶矩更新，二阶统计则另从输入与输出梯度构造；不据此认定复用了前作代码。", "basis": "target_paper_only", "target_locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p4§3.3，p9参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心是现有自适应优化框架内有价值的统计替代、缓存及融合设计；实验支持内存与效果的折中，尚不足支持更强的新保证。", "central_increment": "前作已做行列或子空间状态压缩（本篇转述）；本作新增梯度生成因子的统计表示，支持证据为算法与跨任务结果；尚待排除融合更新和调参对优势的主导作用。", "soundness_observation": "式(15)的单批界不保证跨时间EMA后的界，见minimal_check。附录A承认单调性要求，但算法2未给出相应修正；梯度有界也不能直接推出分离因子统计有界。这些是保证的缺口，不等同于否定经验效果。\n", "significance_observation": "对显存受限训练有实际意义，但仍保存密集动量，且当前hook实现存在时间开销；不能宣称统一优于所有基线。", "main_open_question": "能否针对实际缓存与偏置修正算法，在明确因子界及单调性条件下建立有效regret保证？"}

limitations：[{"text": "主要适配线性层，其他模块可能需要修改；当前PyTorch hook实现引入额外耗时。", "basis": "author_report", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p8§4.5、§5。"}, {"text": "未报告多种子方差；C4混用本次实验与前作数值，1B未等预算搜索；相同rank与buffer不等于相同总状态内存。", "basis": "model_inference", "locator": "TEXT_OR_z0m3EhzhOH_d65ae3a018e5，p6–8表2–6及§4.1–4.4。"}]

minimal_check：{"question": "按式(3)–(4)及算法2，偏置修正后二阶矩是否总不小于Adam？", "control": "标量情形bs=b=1，零初始化，相同β2∈(0,1)；两步的输入/输出梯度依次为(0,0)、(1,1)。", "observable_outcome": "按可读公式手算，第二步IO的v̂=1/(1+β2)²，而Adam为1/(1+β2)，前者严格更小，否定无条件上界。", "resources": "仅需标量手算或短脚本，无需数据集或GPU；本轮未运行代码。", "failure_or_stop_condition": "出现上述严格小于即使上界主张失败，但不直接否定regret结论；若PDF或实现公式与提取文本不同，应先核对版本再归因。"}

missing_fields：["Adafactor参考文献未列独立标识符。", "图2、图3逐点数据及受损公式的可靠排版。", "完整训练硬件与精度、C4总训练预算、调参总成本、多种子统计及完整显存口径。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

输入/输出梯度统计与融合更新有实现价值；继续阅读应围绕实际算法的稳定性条件、因子界、同口径峰值显存和计算预算，而非直接沿用理论上界解释。

身份、版本和阅读范围：题名、14 页官方当前附件、全文哈希和 Pro 返回绑定一致。Pro 初评覆盖全部所供文本；本地核看所列方法、理论和结果页，并观察原 PDF 第 3、6、11 页。没有运行作者代码。

核查定位：text_delivery_manifest.json, structured/pro041.json, p003:L0001；verified_with_scope_limit

中心存储设计与实际持久状态：算法2从输入激活和输出梯度的平方 EMA 构造二阶统计，并把权重梯度生成融合进一阶动量更新。LLM 实验明确保留全尺寸一阶矩 M，没有采用可选的一阶缓冲。二阶状态 b(m+n) 只有在小于 mn 时省存，不能把这个复杂度当整个优化器或训练峰值显存；同 rank 与 buffer 数值也不代表同总状态。

核查定位：PDF physical page 3, Algorithm 2, p004:L0012-L0061, PDF physical page 6, §4.1；mechanism_and_memory_scope_confirmed

二阶矩上界主张的标量核查：原 PDF 算法2确用 (1−β2^t)^2 作二阶偏置修正。取 batch=buffer=1、零初始化，两步输入/输出梯度为(0,0)、(1,1)，则第二步 IO 的修正矩为1/(1+β2)^2，Adam为1/(1+β2)，对0<β2<1前者严格更小。故单批 Cauchy 界不能推出分开 EMA 后的无条件矩上界。附录式22使用平方时间权重的另一较弱下界，本反例没有否定该式，也不单独否定 regret 命题。

核查定位：PDF physical page 3, Algorithms 1–2 and equations 3–4, p005:L0003-L0026, PDF physical page 11, equation 22, local_check/ema_upper_bound_check.json；unconditional_EMA_ordering_counterexample_confirmed

regret 条件的实际覆盖：附录 A 要求在线凸损失、有界梯度和迭代直径、衰减步长及动量，并在第13页承认二阶统计需单调且方法可另行修改；算法2未给出保证该单调性的修正。仅权重梯度乘积有界，也不自动给出分开因子统计的统一界。因此目前不能把所写 O(sqrt(T)) 直接当实际默认算法的已核定保证；其余证明未穷尽核查。

核查定位：p005:L0017-L0063, p011:L0017-L0031, p012:L0014-L0019, p013:L0019-L0029；proof_conditions_and_algorithm_gap_retained

决定性内存、效果和时间数字：原 PDF 第6页表2确认 CoLA测得峰值allocated memory：IO1599.61MB、AdamW2409.89MB、Adafactor1133.41MB；IO的CoLA61.59低于AdamW62.82，SST2则94.04高于92.09，不是全面优胜。C4表3含星号前作转引且1B未做相同学习率搜索。表6报告 IO0.3010秒/步对AdamW0.2817，约7%更慢，硬件为L20Z、batch64累积8批；不能把省存说成端到端加速。

核查定位：PDF physical page 6, Table 2, p007:L0003-L0011, p007:L0058-L0075, p008:L0003-L0013, p008:L0023-L0039；performance_and_cost_tradeoff_confirmed

本地补充/限定：["按原 PDF 的真实偏置修正保存二阶矩反例；额外说明它不否定附录式22的平方权重下界，避免把不同陈述混为一谈。", "保留内存节省的实际证据，同时记录密集一阶矩、Adafactor更低内存及IO每步更慢的条件。"]

核查局限：["未运行优化器、神经网络训练、内存测试或新研究实验；只做源文标量代数。", "未完整验证 regret 证明、矩阵转置实现或可选 Hölder 修改。", "没有核读前作或复算多种子显著性；L1 为 AI 暂评。", "Pro 只看文本，本地只观察三个 PDF 页面。"]


## pro042 · FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU

论文 OR_VzIA4MASxK；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_VzIA4MASxK_6aa320d7288a", "source_url": "https://api2.openreview.net/pdf?id=VzIA4MASxK\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "6aa320d7288a56ef76731d09fa1e01c728b0d4fc9a651ec9d6ca1274a10f2933", "physical_pages": 36}], "read_ranges": ["TEXT_OR_VzIA4MASxK_6aa320d7288a：物理页1—36全部提供文本，包括正文§1—6、参考文献、附录A—H；页标连续，未见文本缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—8仅有图题及部分轴字，未据此推取不可见曲线数值。", "双栏文字交错，部分公式括号、上下标和矩阵排版失真；表格按可辨行列读取，未核对原始版面。", "版本出版身份未核验；未搜索、核读前作、执行代码或复现实验。"]}

问题：如何在不保存成对代价或传输矩阵的条件下，加速大规模平方欧氏EOT及其一、二阶导数计算？

方法：输入点云、正权重、ε及所需扰动；将点范数吸收入对偶势，把Sinkhorn半步写成带动态偏置的点积LSE。Triton内核按行驻留并流式归约，输出对偶势、损失及传输应用；再以PV、PᵀU和Hadamard加权传输组成Schur-CG HVP。方法本身不需训练。

作者主张：双边EOT的稳定化Sinkhorn半步可精确改写为attention式带偏置点积LSE。

论文证据：命题1及附录D.1给出范数平移后的代数等价，算法1/3据此融合点积、偏置和规约。

模型推断：这是有用的局部映射；online LSE及行驻留循环并非本篇首创，附录G.2明确承认与FlashAttention-2一致。

定位：['TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页3，命题1；物理页17—19，附录D；物理页24，G.2。']

作者主张：以线性工作显存完成EOT求解、传输应用和HVP，并显著加速前向及反向计算。

论文证据：定理2给出半步IO为Θ(nd+md+nmd²/M)；命题3和定理5给出传输/HVP的流式分解，HVP工作显存O((n+m)d)，算术O((K_CG+1)nmd)。

模型推断：中心增量是完整流式算子系统及可运行规模，而非新OT目标、收敛机制或首次线性存储。

定位：['TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页3—6，定理2、命题3、定理5；物理页18、21—25，附录D.2、F—G。']

作者主张：使大规模OTDD及回归中的曲率监测更实用。

论文证据：MNIST↔Fashion-MNIST的512维ResNet18特征上，作者报告n=60000显存低于1GB；40000×5细胞特征的合成打乱回归中，72次初始化有71次逃离鞍区，随后Newton中位11步收敛。

模型推断：支持应用可用性，但不是学习准确率提升或全局收敛保证。

定位：['TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页8，§4.2；物理页31—36，H.3—H.4。']

key_results：[{"setting": "均匀点云、均匀边缘，ε=0.1，固定10次Sinkhorn迭代，TF32；与GeomLoss匹配对称调度。", "baseline": "GeomLoss 0.2.6 / PyKeOps 2.3在线后端", "metric_or_guarantee": "基线时间除以FlashSinkhorn时间", "reported_values_and_units": "n=m=10000,d=512：前向32.0×、前向+反向161.4×。附表另报n=m=5000,d=512前向46.6×，n=m=10000,d=1024前向+反向212.3×，不能合并成同一设置。", "information_and_compute": "作者报告；A100-80GB，预热10次；前向50次、前反30次取均值，排除JIT预热。", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页24、26，H.2；物理页28—29，表8—9。\n \n"}, {"setting": "同类合成点云，ε=0.1、10次迭代、TF32；Flash使用交替调度。", "baseline": "OTT-JAX 0.5.1 / JAX 0.8.2在线实现", "metric_or_guarantee": "前向加速比", "reported_values_and_units": "n=m=50000,d=32为5.1×；n=m=5000,d=1024仅0.6×，即该设置Flash更慢。", "information_and_compute": "作者报告；A100-80GB，50次均值；JAX采用同步wall-clock，PyTorch采用CUDA events。", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页24，H.2；物理页30，表12。\n"}, {"setting": "HVP：n=m=50000,d=64，ε=0.1；100次Sinkhorn、固定50次CG、τ=10^-5、严格FP32。", "baseline": "采用同一矩阵无关Schur-CG结构的KeOps后端", "metric_or_guarantee": "HVP时间及Flash峰值显存", "reported_values_and_units": "Flash 4.2秒，KeOps 14.5秒；Flash峰值显存219MB。", "information_and_compute": "作者报告；A100-80GB；CG不早停，此计时不附该规模的最终残差。", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页7，§4.1；物理页24，H.2；物理页29，H.2.3。\n \n"}, {"setting": "小规模HVP一致性：n=m=512,d=4，ε=0.01，τ=10^-5，CG相对残差容限η=10^-6。", "baseline": "密集Moore–Penrose伪逆参考", "metric_or_guarantee": "HVP相对误差、CG次数", "reported_values_and_units": "相对误差8.54×10^-3，即0.854%；195次CG，作者标记收敛。", "information_and_compute": "独立的小规模精度测试，不是上一项固定50次CG性能测试的精度证明。", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页36，表22。\n"}]

prior_work_candidates：[{"citation_as_printed": "Dao, T., Fu, D., Ermon, S., Rudra, A., and Ré, C. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In Advances in Neural Information Processing Systems, volume 35, pp. 16344–16359, 2022.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "分块、online softmax/LSE及IO分析", "claimed_difference": "用于迭代更新双边EOT对偶势，并扩展传输及导数算子。", "basis": "target_paper_only", "target_locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页3、10、24，§3.1、参考文献、G.2。", "prior_actually_read": false}, {"citation_as_printed": "Charlier, B., Feydy, J., Glaunes, J. A., Collin, F.-D., and Durif, G. Kernel operations on the GPU, with autodiff, without memory overflows. Journal of Machine Learning Research, 22(74):1–6, 2021.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "不物化成对矩阵的在线GPU规约", "claimed_difference": "由通用map-reduce改为EOT专用点积融合与张量核计算。", "basis": "target_paper_only", "target_locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页6、10、26—28。", "prior_actually_read": false}, {"citation_as_printed": "Li, X., Lu, F., Tao, M., and Ye, F. X.-F. Robust first- and second-order differentiation for regularized optimal transport. SIAM Journal on Scientific Computing, 47(3):C630–C654, 2025b.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "EOT Hessian分解及敏感度矩阵", "claimed_difference": "通过Schur-CG与流式传输应用计算HVP，不显式存储耦合和数据Hessian。", "basis": "target_paper_only", "target_locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页2、8、11、21—23。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "代数映射本身偏L1，但求解、传输及二阶算子的完整流式实现与规模扩展构成实质系统能力；不足以判路线级L3。", "central_increment": "前作已有在线EOT、IO-aware attention和Hessian分解（仅本篇转述）；本作在结构化代价下新增专用融合算子系统，支持证据为复杂度推导、计时和应用实验；尚待排除不等精度及实现配置造成的优势放大。", "soundness_observation": "核心等价式及传输恒等式可追读，但未逐一定理复证。早停导数针对固定诱导边缘，阻尼HVP亦为近似，不能笼统称原目标的精确导数。", "significance_observation": "价值集中于反复大规模求解和二阶应用；没有降低成对运算的算术阶数，也并非所有尺寸都更快。", "main_open_question": "统一初值、调度、精度和计时边界后，尤其大规模HVP，端到端优势能保留多少？"}

limitations：[{"text": "当前代价支持限于点积可分解结构及指定标签查表扩展；raw Euclidean和learned neural costs列为未来工作。", "basis": "author_report", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页4，§3.1。"}, {"text": "固定10步不等于同求解精度：作者报告不同初始势使Flash与JAX损失相差约2%。大规模HVP固定50次CG，不能直接继承512点精度实验的误差结论。", "basis": "model_inference", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页24、26、31、36，H.2及表22。"}, {"text": "NCU前向测试的约5MB工作集驻留40MB L2；其HBM计数不能直接外推到非缓存规模，也未独立消融融合、张量核和循环顺序的收益。", "basis": "model_inference", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页27，表5—6。"}, {"text": "OTDD排除标签矩阵预计算，20000点亦是库的硬编码GPU限额。H.1称A100-80GB，表24却称40GB，不能统一归因于80GB设备显存耗尽。", "basis": "model_inference", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页24，H.1；物理页33，H.3；物理页36，表24。"}, {"text": "报告存在未解释差异：n=10000,d=512对JAX前反加速在表3为1.2×、表13为1.8×；HVP重复次数H.2写20次，表15—16写50次。", "basis": "model_inference", "locator": "TEXT_OR_VzIA4MASxK_6aa320d7288a，物理页7、24、31—33，表3、13、15—16。"}]

minimal_check：{"question": "代表性大尺寸的前反收益是否在等精度下成立？", "control": "固定n=m=10000,d=512,ε=0.1；Flash交替版与OTT-JAX使用相同初始势、严格FP32、共同边缘L1误差≤10^-5门槛，并以同一高精度参考核对损失和梯度，统一计时边界。", "observable_outcome": "达标后的前向+反向时间、梯度误差和峰值显存。", "resources": "一张A100-80GB、作者代码及固定版本基线；运行耗时未知。", "failure_or_stop_condition": "未达到共同精度则不报告等价加速比；达标后无提速则该设置的性能优势不成立。"}

missing_fields：["PDF图像、前作全文及三条候选文献的独立DOI/arXiv标识未提供。", "缺少原始计时日志、完整误差日志及可核验代码提交标识。", "表21具体收敛判据、大规模HVP最终残差、总GPU时与编译/调优成本未报告。", "OTDD设备容量和部分主附表数值差异未能由材料消解。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

流式一二阶 EOT 算子提供实际系统能力；后续最有价值的是同初值、同停止误差和统一计时边界下的规模验证及近似HVP误差。

身份、版本与范围：题名、36 页官方当前附件、全文文本哈希和 Pro 返回绑定一致。Pro 一轮初评覆盖全部所供文本；本地检查列出的算子、条件和计时页，并观察原 PDF 第 24、29、36 页。没有运行 GPU 实验或作者代码。

核查定位：text_delivery_manifest.json, structured/pro042.json, p003:L0001；verified_with_scope_limit

中心系统机制及复杂度范围：把平方欧氏的逐点范数移入势后，半步变成含动态偏置的点积 LSE，流式融合避免保存 n*m 矩阵。IO 界 Θ(nd+md+nmd²/M) 指双层内存模型及 d≤M≤min(n,m)d；HVP 保持 O((n+m)d) 工作内存，但算术仍为 O((KCG+1)nmd)。已有 KeOps 在线基线也有线性存储，新增价值是专用算子融合和导数系统，不是首次线性空间或减少成对算术阶数。代价支持有明确点积结构限制。

核查定位：p003:L0023-L0056, p004:L0014-L0029, p005:L0039-L0053, p023:L0003-L0020, p024:L0024-L0037, p026:L0003-L0023；system_increment_and_complexity_scope_confirmed

早停、导数和阻尼：传输应用对当前势所诱导的 P 精确，只有 Sinkhorn 收敛时才等于目标边缘的 P*。实现明确用诱导边缘构造梯度/HVP；有限步结果不能笼统称原目标的精确导数。实际 Schur-CG 加 τI 且容限有限，计算的是正则化近似 HVP；τ和残差趋零的理想陈述不等于实测默认配置。

核查定位：p004:L0039-L0050, p005:L0003-L0042, p006:L0003-L0024, p023:L0038-L0057；derivative_target_and_approximation_confirmed

决定性速度与不占优设置：表8报 n=m=10000,d=512 的前向相对 KeOps 32.0倍；原 PDF 第29页表9同尺寸前向+反向161.4倍，d=1024另为212.3倍，不能拼作同一设置。表12在50000,d=32为5.1倍，但5000,d=1024仅0.6倍；表10也有 Tensorized 更快情形。固定10步、TF32、预热排除和不同框架计时边界均有明确记录；文中承认 Flash/JAX 在10步时损失约差2%，所以不是已统一收敛精度的速度比较。

核查定位：p028:L0032-L0042, PDF physical page 29, Tables 9–10, p030:L0013-L0022, PDF physical page 24, H.2, p026:L0025-L0040；reported_speedups_confirmed_precision_scope_qualified

大规模 HVP 与小规模精度不可混用：作者报50000点、d=64时HVP 4.2秒对14.5秒、Flash峰值219MB；性能配置是100次Sinkhorn和固定50次CG、无早停。原 PDF 第36页表22的0.854%相对误差却是512点、d=4、ε=0.01、τ=1e-5、残差容限1e-6，实际195次CG。这不能作为50000点固定50次CG的误差认证。H.2称HVP计时20次，表16又写50次，重复次数仍有文内差异。

核查定位：p007:L0048-L0057, PDF physical page 24, H.2, p029:L0040-L0062, PDF physical page 36, Table 22, p033:L0003-L0013；scale_accuracy_and_repetition_limits_confirmed

缓存与应用基线边界：NCU前向工作集约5MB、A100 L2约40MB，作者明确HBM数值来自L2驻留运行，不能直接外推超缓存规模。OTDD计时排除标签矩阵W预计算，而且库有GPU_LIMIT=20000并在以上回退CPU；表24却统称超过20000在40GB A100 OOM，而H.1写全部实验A100-80GB。保留设备和失败原因口径差异，不把全部基线停点归因于80GB显存不足。

核查定位：p027:L0003-L0064, p033:L0023-L0026, PDF physical page 24, H.1, PDF physical page 36, Table 24；measurement_boundary_and_source_ambiguity_confirmed

本地补充/限定：["核实主要速度表和低ε精度表，保留实际有利设置以及小规模/高维不占优设置。", "将早停导数、阻尼HVP、固定迭代性能与收敛精度分开；没有把小规模精度测试当大规模速度测试的验证。", "原文同时存在OTDD软件限额、40GB/80GB设备描述，不自行选择单一基线失败原因。"]

核查局限：["未运行Triton、GPU profiling、求解器或新的精度/速度实验；没有代码提交和原始日志。", "未完整复证全部定理或逐图核验曲线，未核读引用前作。", "未独立确认各基线库的当前功能；这里只记录本文采用版本和作者描述。", "Pro仅读全文文本，本地只观察三页 PDF；L2为AI暂评。"]


## pro043 · DISTFLOW: A Fully Distributed RL Framework for Scalable and Efficient LLM Post-Training

论文 OR_aPPEyZpKkp；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_aPPEyZpKkp_cb29b2beff23", "source_url": "https://api2.openreview.net/pdf?id=aPPEyZpKkp\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "8dd2dc2c9e898095c4d07fc589ed16f30b2e3e04f669d862ee73b9a5b3c3f2ec", "source_pdf_sha256": "cb29b2beff232517c97e2eefb1b21c06b9662ab324de5e920c0b593e56cef002"}], "read_ranges": ["TEXT_OR_aPPEyZpKkp_cb29b2beff23：物理页1—11全部所供文本，包括摘要、§1—8、Impact Statement、参考文献、附录A.1/B及表1；连续页标无缺号。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—12仅有提取文字，不能核读实际曲线、柱高或全部数据点。", "双栏文字有交错；算法1、公式(1)和表1主要内容可辨，但排版未获图像核验。所引实验数值来自正文或可辨表格，非复现实测。", "未提供前作全文、其他版本、代码或运行日志；未进行外部核读。"]}

问题：同置PPO/GRPO在推理与训练之间切换并行策略时，如何避免中央节点搬运中间张量成为吞吐与扩展瓶颈？

方法：输入工作流DAG、数据与并行配置。Planner按深度增添依赖，将DAG线性化；逐GPU Worker执行任务，控制面仅交换元数据。每GPU按DP分片加载，每节点DataBuffer收集TP rank 0输出；DP不变走本地缓存，变化时重分片。等基数LPT平衡序列长度；双缓冲用指针交换将内存回收移到后台，输出下一阶段数据及更新后的策略。

作者主张：提出完全分布式、多控制器RL框架，解耦控制与数据，最高获得2.63x吞吐并近线性扩展到512 GPU。

论文证据：提供具体数据通路、逐项累加消融及512 GPU范围的扩展实验；表1显示后端计算总时相近，而总步时明显缩短。

模型推断：中心增量是既有同置RL范式内的数据面重构，不是新RL目标。DAG中的模型阶段仍线性执行；双缓冲异步不等于异步策略训练。

定位：['TEXT_OR_aPPEyZpKkp_cb29b2beff23：p4—5 §5—6；p6—8 §7；p11表1。']

key_results：[{"setting": "GSM8K，单个GRPO step，32 GPU；每节点batch=512，每prompt 8个响应；input/output length=8192，沿用表题表述。", "baseline": "verl", "metric_or_guarantee": "逐阶段耗时，单位秒", "reported_values_and_units": "DistFlow/verl总时91.881/192.326 s，后端计算81.196/79.886 s；DistFlow put/get为10.405 s，verl dispatch为83.213 s。后两项属于不同操作列。", "information_and_compute": "该表未明确模型规模；是单步profiling，不是完整训练耗时。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p11，附录B、表1。 \n"}, {"setting": "Qwen-2.5-Instruct 7B/32B/72B，DeepScaleR-Preview，PPO/GRPO；依模型配置使用8—128 GPU；最大prompt/response长度2048/4096。", "baseline": "verl，双方使用vLLM与FSDP", "metric_or_guarantee": "全局batch token数除以迭代时间所得吞吐及其加速比", "reported_values_and_units": "正文报告PPO为1.09—1.64x、GRPO最高2.62x；摘要及结论写2.63x，未明确对应配置，保留差异。", "information_and_compute": "平台每节点8块Hopper GPU、NVLink、RoCE v2；PyTorch 2.6.0、CUDA 12.6、vLLM 0.8.5.post1、NCCL 2.21.5。PPO采用函数奖励，critic与actor同规模。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p6 §7.1、p7 §7.2；p1摘要、p8结论。 \n \n"}, {"setting": "Qwen-2.5-VL-Instruct，GRPO，MM-Eureka；图9文本横轴为7B：32—256 GPU，32B/72B：64—512 GPU。", "baseline": "各模型较小规模配置对应的理想线性扩展；作者称verl同类测试OOM。", "metric_or_guarantee": "Scaling Efficiency=(T2/T1)/(N2/N1)×100%", "reported_values_and_units": "正文分别报告7B、32B、72B为90.1%、93.9%、91.8%。", "information_and_compute": "全局batch随节点数同比增大，属于弱扩展，不能解释为固定batch的强扩展；效率计算端点未在正文逐项列明。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p7 §7.3、公式(1)；p8图9文本。 \n \n"}, {"setting": "7B LLM，GRPO，32 GPU；batch=1024/2048/4096的累加消融。", "baseline": "内部O1基线；分布式缓冲对照将4节点中的DataBuffer数量限制为1。", "metric_or_guarantee": "相对O1的吞吐加速比", "reported_values_and_units": "batch=2048：缓存1.38x，加双缓冲1.45x，全量1.70x；batch=4096：加负载均衡由1.38x升至1.58x，全量1.69x。", "information_and_compute": "按缓存、双缓冲、负载均衡、分布式缓冲顺序累加；未测完整组件交互。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p6 §7.1、p8 §7.4。 \n"}, {"setting": "32B模型、GRPO、32 GPU、DeepScaleR-Preview，训练20 epochs。", "baseline": "相同超参数的verl", "metric_or_guarantee": "训练reward/entropy及总执行时间", "reported_values_and_units": "作者称两条训练曲线接近，总时间减少21%；未给可独立核读的精确曲线值或测试准确率。", "information_and_compute": "绝对耗时、GPU小时和重复实验数量未报告。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p8 §7.5、p9图11。 \n"}, {"setting": "附录长上下文测试：7B的8k—64k及72B的32k上下文。", "baseline": "verl", "metric_or_guarantee": "吞吐加速比及任务能否完成", "reported_values_and_units": "7B由8k时1.48x增至64k时2.03x；72B/32k时verl OOM，DistFlow完成。", "information_and_compute": "本附录未说明GPU数、batch和所用RL算法，不能与主实验直接拼接比较。", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p11，附录A.1。 \n"}]

prior_work_candidates：[{"citation_as_printed": "Sheng, G., Zhang, C., Ye, Z., Wu, X., Zhang, W., Zhang, R., Peng, Y., Lin, H., and Wu, C. Hybridflow: A flexible and efficient rlhf framework. In Proceedings of the Twentieth European Conference on Computer Systems, EuroSys ’25, pp. 1279–1297. ACM, March 2025b. doi: 10.1145/3689031.3696075.", "identifier_if_present": "10.1145/3689031.3696075", "relation_candidate": "组件复用、比较基线", "shared_component": "同置执行、分层API及3DParallelWorker设计。", "claimed_difference": "本篇称verl仍集中处理数据，DistFlow将数据生命周期下放到分布式通路。", "basis": "target_paper_only", "target_locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p2、p4 §4、p10参考文献。 \n", "prior_actually_read": false}, {"citation_as_printed": "Zhong, Y., Zhang, Z., Wu, B., Liu, S., Chen, Y., Wan, C., Hu, H., Xia, L., Ming, R., Zhu, Y., et al. Optimizing RLHF training for large language models with stage fusion. In 22nd USENIX Symposium on Networked Systems Design and Implementation (NSDI 25), pp. 489–503, 2025b.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "同置RL系统及降低阶段空泡的优化目标。", "claimed_difference": "本篇转述RLHFuse以子任务融合改善执行；DistFlow重点处理控制与数据解耦，未直接比较二者。", "basis": "target_paper_only", "target_locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p3 §2、p10参考文献。 \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心证据支持明确的数据管理、吞吐和可运行规模改善；目前更像既有同置RL范式内的系统重构，尚不足以确认更高层次的新机制或独立能力增量。", "central_increment": "verl已支持同置执行与混合控制（本篇转述）；本作在异构并行切换下下放数据管理，表1支持通信成本降低；尚待排除基线配置及缓存优化差异。", "soundness_observation": "表1比不可见吞吐图更直接支持瓶颈诊断；但训练曲线接近不等于准确率等价，OOM也未定位具体内存域。", "significance_observation": "对大批量、长上下文同置RL有实际价值；跨后端集成具有工程工作量，但开发成本未量化。", "main_open_question": "匹配缓存、批量、并行布局和有效token口径后，分布式数据通路本身还保留多少收益？"}

limitations：[{"text": "作者指出batch=1024时负载均衡收益被调度成本抵消；Distributed Dataloader未纳入吞吐消融，理由是主要改善启动延迟及内存。", "basis": "author_report", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p8 §7.4。"}, {"text": "直接系统基线仅verl；排除异步框架不能证明它们必然损害收敛或正确性。扩展实验增大batch，收敛测试仅覆盖单一配置。", "basis": "model_inference", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p6 §7.1、p7 §7.3、p8 §7.5。"}, {"text": "短响应使用padding，但吞吐是否计入padding不明确；未报告完整并行划分、基线版本及重复实验误差，限制公平性核验。", "basis": "model_inference", "locator": "TEXT_OR_aPPEyZpKkp_cb29b2beff23：p6 §7.1、p8 §7.4。"}]

minimal_check：{"question": "分布式缓冲的独立收益能否复核？", "control": "复做O4→O5的1/4 DataBuffer对照；固定同一批rollout张量、缓存/LPT/双缓冲、后端及DP/TP布局。", "observable_outcome": "重分片耗时、后续训练吞吐、节点内存，以及样本和GRPO分组是否保持一致。", "resources": "沿用论文4节点×8 Hopper GPU配置；精确显存、带宽和运行耗时未知。", "failure_or_stop_condition": "样本或分组不一致则停止性能比较；匹配条件后增益消失，则不支持该组件的独立收益。"}

missing_fields：["GPU具体型号/显存、节点CPU/RAM、网络带宽、verl版本或提交号。", "主实验完整batch、采样与并行配置，重复次数/方差，绝对训练时间及GPU小时。", "图中完整数值、独立测试准确率、OOM内存域及2.63x对应配置。", "表1模型规模、附录A.1详细配置；第二前作未列标识符，前作全文均未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

对大批量和长上下文同置RL有工程价值；进一步阅读应固定样本、GRPO组、并行布局与有效token口径，确认分布式数据通路的独立收益。

身份、版本和范围：题名、11 页官方当前附件、全文文本哈希与 Pro 返回绑定一致。Pro 覆盖全部所供文本；本地核查列出的方法和评测页，并观察原 PDF 第 8、11 页。未运行分布式训练或下载框架代码。

核查定位：text_delivery_manifest.json, structured/pro043.json, p004:L0001；verified_with_scope_limit

中心系统改动与算法边界：重构的是同置 RL 的数据管理通路：每 GPU 执行线性化 DAG、每节点缓冲，DP一致时走本地缓存、变化时重分片。Planner明确给同深度节点添加顺序依赖，双缓冲异步回收内存不等于异步策略训练。约束 LPT 要求 N mod K=0并保持各 worker 样本数相等；没有从该启发式推出一般最优调度保证。

核查定位：p004:L0025-L0076, p005:L0003-L0034, p005:L0036-L0059；system_mechanism_and_execution_scope_confirmed

单步时间表对瓶颈的支持：原 PDF 第 11 页表1确认32 GPU、GSM8K单GRPO步：DistFlow/verl总时91.881/192.326秒，后端计算81.196/79.886秒。优势主要来自非计算时间，而不是后端计算本身加速。DistFlow的Put/Get10.405秒与verl的Dispatch83.213秒是不同操作列，不能直接称同一通信算子加速比。表未给模型规模，不把该单步结果替换为完整训练成本或最高2.63倍配置。

核查定位：PDF physical page 11, Table 1 and B；decisive_profile_numbers_confirmed

规模扩展与消融的真实比较范围：全局batch随节点数同比扩大，90.1/93.9/91.8%的效率是弱扩展。原 PDF 第8页图9显示7B为32–256 GPU，32B/72B为64–512，不能统称每个模型从32到512。图10确认2048 batch的缓存1.38、双缓冲1.45、完整1.70倍；4096时加负载均衡1.38→1.58、完整1.69倍。它们是顺序累加对照，DataLoader未纳入吞吐消融，不能据此分离所有组件交互。

核查定位：p007:L0029-L0067, PDF physical page 8, Figures 9–10 and §7.4；scaling_and_ablation_scope_confirmed

吞吐、收敛与正确性的区分：吞吐以全局batch token除以迭代时长，短输出有padding但计分是否含padding未明确。32B、32GPU、20epoch的reward/entropy接近与总时少21%仅覆盖该训练配置，未提供独立测试准确率等价检验。主文GRPO最高2.62倍、结论2.63倍的对应配置未说明；直接基线仅verl，未评测的异步系统不能据此一概判为损害正确性。

核查定位：p006:L0036-L0066, p007:L0029-L0035, PDF physical page 8, §7.5 and conclusion, PDF physical page 11, A.1；throughput_and_correctness_claims_qualified

本地补充/限定：["新增原图与时间表核查，确认数据路径收益及顺序累加消融；精确区分各模型扩展端点。", "不把双缓冲异步等同异步RL，不把弱扩展叫强扩展，也不把训练曲线接近当成独立准确率等价证明。"]

核查局限：["未执行训练、部署框架、基线调参或分布式对照实验。", "未定位OOM的具体内存域、基线版本、实际padding口径或完整重复实验误差。", "前作未独立核读；L1为当前AI暂评，不否认系统集成的实用工作量。", "Pro只看全文文本，本地仅观察两页原PDF。"]


## pro044 · Not All Prefills Are Equal: PPD Disaggregation for Multi-turn LLM Serving

论文 OR_RW23qIUb5f；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_RW23qIUb5f_95dc50719905", "source_url": "https://api2.openreview.net/pdf?id=RW23qIUb5f\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "01ab28fe488cb36ec0e785ec82354b9b9cd90c32eeb60647f151c8415caff999", "source_pdf_sha256": "95dc50719905b340bc1a85f70ccc8fca0a4b029b6cb1379c7d5ecd2b5dec278c"}], "read_ranges": [{"source_id": "TEXT_OR_RW23qIUb5f_95dc50719905", "physical_pages": "1–17，页标连续，无可见缺页", "sections": "全部已提供文本：正文§1–8、Impact Statement、参考文献、附录A–C.5，包括算法、表格及图注"}], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像，图1–11的曲线、散点及误差表现不可见；仅采用正文、表格或图注明示数值。", "双栏文本存在串行混杂，式(2)分式和表4部分分数排版有损；式(1)、算法1及主要表格数值可辨。", "版本角色未核定；未搜索、核读前作或复现实验，以下数值均为作者报告。"]}

问题：多轮LLM服务中，后续轮的Append-Prefill应返回P节点，还是在持有历史KV的D节点本地执行，才能平衡首token延迟、生成延迟和吞吐？

方法：离线按上下文长度、输入/预期输出比和QPS分格，测量x=0与x=1的相对TTFT收益及TPOT损失。给定P:D配置和权重，计算S=wttft·Δttft−wtpot·Δtpot；在线首轮走P，后续轮查最近格，S>0在原D做AP，否则走P→D。作者报告查表开销<1 ms，无新增模型训练。

作者主张：AP与full prefill的decode干扰存在数量级差异，使后续轮在D本地执行具有可行性。

论文证据：单prefill微基准报告48%对2%的TPOT退化；增加并发及上下文长度后仍有差距。

模型推断：为区分冷启动prefill和缓存命中AP提供了具体测量依据，但不能推成所有负载下都低干扰。

定位：['TEXT_OR_RW23qIUb5f_95dc50719905:p4/§4.1', 'TEXT_OR_RW23qIUb5f_95dc50719905:p14/§C.1']

作者主张：通过离线优化和动态AP路由提供可调TTFT–TPOT折衷，并改善多轮服务稳定性。

论文证据：算法1给出实现；表3中PPD取得最多TTFT和TPOT胜场，但作者同时说明其与固定x=1的端到端延迟基本重合。

模型推断：新增价值主要是选择缓存本地执行的运行点，而非首次实现AP→D或证明普适最优。

定位：['TEXT_OR_RW23qIUb5f_95dc50719905:p6–8/§5–6.5、表3', 'TEXT_OR_RW23qIUb5f_95dc50719905:p15–17/§C.5']

key_results：[{"setting": "单H100、Llama-3.1-8B、decode batch size=200；图2注明prefill处理1024 tokens", "baseline": "纯decode；分别加入full prefill或AP", "metric_or_guarantee": "TPOT相对退化", "reported_values_and_units": "单prefill：full约+48%，AP约+2%；4个并发prefill：约+57%与+21%。", "information_and_compute": "微基准；完整批处理、缓存长度及重复测量细节未列。", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p4/§4.1，p14/§C.1。\n"}, {"setting": "Llama-3.1-8B，两轮合成负载；低/中/高QPS分别为0.5–2、4–8、12–20", "baseline": "相同P:D配置下的x=0", "metric_or_guarantee": "Turn 2 TTFT相对下降", "reported_values_and_units": "固定x=1：1P_3D下降57.8%/65.2%/73.3%；3P_1D下降44.3%/38.1%/24.9%。这些是静态本地路由收益，不是动态PPD相对x=1的增益。", "information_and_compute": "4×H100 80GB、NVLink；整体扫描17配置×18负载×10个QPS=3060点，每点10秒Poisson到达；初始化及总GPU时未报。", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p5/§4.2–4.3、表1。\n"}, {"setting": "WildChat，3种P:D配置×9个QPS=27点，PPD权重w=(1,1)", "baseline": "PD x=0及Full AP-to-D x=1", "metric_or_guarantee": "逐指标胜场数及100%成功率测试点数", "reported_values_and_units": "按x=0/x=1/PPD顺序：TTFT胜场0/13/14，TPOT胜场10/5/12；达到100%成功率的点数为4/27、27/27、27/27。", "information_and_compute": "同预算4卡；附录以30秒超时定义失败。胜场数不代表平均提升幅度或显著性。", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8/表3，p15–17/§C.5。\n"}, {"setting": "WildChat 500对话，1P_3D，QPS=1；模拟有效带宽150→10 GB/s", "baseline": "PD x=0", "metric_or_guarantee": "Turn 2+ TTFT", "reported_values_and_units": "PD由143.7升至170.6 ms，PPD保持约51 ms；相对下降约64%→70%。", "information_and_compute": "在单节点接收路径注入延迟模拟慢网，非真实跨节点网络测量；数值取自图注及正文。", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8/§6.4，p9/图5，p13–14/§B.6。\n"}]

prior_work_candidates：[{"citation_as_printed": "He, W., Jiang, Y., Zhao, P., Xu, Q., Yoneki, E., Cui, B., and Fu, F. Efficient multi-round LLM inference over disaggregated serving, 2026.", "identifier_if_present": "arXiv:2602.14516", "relation_candidate": "同期独立工作", "shared_component": "AMPD同样将增量prefill路由到D以复用历史KV。", "claimed_difference": "本篇称AMPD采用实时队列状态及离线硬件规划，PPD侧重干扰测量、离线查表及单权重比控制。", "basis": "target_paper_only", "target_locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8–9/§7，p10/参考文献", "prior_actually_read": false}, {"citation_as_printed": "Zhong, Y., Liu, S., Chen, J., Hu, J., Zhu, Y., Liu, X., Jin, X., and Zhang, H. DistServe: Disaggregating prefill and decoding for goodput-optimized large language model serving. OSDI 24, pp. 193–210, 2024.", "identifier_if_present": "https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin\n", "relation_candidate": "方法继承", "shared_component": "P/D分池隔离prefill与decode。", "claimed_difference": "本篇允许后续轮AP选择性回到持有KV的D，而非总走P→D。", "basis": "target_paper_only", "target_locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p2–3/§2.2，p12/参考文献", "prior_actually_read": false}, {"citation_as_printed": "Gao, B., He, Z., Sharma, P., Kang, Q., Jevdjic, D., Deng, J., Yang, X., Yu, Z., and Zuo, P. Cost-Efficient large language model serving for multi-turn conversations with CachedAttention. USENIX ATC 24, pp. 111–126, 2024.", "identifier_if_present": "https://www.usenix.org/conference/atc24/presentation/gao-bin-cost\n", "relation_candidate": "背景引用", "shared_component": "复用多轮历史KV以减少重复计算。", "claimed_difference": "本篇将其描述为分层缓存路线，自身调整请求路由；未提供直接实验比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p3/§2.3，p10/参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "具有明确的多轮服务改进价值，但共享核心AP→D思路已有同期工作；可确认增量集中于干扰量化和离线加权路由，尚不足支持路线级新框架判断。", "central_increment": "前作已做PD隔离和历史KV复用，AMPD也探索AP→D（均据本篇转述）；本作新增离线性能表驱动的逐请求切换，证据为算法1及表3；待排除最佳静态策略和测量波动的解释。", "soundness_observation": "评分规则清楚，但离线两端点测量不等于混合流量下的全局最优保证；作者明确不保证硬SLO。未报告重复实验区间，微基准配平细节不足。", "significance_observation": "减少多轮重算与KV传输具有实际系统价值；工程复用程度高，但真实跨节点和缓存失效场景的收益尚不明确。", "main_open_question": "相对按同一SLO调优的最佳静态x，PPD在独立、非平稳流量中究竟有多大可重复增益？"}

limitations：[{"text": "离线表在硬件或负载分布漂移时可能次优；PPD只是路由执行器，硬SLO仍需闭环准入和批调度。", "basis": "author_report", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8/§6.5，p9/§7"}, {"text": "路由输入包含预期输出长度，但估计方法未交代；缓存驱逐、会话迁移和本地KV失效后的回退缺少评测。", "basis": "model_inference", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p13/§B.1–B.4"}, {"text": "对最强静态x=1主要报告胜场且端到端延迟近似相同，不能据此认定动态路由普遍占优；未直接比较AMPD或外部KV缓存方案。", "basis": "model_inference", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8/表3，p9/§7，p15–17/§C.5"}, {"text": "慢网实验仅注入传输延迟，不能完整模拟共享链路拥塞及跨节点调度，因此不足证明NVLink结果必然是实际部署收益下界。", "basis": "model_inference", "locator": "TEXT_OR_RW23qIUb5f_95dc50719905:p8/§6.4，p13–14/§B.6"}]

minimal_check：{"question": "动态查表相对x=1的增益是否可重复？", "control": "固定2P_2D，用未参与校准的WildChat流在QPS=8/16比较PPD和x=1，保持缓存配置及权重一致，不向路由器提供真实未来输出长度。", "observable_outcome": "重复测量预先固定的等权目标、TTFT/TPOT效应量、置信区间及超时率，而非只数胜场。", "resources": "4×H100 80GB、同版vLLM及PPD实现；所需GPU时长未知。", "failure_or_stop_condition": "若改善跨重复不稳定，或只能以更高超时率换取，则不支持动态部分的独立收益。"}

missing_fields：["完整逐点原始数据、重复次数及统计区间", "离线校准总成本、完整负载网格及输出长度估计方法", "vLLM具体版本、缓存失效回退和真实多节点测量", "前作全文及图像内容"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

多轮KV驻留与append-prefill干扰分析有工程价值；继续阅读应围绕非平稳独立流量下，相对同SLO调优的静态x=1，动态查表是否带来可重复的独立收益。

身份、版本和范围：17页官方当前附件、所供全文及返回的身份和哈希一致。Pro读完所供全部文本；本地核查列示页面并观察原PDF第8、14页。版本角色未进一步认定，前作未独立核读。

核查定位：text_delivery_manifest.json, structured/pro044.json；verified_with_scope_limit

路由规则及保证边界：离线按上下文长度、输入与预期输出比、QPS建表，以相对TTFT收益减加权TPOT损失决定后续轮去D或P；首轮固定去P。最近格查表不是在线队列优化证明。作者明确其为路由执行器，不保证端到端硬SLO；预期输出长度估计以及KV失效回退评测不足。

核查定位：PDF physical pages 4 and 6, Eq.1 and Algorithm 1, p008, §6.5, p013:L0042-L0062；central_mechanism_and_conditions_confirmed

固定本地路由与动态收益分开：表1的1P_3D TTFT下降57.8/65.2/73.3%是静态x=1相对x=0。原PDF第8页表3确认27点中TTFT胜场x=0/x=1/PPD为0/13/14，TPOT为10/5/12；100%成功率点数为4/27、27/27、27/27。它们是胜场数量而非效应量或显著性。附录C.5明确x=1与PPD端到端曲线几乎重合，不能把相对较弱x=0的整体收益归于动态决策独立贡献。

核查定位：PDF physical page 5, Table 1, PDF physical page 8, Table 3, p015:L0023-L0055, p017:L0007-L0011；decisive_baseline_and_denominators_confirmed

慢网证据为注入延迟模拟：图5报告在1P_3D、QPS=1、WildChat500对话时，带宽150→10GB/s使PD TTFT143.7→170.6ms而PPD约51ms。原PDF第14页式2确认接收路径注入max(0,B/βtarget−tNVLink)延迟，PPD本地AP不受注入影响。该实验隔离传输代价，未测真实多节点拥塞，不能证明所有真实网络下收益均不低于NVLink结果。

核查定位：p009:L0007-L0011, p013:L0058-L0062, PDF physical page 14, Eq.2 and B.6；simulation_scope_confirmed

干扰测量和稳定性口径：单prefill报告48%对2%退化；4并发的正文与图7图注报告57%对21%，不能将数量级差距推广到该并发设置。17配置×18负载×10QPS共3060点且每点10秒；作者未给完整重复区间。表3的4/27是100%成功点数，图11的13/27失败按SR<95%计，两者阈值不同，不能当成互补数量。

核查定位：PDF physical pages 4–5, §4.1–4.2, PDF physical page 14, Figure 7 and C.1, PDF physical page 8, Table 3, p017:L0007-L0009；interference_and_success_thresholds_qualified

本地补充/限定：["补充原表3及带宽注入公式核查；区分100%成功点和SR<95%失败点，二者不应相减互推。", "保留动态PPD相对x=1效应量尚不清楚的判断，不将静态缓存收益直接算作动态调度收益。"]

核查局限：["未部署vLLM、执行负载回放或真实跨节点测试。", "未独立读取AMPD等前作，也未确认最终出版版角色。", "Pro仅看全文文本，本地仅观察两页原PDF，不将曲线图注当作重新测量。", "L1是AI暂评；工程可用性和新颖性级别分开判断。"]


## pro045 · LiftQuant: Continuous Bit-Width LLM via Dimensional Lifting and Projection

论文 OR_1GvXUhLIMP；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_1GvXUhLIMP_7065ebbde21f", "source_url": "https://api2.openreview.net/pdf?id=1GvXUhLIMP\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_1GvXUhLIMP_7065ebbde21f：物理页1—13全部提供文本，页标连续；包括正文§1—5、参考文献、附录A—F。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅收到全文提取文本，未看过PDF图像，不认定为最终出版版。", "图1—4只有图题及零散标签，不能恢复曲线坐标或Qwen系列、MMLU的精确结果。", "公式转置、上下标及双栏表格布局可能有损；未据此确认所有矩阵维度和表7复杂度表达。", "附录表7—9使用LiftUQ名称；表8中PTQ1.61的来源与评测上下文未明确，不与主表结果直接合并。"]}

问题：如何在固定显存预算下细粒度调整LLM权重存储率，同时避免为不同位宽维护不同解码机制？

方法：以w≈Mq表示d维权重，q为D维±1向量，名义位宽D/d。先用标准高斯样本学习共享M，以伪逆和辅助二值向量启发式搜索码字；再学习层级T=diag(s1)(P1⊗P2)diag(s2)重塑权重分布。投影与逆变换融合后执行二值权重—浮点激活乘法；块级STE校正更新二值权重和变换，随后E2E微调连续参数。

作者主张：通过lift-then-project产生非均匀向量码本，实现近连续位宽调节及Pareto最优部署。

论文证据：表2展示整数附近和2.4bit配置的精度；表5加入M后，WikiText-2 PPL从7.77降至6.79。

模型推断：支持一种兼顾可调存储率与统一解码的结构化量化机制；不支持数学意义的连续位宽、历史首创或全局最优性。

定位：['TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页3—5，§3.1—3.2；物理页7表2；物理页8表5。\n']

作者主张：用统一线性变换和Int1运算替代复杂VQ解码，兼顾精度与吞吐。

论文证据：表4中Llama-2-70B的约2bit解码为31.3 tokens/s，QTIP为24.5；AWQ为36.1。

模型推断：支持所测单卡、batch=1条件下较QTIP更快，但不是最快方法，也不能外推至所有批量或预填充场景。

定位：['TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页7表4、§4.3；物理页8实现说明。\n']

key_results：[{"setting": "Llama-2-7B，CTX=2048；Llama-3-70B，CTX=8192；WikiText-2/C4。", "baseline": "QTIP，2.00bit。", "metric_or_guarantee": "PPL，越低越好；以下均为作者报告。", "reported_values_and_units": "按上述模型顺序，QTIP为6.28/7.94、4.97/6.80；LQ-32/16为6.52/8.21、4.69/6.73；LQ-24/10为6.10/7.70、4.10/6.47。表2对应有效位宽分别标为2.01—2.02、2.41—2.42bit。", "information_and_compute": "块校准：RedPajama 4096×2048，留128样本验证，2轮；E2E：4096×4096，1轮，作者报告70B可用单张A100-80GB微调。GPU时未报告。", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页7表2；物理页11附录A—B。\n"}, {"setting": "Llama-2-7B递增加组件消融，基线为2bit对称UQ。", "baseline": "保留随机正交P1、P2；作者称去掉二者会训练崩溃。", "metric_or_guarantee": "WikiText-2 PPL。", "reported_values_and_units": "P1+P2：8.76；加s1：8.28；加s2：7.77；加M：6.79；再微调：6.53。", "information_and_compute": "属于累加消融，未给各项等训练预算对照；表内未指定D、d。", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页8，§4.4、表5。\n"}, {"setting": "Llama-2-70B，context length=512、batch=1；表题标GTX4090D-48G，正文作RTX 4090D（48GB）。", "baseline": "QTIP 2/3bit；AWQ 2bit。", "metric_or_guarantee": "端到端解码吞吐，tokens/s。", "reported_values_and_units": "LiftQuant LQ-32/16、24/10、24/8分别31.3、25.7、20.8；QTIP 2/3bit分别24.5、17.6；AWQ 2bit为36.1。", "information_and_compute": "使用torch.compile和BitBLAS UINT1–FP16 GEMV；未给重复测量误差。", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页7表4、§4.3；物理页8实现说明。\n"}]

prior_work_candidates：[{"citation_as_printed": "Lee, D. and Song, H. O. Q-palette: Fractional-bit quantizers toward optimal bit allocation for efficient llm deployment. arXiv preprint arXiv:2509.20214, 2025.", "identifier_if_present": "arXiv:2509.20214", "relation_candidate": "背景引用", "shared_component": "分数位宽与显存预算匹配。", "claimed_difference": "本文称其需要混合量化器和多类内核，而LiftQuant只调整投影维度。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页3§2、物理页9参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Park, S., Bae, J., Kwon, B., Kim, M., Kim, B., Kwon, S. J., Kang, U., and Lee, D. Unifying uniform and binary-coding quantization for accurate compression of large language models. arXiv preprint arXiv:2506.03781, 2025.", "identifier_if_present": "arXiv:2506.03781", "relation_candidate": "背景引用", "shared_component": "二值编码的加性表示，结构上接近投影码本。", "claimed_difference": "本文将BCQ归为标量非均匀量化，称其未利用维间相关；实际覆盖边界未核读。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页2§2、物理页10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Tseng, A., Sun, Q., Hou, D., and De Sa, C. M. Qtip: Quantization with trellises and incoherence processing. Advances in Neural Information Processing Systems, 37:59597–59620, 2024b.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "非均匀低比特编码及分布预处理。", "claimed_difference": "QTIP使用trellis处理更高维编码；LiftQuant以有限维二值投影换取可调位宽与较简单解码。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页4§3.1、物理页10参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "可调率投影码本与统一解码的组合提供实质能力，且有精度和吞吐支持；分数位宽本身已有前作，尚不足判为路线级首创。", "central_increment": "前作已提供分数位宽或非均匀编码（本文转述）；本作在有限维搜索和校准条件下，将D/d调率与二值矩阵解码结合；证据为表2、4、5，尚待排除等预算前作覆盖。", "soundness_observation": "CLT是设计动机，未给有限维误差界或Pareto保证；存在正文数值冲突，STE也不等于离散搜索可精确微分。", "significance_observation": "对2—3bit部署空隙有价值；工程简化有单设备证据，跨硬件及24GB完整部署尚不充分。", "main_open_question": "匹配总存储、校准与训练预算后，相对Q-Palette及binary-coding前作还保留多少独立机制和部署收益？"}

limitations：[{"text": "启发式搜索仍按2^(D−d)增长；作者限制D−d≤20，并承认严格2bit编码效率不及QTIP，高位宽需缩小d而损失相关性收益。", "basis": "author_report", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页3—4，§3.1、表1。\n"}, {"text": "§4.1称2.4bit的5.86 PPL优于2bit的5.31，与PPL方向及表2均不一致；本评保留表2数据，不推测正文原意。", "basis": "model_inference", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页6，§4.1；物理页7表2。\n"}, {"text": "2.4bit优于2bit并非等预算证明；基线是否匹配训练预算未充分交代。“Ideal 4-Bit”是假想FP16精度参照，并非实测对照或最优性证明。", "basis": "model_inference", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页6，§4、§4.2。\n"}, {"text": "24GB/12GB部署主要由文字和不可见图支持，未给对应峰值显存及完整KV配置；实际吞吐表测于48GB、batch=1，不能证明任意预算或批量均Pareto最优。", "basis": "model_inference", "locator": "TEXT_OR_1GvXUhLIMP_7065ebbde21f，物理页2图1说明、物理页6§4.2、物理页7表4。\n"}]

minimal_check：{"question": "统一投影在相同总存储预算下是否仍有部署收益？", "control": "Llama-2-7B：LQ-24/10对Q-Palette最接近且不超预算配置；匹配实际总字节、校准/E2E预算、CTX=2048及batch=1。", "observable_outcome": "比较WikiText-2 PPL、峰值显存和解码tokens/s。", "resources": "需双方代码、权重、RedPajama及GPU；具体显存和GPU时待核实，本轮未运行。", "failure_or_stop_condition": "无法匹配预算则停止归因；若对照同预算下PPL不高且吞吐不低，则该设置的Pareto优势不成立。"}

missing_fields：["图形原始数据与PDF视觉核验", "M训练样本量、完整训练GPU时及重复试验误差", "24GB/12GB部署峰值显存和完整运行配置", "QTIP参考条目未提供DOI或arXiv标识", "前作全文与最小检验的实际资源成本"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

结构化二值投影与分数存储率的组合值得了解；关键追问是在相同总字节、校准成本和真实部署配置下，较已有分数位宽与二值编码方案的独立收益。

身份、版本与实际投递：当前13页官方PDF哈希7065ebbde21f前缀与返回绑定一致。成功初评使用同一PDF的文本投递revision2，仅压缩横向空白；原输入、第一次Failed to fetch及重试证据均保留。本地核查方法、主结果及训练细节，观察原PDF第6、7页，不将重试记作第二轮科学复审。

核查定位：text_delivery_manifest.json, structured/pro045.json, browser/pro045_conversation.json；source_and_retry_revision_confirmed

可调比特率与机制边界：w≈Mq把d维向量编码为D维二值向量，名义率D/d；D和d仍为整数，且搜索启发式为2^(D−d)、实用约束D−d≤20。CLT提供设计动机，没有有限维误差或全局Pareto保证。矩阵M在高斯源训练，层级缩放与Kronecker混合后还有STE块校准及E2E微调，不能称为无训练或离散argmin可精确微分。

核查定位：p003, §3.1, p004:L0026-L0058, p005, §3.2–3.3, p011, A–B；central_mechanism_and_costs_confirmed

正文与主表PPL冲突：原PDF第6页确实写Llama3-70B 2bit PPL5.31、2.4bit5.86并称后者更优；PPL越低越好，且第7页表2对应WikiText2实为4.69、4.10，C4为6.73、6.47。保留表文冲突，不自动把正文数字修成表值。表2亦确认Llama2-7B QTIP6.28/7.94优于约2bit LQ6.52/8.21，而2.4bit LQ6.10/7.70使用更多存储。

核查定位：PDF physical page 6, §4.1, PDF physical page 7, Table 2；reported_numeric_conflict_visually_confirmed

吞吐设备和直接基线：原表4确认Llama2-70B、CTX512、batch1，LQ32/16、24/10、24/8分别31.3、25.7、20.8tokens/s；QTIP2/3bit24.5/17.6，AWQ2bit36.1。设备原文分别标GTX4090D-48G和RTX4090D(48GB)，本地不擅自纠正配置。该表支持部分配置比QTIP更快，但不支持最快、24GB完整运行或所有批量加速的结论。

核查定位：PDF physical page 7, Table 4 and §4.3, p008:L0050-L0059；throughput_and_hardware_scope_confirmed

消融与训练预算：表5为逐项累加：8.76→8.28→7.77→6.79→6.53，缺P1/P2会训练崩溃；未给等成本全组合消融。附录A为4096×2048、其中128留出、两轮块校准；B另有4096×4096一轮E2E。附录C改用10×20矩阵且只做块校准，不能与主LQ32/16无条件合并。Ideal4bit明确是假设达到FP16精度的参考，不是实测量化基线。

核查定位：p008:L0050-L0069, p011:L0018-L0048, PDF physical page 6, §4.2；ablation_and_reference_comparison_qualified

本地补充/限定：["原PDF确认5.31/5.86的正文冲突并核实表2和表4，不以推测替作者更正。", "明确成功输入是保持非空白内容及页锚的投递revision2；初次网络失败不重复计科学评审。"]

核查局限：["未核读Q-Palette、QTIP等前作全文，L2保持AI暂评。", "未执行量化、训练或设备吞吐测量，未独立验证48GB设备身份及24GB部署峰值。", "未核查所有矩阵转置和附录复杂度表达；不作完整算法或证明审计。", "Pro仅看全文文本，本地观察第6、7页，其他图曲线未重新取数。"]


## pro046 · AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs

论文 OR_ymHDVBwmta；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_ymHDVBwmta_052989bed120", "source_url": "https://api2.openreview.net/pdf?id=ymHDVBwmta\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "13156acccc1e0da4a355b0970f6017d29e040f67782a0dd096a7ad8e52797320", "source_pdf_sha256": "052989bed120ad2f1f18b4dca187088b81548daa2c588b04b86bc86c18a42433"}], "read_ranges": ["TEXT_OR_ymHDVBwmta_052989bed120：物理页1–16连续全文，包括正文§1–7、Impact Statement、参考文献及附录§8.1–8.2；未发现缺失页标。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅阅读全文提取文本，未看到原PDF图像；图1–11的图形、曲线及图中数值不可核验。", "表1–15有可辨文本，但双栏交错及公式上下标存在提取损失；公式与报告冲突不擅自修正。", "未提供前作全文、其他版本或作者代码；当前附件的最终出版身份未核验。"]}

问题：如何同时压缩LLM训练中的激活缓存、常驻梯度和梯度通信，而不明显损害训练质量？

方法：前向计算后量化所需激活，反向恢复BF16/FP16；按算子选择保存输入或重算中间值，Attention保持高精度，其余采用块大小128的低比特量化。利用PP阶段显存余量提高部分阶段位宽。梯度常驻FP8，本地累加先反量化；跨设备采用All-to-All→FP32本地归约→再量化→All-Gather。并非全模型4-bit计算。

作者主张：通过算子感知量化、重算与PP位宽补偿，实现接近4-bit的激活存储并保持训练质量。

论文证据：表1按U=batch×sequence×hidden×2字节计算，激活存储由28U降至7.75U；表12的DBC消融在六任务中改善四项；p16文字报告全部激活统一4-bit不收敛。

模型推断：增量是保存/重算与精度分配的联合设计，不是新量化原语；局部扰动分析尚不能作为FP4训练收敛保证。

定位：['TEXT_OR_ymHDVBwmta_052989bed120，p4–6 §4、表1。\n', 'TEXT_OR_ymHDVBwmta_052989bed120，p13–16 §8.1–8.2、表12']

作者主张：QuanGrad同时降低梯度存储和通信成本，并保持归约精度。

论文证据：§5给出低精度存储、高精度加和流程；表4报告通信延迟下降，图8的损失比较只能读取作者文字描述。

模型推断：高精度归约避免直接FP8求和的部分数值风险，但反复量化仍有误差，不能解释为无损All-Reduce。

定位：['TEXT_OR_ymHDVBwmta_052989bed120，p7 §5；p8 图8；p9 表4']

key_results：[{"setting": "LLaMA2-13B，序列长度80K", "baseline": "Megatron-LM及其ZeRO-1版本", "metric_or_guarantee": "训练时间", "reported_values_and_units": "作者报告Megatron-LM/ZeRO-1/AGoQ分别为149667/149288/111422 ms，约1.34×加速；前两者重算10层，AGoQ整层重算数为0，但仍有方法内的局部重算。", "information_and_compute": "64×A6000、200Gb/s InfiniBand；TP=8、PP=4，mini-batch=1、global batch=16。", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p7 §6.2、表2。\n"}, {"setting": "LLaMA2-13B，12K序列，GPU内存消融", "baseline": "Megatron-LM、仅优化器量化O、优化器加梯度量化O+G", "metric_or_guarantee": "内存占用", "reported_values_and_units": "作者表8报告：基线46.1 GB，O为37.7 GB，O+G为35.3 GB，AGoQ为22.3 GB；据表计算总降幅约51.6%，附录文字却称53%。", "information_and_compute": "TP=8、PP=1；总收益包含借用的8-bit优化器，不能全部归于新增机制。", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p15 §8.2、表8。\n"}, {"setting": "OLMo-1B，24K序列", "baseline": "COAT", "metric_or_guarantee": "时间与内存", "reported_values_and_units": "作者报告COAT→AGoQ：6291→6161 ms，94100→66852 MB；据表计算内存下降约29.0%，正文称31%，两者不一致。", "information_and_compute": "16×Pro6000，global batch=64；不是与A6000结果跨硬件直接比较。", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p8 §6.2、表3。\n"}, {"setting": "32 MB消息，200/10 Gbps两种带宽", "baseline": "原All-Reduce", "metric_or_guarantee": "通信延迟", "reported_values_and_units": "作者分别报告131.23→39.17 ms、1603.78→432.36 ms；对应约3.4×、3.7×加速。", "information_and_compute": "TP=8、DP=8；表中AGoQ总延迟包含量化/反量化。", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p9 表4。\n"}, {"setting": "LLaMA2-7B训练2B tokens、LLaMA3.2-1B训练10B tokens；六项zero-shot任务", "baseline": "Megatron-LM FP16", "metric_or_guarantee": "准确率差", "reported_values_and_units": "据作者表10换算，7B各任务差值范围为−1.54至+2.06个百分点，1B为−0.80至+2.22个百分点；不是逐任务均无损。", "information_and_compute": "7B使用OpenWebText；1B的10B-token语料未明确。未报告重复种子及误差区间。", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p8 §6.3；p15 表10。\n"}]

prior_work_candidates：[{"citation_as_printed": "Xi, H., Cai, H., Zhu, L., Lu, Y., Keutzer, K., Chen, J., and Han, S. COAT: Compressing optimizer states and activations for memory-efficient FP8 training. In The Thirteenth International Conference on Learning Representations, 2025.", "identifier_if_present": "XfKSDgqIRj", "relation_candidate": "比较基线", "shared_component": "低精度激活与优化器状态存储", "claimed_difference": "本篇称进一步降低激活位宽，并压缩常驻梯度及其通信。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ymHDVBwmta_052989bed120，p2 §1；p8 §6.2；p12 参考文献", "prior_actually_read": false}, {"citation_as_printed": "Peng, H., Wu, K., Wei, Y., Zhao, G., Yang, Y., Liu, Z., Xiong, Y., Yang, Z., Ni, B., Hu, J., Li, R., Zhang, M., Li, C., Ning, J., Wang, R., Zhang, Z., Liu, S., Chau, J., Hu, H., and Cheng, P. FP8-LM: training FP8 large language models. CoRR, abs/2310.18313, 2023b.", "identifier_if_present": "arXiv:2310.18313", "relation_candidate": "比较基线", "shared_component": "FP8梯度存储及All-Reduce", "claimed_difference": "作者称其FP8累积损害收敛，本篇改用反量化后的高精度累加与归约。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ymHDVBwmta_052989bed120，p2 §1；p8 §6.3；p11 参考文献", "prior_actually_read": false}, {"citation_as_printed": "Chen, P., Deng, Z., Li, P., He, S., Zhu, H., Zheng, Y., Wang, Z., Huai, B., and Guo, M. Adacc: An adaptive framework unifying compression and activation recomputation for llm training. arXiv preprint arXiv:2508.00806, 2025.", "identifier_if_present": "arXiv:2508.00806", "relation_candidate": "背景引用", "shared_component": "题名涉及激活压缩与重算联合，具体重叠范围未知。", "claimed_difference": null, "basis": "target_paper_only", "target_locator": "TEXT_OR_ymHDVBwmta_052989bed120，p1 §1；p10 参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "最可能是具有实质能力增量的联合系统设计：在部分训练条件下同时降低激活、梯度驻留和通信成本；并非新量化原语或路线级框架。", "central_increment": "前作已做FP8激活/优化器及FP8梯度训练（本篇转述）；本作新增算子重算、PP余量精度补偿和梯度通信的联合实现。表2、8支持效能，尚需排除等预算压缩/重算基线的覆盖。", "soundness_observation": "局部小扰动分析不是端到端收敛证明；部分推导、阶段公式及指标报告有待核项，不能把工程收益视为理论正确性的证明。", "significance_observation": "对显存受限长序列训练有实用价值；34B主要提供速度证据，质量验证覆盖更小模型和有限token预算。", "main_open_question": "在同峰值显存、同训练token与重算预算下，阶段感知精度补偿是否仍提供独立且长期稳定的收益？"}

limitations：[{"text": "COAT比较受硬件限制仅覆盖16张Blackwell；更大集群上的额外加速属于作者预期，非实测。", "basis": "author_report", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p8 §6.2"}, {"text": "按附录SiLU一阶式，y趋近0时导数误差约为yδ_y/2，与用于小输入比较的O(y²|δ_y|)不符，尚不足以支持其“严格更小界”；需核原PDF公式。", "basis": "model_inference", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p13 §8.1.1，p013:L0028–L0042"}, {"text": "式(21)的Ni随阶段编号递增，与文本11/9/7/5反序；代入式(22)会产生低于4的位宽，无法按现有文本复现4/5/6/8规则，可能涉及索引或排版问题。", "basis": "model_inference", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p6 §4.2，式(21)–(22)"}, {"text": "表7标注samples/sec，AGoQ数值却更低，正文仍称更快；单位或方向冲突，短序列加速暂不可确认。", "basis": "model_inference", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p9 表7及Extended Throughput Analysis"}, {"text": "表14的32K/64K试验分别用36/16层，不能视为固定模型规模的跨长度比较；表15梯度范数接近也不能替代长期损失和任务质量验证。", "basis": "model_inference", "locator": "TEXT_OR_ymHDVBwmta_052989bed120，p16 表14–15"}]

minimal_check：{"question": "DBCA-PP能否在不增加峰值显存的前提下降低梯度误差？", "control": "固定同一模型、批次、PP=4、LAAQ、QuanGrad、优化器和重算；仅比较相同可压缩激活统一4-bit与4/5/6/8-bit配置，Attention均不变。", "observable_outcome": "记录各阶段同时存活的激活批次数、包含元数据及临时缓冲的峰值显存，以及相对BF16的梯度误差。", "resources": "作者量化实现及可运行四阶段PP的GPU环境；具体显存需求和GPU时未知。", "failure_or_stop_condition": "若峰值超过对照或梯度误差未改善，则该设置下的补偿主张不成立；若阶段编号及5/6-bit格式无法确定，停止数值比较并记录实现缺口。"}

missing_fields：["图形及数值损失曲线不可见。", "5/6-bit格式、梯度FP8格式及完整缩放/舍入实现细节未明确。", "完整训练超参、初始化、重复种子、统计区间及总GPU时未报告。", "前作全文、与AdaCC的直接差异及等预算近邻对照未提供。", "最终出版版本身份未核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

联合压缩与重算有实际显存价值；继续阅读先确认阶段位宽实现和计时单位，再判断同峰值显存、同token及同重算预算下的独立质量收益。

身份与中心机制：16页官方当前附件与输入、返回绑定一致。算子感知保存/局部重算、PP显存余量提高部分阶段精度，加上FP8常驻梯度与通信，构成联合设计。Attention激活不量化；前后向计算仍恢复高精度。本地梯度FP16/BF16累加、跨DP本地FP32归约后仍重新量化，不能称全4bit计算或无损归约。

核查定位：text_delivery_manifest.json, structured/pro046.json, p004–p007, §4–5；source_and_mechanism_confirmed

阶段编号与位宽公式：原PDF第6页确认为Ni=n+2i−1和Bi=4N1/Ni。n=4代入Ni=[5,7,9,11]、Bi=[4,2.857,2.222,1.818]，与同页文字11/9/7/5、最低4bit及第8页4/5/6/8配置不一致。应澄清索引、裁剪及舍入实现，不能直接据所印公式复现不增加峰值显存的规则。

核查定位：PDF physical page 6, Eq.21–22 and §4.2, p008:L0045-L0046 and L0062-L0063, local_check/bounded_formula_checks.json；formula_internal_inconsistency_confirmed

SiLU小输入误差阶：原PDF第13页的Case1一阶式为[σ(y)+yσ'(y)]yδy，但随后写O(y²|δy|)。当y趋近0，方括号趋近1/2，因此一阶误差为yδy/2量级。小输入下据此证明严格更小界的该步不成立；不由此否定量化重算的实测效果或断言端到端训练失败。局部公式算术记录另存，未运行模型实验。

核查定位：PDF physical page 13, §8.1.1 Case1 and comparison paragraph, local_check/bounded_formula_checks.json；local_asymptotic_gap_confirmed

工程收益与误写百分比：表2确认80K、13B、64A6000、TP8PP4时149667→111422ms约1.34倍，基线重算10整层而AGoQ为0整层，但方法内仍重算中间值。表8的46.1→22.3GB是51.63%下降而非附录53%；含借用的8bit优化器收益。表3的COAT94100→66852MB为28.96%而非正文31%，且该比较在16Pro6000。不同硬件和重算策略不能混作同一算子速度比较。

核查定位：p007, Table 2 and §6.1–6.2, p008, Table 3, p015, Table 8, local_check/bounded_formula_checks.json；principal_numbers_and_cost_boundaries_confirmed

短序列吞吐单位及通信：原PDF第9页表7明确标samples/sec，但2k行基线2862.22、AGoQ2148.82更低，正文却称1.33倍更快；不能擅自改成毫秒，短序列加速保持待核。表4的32MB通信131.23→39.17ms与1603.78→432.36ms可核，并包含量化反量化；通信优势不直接等于全训练倍数。

核查定位：PDF physical page 9, Tables 4 and 7；throughput_unit_conflict_visually_confirmed

训练质量证据范围：表10六任务7B差值−1.54至+2.06个百分点，1B为−0.80至+2.22，并非逐任务无损。表12的DBC改善四项、两项下降。表14的32k/64k分别使用36/16层，不是固定模型跨长度对照。表15长期梯度范数接近不能替代最终任务质量和损失收敛；未报告重复种子区间。

核查定位：p015, Table 10, p016, Tables 12, 14 and 15；quality_and_scaling_scope_qualified

本地补充/限定：["用原PDF确认阶段公式、SiLU误差阶及短序列吞吐单位问题，原先待核项得到局部证据支持。", "保持工程效果与理论保证分开；未把这些局部问题扩展为整篇实验不可信或算法必然失败。"]

核查局限：["未部署分布式训练或执行最小实验；局部计算只是印刷公式代入。", "未完整审计所有梯度推导，也未核读COAT、FP8-LM或AdaCC全文。", "Pro读全文文本，本地核查列示页并观察三页原PDF。", "L2仍为AI暂评，不是已验证的历史首创或完整收敛证明。"]


## pro047 · On Structured State-Space Duality

论文 OR_DKathyl3XN；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_DKathyl3XN_98f26f9e2a37", "source_url": "https://api2.openreview.net/pdf?id=DKathyl3XN\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "ed1507eb8bb03dfd8cc1efe535b2a91898acbb6bad696683399bc3e7cb8d73cc", "source_pdf_sha256": "98f26f9e2a37dd44c017667017583608db193896ce8105909e20ab9d1007bb3d"}], "read_ranges": ["TEXT_OR_DKathyl3XN_98f26f9e2a37：物理页1—27连续全文；正文1—9，参考文献10，附录A及目录11—12，证明B.1—B.2为13—17，实验C.1—C.7为18—27。题名吻合，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供文本，未看PDF图像；图1—15只有图注或零散文字，不能读取曲线和误差带。Table 1数值可读。", "双栏、矩阵和上下标排版有损；未逐式验证全部证明，未访问链接代码、核读前作或复现实验；出版版本身份未核定。"]}

问题：哪些N维因果线性SSM具有同宽度1-SS masked attention精确对偶？一般对角转移能否保留线性时间计算？

方法：展开核M[t,s]=c_t^T A_t···A_{s+1}b_s；对角情形按状态维分成N个1-SS头，可逆时将累计转移乘积吸入Q/K。将尾列M[t:T,t]不属于此前列同段张成空间的情况定义为new column，通过上三角低秩补全和零转移分块刻画对偶。

作者主张：对角SSD支持更丰富动态，同时匹配标量情形的最优训练复杂度。

论文证据：给出N头求和、满秩时单掩码重写及O(TNd)算法；Remark 3.1给出N=2、T=4的同维表达分离例。

模型推断：主要是既有SSD的代数扩展。满秩情形可重参数化为同维scalar-identity模型；严格分离示例依赖零转移。

定位：['TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页4—6，§3.1—3.3、Remark 3.1、Algorithm 1']

作者主张：给出一般SSM具有1-SS masked-attention对偶的必要充分条件。

论文证据：Theorem 3.1要求所有非零元落在连续主对角块内，且每块至多N个new columns；B.2提供低秩补全构造。

模型推断：可能的实质新增是可对偶性的精确边界，而非作者已承认属于既有知识的N-SS/SSS等价。

定位：['TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页7—8，Proposition 3.2、Lemma 3.1、Theorem 3.1。\n', 'TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页15—17，B.2']

作者主张：softmax秩爆炸阻断SSD；低状态维度的一般SSM也未必有1-SS对偶。

论文证据：§4使用V[i,j]=ij及其指数矩阵；Proposition 4.1使用M=I+E[T,1]，迫使内容矩阵秩至少T−1。

模型推断：应限定为固定N、随T增长的精确线性SSM对偶障碍；不排除增大状态维度、特殊输入结构或近似表示。

定位：['TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页8—9，§4、Proposition 4.1、Remark 4.1']

key_results：[{"setting": "Algorithm 1，对角SSM，输入T×d、状态维度N", "baseline": "scalar-identity SSD的复杂度，本篇转述", "metric_or_guarantee": "前向算术复杂度及存储元素数", "reported_values_and_units": "O(TNd) FLOPs；O(TNd)总存储元素", "information_and_compute": "状态参数占O(TN)，中间量占O(TNd)；不是训练耗时或GPU吞吐实测。", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页6，§3.3。\n"}, {"setting": "C.2：N=2，衰减率(0.5,0.8)，B=C=1，高斯标量输入", "baseline": "同一模型的直接递推，对比N个1-SS头求和", "metric_or_guarantee": "最大输出绝对误差", "reported_values_and_units": "作者报告约10^-14；时变A/B/C试验也在该量级", "information_and_compute": "float64；固定参数试验1000个随机种子，具体T扫描范围未列。", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页19—20，C.2。\n"}, {"setting": "WikiText-2词级末位next-token预测；训练5000、验证1000个窗口；L=128，d_model=64、d_state=16、2层", "baseline": "Ma的minimal Mamba，而非优化后的大规模Mamba基准", "metric_or_guarantee": "最佳验证交叉熵、最佳验证准确率", "reported_values_and_units": "Mamba：10.5、9.5%；SSD-Mamba：9.7、11.1%。交叉熵单位未标。", "information_and_compute": "6种子平均；10 epochs；batch=64；AdamW学习率10^-3；硬件及训练时长未报告。", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页24—25，C.6、Table 1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Tri Dao and Albert Gu. Transformers are ssms: Generalized models and efficient algorithms through structured state space duality. arXiv preprint arXiv:2405.21060, 2024.", "identifier_if_present": "arXiv:2405.21060", "relation_candidate": "理论扩展", "shared_component": "scalar-identity SSD、N-SS/SSS对应", "claimed_difference": "对角情形的形式化和一般可对偶性判据", "basis": "target_paper_only", "target_locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页2、6、10", "prior_actually_read": false}, {"citation_as_printed": "Yuli Eidelman, Israel Gohberg, and Iulian Haimovici. Separable type representations of matrices and fast algorithms. Springer, 2014.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "结构化矩阵与状态空间表示等价", "claimed_difference": "提供SSM/SSD记号下的自包含构造证明，不主张该数学等价首次成立", "basis": "target_paper_only", "target_locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页2脚注、6 Remark 3.5、10参考文献", "prior_actually_read": false}, {"citation_as_printed": "Jerome Sieber, Carmen A Alonso, Alexandre Didier, Melanie N Zeilinger, and Antonio Orvieto. Understanding the differences in foundation models: Attention, state space models, and recurrent neural networks. Advances in Neural Information Processing Systems, 37:134534–134566, 2024.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "softmax精确递归实现需要无界状态维度的障碍", "claimed_difference": "本篇使用矩阵秩及半可分结构表述", "basis": "target_paper_only", "target_locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页9 Remark 4.1、10参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心充要判据提供明确的表示能力边界；对角分解及基础等价本身更接近局部扩展，不支持L3。", "central_increment": "前作已做到scalar-identity SSD（本篇转述）；本作在固定宽度、精确因果核条件下新增分块new-column判据，证据为Theorem 3.1及B.2；待排除既有矩阵补全结果的覆盖。", "soundness_observation": "存在明确内部冲突：C.2/C.3按B=C=1构造的M为下三角且对角恒N，因此普通rank(M)=T，而非其报告的N；这是由给定公式直接推出，并非复现实测。该错误损害附录秩验证，但不自动推翻独立的分解和充要条件证明。\n", "significance_observation": "主要价值是表征理论；小数据实验不足以建立大模型质量或硬件效率优势。", "main_open_question": "Theorem 3.1的新列分块判据相较Dao–Gu及Eidelman体系究竟增加了何种未被覆盖的结论？"}

limitations：[{"text": "没有专用diagonal-SSD kernel；一般表示构造尚无满足相同效率目标的算法，结构定理也不是训练实施方案。", "basis": "author_report", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页6 Remarks 3.3—3.4、8 Remark 3.8"}, {"text": "C.5只测整个因果softmax矩阵的普通秩；整体满秩不等于半可分秩无界，不能单独验证所声称的障碍。", "basis": "model_inference", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页23，C.5"}, {"text": "C.6同时改变输入选择性：SSD-Mamba用输入无关参数，基线B/C/Δ依赖输入；参数量未报。C.7比较N=1与N>1且包含多通道非线性网络，不能单独证明同N的严格表达分离；精确MSE不可读。", "basis": "model_inference", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页24—27，C.6—C.7"}, {"text": "C.4仅与显式T×T核实现比较，不是与优化scalar-SSD比较；每点3次重复与结果称100次运行的汇总关系不清。", "basis": "model_inference", "locator": "TEXT_OR_DKathyl3XN_98f26f9e2a37，物理页21—22，C.4"}]

minimal_check：{"question": "C.3是否把普通矩阵秩误记为半可分秩？", "control": "按其公式构造T=15、N=1、λ=0.9、B=C=1，同时检查因果M、生成矩阵G及完全位于下三角的子块。", "observable_outcome": "公式预期为rank(M)=15、rank(G)=1、合法非空下三角子块秩为1；核对作者实际计算对象是否另有所指。", "resources": "纸笔或CPU小矩阵计算即可，无需训练；未执行，实际运行成本未知。", "failure_or_stop_condition": "若原脚本计算未掩码矩阵，先澄清对象标注；否则rank(M)=1的报告无法成立，应停止将C.2/C.3作为有效秩验证。"}

missing_fields：["图像、曲线精确数值及误差带；C.7具体MSE和随机种子数。", "硬件、训练时长、显存峰值、反向传播计数及模型参数量。", "前作全文；Eidelman和Sieber条目未提供独立DOI/arXiv标识；未核定最终出版版本。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

优先读new-column分块判据及低秩补全构造，进一步核查与既有结构矩阵理论的覆盖；附录秩实验应先澄清实际计算对象。

身份与对偶范围：27页官方当前附件及全部所供文本与Pro返回绑定一致。对角状态递推按N个模式分成1-SS头；可逆对角转移的累计乘积可吸入Q/K，因此同N下严格表达分离示例依赖允许零转移。讨论为精确线性因果核，不能直接解释为带softmax的Transformer与任意固定状态RNN等价。

核查定位：text_delivery_manifest.json, structured/pro047.json, p004–p005, §3.1–3.2 and Remark3.1；source_and_representation_conditions_confirmed

中心充要判据与构造：Theorem3.1要求全部非零元处于连续主对角块内，且各块内部new columns数至多N，Q/K宽度固定为N。B.2先以非零行列缩放处理fine mask，再用新列线性独立证明必要性、逐列填上三角低秩补全证明充分性；零mask转移提供块边界。已核对这一论证链及定义，未作全篇证明认证，也未查明结构矩阵前作是否覆盖。

核查定位：p007, Definition3.2 and Proposition3.2, p008, Theorem3.1 and Remark3.8, p015–p017, B.2；central_claim_located_and_constructive_scope_checked

附录普通秩与半可分秩混淆：原PDF第20页确实报告rank(M)=N并称所有运行符合。按第19–20页的B=C=1公式，M是对角恒N的下三角矩阵，det(M)=N^T非零，普通rank(M)=T；重复衰减也不改变此结论。该报告与给定构造冲突，不能作为有效秩验证，但不自动推翻独立的代数分解或充要条件。

核查定位：p019:L0039-L0064, PDF physical page 20, C.2–C.3, local_check/bounded_rank_arguments.json；algebraic_conflict_visually_confirmed

softmax负测试不具诊断性：原PDF第23页只测整个因果softmax矩阵的数值rank。正对角下三角矩阵的普通秩本就为T。即使QK^T=0，因果均匀权重A[t,s]=1/t的普通秩仍为T，但合法下三角矩形子块秩为1。这说明该数值测试不能单独验证半可分秩增长；正文的固定N、随T增大的generic精确表示障碍需靠下三角子块论证。Proposition4.1的反例矛盾也需要T−1>N。

核查定位：PDF physical page 23, C.5, p008–p009, §4 and Proposition4.1, local_check/bounded_rank_arguments.json；negative_test_scope_corrected

复杂度与小模型证据：Algorithm1是O(TNd)前向算术及中间存储，未测专用kernel；作者明确将kernel留待未来。原PDF第25页表1确认最佳验证loss10.5→9.7、准确率9.5→11.1%，为5000训练/1000验证窗口、词级末位预测、两层64宽16状态、10epoch六种子的小模型实验。基线参数B/C/Δ依赖输入，SSD变体固定输入无关参数，因此不只是等价计算实现的比较，也不能据此证明大模型或GPU吞吐优势。

核查定位：p006, Algorithm1 and Remark3.3, p024, C.6 setup and models, PDF physical page 25, Table1 and training details；compute_and_empirical_scope_confirmed

本地补充/限定：["确认附录普通秩错误并补充因果均匀注意力的代数说明，明确全矩阵满秩不足以验证半可分秩增长。", "保留中心结构判据的独立潜在价值；未把附录数值验证问题自动视为定理被推翻。"]

核查局限：["未运行作者代码或最小矩阵实验；记录的是给定公式的确定性代数推论。", "未核读Dao–Gu、Eidelman及Sieber全文，L2为暂定增量判断。", "未逐式审计B.1、全部实验和所有图；Pro为全文文本阅读，本地只观察三页PDF。", "没有确认训练下界、专用kernel性能或大规模模型收益。"]


## pro048 · Why Are Linear RNNs More Parallelizable?

论文 OR_29sn1uqWn3；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_29sn1uqWn3_229e0814b371", "source_url": "https://api2.openreview.net/pdf?id=29sn1uqWn3\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "229e0814b371327512fd3781d5f0131db03721289ddcfa28f8b64fc3c07f8f33", "version_note": "按清单保留当前附件身份；未核实最终出版版本，仅阅读所提供文本。"}], "read_ranges": ["TEXT_OR_29sn1uqWn3_229e0814b371：物理页1–31全部文本，含正文§1–7、参考文献、附录A–F及表1；页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–2图像未提供；图2柱高、准确率及误差信息不能从图题或坐标轴推定。", "双栏文本存在交错，部分公式上下标、矩阵排版受损；表1主要配置可读。未查看PDF图像、外部前作或代码，未复现实验。"]}

问题：线性状态更新为何更易并行，以及不同RNN参数化的表达能力究竟相差多少？

方法：在固定宽度、固定层数及有理数Q算术下，把线性递推展开为矩阵连乘并构造算术电路；以计数器、多栈机器及WFA模拟建立下界，再用合成任务检查可学习行为。

作者主张：一般LRNN属于PNC^1，可用O(log n log* n)深度布尔电路模拟；log精度时上界收紧为AC^0[ENC^1]。

论文证据：定理3–4和推论5给出矩阵连乘、电路转换及有限精度输出枚举论证。

模型推断：新增的是并行性的比特复杂度刻画，不是新的GPU加速算法。

定位：['TEXT_OR_29sn1uqWn3_229e0814b371：物理页6–7，定理3–4、推论5；物理页30，附录E。\n']

作者主张：log精度非线性MLP RNN可解决L-complete问题，多项式精度时可解决P-complete问题。

论文证据：定理1–2以多栈和计数器模拟建立能力下界；P-complete语言构造使用多项式padding。

模型推断：提供线性与非线性递推的分离候选，但强深度下界有额外猜想条件。

定位：['TEXT_OR_29sn1uqWn3_229e0814b371：物理页5–6，定理1–2、推论1–4；物理页13–15，附录A。\n']

作者主张：四层RWKV-7和DeltaNet能模拟Q上WFA、解决PNC^1-complete矩阵连乘判定；PD LRNN则为NC^1-complete。

论文证据：定理5–8及附录B–C给出overwrite、对称秩一更新分解、有限窗口路由及PD乘积闭式。

模型推断：在前作已支持状态跟踪的架构间增加实质性的细粒度能力区分。

定位：['TEXT_OR_29sn1uqWn3_229e0814b371：物理页8，定理5–8；物理页16–29，附录B–C。\n']

key_results：[{"setting": "Sorted Deterministic Graph Connectivity；训练/验证规模区间[1,100]，测试区间另含[101,200]、[201,300]。", "baseline": "RWKV-7、DeltaNet、Mamba、Transformer，对比非线性RNN。", "metric_or_guarantee": "准确率与长度外推表现。", "reported_values_and_units": "正文称各模型分布内表现较高；仅非线性RNN跨区间保持近乎完美，其余随长度退化。精确百分比不可读。", "information_and_compute": "训练70K、验证20K、每测试区间10K样本；表1模型均为2层、d_m=256，最多60K训练步；批量和学习率存在文内冲突。", "locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页8–9，§6；物理页30–31，附录F、表1。\n"}, {"setting": "3×3矩阵序列连乘：固定素数模m版本与整数无模版本；使用相同三个长度区间。", "baseline": "Transformer、Mamba，对比非线性RNN、RWKV-7、DeltaNet。", "metric_or_guarantee": "模版本预测前缀积指定元素；无模版本预测最终(0,0)元素是否等于零。", "reported_values_and_units": "正文称前三种递推模型在模版本分布内近乎完美、外推中度下降；无模版本各区间近乎完美。图2b–c精确准确率缺失。", "information_and_compute": "作者报告监督训练结果，非本地实测；模版本采用逐步监督，无模标签计算允许可选裁剪，实际是否启用未说明。", "locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页9，§6；物理页30，附录F。\n"}]

prior_work_candidates：[{"citation_as_printed": "Merrill, W., Petty, J., and Sabharwal, A. The illusion of state in state-space models. In Forty-first International Conference on Machine Learning, 2024.", "identifier_if_present": "OpenReview: QZgo9JZpLq", "relation_candidate": "理论扩展", "shared_component": "LRNN的电路复杂度分析。", "claimed_difference": "从简单参数化的TC^0限制推进到一般PNC^1上界和更细分离。", "basis": "target_paper_only", "target_locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页6，§4；物理页11，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Peng, B., Zhang, R., Goldstein, D., Alcaide, E., Du, X., Hou, H., Lin, J., Liu, J., Lu, J., Merrill, W., Song, G., Tan, K., Utpala, S., Wilce, N., Wind, J. S., Wu, T., Wuttke, D., and Zhou-Zheng, C. RWKV-7 ”goose” with expressive dynamic state evolution. In COLM, 2025.", "identifier_if_present": "OpenReview: ayB1PACN5j", "relation_candidate": "方法继承", "shared_component": "三层router加一层乘法模拟器。", "claimed_difference": "从正则语言构造推广到有理权WFA和矩阵连乘。", "basis": "target_paper_only", "target_locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页17–20，附录B.2–B.3；物理页11–12，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Terzic, A., Menet, N., Hersche, M., Hofmann, T., and Rahimi, A. Structured sparse transition matrices to enable state tracking in state-space models. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025.", "identifier_if_present": "OpenReview: RDbuSCWhad", "relation_candidate": "理论扩展", "shared_component": "PD参数化及其乘法闭包。", "claimed_difference": "补充NC^1上界，与既有正则语言能力合成完备性定位。", "basis": "target_paper_only", "target_locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页8、28–29，§5.2、附录C；物理页12，参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是已有架构的新复杂度保证与结构性区分，超出局部性能改进；不是新架构或已证实的路线级突破。", "central_increment": "前作已给出TC^0限制及状态跟踪能力（本篇转述）；本作在固定架构和Q算术下新增PNC^1定位、DPLR/PD细分及非线性边界，证据主要是构造证明。", "soundness_observation": "未完成逐定理验证。A.2存在明确输入承诺缺口，见最小检验；D.1用语言指示函数的Hankel秩排除阈值WFA识别，未证明阈值分数可转为该指示函数，现有论证不足。\n", "significance_observation": "可为序列架构选择提供理论坐标；表达存在性不保证可训练性、自然任务收益或实际并行加速。", "main_open_question": "将图任务明确限制为汇点目标后，L完备性归约与一遍MLP模拟能否完整满足作者声称的FO保证？"}

limitations：[{"text": "作者采用满足结合律的Q算术及随长度增长的精度；这些保证不直接覆盖固定浮点数舍入语义。", "basis": "author_report", "locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页2–4，§2.1、Precision"}, {"text": "实验图仅为两条不相交路径且二进制序列化；模矩阵任务状态空间有限；无模实验测零判定而非PNC^1正值判定，可选裁剪还可能改变目标。因此实验不能直接验证所述复杂度分离。", "basis": "model_inference", "locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页7–8，定义12、命题3；物理页30，附录F"}, {"text": "主文报batch=64、lr=1e-4；附录及表1报batch=128、lr=3e-4。未报告PD实验、参数量匹配或实际并行耗时，不能将统一步数视为等算力。", "basis": "model_inference", "locator": "TEXT_OR_29sn1uqWn3_229e0814b371：物理页9，§6；物理页30–31，附录F、表1"}]

minimal_check：{"question": "附录A.2的计数器是否能处理可达但不是汇点的目标？", "control": "固定s=1、边(1,2),(2,3)；对照t=3与t=2。两者按定义11都应接受。", "observable_outcome": "按文字规则推演，最终S=3；读取t=2后S=1，算法拒绝，说明它只检测路径终点。\n", "resources": "手工整数状态追踪即可，无需训练或GPU；本轮未运行作者代码。", "failure_or_stop_condition": "若未明示t为汇点，该反例即否定Lemma2当前构造对完整定义的覆盖；不据此否定所有可能的L完备下界。"}

missing_fields：["图2精确准确率、误差条及重复实验统计", "GPU、训练耗时、完整参数量、随机种子与重复数", "模数m、图生成概率p、裁剪启用情况及上限", "实际采用的批量、学习率及完整正则化配置", "PDF图像、前作全文及出版版本身份核验"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

LRNN上界与不同参数化的理论坐标值得读；优先澄清图任务的汇点承诺、归约uniformity和阈值WFA证明，再依赖其强分离结论。

身份、语义与主上界：31页官方当前附件与返回绑定一致。理论采用满足结合律的Q算术、固定网络规模、FO-uniform多项式规模电路及最终正值判断；精度可随输入长度增长。Theorem3/4将LRNN定位PNC1及log精度子类AC0[ENC1]，布尔电路深度上界O(log n log* n)。这不是固定FP16舍入或实测GPU并行速度保证，严格分离还依赖所述复杂度猜想。

核查定位：text_delivery_manifest.json, structured/pro048.json, p002–p004, §2, p005–p007, Theorems2–4 and Corollaries3–6；central_guarantee_and_assumptions_confirmed

图连通构造的输入承诺缺口：Definition11未要求目标t是汇点。原PDF第14–15页的Lemma2只保留从s走到的最终节点并与最后给出的t比较。手推s=1、边(1,2),(2,3)、t=2时，S依次1→2→3，读目标后S=1而拒绝，尽管1到2可达。归约段另以无出边n为目标，提示可修正承诺方向，但当前构造没有覆盖完整定义；不据此否定所有可能的L完备下界。

核查定位：p005–p006, Definition11, PDF physical page 14, reduction and Lemma2, PDF physical page 15, acceptance rule, local_check/bounded_counterarguments.json；printed_construction_counterexample_confirmed

Hankel论证与阈值识别：原PDF第29页Theorem13从语言指示函数的无限秩排除WFA，未补充阈值分数到指示函数的桥梁。仅就它使用的无边图子块，F(s,t)=1/2−(s−t)^2的分数矩阵秩至多3，却在整数s,t上恰于s=t为正，阈值后成为无限秩单位指示矩阵。因此该Hankel推断不足；这不是构造了识别所有图连通实例的WFA。

核查定位：p004, Definition9 positive-threshold recognition, PDF physical page 29, Theorem13 and proof, local_check/bounded_counterarguments.json；threshold_inference_gap_confirmed

实验任务与理论语言不同：附录图数据仅两条不相交路径，查询0到n并二进制序列化，理论定义则一元编码。模矩阵任务为固定有限模数、逐步监督；无模任务标签是最终元素是否为零，并允许可选中间裁剪，实际启用与否不明，不能直接当成正值判定PNC1完备任务的实测验证。未从不可见图2推测准确率小数。

核查定位：p006, Definition11, p007, Definition12, p030:L0023-L0047, p009, Figure2 and §6；empirical_to_theoretical_scope_qualified

训练预算的文内冲突：主文第9页为batch64、学习率1e-4；附录第30页及原PDF第31页表1为batch128、学习率3e-4。两层、宽度256和最多60k步并不匹配不同架构的参数量及算力；未给PD实验或实际并行耗时。保留冲突而不选择一套作为已确认实现。

核查定位：p009:L0035-L0044, p030:L0049-L0054, PDF physical page 31, Table1；experimental_configuration_conflict_confirmed

本地补充/限定：["原PDF核实A.2最终节点判断和D.1指示函数Hankel推断；新增受限子块的低秩分数例解释后者缺口。", "未核实的栈阈值、二维旋转有理参数等问题保持Pro提出的待核项，不列为本地确认错误。"]

核查局限：["没有重跑作者代码、合成任务训练或性能测试；局部手推不构成全篇形式化证明审计。", "未独立核读复杂度与WFA前作，L2仍为暂评。", "没有完整核验DPLR路由、旋转构造和栈模拟；主上界亦未逐门形式化检查。", "Pro阅读全文文本，本地只核查列示页并观察四页PDF。"]


## pro049 · Recursive Models for Long-Horizon Reasoning

论文 OR_nERMuZtneC；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_nERMuZtneC_1ce5c9701ebe", "source_url": "https://api2.openreview.net/pdf?id=nERMuZtneC\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_nERMuZtneC_1ce5c9701ebe：物理页1–29全部文本，包括正文、参考文献及附录A–K；连续页标无缺号。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅提供文本，未看过PDF图像；图1–3图像不可见，图3曲线及具体数值无法核验。表1主要数值可读，双栏、公式及上下标局部交错。", "前作正文未提供；当前附件未核定为最终出版版。"]}

问题：固定活跃上下文下，递归自调用能增加多少推理能力？这种能力是否超过单上下文管理，并达到更一般智能体控制系统的上限？

方法：同一生成器通过call暂停父上下文并建立独立子上下文，return丢弃子推理，仅返回答案。实验另保留子问题描述、为每层添加原问题前缀，并按活跃帧拆分DPLL轨迹做SFT。

作者主张：深递归能够以指数更小的活跃上下文组织长计算。

论文证据：定理1给出TIME(2^{O(S)})的局部空间O(S)实现；附录E/F分别给出递归TM重构及ATM的AND/OR树构造。

模型推断：增量是受限Transformer的可实现性保证，而不是首次提出递归。

定位：['TEXT_OR_nERMuZtneC_1ce5c9701ebe:p5，定理1；p17–24，附录E/F。\n']

作者主张：简单call/return模型在更一般递归智能体系统中已具最优渐近能力。

论文证据：定理4给出深递归的指数时间oracle上界；定理5给出常深递归的线性局部空间oracle上界，与前面的构造对应。

模型推断：提供控制系统的资源比较框架；不能解释为任意外部工具都无法增强能力。

定位：['TEXT_OR_nERMuZtneC_1ce5c9701ebe:p7，定理4–5；p27–29，附录I–K。\n']

作者主张：训练3B模型递归求解SAT，可超过表中更大模型并迁移到困难实例。

论文证据：表1报告easy/medium/hard准确率为98%/95%/64%。

模型推断：支持算法轨迹监督下的场景价值；SAT实验不能直接验证深递归与总结的复杂度类分离。

定位：['TEXT_OR_nERMuZtneC_1ce5c9701ebe:p8，表1；p12，B.1']

key_results：[{"setting": "S(n)≥n的理想化Transformer；D按含根帧的栈高度计数。", "baseline": "D=1为普通CoT；常深构造实际使用D=2。", "metric_or_guarantee": "深递归覆盖TIME(2^{O(S)})；CoT能力介于TIME(O(S))与TIME(Õ(S²))；D=2覆盖SPACE(S)，且可用O(T)生成token模拟TM(S,T)。", "reported_values_and_units": "局部上下文O(S) token；深递归构造深度可达2^{O(S)}。", "information_and_compute": "附录E直接模拟的调用量上界为O(4^T)，在T=2^{O(S)}时可达双指数上界；基本模型不含memoization。", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p5，定理1–3；p19–20，E.2；p25–27，H。\n"}, {"setting": "SATBench自然语言SAT；easy/medium/hard分别为4–19、20–30、31–50子句，本作每档测试100题。", "baseline": "表1转录Wei等（2025）的提示式基线，未说明在本作同一测试子集重新评测。", "metric_or_guarantee": "准确率，顺序为easy/medium/hard。", "reported_values_and_units": "作者报告：本作98/95/64%；Qwen3-235B为88.0/64.8/51.4%；LLaMA3.3-70B为65.1/58.1/52.9%。", "information_and_compute": "Qwen2.5-3B-Instruct用DPLL轨迹SFT；10 epochs，batch 16，学习率1e-5、余弦衰减；4096-token训练窗口，超长左截断；2×H200约8小时。推理预算未报。", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p8，表1；p12，B.1–B.2。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Yang, C., Srebro, N., McAllester, D., and Li, Z. Pencil: Long thoughts with short memory. arXiv preprint arXiv:2503.14337, 2025b.", "identifier_if_present": "arXiv:2503.14337", "relation_candidate": "理论扩展", "shared_component": "总结式空间模拟、FASP及Transformer编译原语。", "claimed_difference": "由单上下文总结推广至深递归及一般scaffold上界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p11，参考文献；p21、24、26，构造说明", "prior_actually_read": false}, {"citation_as_printed": "Lee, S. and Kim, G. Recursion of thought: A divide-and-conquer approach to multi-context reasoning with language models. arXiv preprint arXiv:2306.06891, 2023.", "identifier_if_present": "arXiv:2306.06891", "relation_candidate": "背景引用", "shared_component": "多上下文中的递归分治。", "claimed_difference": "本篇称前作侧重固定算术递归，本作研究通用计算及递归深度的资源作用。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p9，§7；p10，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Savitch, W. J. Recursive Turing machines. International Journal of Computer Mathematics, 6(1):3–31, 1977.", "identifier_if_present": null, "relation_candidate": "理论扩展", "shared_component": "独立工作区的递归子程序及调用返回。", "claimed_difference": "增加受限Transformer逐步逻辑的可实现性与注意窗口资源刻画。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p10，参考文献；p12，附录A", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是有上下界支撑的机制理解与形式保证，不只是递归接口或SAT性能改进；不足以认定路线首创。", "central_increment": "前作已有递归多上下文及短记忆总结（本篇转述）；本作在受限Transformer条件下新增深度分层和scaffold能力上界，证据为定理1–5。", "soundness_observation": "未逐条验证证明；Transformer原语细节转引未提供前作。附录J仅有空间cutoff不足以保证每次更新停机，尚需补显式超时或循环检测论证，不据此判定定理错误。\n", "significance_observation": "理论贡献高于当前实验验证强度；工程接口简单，但外存、重算和深层错误成本仍重要。", "main_open_question": "匹配DPLL监督、基座及总推理预算后，深递归相对单上下文总结是否仍有独立收益？"}

limitations：[{"text": "原输入仍须进入可访问上下文；全局栈可很大，深层错误可能传播，递归不自动解决长输入访问。", "basis": "author_report", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p4–5，§3.1及Remark 1–2；p9，§6.3"}, {"text": "摘要对单上下文的严格超越表述需限定：多项式上下文时比较的是PSPACE与EXPTIME，正文承认其严格分离仍属通常假设。", "basis": "model_inference", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p6，§3.3。\n"}, {"text": "专门微调与外部提示基线混合比较，子集及预算未对齐；未报告重复运行或置信区间，不能将全部差值归因于递归。", "basis": "model_inference", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p8，表1；p12，B.1–B.2"}, {"text": "图3无法核数；§6.1的加速讨论依赖外置并恢复KV缓存，未提供端到端墙钟或传输开销测量。", "basis": "model_inference", "locator": "TEXT_OR_nERMuZtneC_1ce5c9701ebe:p8，图3及§6.1"}]

minimal_check：{"question": "递归能否在匹配监督和预算后优于单上下文总结？", "control": "同3B基座、同DPLL实例与监督来源、相当训练token及总生成预算，固定4096上下文，比较递归栈与单上下文状态总结。", "observable_outcome": "同测试题配对准确率、总token、最大活动上下文及墙钟时延。", "resources": "需原始划分、轨迹、检查点与GPU；新增对照成本未知。", "failure_or_stop_condition": "无法对齐数据或预算则停止因果归因；优势消失则不支持递归的独立实用增益。"}

missing_fields：["训练实例及轨迹总数、测试实例ID。", "推理迭代上限、总token与深度预算、采样参数及超限处理。", "测试硬件、端到端时延、外存开销和图3原始数值。", "Savitch（1977）的独立文献标识符未列；全部前作正文未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

局部窗口、全局栈、递归深度和总生成量的分开建模具有迁移价值。优先阅读定义和上下界，再用等基座、等算法监督及总预算对照判断实用递归收益。

身份、模型与资源定义：29页官方当前附件及输入返回绑定一致。理论生成器为常数大小、average-hard attention、O(log S)精度的Transformer；局部空间含可见原输入/前缀，悬置父帧计入全局栈而非活动窗口。递归不免除长输入访问、栈存储和搬运成本。

核查定位：text_delivery_manifest.json, structured/pro049.json, p004, Definition1–2 and Base Transformer Model, p005, Remark1；source_and_resource_conditions_confirmed

深度层次与时间代价：Theorem1在S>=n且不限制总生成量时覆盖TIME(2^O(S))；深度可为指数。附录E.2的直接重构给O(4^T)调用上界，代入指数T可成为双指数上界，不能解读为高效推理。第26–27页常深构造实际用两层栈交替返回/重开并总结状态，保持O(S)窗口与O(T)token。深递归与单上下文总结在多项式S下对应PSPACE/EXPTIME比较，正文承认严格分离仍是假设。

核查定位：p005, Theorems1–3 and Remark2, p006:L0008-L0022, p019–p020, E.2, p026–p027, depth2 construction；depth_and_compute_tradeoff_confirmed

一般控制器上界的条件：Theorem4/5是确定性scaffold在每帧L有界、问答字符串计入存储下的oracle时间/空间界。移除oracle另需各工具在2^O(L)时间、O(L)空间可算，不能说任意外部工具不增加能力。第28页J仅写空间cutoff后直接称每次表项更新指数时间内停机；对不终止的无关配置，还需明确配置重复检测或时间cutoff。有限配置数给出可补足的论证方向，因此记录为证明省略，未判定定理错误。

核查定位：p006, Definition3–4, p007, Theorems4–5, PDF physical page 28, I.4 and J, p029, K；oracle_scope_and_local_proof_omission_qualified

SAT数值和比较公平性：原PDF第8页表1确认本作98/95/64%，Qwen3-235B88.0/64.8/51.4%，LLaMA3.3-70B65.1/58.1/52.9%；表注明基线来自Wei等而非已确认同子集重测。本作3B模型用DPLL算法轨迹专门SFT，测试每档100个留出样本。故结果支持场景可行性，不能把全部差值归给递归本身，也不能用SAT实验验证复杂度类严格分离。

核查定位：PDF physical page 8, Table1 and §5, PDF physical page 12, B.1；decisive_results_and_training_information_confirmed

训练、窗口和真实效率边界：原PDF第12页为easy/medium且<=15变量训练；10epoch、batch16、lr1e-5、4096训练窗口、超长左截断，2H200约8小时。第8页图3可见总轨迹和最大活动窗口明显分离，但无原始逐点数值，不取图估计为精确测量。§6.1的加速比例依赖外置并恢复KV缓存，未报告墙钟或传输开销；单上下文总结也会压缩历史，不能直接以整个全局栈长度当其实际活动长度。

核查定位：PDF physical page 12, B.1–B.2, PDF physical page 8, Figure3 and §6.1；training_and_efficiency_claims_qualified

本地补充/限定：["本地查看图3仅确认趋势，仍不补写精确曲线数值。", "将J的停机问题限定为需补配置循环/时间界的证明步骤，不误报为上界已被反驳；进一步限定GS/LS加速比对实际总结基线的适用性。"]

核查局限：["未逐条核验Transformer编译原语、全部递归程序或交替空间证明；前作全文未读。", "没有训练模型、运行SAT或实现缓存搬运实验。", "测试ID、总监督量、推理预算与墙钟开销仍缺失。", "Pro仅阅读全文文本，本地观察三页PDF；L2保持AI暂评。"]


## pro050 · Revisiting Padded Transformer Expressivity: Which Architectural Choices Matter and Which Don’t

论文 OR_nBuL6HywFX；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_nBuL6HywFX_a2c6e83a295a", "source_url": "https://api2.openreview.net/pdf?id=nBuL6HywFX\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页1—33全部已提供文本，包括正文、参考文献、附录目录及附录A—C；连续页标未见缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF页面图像；图1仅有提取标签和图注，不能核验其原始布局、色线及标记位置。", "双栏文字存在交错，部分公式上下标、根式与关系符号失真；以下按可辨正文、定理及证明定位，不声称完成原PDF或全部证明核验。"]}

问题：多项式填充后，注意力类型、宽度、数值精度及uniformity如何决定Transformer的精确语言识别能力？

方法：输入字符串加多项式数量空白token，末位输出成员判定；通过定点寻址、门求值和归约构造表达能力下界，通过逐组件电路模拟给上界。循环共享层块，使电路深度随循环次数增长；不是训练算法。

作者主张：充足volume下，常深度表达能力由精度而非额外宽度决定。

论文证据：Theorem 4.2结合常数宽TC^0下界与多项式资源上界；§C.2给出PE替换构造。

模型推断：相对前作的对数宽结果，新增常宽刻画及资源饱和边界，不是新架构路线。

定位：['TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页5—6、24—26，Lemmas 4.1—4.2、Theorem 4.2。\n']

作者主张：Θ(log^d N)循环将常精度模型刻画为FO-uniform AC^d，将增长精度模型刻画为FO-uniform TC^d。

论文证据：Theorem 5.1；常精度下构造连通性、归约及wide-AC^d求值，增长精度下继承AHAT下界并转移至SMAT。

模型推断：主要新增是常精度循环分支及跨规格统一，不能把既有looping本身算作本篇发明。

定位：['TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页7、26—33，§5、附录C.3。\n']

作者主张：对数精度L-uniform AHAT可由同精度量级的L-uniform SMAT精确模拟。

论文证据：Lemma 3.1利用温度缩放、同阶内部高精度和舍入，声称逐层输出一致。

模型推断：这是从实数近似到指定定点语义下精确模拟的扩展，不覆盖固定温度或fully uniform SMAT的普遍等价。

定位：['TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页4—5、22—24，Lemma 3.1、附录C.1。\n']

key_results：[{"setting": "常深度、多项式padding、充足volume的L-uniform模型；SMAT与AHAT。", "baseline": "本篇转述的London & Kanade (2025)对数宽SMAT等价。", "metric_or_guarantee": "作者给出的语言类精确等价。", "reported_values_and_units": "b=Θ(1)：L-uniform AC^0；b=Θ(log N)：L-uniform TC^0。精度增至多项式不越过TC^0。", "information_and_compute": "PE可编码目标电路；padding的多项式指数依构造而定。无训练或运行时间实测。", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页5—6、25—26，Theorem 4.2、Lemma 4.2。"}, {"setting": "d≥1，循环Θ(log^d N)次。", "baseline": "Merrill & Sabharwal (2025a)的fully uniform增长精度AHAT。", "metric_or_guarantee": "常精度对应FO-uniform AC^d，对数精度对应FO-uniform TC^d；不等于证明每阶严格分离。", "reported_values_and_units": "常精度电路求值：O(log M)+L次循环；M为序列规模，L为电路深度。", "information_and_compute": "二进制指针读取一次，再逐层求值；允许有限个顺序组合的循环块。", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页31—33，Lemma C.3、Theorem 5.1。"}, {"setting": "N个顶点的有向或无向图，输入邻接矩阵及二进制s、t。", "baseline": "Merrill & Sabharwal (2025b)的对数精度连通性构造。", "metric_or_guarantee": "作者构造可判定s-t连通性的常精度模型。", "reported_values_and_units": "N²个邻接位、N³个padding位置；Θ(log N)宽度、O(log N)循环。", "information_and_compute": "PE预计算位置、除法及取模信息；通过两层更新将可达路径长度翻倍。N此处为顶点数。", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页29—30，Theorem C.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "London, C. and Kanade, V. Pause tokens strictly increase the expressivity of constant-depth transformers. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025.", "identifier_if_present": "OpenReview:eG5oh8l1WZ", "relation_candidate": "理论扩展", "shared_component": "L-uniform padding与门模拟。", "claimed_difference": "推广到常数宽、AHAT及更宽资源范围。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页5、12、24—26，§4、参考文献、附录C.2。", "prior_actually_read": false}, {"citation_as_printed": "Merrill, W. and Sabharwal, A. Exact expressive power of transformers with padding. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025a.", "identifier_if_present": "OpenReview:O1abxStFcy", "relation_candidate": "理论扩展", "shared_component": "归约闭包、循环电路求值与TC^d下界。", "claimed_difference": "加入常精度AC^d分支及L-uniform SMAT。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页7、12、28—33，§5、参考文献、附录C.3。", "prior_actually_read": false}, {"citation_as_printed": "Yang, A., Strobl, L., Chiang, D., and Angluin, D. Simulating hard attention using soft attention. Transactions of the Association for Computational Linguistics, 14:147–166, 2026a. doi: 10.1162/tacl.a.597.", "identifier_if_present": "doi:10.1162/tacl.a.597", "relation_candidate": "理论扩展", "shared_component": "attention gap与温度控制的近似误差界。", "claimed_difference": "声称通过定点舍入得到全输入精确模拟。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页4、13、22—24，§3、参考文献、附录C.1。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是非显然的表达能力边界统一，超出单一局部性能改进；但仍在既有padding—circuit路线内，不足以判为L3。", "central_increment": "在充足volume和指定定点条件下，补齐常宽TC^0、常精度循环AC^d及注意力类型之间的联系。", "soundness_observation": "附录有完整证明链条的文本，但未完成独立证明审计。另有明确范围疑点：Lemma 5.1仅要求r(N)d(N)≥1，证明援引的uniformity collapse却限定d≥1的多对数深度；应收紧陈述，不直接否定其在本文循环主定理中的应用。\n", "significance_observation": "为理论分析选择等价模型提供依据；没有证明这些构造可被训练学得或具备现实推理效率。", "main_open_question": "§C.1的精确模拟能否在§A.3逐子步舍入语义下覆盖并列最大值、舍入中点及饱和边界，而不仅是实数近似？"}

limitations：[{"text": "不足volume的紧刻画、具体问题的最小padding量及可学习性未解决；作者明确提醒结论尤其上界未必迁移到浮点算术。", "basis": "author_report", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页8—9，§6—7。\n"}, {"text": "PE可携带电路结构和模型自身不能计算的除法、取模结果，另允许分块layer normalization与同阶内部高精度；不能把结果理解为现成模型加少量pause tokens即可获得同等能力。", "basis": "model_inference", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页16—18，附录A.4。"}, {"text": "仅分别分析常数、对数及多项式精度，不能自动外推到所有介于常数与对数之间的增长精度；AC^d/TC^d刻画也未给出d≥1时逐阶严格分离。", "basis": "model_inference", "locator": "TEXT_OR_nBuL6HywFX_a2c6e83a295a：物理页15、17，附录A.2、A.4。"}]

minimal_check：{"question": "Lemma 3.1的舍入一致性是否存在边界反例？", "control": "构造单层注意力：两个并列最大分数的value均值落在Fb舍入中点，再加入一个非最大项；对照原AHAT与按式(34)选温度的SMAT。", "observable_outcome": "严格按附录A.3记录每个子步骤，比较最终Fb坐标是否一致。", "resources": "纸笔定点核算即可起步；可辅以有理数检查器，无需训练。自动枚举成本未估计。", "failure_or_stop_condition": "任一满足假设的输入产生不同输出即暴露该模拟步骤缺口；有限例子全部一致不构成全称证明。"}

missing_fields：["原PDF图像、前作全文及其他版本未提供。", "训练数据、学习实验、硬件与实测运行成本未报告；本篇为理论研究。", "当前附件是否最终出版版未核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

宽度、精度、uniformity与额外位置计算的拆分有理论价值；继续阅读应优先补齐精确舍入语义与引理范围，再把结论用于架构等价判断。

身份及理论建模范围：33页官方当前附件与全文输入返回绑定一致。本篇是语言识别的理论刻画，无训练或实测速度结果。采用L-uniform按长度生成的模型/PE、多项式padding、逐子步定点舍入，允许同阶内部高精度和分块layer normalization；这些条件不是现成固定模型加少量pause token。

核查定位：text_delivery_manifest.json, structured/pro050.json, p015–p018, A.2–A.5；source_and_model_scope_confirmed

宽度精度及循环的中心结论：Theorem4.2在volume bD至少对数量级且宽度至多多项式时，常精度对应L-uniform AC0、对数精度对应L-uniform TC0；常精度因此需要至少对数宽度，对数精度可以常宽。Theorem5.1则限定d>=1、Θ(log^d N)循环，常精度对数宽与对数精度常宽分别对应FO-uniform AC^d/TC^d。没有给所有次对数增长精度的统一刻画，也不代表d>=1时逐阶严格分离已证。

核查定位：p005, Lemma4.1, p006, Theorem4.2, PDF physical page 7, Theorem5.1, p017:L0025-L0030；central_bounds_and_conditions_confirmed

位置信息和精确模拟的额外资源：常宽构造以二维unit-length PE替换对数宽二进制地址，PE仍可携带电路连线。A.4.2明确PE可预计算模型自身不能在线计算的除法、取模。Lemma3.1还用随N变化且logspace可算的温度与b'=κb内部精度，不能转述为固定温度fully uniform softmax与hard attention无条件等价。

核查定位：p018:L0020-L0028, PDF physical pages 23–24, C.1 Steps3–5 and C.2, p005:L0006-L0016；simulation_resource_boundary_confirmed

精确舍入论证的待补环节：原PDF第23页Step2定义h为不舍入的实数层输出，Step3却将其作为Fb网格值使用；小于半格的两实数误差一般不足以保证它们舍入相同。A.3又要求每子步舍入、平局取更大绝对值。应补证相对真实定点AHAT输出的界、舍入中点和饱和边界，或给出逐子步一致性构造。本地没有完整构造满足全部架构条件的反例，因此这是可定位的论证缺口，不是已否定Lemma3.1。

核查定位：p016:L0005-L0023, PDF physical page 23, Steps2–4, PDF physical page 24, Step5；proof_bridge_requires_further_check

uniformity引理陈述范围：Lemma5.1允许r(N)d(N)>=1的任意多项式可算函数；第27页Step2却援引d>=1的AC^d/TC^d uniformity collapse，不能仅凭乘积>=1覆盖常深等全部情形。主循环应用在Θ(log^d N)、d>=1范围内，故记录为引理陈述需收紧或补证，不据此直接否定本文主循环定理。

核查定位：p006, Lemma5.1, p026:L0027-L0035, p027:L0013-L0015 and L0047-L0055；lemma_scope_mismatch_confirmed

本地补充/限定：["核对原PDF后将精确模拟问题定位到实数层输出与定点网格输出之间的证明桥梁；没有把泛化的舍入反例当成完整Transformer反例。", "确认uniformity引理范围问题，保留其在主文多对数循环设定下的独立适用可能。"]

核查局限：["未做完整形式化证明审计或枚举Transformer舍入反例；最小检验仍为建议。", "未独立核读被继承的电路、PE及模拟前作，L2为AI暂评。", "本地未逐步复核全部常数精度寻址和电路求值构造。", "Pro读全文文本，本地核查列示页并观察三页原PDF，无实验实测。"]

