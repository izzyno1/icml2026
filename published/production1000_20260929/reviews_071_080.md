# 单轮全文初评与有界本地核对 71–80

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro071 · TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering

论文 OR_KMwrxaoAW4；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_KMwrxaoAW4_0adabf07d26d", "source_url": "https://api2.openreview.net/pdf?id=KMwrxaoAW4\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "623844c9bfe60cccad8aab70dcc06e58f21d5eab1af7838003a917d892865d8a", "source_pdf_sha256": "0adabf07d26d445b2a95ee25c5f881f287b181e7639218585dd1b7de3bd05bc4"}], "read_ranges": ["TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页1–18全部提供文本，包括正文、参考文献及附录A–C；连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–8仅有图题及部分残留文字，不能读取图5曲线数值。", "双栏文字及表7–8局部交错，部分公式比值排版失真；采用可明确对应的表格和正文数值。", "未提供原始数据、代码及前作全文；当前附件的最终出版版本身份未核实。"]}

问题：仅依据早期实验序列及活性，排序后期首次出现的TadA变体，识别有限实验预算下的高活性候选。

方法：轮内按富集比排序，仅连接相邻序列；跨轮重复序列充当锚点。强连通分量内贪心删除反馈边，以TadA8e=1为参考，沿最少边路径按方向累加对数比率赋分。DNA经T→U形成RNA视图，同义DNA活性取均值得蛋白标签；基线用冻结编码器和两层MLP预测排序分数。

作者主张：提供兼具时间回放、百万变体覆盖及统一标签的TadA工程基准。

论文证据：31轮产生1,027,200条DNA序列及对应RNA视图，归并为409,869条蛋白序列；报告三视图划分间精确序列重叠均为0。

模型推断：构成有实质价值的纵向实验数据资源；百万规模不是百万种不同蛋白，也不是三种独立实验模态。

定位：['TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页15，B.3。\n', 'TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页17，表6。\n']

作者主张：Seq2Graph将噪声、多批次富集测量统一为稳定的相对活性标签。

论文证据：给出稀疏构图、去环及赋分流程，并报告GFP排序验证和两种子采样稳定性分析。

模型推断：增量是数据集成方案，不是新图论原语；去环本身不保证多路径比率一致。

定位：['TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页5，§3.4–3.5；物理页15，B.1–B.3']

作者主张：随机插值强但未来排序和有限预算筛选弱；相关区域覆盖比局部密采样更有效。

论文证据：表1–4及7–8报告基线与适配诊断；§4.3报告短名单命中率；§4.4正文报告训练子集比较趋势。

模型推断：支持该实验活动上的泛化缺口，不能外推为普遍机制；所谓diversity实际依据验证序列相似性选样。

定位：['TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页6–8，§4.2–4.4；物理页18，表7–8']

key_results：[{"setting": "蛋白视图：时间切分训练/验证/测试为256,429/45,208/108,232条；对照为全数据随机8:1:1切分。", "baseline": "同一ESMC-600M冻结编码器，在两种划分下训练MLP。", "metric_or_guarantee": "测试Spearman ρ及Recall@10%，均无量纲。", "reported_values_and_units": "时间切分ρ=0.0509、Recall=0.1180；随机切分ρ=0.8079、Recall=0.2317。", "information_and_compute": "MLP训练20 epochs，1 epoch预热；学习率从{3e-5,1e-4,3e-4}按验证表现选择。硬件和时长未报告。", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页5，§4.1；物理页6，表2；物理页7，表4；物理页17，C.3。\n \n"}, {"setting": "固定时间切分下的全参数微调及prompt tuning；报告已检查设置中的最佳测试相关性。", "baseline": "冻结编码器探针的低相关表现；不是所有模型逐一对应的改进比较。", "metric_or_guarantee": "测试Spearman ρ。", "reported_values_and_units": "全调ESM2-8M、lr=1e-4：0.0553；全调NT-500M、lr=3e-5：0.0630；NT-50M prompt采用uniform/prepend、长度32、层0：0.0754；ESMC-300M prompt采用uniform/prepend、长度1、层10：0.0266。", "information_and_compute": "表7列三种学习率；表8列prompt配置。总搜索算力和运行时长未报告。", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页18，表7–8。\n"}, {"setting": "蛋白未来测试集；按ESM2-35M、ESMC-300M排序，分别选96或384个候选。", "baseline": "均匀随机选择的top-5%命中率期望为5%。", "metric_or_guarantee": "入选候选中真实top-5%占比，以及top-1%命中数。", "reported_values_and_units": "依上述模型顺序，K=96时为3.1%/4.9%；K=384时为4.3%/4.2%；两模型两预算下top-1%命中数均为0。", "information_and_compute": "离线固定候选回放，没有实际新增96或384次湿实验；重复及平均口径未说明。", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页7，§4.3。\n"}, {"setting": "选择部分关键变体做GFP独立测量；分别保留50%轮次或每轮50%序列重跑标签流程。", "baseline": "GFP对照NGS排序；子采样标签对照完整数据标签。", "metric_or_guarantee": "Spearman ρ。", "reported_values_and_units": "GFP与NGS排序ρ>0.99；轮次子采样ρ=0.90；序列子采样ρ=0.95，后两者均p<1e-5。", "information_and_compute": "作者报告原始测序每轮>100G bases；GFP样本量、重采样次数及构图资源未报告。", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页8，§4.5；物理页14，A.2.3–A.2.4。\n \n \n"}]

prior_work_candidates：[{"citation_as_printed": "Notin, P., Kollasch, A., Ritter, D., Van Niekerk, L., Paul, S., Spinner, H., Rollins, N., Shaw, A., Orenbuch, R., Weitzman, R., et al. ProteinGym: Large-scale benchmarks for protein fitness prediction and design. In Advances in Neural Information Processing Systems, volume 36, pp. 64331–64379, 2023.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "蛋白适应度排序评测及指标实践。", "claimed_difference": "本篇强调单一实验活动的31轮时间回放，而非广泛汇编不同蛋白的DMS数据。", "basis": "target_paper_only", "target_locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页3，§2.1；物理页10，参考文献；物理页17，C.1", "prior_actually_read": false}, {"citation_as_printed": "Dallago, C., Mou, J., Johnston, K. E., Wittmann, B. J., Bhattacharya, N., Goldman, S., Madani, A., and Yang, K. K. FLIP: Benchmark tasks in fitness landscape inference for proteins. In Advances in Neural Information Processing Systems Datasets and Benchmarks, 2021.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "蛋白适应度景观预测基准。", "claimed_difference": "本篇以单TadA实验活动的深度、统一标签和后期排序为互补定位，未直接复评FLIP。", "basis": "target_paper_only", "target_locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页3，§2.1；物理页9，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Eades, P., Lin, X., and Smyth, W. F. A fast and effective heuristic for the feedback arc set problem. Information processing letters, 47(6):319–323, 1993.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "反馈弧集贪心去环启发式。", "claimed_difference": "本篇将已有启发式用于富集图清洗，明确不主张新图论算法。", "basis": "target_paper_only", "target_locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页5，§3.4；物理页9，参考文献；物理页15，B.2", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可回放的纵向实验资源及配套证据，超出单项性能优化；不宜提升为新自主科研路线或新图学习框架。", "central_increment": "前作已有适应度预测基准与去环组件（本篇转述）；本作在单一TadA活动下新增31轮百万核酸变体的统一标签和时间排序接口，证据为数据规模、划分审计及基线落差；尚待排除未来测量进入训练标签。", "soundness_observation": "独立报告器与子采样支持部分标签可靠性，但随机插值可学不等于全库标签准确；去环也不保证所有相对比率一致。", "significance_observation": "为模型进入昂贵闭环实验前提供有用筛查任务；目前意义限于该TadA细胞活性场景。", "main_open_question": "按全文描述，Seq2Graph使用全部31轮建图；后期测量是否经锚点、路径或同义聚合改变了训练标签，从而偏离仅使用早期实验信息的任务定义？"}

limitations：[{"text": "固定候选、单TadA细胞功能评分，不是纯催化常数，也不评估提案、规划或自主湿实验；Cas9仅为构建示例。", "basis": "author_report", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页4，§3.2；物理页8，Limitations；物理页16，B.4"}, {"text": "序列不重叠不能排除标签构建的信息泄漏；尚无仅凭1–27轮生成训练标签的依赖审计，此处是风险而非已证实泄漏。", "basis": "model_inference", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页15，B.1–B.3；物理页17，C.2"}, {"text": "随机与时间切分训练量及分布不同；coverage分析又使用验证序列选样，不能将结果解释为通用因果规律或可部署采集策略。", "basis": "model_inference", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页5，§4.1；物理页7–8，§4.4"}, {"text": "GFP样本量、重复次数和主结果误差条缺失；缺少简单序列基线及标签构建对照，尚不足以完全定位失败来源。", "basis": "model_inference", "locator": "TEXT_OR_KMwrxaoAW4_0adabf07d26d：物理页6–8，§4.2–4.5；物理页14，A.2.4；物理页17–18，C.3–C.4"}]

minimal_check：{"question": "训练标签是否依赖未来轮次测量？", "control": "比较原31轮构图与仅1–27轮构图，固定参考序列及确定性规则，仅审计两者共有且可达的早期变体。", "observable_outcome": "比较训练标签相对比率、排序及覆盖率，并追踪差异涉及的未来锚点或传播路径。", "resources": "逐轮测量、序列轮次记录和Seq2Graph实现；不需新湿实验，CPU、内存与时间需求未知。", "failure_or_stop_condition": "移除未来测量后早期相对标签改变，则严格历史信息隔离未成立；缺逐轮数据或可重建实现则停止，保留未核实状态。"}

missing_fields：["图像及图5定量曲线。", "原始数据、代码可运行性和前作全文；所列前作未提供显式标识符。", "GPU、显存、运行时长、总费用及部分训练实现细节。", "GFP样本量、重复次数、重采样次数及主结果不确定性。", "训练标签的时间依赖审计、重复序列跨轮归属的具体处理规则。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

纵向基准有价值，但严格未来发现结论首先需要训练标签不依赖未来轮次的构图/聚合审计。

身份、规模与任务分母：完整题名与18页附件相符。1027200是DNA序列数，RNA只是T→U映射，蛋白为同义归并后的409869条，非百万不同蛋白或三种独立实验。训练1–27轮、验证28、测试29–31；为固定候选离线排序，未做自主提案或新增湿实验。

核查定位：p001 title, p005, Section4.1, PDF physical page15, B.3；identity_dataset_grain_and_replay_scope_confirmed

时间隔离仍未证明：原B.1明确合并全部31轮构图、节点平均出现1.58轮，再去环和最少边路径赋分，同义标签也统一平均。原表6只确认序列零重叠；500查询×5000训练子样本Hamming不是全库最近邻审计。未来测量是否改变早期标签需只用1–27轮重建核对，目前是未排除依赖风险，未证实实际泄漏。

核查定位：PDF physical page15, B.1–B.3, PDF physical page17, Table6/C.2；sequence_disjointness_confirmed_label_temporal_independence_unverified

排序分数与有限预算命中率：原表2/4确认ESMC600M时间/随机Spearman .0509/.8079、Recall@10% .1180/.2317。随机训练为80%全库、时间训练256429条，分布及训练量不同；不能只归因为时间。原正文K96命中真实top5%为3.1%/4.9%，K384为4.3%/4.2%，top1%均零。未说明重复平均口径，保留百分比原报值而不反推非整数命中数；这些不是新实验完成数。

核查定位：PDF physical page6, Table2, PDF physical page7, Table4/Section4.3, p005, split counts；decisive_metrics_and_hit_rate_scope_confirmed

Seq2Graph的一致性范围：去有向环可消除排序环，不保证比率多路径一致。例如DAG a→b比2、b→c比2、a→c比3无环，但路径乘积4与3不同。所选最少边路径提供一种确定标签，不验证所有测量兼容；较大比率更可靠也属假设。GFP相关>.99及两类50%子采样相关.90/.95是局部支持，缺样本量/重复数，不能认证全库真值。

核查定位：PDF physical page15, B.2–B.3, p008, Section4.5；acyclicity_and_ratio_consistency_distinguished

覆盖诊断的目标信息：Diversity实际按与验证序列相似性选样，Round也用验证相似性；未用验证活性训练，但这是目标序列已知的诊断，不是无未来信息的普遍采集策略。适配表3取已检查设置中的最佳测试相关作为上界诊断，不能当规范选参榜单。

核查定位：PDF physical page7, Section4.4, p008, continuation, PDF physical page6, Table3 caption；validation_aware_selection_scope_confirmed

本地补充/限定：["补充Hamming距离只基于500×5000子样本，非全库近邻结果。", "百分比短名单命中口径未明，不将其转换为确定整数湿实验计数。"]

核查局限：["未取得/重建原数据或图，未核实发布可用性和实际标签泄漏。", "未执行作者代码、模型训练或生物实验，也未核读前作。", "第1页仅读标题开头；未读取图5数值，版本角色未确认。"]


## pro072 · scDEBART: Predicting in silico Single-Cell Perturbation Responses via Large-Scale Differential Expression Learning

论文 OR_pJyidZg93y；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_pJyidZg93y_780263ff87f3", "source_url": "https://api2.openreview.net/pdf?id=pJyidZg93y\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "abdfcd3e954950da42445e24f2b9d50d9f672ef945651e88fb35843117c188f8", "source_pdf_sha256": "780263ff87f3093087ddc12b83e1c4ad77891b79a296e4f962ccda9e92af04b5"}], "read_ranges": ["TEXT_OR_pJyidZg93y_780263ff87f3：物理页1–33连续全文，包括正文§1–5、参考文献、附录A.1–A.11及全部图表的提取文字。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未见页标缺口，但仅收到文本，未查看原PDF；图1–17的图像不可见，不从零散坐标推算数值。", "双栏顺序及公式排版局部失真；表1–4文字可读，不能核验图形、误差条及未被正文报告的数值。"]}

问题：给定对照表达与扰动靶基因，预测群体层面的logFC和差异表达基因排序，并检验反向识别及药物迁移。

方法：以scVI计算细胞群间后验logFC，筛选双侧检测率≥0.3、Proba-DE≥0.8及变化幅度≥1.5倍的基因。融合基因先验、基线表达和logFC，用8层编码器/4层解码器BART遮蔽15%基因，以0.8倍logFC损失加0.2倍嵌入损失重建。微调时改用±10扰动指示，预测至多5000个HVG的群体响应，优化加权MSE与全局/高变化基因相关性。

作者主张：通过大规模差异表达预训练和可靠监督，学习更适合扰动预测的共调控变化模式。

论文证据：从66,611,859个人类细胞、617个数据集构建6,282,796个差异谱；Norman消融中去掉预训练使top-50 EF下降14.8%。

模型推断：构成任务对齐的表征与数据流程增量；观察性群体差异不等于因果干预，实验尚未直接证明学到了调控机制。

定位：['TEXT_OR_pJyidZg93y_780263ff87f3:p002–p004，§1、§3', 'TEXT_OR_pJyidZg93y_780263ff87f3:p014，A.1.7；p026–p027，A.7、表3']

作者主张：显著改善扰动响应预测，并支持反向扰动识别及跨模态药物迁移。

论文证据：五集主评测、DESeq2替代评测、7例反向识别及65种药物测试提供支持；优势集中于DEG恢复，并非所有指标均领先。

模型推断：支持条件内预测改进和初步迁移，不足以建立通用药物响应能力。

定位：['TEXT_OR_pJyidZg93y_780263ff87f3:p005–p008，§4', 'TEXT_OR_pJyidZg93y_780263ff87f3:p025–p026，A.6.2']

key_results：[{"setting": "Norman K562、Replogle K562/RPE1、Nadig HepG2/Jurkat；80/10/10扰动基因划分，三种子，top-50评测。", "baseline": "GEARS、scGPT、MLP、LR，各有scVI及counts设置；scVI-MLP/LR直接预测logFC，其余通过绝对表达转换。", "metric_or_guarantee": "EF与cosine similarity，均无量纲。", "reported_values_and_units": "作者汇总平均EF为11.96，对比scGPT 1.74、GEARS 2.99；cosine仅两集第一、三集第二。", "information_and_compute": "每扰动生成50组、每组1000次后验抽样的差异谱。作者报告预训练4×H100 80GB、113小时，即452 GPU小时；微调每数据集10–50 H100 GPU小时。", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p002，贡献汇总；p005，§4.1；p018，A.2.3；p028，A.10。\n \n"}, {"setting": "Norman K562消融，top-50，表3标注三种子中位数±标准差。", "baseline": "相同scDEBART架构，不做预训练。", "metric_or_guarantee": "EF及方向分类F1。", "reported_values_and_units": "完整模型EF 14.901±4.919，无预训练12.693±4.865；F1分别0.684±0.182与0.616±0.187。不能与主实验均值直接混合。", "information_and_compute": "相同80/10/10划分；消融运行成本未单列。", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p026–p027，A.7.1、表3。\n"}, {"setting": "五集DESeq2 pseudobulk替代评测，top-50，三种子；DEG按Wald统计量选择。", "baseline": "GEARS、scGPT及counts-MLP/LR等；scVI-MLP/LR因预测不随扰动变化而被排除。", "metric_or_guarantee": "EF与cosine similarity。", "reported_values_and_units": "EF四集第一；Replogle K562为5.10，低于scVI-GEARS的6.89，排名第三。Norman cosine为0.365，低于scVI-GEARS的0.483，排名第六。", "information_and_compute": "同批细胞随机分成至多三个pseudobulk重复，属于替代分析流程，不是独立生物学重复实验。", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p025–p026，A.6.2；p031，图14图注。\n"}, {"setting": "Norman最常扰动的20个基因，57个已观测组合按47/3/7划分；从210个单/双扰动候选检索。", "baseline": "scGPT、GEARS。", "metric_or_guarantee": "按logFC欧氏距离排序的top-1精确匹配。", "reported_values_and_units": "scDEBART为5/7，即71.4%；作者bootstrap 95%区间28.6%–100%；两个基线均0/7。", "information_and_compute": "生成210个候选响应；测试样本仅7个。", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p007，§4.2。\n"}, {"setting": "Replogle K562模型迁移SCIPLEX K562，65/188种药物，10、100、1000、10000 nM，top-20。", "baseline": "scVI-scGPT。", "metric_or_guarantee": "cosine、EF与方向F1。", "reported_values_and_units": "scDEBART cosine随剂量由0.04升至0.30；EF 2.91–4.32，对照0.36–0.95；F1 0.05–0.09，对照0.03–0.24，并非全面领先。", "information_and_compute": "预测器无药物微调，以靶标同时抑制近似药物；SCIPLEX仍另拟合scVI计算标签，评测采用三种子。", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p008，§4.3；p024，A.5。\n"}]

prior_work_candidates：[{"citation_as_printed": "Cui, H., Wang, C., Maan, H., Pang, K., Luo, F., Duan, N., and Wang, B. scGPT: toward building a foundation model for single-cell multi-omics using generative AI. Nature Methods, 21(8):1470–1480, August 2024.", "identifier_if_present": "doi:10.1038/s41592-024-02201-0", "relation_candidate": "比较基线", "shared_component": "基因Transformer与大规模预训练。", "claimed_difference": "本文转述：从静态表达重建转向基线条件化差异表达学习。", "basis": "target_paper_only", "target_locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p002，§2.2；p010，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Roohani, Y., Huang, K., and Leskovec, J. Predicting transcriptional outcomes of novel multigene perturbations with GEARS. Nature Biotechnology, 42(6):927–935, June 2024.", "identifier_if_present": "doi:10.1038/s41587-023-01905-6", "relation_candidate": "比较基线", "shared_component": "利用基因先验预测单/多基因扰动。", "claimed_difference": "本文采用差异谱预训练而非GEARS式图消息传递。", "basis": "target_paper_only", "target_locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p002，§2.2；p011，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Lopez, R., Regier, J., Cole, M. B., Jordan, M. I., and Yosef, N. Deep generative modeling for single-cell transcriptomics. Nature Methods, 15(12):1053–1058, December 2018.", "identifier_if_present": "doi:10.1038/s41592-018-0229-2", "relation_candidate": "组件复用", "shared_component": "scVI去噪表达及后验差异表达。", "claimed_difference": "复用scVI生成监督，再训练扰动预测器；未提出新的scVI模型。", "basis": "target_paper_only", "target_locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p002，§2.1；p010，参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "差异表达监督、语料构建及任务衔接形成实质能力增量，且有多集与替代DE流程支持；不足以称路线级突破。", "central_increment": "前作已有表达预训练、图扰动预测和scVI差异分析（均据本文转述）；本作把群体差异组织成大规模任务监督，新增可靠DEG恢复能力，尚待排除评测和训练配置的贡献。", "soundness_observation": "实验支持预测价值而非因果机制。按所列损失，独立可学习α、γ存在共同趋零的退化方向，需核实际实现与权重轨迹。\n", "significance_observation": "对筛选可靠响应基因有实用价值；收益不能外推为逐细胞响应分布或普适药理预测。", "main_open_question": "统一真值与可检出候选基因域后，主要EF优势是否仍成立，而非主要来自筛选、输出转换或基线配置差异？"}

limitations：[{"text": "作者承认scVI偏置、低表达基因覆盖损失、药物靶标不完整及逐数据集微调的局限。", "basis": "author_report", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p009，§5"}, {"text": "A.4.3称评测限制检测率≥0.3，A.6.1却分析基线低检测率预测；预测排序、真值与EF分母是否应用同一筛选域不清。共同logFC尺度也不自动意味着共同真值，不能据此直接判定实现错误。", "basis": "model_inference", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p022，A.4.3；p024–p025，A.4.4、A.6.1"}, {"text": "scVI、PS阈值及HVG选择与测试集的隔离未明确；GEARS训练20轮、scGPT仅部分模块10轮。去过滤消融同时更换评测数据，不能纯归因于训练质量。", "basis": "model_inference", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p017–p018，A.2；p023，A.4.4；p026，A.7.1"}, {"text": "噪声实验仅单种子且只改微调标签；反向测试仅7例。药物输入未编码剂量，剂量升高时匹配改善不等于模型学到了剂量响应。", "basis": "model_inference", "locator": "TEXT_OR_pJyidZg93y_780263ff87f3:p007，§4.2；p024，A.5.3；p027–p028，A.9"}]

minimal_check：{"question": "EF优势是否依赖不同候选基因域或真值处理？", "control": "固定一份共同logFC真值及各模型共同可输出、双侧检测率≥0.3的基因集合，在排序前统一筛选，并用同一集合计算EF随机期望。", "observable_outcome": "对照原口径，比较逐扰动top-50交集数、EF及模型排名。", "resources": "需要各模型逐基因预测、检测率、原始真值与划分；无需重训，具体耗时和内存未知。", "failure_or_stop_condition": "若优势消失或反转，则原优势不能排除评测域影响；缺原始预测或筛选定义时停止归因。"}

missing_fields：["图像及仅存在于图形中的数值。", "语料构建、全部scVI拟合和重复试验总成本，推理时延及参数量。", "预处理隔离、统一评测域和真值转换的实现细节。", "前作全文、其他版本及代码权重的实际核验；本轮未搜索或复现。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

差异谱预训练和DEG恢复有实证价值；优先查统一真值/候选域及权重实现，再解释相对机制优势。

身份及预测对象：完整题名与33页附件绑定。核心是群体scVI差异表达谱的BART预训练，再用扰动指示微调预测logFC；66.6M细胞产生6.28M差异谱。观察性群体差异不是因果机制标签，也不是生成逐细胞响应分布。

核查定位：p001 title, p004, Figure1 and input/objective, p005, Section4.1；identity_and_prediction_grain_confirmed

决定性EF指标依赖评测集合：原A.4.3要求双侧检测率≥.3，EF=(交集+.05)/(Kpred Ktrue/|G|+.05)。A.6.1却报告若干基线top50检测率中位数.09–.28；这可能是筛选前诊断，尚不明确排序/真值/分母是否同域。绝对表达转logFC还分别用平均或配对control，共同尺度不证明共同真值。不能只按EF倍数推出机制更准。

核查定位：PDF physical page22, Eq3 and filter paragraph, p024, conversion protocol, p025, A.6.1；metric_formula_confirmed_common_domain_requires_implementation_audit

消融与替代真值：原表3完整/无预训练EF14.901±4.919/12.693±4.865，标为三种子中位数±标准差；不能混同主实验均值。去过滤组还在自己的未过滤数据上评估，混合了训练/测试变化。原图14与A.6.2确认DESeq2下EF四集第一，ReplogleK562为5.10低于6.89；Norman cosine .365低于.483、排第六。DESeq2重复是同批细胞随机分组，不是独立生物实验。

核查定位：PDF physical page27, Table3, p025–p026, A.6.2/A.7.1, PDF physical page31, Figure14；mixed_empirical_results_and_ablation_confound_confirmed

可学习损失权重的退化方向：原p5及A.4.2均写alpha、gamma独立sigmoid并联合最小化alpha*非负MSE+gamma*非负相关损失，无和为1约束。固定预测时让两权重趋零可让该数据目标趋零，故损失下降本身不证明预测改善。实际优化另含AdamW及早停，未读取代码/权重轨迹，不能宣称实际训练已退化。预训练alpha=.8固定不受此问题影响。

核查定位：p004, objectives, PDF physical page5, trainable scalar paragraph, p021, A.4.2；objective_degeneracy_direction_confirmed_actual_training_unknown

小样本迁移和资源范围：反向任务只有7测试、5命中；0/7或7/7的退化bootstrap区间不表示总体成功率确定为0或1。药物只65/188且K562/抑制靶标，输入未显式编码剂量，随剂量更匹配不证明学习剂量响应。预训练4×H100×113小时=452GPU小时，逐数据集微调10–50GPU小时，尚不含语料构建及全部scVI成本。

核查定位：p007, Section4.2, p008, Section4.3, p024, A.5, p028, A.10；small_sample_generalization_and_compute_limits_confirmed

本地补充/限定：["明确损失权重问题是所印数据目标的退化方向，未证实含AdamW的实际训练发生坍塌。", "去过滤消融同时更换评测集，反向识别bootstrap边界区间不提供总体确定性。"]

核查局限：["未执行模型训练、预测重评或生物实验；未核读前作。", "未取得权重轨迹、逐基因预测或预处理划分，评测问题仍是未排除风险。", "第1页仅读标题开头；本地只查列明页段与图，版本角色未确认。"]


## pro073 · TerraBind: Fast and Accurate Binding Affinity Prediction through Coarse Structural Representations

论文 OR_xlevHY3oJO；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7", "source_url": "https://api2.openreview.net/pdf?id=xlevHY3oJO\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：物理页1–25全文；正文1–9、参考文献9–12、附录A–C 13–25；页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["只有全文抽取文本，未看PDF图像；图中部分数字标签可读，曲线、误差条及几何细节不可核验；双栏和部分公式排版失真。", "当前附件不能确认是最终出版版；未提供前作全文，未外搜或复现。"]}

问题：能否绕过全原子扩散，直接用口袋级结构表示预测亲和力，同时保留配体姿态与可靠的不确定性？

方法：冻结ESM-2/COATI-3编码后，48层Pairformer预测蛋白Cβ（甘氨酸Cα）与配体重原子的64档距离；6层亲和力模块直接读取潜变量和距离概率，输出结合概率及pIC50。可选Adam距离拟合生成坐标，不参与亲和力推断。距离熵HLP表征结构不确定性；epinet共享随机索引生成联合预测，GP条件化更新后用EMAX选批。

作者主张：粗结构足以兼顾姿态和亲和力，约26×加速且相关性提升16–20%。

论文证据：公开姿态集、CASP16和18个私有assay提供支持；3/6个晶体微调结构模块而冻结亲和力模块，作者报告约17%相关性提升。

模型推断：支持特定小分子任务的实质成本—精度改进，不证明全原子结构普遍多余。

定位：['TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p3，§2.2；p6–8，§3；p18，A.7–B.1']

作者主张：epinet提供校准不确定性，并支持持续学习和风险对冲选批。

论文证据：低IQR对应更高±1 pIC50命中率；Target I回放报告6×IC50改善，非真实新实验。

模型推断：主要是既有联合预测与贝叶斯选批的集成；误差排序不能证明概率校准。

定位：['TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p4–5，§2.4；p8，§3.2.3–4；p17–18，A.6；p20，表3']

key_results：[{"setting": "196-token复合物，10个姿态样本及亲和力预测", "baseline": "Boltz-2", "metric_or_guarantee": "作者报告的推理时延", "reported_values_and_units": "1.045 vs 27.8秒/复合物，26.6×；纯亲和力配置为17.01×，此时Boltz-2保留5个扩散样本。", "information_and_compute": "单A6000、bfloat16、相同cuEquivariance；包含编码器，不含MSA生成；初始全蛋白定位成本是否摊入不清。", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p6，§3.1.3；p18，A.8/B.1。\n \n"}, {"setting": "FoldBench n=556；PoseBusters n=307；Runs N’ Poses n=2687", "baseline": "Boltz-1，非Boltz-2", "metric_or_guarantee": "RMSD<2Å；同时满足LDDT-PLI>0.8的联合成功率", "reported_values_and_units": "按上述数据集顺序，TerraBind/Boltz-1的RMSD成功率为55.3%/55.1%、68.8%/69.7%、62.5%/61.3%；联合成功率为45.1%/47.3%、55.1%/58.6%、49.7%/54.4%。仅据图3明确文字标签。", "information_and_compute": "10候选择优；TerraBind按优化损失、Boltz-1按ipTM；均用Cβ与配体重原子评测。", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p5–6，§3.1.1/图3。\n"}, {"setting": "CASP16；全体私有数据27075分子、18个assay", "baseline": "Boltz-2 Affinity", "metric_or_guarantee": "Pearson相关，提升为相对比例", "reported_values_and_units": "表8：L3000（n=123）0.725/0.625，+16%；L1000（n=17）0.470/0.470，持平。正文私有数据报告约+20%，15/18靶点胜出。", "information_and_compute": "TerraBind/Boltz-2；公开与私有设置分开，私有结果不可独立复算。", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p2、p7，§3.2.1；p24，表8。\n \n"}, {"setting": "私有assay分任务评测，binder定义pIC50>5", "baseline": "Boltz-2 Affinity及Combined", "metric_or_guarantee": "hit-finding AUROC；hit-to-lead Pearson", "reported_values_and_units": "每类≥50分子的13个assay：AUROC为TerraBind 0.802、Affinity 0.765、Combined 0.835。≥50个binder的14个assay：Pearson 0.470/0.491；≥100个binder的10个assay：0.536/0.486（TerraBind/Affinity）。", "information_and_compute": "同一私有数据的不同子集，非独立验证；Combined额外使用二分类头。", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p23–24，表6–7。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A. J., Bambrick, J., and Jumper, J. M. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature, 630(8016):493–500, 2024.", "identifier_if_present": "doi:10.1038/s41586-024-07487-w", "relation_candidate": "方法继承", "shared_component": "Pairformer三角注意力/乘法", "claimed_difference": "移除single表示与扩散，专注粗距离。", "basis": "target_paper_only", "target_locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p3，§2.2.1；p9参考文献；p13，A.1", "prior_actually_read": false}, {"citation_as_printed": "Passaro, S., Corso, G., Wohlwend, J., Reveiz, M., Thaler, S., Somnath, V. R., Getz, N., Portnoi, T., Roy, J., Stark, H., Kwabi-Addo, D., Beaini, D., Jaakkola, T., and Barzilay, R. Boltz-2: Towards accurate and efficient binding affinity prediction. bioRxiv, 2025.", "identifier_if_present": "doi:10.1101/2025.06.14.659707", "relation_candidate": "比较基线", "shared_component": "结构条件化亲和力模块、相对损失和诱饵策略", "claimed_difference": "直接读取预测距离分布，非扩散坐标生成的distogram。", "basis": "target_paper_only", "target_locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p4–5，§2.4；p11参考文献；p23–25，附录C", "prior_actually_read": false}, {"citation_as_printed": "Wang-Henderson, M., Kaufman, B., Williams, E., Pederson, R., Rossi, M., Howell, O., Underkoffler, C., Mardirossian, N., and Parkhill, J. Pretrained joint predictions for scalable batch bayesian optimization of molecular designs. arXiv preprint arXiv:2511.10590, 2025.", "identifier_if_present": "arXiv:2511.10590", "relation_candidate": "组件复用", "shared_component": "epinet联合预测与EMAX批量选择", "claimed_difference": "接入粗结构共折叠亲和力模型。", "basis": "target_paper_only", "target_locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p4–5，§2.4；p8，§3.2.4；p12参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "结构表征重构带来显著推理收益及有条件的预测改进，超出单点调参；不是全新Pairformer或贝叶斯优化路线。", "central_increment": "Boltz-2已联合结构与亲和力预测（仅本篇转述）；本作在药物样口袋内新增无需生成坐标的亲和力通路，支持证据为时延与基准结果；尚待排除监督和输出头口径差异。", "soundness_observation": "无独立复现；RMSD接近但联合结构指标较低；IQR分桶是风险分层，不是充分校准验证。", "significance_observation": "具有高吞吐推断价值；工程依赖大规模预训练和蒸馏，约30M仅指可训练参数，不含650M ESM-2等冻结编码器。", "main_open_question": "整体亲和力优势中，有多少来自区分活性/阴性，而非对已知binder的更准确排序？"}

limitations：[{"text": "粗坐标限制全原子物理管线；大体系优化、远程变构/细胞背景及偏乐观的高斯不确定性仍受限。", "basis": "author_report", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p8–9，§4"}, {"text": "不能概括为全面胜过Boltz-2：Combined的hit-finding AUROC更高，binder排序优势随样本过滤变化。", "basis": "model_inference", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p23–24，表6–7"}, {"text": "正文称两个CASP16靶点Pearson均改善，表8的L1000却持平；表4/5与图3的同名姿态结果也不同，配置差异未充分说明，不能合并。", "basis": "model_inference", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p6–7，图3/§3.2.1；p22–24，表4、5、8"}, {"text": "A.5将配体纳入真值刚体对齐；仅距离优化未说明手性/化学有效性约束，不能直接等同全原子姿态有效。", "basis": "model_inference", "locator": "TEXT_OR_xlevHY3oJO_b7f36c5cbbe7：p16–17，A.5/算法2"}]

minimal_check：{"question": "已知binder的排序优势是否稳健？", "control": "固定表7中≥50个binder的14个assay，比较TerraBind Quant与Boltz-2 Affinity，不再改变筛选阈值。", "observable_outcome": "逐assay配对重采样，报告平均Pearson/Spearman差及置信区间。", "resources": "需逐分子标签、靶点ID和双方预测；私有数据未提供，不需重训，实际耗时未知。", "failure_or_stop_condition": "差值区间跨零或偏负，不支持稳定优势；拿不到逐分子数据则停止。"}

missing_fields：["亲和力/编码器预训练的完整截止、去重划分及亲和力总训练规模。", "代码、权重、私有原始预测；随机种子、重复次数及关键差值置信区间。", "总GPU小时、每节点GPU数、编码器预训练成本及初始口袋发现摊销。", "图像核验、图8精确逐轮值，以及正文/附录不一致的原因。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

省去坐标生成的亲和力通路有实用潜力；继续阅读先固定binder集合、输出头和口袋定位计时，再衡量收益。

身份、机制与模型预算：完整题名和25页附件绑定。48层Pairformer预测粗距离，亲和力直接使用结构潜变量，可省去扩散坐标生成；约27M主干/30M可训练规模不含冻结650M ESM2及分子编码器。105k步、batch128、4个H100节点和蒸馏数据已给，但每节点卡数/完整总GPU小时未知。

核查定位：p001 title, p003, Sections2.2.1–2.2.2, p018, B.1；identity_mechanism_and_training_scope_confirmed

时延的实际配置：1.045对27.8秒、26.6倍限196token/A6000/bfloat16/相同内核、10姿态+亲和力，含编码器、不含MSA生成。仅亲和力对照仍让Boltz2产生5个扩散样本，报告17.01倍。口袋模式先全蛋白定位再裁剪，初次定位如何摊入该196token计时未明；不能推广为任意蛋白完整流程速度。

核查定位：p003, pocket two-stage inference, PDF physical page6, Section3.1.3, p018, A.8/B.1；runtime_workload_and_exclusions_confirmed

姿态成功的代价：原Figure3三公共集TerraBind RMSD成功55.3/68.8/62.5%，Boltz1为55.1/69.7/61.3%；联合RMSD+LDDT则45.1/55.1/49.7%，均低于47.3/58.6/54.4%。对照为Boltz1不是Boltz2。A.5刚体对齐含配体与蛋白等权，距离优化未提供手性有效性约束，不能等同全原子物理姿态有效性。附录同名消融值不同且自称方向性检查，不混合为同一运行。

核查定位：PDF physical page6, Figure3, PDF physical page16, A.5, p022–p023, Tables4–5；structure_tradeoff_and_alignment_scope_confirmed

亲和力优势随任务口径变化：原表6每类≥50的13assay AUROC TerraBind .802、Boltz2Affinity .765、Combined .835。原表7仅binders≥50的14assay Pearson .470/.491，换≥100的10assay变.536/.486；Spearman也须独立报告。CASP16 L3000 .725/.625，L1000 .470/.470持平。故整体相关性提升不等于识别阴性或已知binder排序均优。私有结果不能独立重算。

核查定位：PDF physical page23, Table6, PDF physical page24, Tables7–8；task_stratified_affinity_results_confirmed

不确定性与持续学习证据：IQR越低、±1pIC50命中越高属于误差排序证据，未构成概率覆盖校准证明。TargetI每轮5候选的DMTA是固定池离线回放，6倍IC50改善不是新湿实验；缺多靶点重复/不确定性区间。

核查定位：p008, Sections3.2.3–3.2.4；calibration_and_offline_replay_claims_bounded

本地补充/限定：["数值经原图表确认；把26.6倍、17.01倍及姿态Boltz1/亲和力Boltz2对照分别标注，不混为一个全面优势。"]

核查局限：["未重跑结构预测、药物筛选、私有assay或作者代码；没有新增湿实验。", "未读取前作或图8逐轮精确终值；仅核查文本所报回放性质。", "第1页仅读题名；当前附件角色未独立确认。"]


## pro074 · Inference-time optimization for experiment-grounded protein ensemble generation

论文 OR_kbhIfLokFn；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_kbhIfLokFn_0fc3c1866695", "source_url": "https://api2.openreview.net/pdf?id=kbhIfLokFn\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "ceaafc5c08998dcd5a854fdaa235a55ff8a6a8e5e315219cce22ff05c179b2ca", "source_pdf_sha256": "0fc3c186669568fff766d139daf2545ef8c0f9789041beab61ad63f6f2ede599"}], "read_ranges": ["TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页1–41全部文本；正文1–9，致谢及参考文献10–13，附录A 14–29、B 30–34、C 35–41。页标连续，无可见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–15仅图注和零散轴标可读，不能核验结构叠图、曲线及误差条。", "双栏文本、公式与伪代码存在布局损失；数值仅取可明确对应设置的文字及表格。未搜索前作、执行代码或复现实验。"]}

问题：给定序列和NOE约束或晶体密度，生成符合实验且能量合理的多构象集合，并检验ipTM作为优化目标的可靠性。

方法：冻结生成模型，优化成批Pairformer输出Z=(s,z)：每步将实验集合损失经去噪器回传到Z，跨重新采样噪声的外循环保留Z。加入表征锚定及几何有效性项，最后仍运行坐标Guidance；可用ProteinEBM能量权重计算集合观测。输出优化Z及其条件生成集合。

作者主张：通过表征空间的累积优化解除固定采样时域限制，并消除初始化偏差。

论文证据：NMR及X-ray表格显示多数指标改善；800次去噪调用对照中4例均优于Guidance，200次时则均不优。

模型推断：支持跨轮条件记忆带来的实质扩展，不支持无条件的初始化无关性。

定位：['TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页18、22–26，表3、11–20。']

作者主张：融合结构与能量先验，得到实验一致的Boltzmann加权集合。

论文证据：2K0M的IT-Opt违规率经能量加权由10.5%降至4.4%；表7加权IT的ESS约为2–2.913。

模型推断：显示能量偏置的局部价值，但不是已验证的真实平衡态占比恢复。

定位：['TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页19、21，表4、7；物理页38–40，§C.3.4。']

作者主张：小幅embedding扰动可以人为抬高ipTM，而不相应提高结构准确性。

论文证据：七复合物扰动实验报告置信度与结构指标分离；同时存在1YCS等真实改善例。

模型推断：提供对共享表征置信度目标的有效失效诊断，不等于证明实际binder筛选假阳性率下降。

定位：['TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页8–9，§5.3；物理页14–15，图10–13图注；物理页26，表21。']

key_results：[{"setting": "NMRDB主评测20蛋白；以下为2K0M，104残基、1834条NOE。", "baseline": "PDB、Guidance、均匀IT-Opt。", "metric_or_guarantee": "NOE违规率及仅在违规约束上计算的中位违规距离。", "reported_values_and_units": "PDB：12.8%、0.29 Å；Guidance：11.5%、0.32 Å；均匀IT：10.5%、0.22 Å；能量IT：4.4%、0.11 Å。均为作者报告。", "information_and_compute": "实验NOE参与优化；默认Protenix v0.2.0、n=16、K=20、Adam学习率0.05，embedding更新至内循环160步，之后坐标引导及松弛。表4标称300 K。", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页17、19，表1、4；物理页35–37，§C.2。\n"}, {"setting": "X-ray 6I42:B，13残基肽，分辨率1.38 Å，不固定肽端点。", "baseline": "密度Guidance及沉积PDB。", "metric_or_guarantee": "局部密度余弦相似度、精修后Rwork/Rfree。", "reported_values_and_units": "Guidance→IT：余弦0.817→0.876，Rwork 0.195→0.175，Rfree 0.212→0.192；PDB分别为0.905、0.169、0.183。三个指标均无量纲。", "information_and_compute": "输入实验密度；主表覆盖8个肽区段和5个altloc区段，altloc实验锚定其余结构；另有两个整蛋白补充例。", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页18、22–23、25，表2、11–13、18。\n"}, {"setting": "2B3W、2M47、2LF2、2L06的匹配去噪调用预算对照。", "baseline": "坐标Guidance。", "metric_or_guarantee": "NOE违规率、每轮墙钟时间和峰值显存。", "reported_values_and_units": "200次调用时IT四例均较差，800次时四例均较好；2B3W分别为Guidance/IT 13.7%/14.4%与13.7%/8.4%。表19该目标每轮时间716/800 s，显存11898/13918 MiB。", "information_and_compute": "运行分析n=16；论文使用H100和L40，但未逐项标明硬件归属。每轮时间不是K轮端到端总成本。", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页26，表19–20；物理页35，§C.2.1–C.2.2。\n"}, {"setting": "七复合物，有/无MSA的置信度目标优化。", "baseline": "未扰动embedding的AF3。", "metric_or_guarantee": "组合置信度与DockQ、Fnat、氢键恢复等结构指标的关系。", "reported_values_and_units": "正文称约0.01%相对扰动即可抬高置信度；图10另在相对预算0.1，即10%，报告6/7例结构准确性基本不变。两种预算不可混同；此处仅提取作者文字结论。", "information_and_compute": "默认K=10、n=5、学习率0.1，达到扰动预算停；未以实验结构作优化目标。", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页8、14、37，§5.3、图10图注、ipTM设置。\n"}, {"setting": "轨迹平均代理目标J̃的有偏随机梯度分析。", "baseline": null, "metric_or_guarantee": "条件近驻点界，而非真实后验的全局最优保证。", "reported_values_and_units": "定理B.8：min_k E||∇J̃(Z_k)||² ≤ 4(J̃*−J̃(Z_0))/(ηK)+3B²+2Lησ²；O(1/K)项之外保留偏差与方差误差底。", "information_and_compute": "要求局部L光滑、有界偏差B及方差σ²、η≤1/(4L)；代理梯度省略分布依赖的score项。", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页30–34，附录B、定理B.8。\n"}]

prior_work_candidates：[{"citation_as_printed": "Maddipatla, A., Bojan, N. S., Bojan, M., Masalitin, V., Vedula, S., Schanda, P., Marx, A., and Bronstein, A. M. Experiment-guided alphafold3 resolves accurate protein ensembles. bioRxiv, 2025a.", "identifier_if_present": "10.1101/2025.10.11.681796", "relation_candidate": "方法继承、比较基线", "shared_component": "实验集合似然、AF3坐标引导和后处理。", "claimed_difference": "本作将优化移至可跨采样轮次保留的条件表征。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页9，§6；物理页11，参考文献；物理页35、40。", "prior_actually_read": false}, {"citation_as_printed": "Fadini, A., Li, M., McCoy, A. J., Banjara, S., Okumura, H., Napier, E., Fontana, P., Khan, A. R., Jovine, L., Terwilliger, T. C., Read, R. J., Hekstra, D. R., and AlQuraishi, M. Alphafold as a prior: experimental structure determination conditioned on a pretrained neural network. Nature Methods, 23(4):785–795, Apr 2026.", "identifier_if_present": "10.1038/s41592-026-03047-4", "relation_candidate": "背景引用", "shared_component": "通过优化AlphaFold条件信息拟合实验。", "claimed_difference": "本文称前作优化AF2 MSA profile并针对单结构，本作直接优化批量Pairformer输出；未核验该概括。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页9，§6；物理页11，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Roney, J. P., Ou, C., and Ovchinnikov, S. Protein diffusion models as statistical potentials. bioRxiv, pp. 2025.12.09.693073, 2025.", "identifier_if_present": "10.64898/2025.12.09.693073", "relation_candidate": "组件复用", "shared_component": "ProteinEBM可微能量模型。", "claimed_difference": "本作不新训练能量模型，而将其用于实验约束下的集合重加权。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页12，参考文献；物理页40，Choice of Energy Model。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是持久化批量表征的实验集合优化，并有跨任务及计算预算证据；超过单纯调参，但不足确立路线级首创。", "central_increment": "前作已有实验坐标引导及MSA优化（均为本篇转述）；本作新增跨噪声轨迹累积条件更新，仍需排除初始化和完整计算差异。", "soundness_observation": "B.8只约束有偏代理目标；附录以紧集上连续可微推出有限曲率的论证不足，实际Adam也未被所写固定步长证明直接覆盖。未完成逐定理证明核验。", "significance_observation": "价值在实验结构拟合及置信度失效诊断；工程工作包括可微氢坐标、多阶段反传和物理后处理，不涉及新增基础模型训练。", "main_open_question": "固定初始化、真实墙钟预算和后处理后，跨轮保留Z能否仍稳定改善留出实验数据的拟合？"}

limitations：[{"text": "作者承认迭代总成本更高、能量模型受训练数据和模型形式限制；cryo-EM仍属未来扩展。", "basis": "author_report", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页9、35、40，§7、C.2.1、Choice of Energy Model。"}, {"text": "目标分布仍含AF3先验；能量的百分位截断及EMA不等同于原能量的纯Boltzmann权重。表9默认β=0.6与正文300 K对应β=1.68的口径未解释。", "basis": "model_inference", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页6、22、38–39，式(9)、表9、§C.3.4。\n"}, {"text": "NOE实际使用线性平均距离；表10稀疏测试只检查单个2B5B的几何有效性，不能证明留出NOE泛化或真实构象占比恢复。", "basis": "model_inference", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页4、22、37–38，式(3)、表10、式(39)–(42)。"}, {"text": "并非逐项胜出：2MRW违规率22.6%→24.5%，6QQF的Rfree 0.205→0.206。正文称ipSAE基本不变而图13图注称升高；9HAF起点27%与图9的41.9%亦冲突，未自行调和。", "basis": "model_inference", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页8、14–15、18、23，§5.3、图9/13图注、表3/13。"}, {"text": "匹配调用预算仅四例，真实前反传及后处理计费仍不清。样本清单也不完全一致：表11较表2多3例，§C.5.2较主文七复合物另列9HAE。", "basis": "model_inference", "locator": "TEXT_OR_kbhIfLokFn_0fc3c1866695：物理页18、22、26、28、41，表2/11/20、算法2、§C.5.2。"}]

minimal_check：{"question": "隔离检验跨轮保留Z是否带来可泛化的收益。", "control": "在2B3W固定MSA、起始Z、NOE训练/留出划分及后处理，对比保留Z与每轮重置Z；n=16，按实测GPU秒对齐。", "observable_outcome": "比较留出NOE违规率、违规幅度和几何有效性，使用相同的至少5个种子。", "resources": "需Protenix、原始NOE及可反传GPU；论文使用H100/L40，最低显存和检验总耗时未确定。", "failure_or_stop_condition": "等预算优势消失，或只改善训练NOE却损害留出约束或几何，则不支持该例的持久记忆增益。"}

missing_fields：["图内精确数值、能量变化量及误差条不可见。", "逐目标端到端GPU总时长、硬件对应关系和原始重复实验数据未提供。", "温度、样本清单及重复结果冲突的解释未提供。", "前作全文、代码核验与独立复现实验未提供或未执行。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

跨轮保留条件表征与实验目标结合值得研究；优先验证等GPU秒、留出约束及未经截断权重的影响，再解释热力学或泛化结论。

身份、中心优化和观测对象：完整题名与41页附件匹配。跨重新采样轮次保留/优化条件Z，最终仍有坐标Guidance及物理后处理；实验NOE/密度直接参与拟合。式3采用距离线性集合平均，并非直接平均r^−6强度。结果首先是给定实验约束拟合，不自动认证未见约束或真实构象人口。

核查定位：p001 title, p004, Eq1–4, PDF physical page14, Figure8 caption, p035, C.1–C.2；identity_optimization_target_and_fitting_scope_confirmed

主效果与匹配预算：原表4的2K0M为Guidance11.5%/.32Å、IT10.5%/.22Å、EnergyIT4.4%/.11Å；距离中位数只对违规组计算。2MRW均匀IT违规率24.5%反高于22.6%。表20在200次调用四例均更差、800次四例均更好；2B3W为13.7/14.4%及13.7/8.4%。表19的716/800秒是每循环，不能当K循环总成本或把调用对齐当完整GPU秒对齐。

核查定位：PDF physical page19, Table4, p038, Eq41–42, PDF physical page26, Tables19–20；decisive_numbers_and_budget_dependence_confirmed

能量权重与ESS的实际含义：目标是AF3先验乘能量倾斜，并非无先验的纯Boltzmann分布；还使用EMA及max(E−E10,0)截断，这不只是平移不变操作。默认n16时若用常见线性10%分位数，最低两项获得相同最大权重，从而最大归一化权重≤1/2、ESS=1/sum(w²)≥2。表7加权IT最低常为2、范围2–2.913，不能把这一提升完全解释为物理多样性恢复，实际分位实现仍需核查。表9默认beta=.6而C.3.4指定1.68对应300K，口径未统一。

核查定位：PDF physical page21, Table7, p022, Table9, p038, Eq43–47, PDF physical page39, annealing/energy biasing；modified_weight_target_and_conditional_ess_floor_identified

置信度优化不等于结构改善：原图10在相对扰动预算.1即10%下，七复合物置信度均升；六例DockQ/Fnat/氢键恢复无对应整体改善，1YCS确有改善。这支持对共享embedding置信度目标的失效诊断，不是所有优化无效，也不能与正文所述.01%阈值混为同一实验。

核查定位：PDF physical page14, Figure10 and caption, PDF physical page26, Table21；confidence_accuracy_decoupling_visually_confirmed

收敛保证的条件：B.8原式保留3B²+2Leta sigma²误差底，只对局部光滑的有偏代理目标给近驻点界。B.10用紧集上的C1推出有限曲率并不足够，例如|x|^(3/2)在[-1,1]为C1却梯度不Lipschitz；B.7仍应保留为额外假设。所写固定步长上升分析也未直接覆盖实际Adam。没有据此否定所给条件下的一般有偏梯度界。

核查定位：p033, AssumptionB.7/TheoremB.8, p034, RemarkB.10；surrogate_convergence_scope_and_unproved_smoothness_bridge_confirmed

本地补充/限定：["补充能量10%分位截断在n16常用实现下隐含ESS≥2，不能单凭ESS抬升推断采样物理多样性。", "原图10确为10%相对扰动配置；将此与其他极小扰动文字结果分列。"]

核查局限：["未运行结构生成、ProteinEBM或实验复现；ESS下界是指定分位实现条件下的代数推导。", "未全面验证理论或逐目标后处理/硬件成本，未核读前作。", "第1页仅读标题开头，p35仅读所打印段落；版本角色未确认。"]


## pro075 · A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions

论文 OR_aDPbUSUCwh；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_aDPbUSUCwh_70cb3a23d080", "source_url": "https://api2.openreview.net/pdf?id=aDPbUSUCwh\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p1–20全部提供文本，含正文§1–6、参考文献、附录A–E；页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–10仅有题注和零散坐标文字，不能核验曲线、空间分布或参数速度投影。", "双栏文字存在串行和公式排版损失；核心更新式及表1–4数值可辨，未核验原PDF版面。"]}

问题：非线性参数化PDE解的Jacobian降秩或病态时，如何避免参数演化停滞，同时保留瞬时残差最小化？

方法：输入PDE算子、初值及可微参数化ûθ，先拟合θ0；每步求DF参考速度η̄，维护τṁ=η̄−m，再取θ̇=η̄+λPm。实践中η̄=Jε†f、Pε=I−VεVεᵀ，历史用EMA更新，输出随时间演化的ûθ。真零空间投影不改变当前函数导数；截断近零方向时不自动具有此性质。

作者主张：用Onsager历史变量固定DF的gauge，在保留残差最优性下缓解切空间坍塌。

论文证据：式(14)–(15)给出耦合动力学；命题A.1构造特定λ下的精确波碰撞穿越轨迹，附录A.2分析零秩脱困。

模型推断：实质增量是受零空间约束的动量选择，不是简单把普通动量加到全部参数方向。

定位：['TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p5，§4.2，式(12)–(15)。\n', 'TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p12–14，附录A。']

作者主张：参数速度更平滑、求解误差更低，附加成本近乎可忽略。

论文证据：表1三个任务平均误差最低；表2改善5D统计误差；表3提供五档截断阈值检验。

模型推断：支持所测小网络实例的实用价值，不能外推为任意维数、任意参数选择下的可靠性。

定位：['TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p7–8，§5.2–5.3、表1–2；p19表3–4。']

key_results：[{"setting": "双高斯波碰撞，ρ=0、c=1、m(0)=0，参数初值位于指定精确路径。", "baseline": "最小范数DF在碰撞点没有分离方向分量。", "metric_or_guarantee": "命题A.1：指定参数路径可精确穿越碰撞并表示解析PDE解。", "reported_values_and_units": "碰撞时刻t=2；要求λ=(1−exp(−2/τ))⁻¹。不是任意λ下的保证。", "information_and_compute": "连续时间特例推导；数值波例另取τ=0.5、λ=1，不能混同命题条件。", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p13，Proposition A.1、式(22)–(28)及数值设置。"}, {"setting": "RDW、2D输运、Vlasov；终止时间依次8、20、10。", "baseline": "DF+tSVD、DF+Tikhonov、NIVP、RSNG、TENG。", "metric_or_guarantee": "表1平均L2 err.及终点误差；具体归一化和聚合定义未充分展开。", "reported_values_and_units": "依上述任务顺序，DFO平均误差为2.10e−3、1.23e−2、3.95e−3；DF+tSVD为6.06e−3、3.82e−2、1.22e−2。两者相对耗时均列为1×。输运终点NIVP为2.32e−2，优于DFO的2.63e−2。", "information_and_compute": "参数量922/3265/3265；初值Adam训练50k/100k/100k步；统一Δt=0.004，多数方法RK4，TENG用Heun。作者扫参取最优，RSNG报5次均值。", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p8表1；p17–19附录C.1、C.3、C.5–C.6。\n"}, {"setting": "5D Fokker–Planck，T=8，周期截断域[0,4]⁵。", "baseline": "DF+tSVD、RSNG、NIVP、TENG。", "metric_or_guarantee": "表2 Err. mean、Err. cov及相对运行时间。", "reported_values_and_units": "DFO误差为(4.47e−3,5.26e−2)，DF+tSVD为(1.46e−2,3.17e−1)，均耗时1×；RDFO为(4.51e−3,5.60e−2)，耗时0.5×。表3五档εrel∈[1e−5,1e−2]中，调参DFO的五次平均均值误差均低于DF。", "information_and_compute": "1581参数；初值Adam 100k步；每步2000均匀加2000高斯配点，Euler推进；参考统计来自10⁵条Euler–Maruyama粒子轨迹。绝对耗时未报告。", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p8表2；p17–19，附录B.4、C.1、C.3、C.6–C.7。\n"}]

prior_work_candidates：[{"citation_as_printed": "Bruna, J., Peherstorfer, B., and Vanden-Eijnden, E. Neural Galerkin schemes with active learning for high-dimensional evolution equations. J. Comput. Phys., 496:112588, 2024.", "identifier_if_present": "112588", "relation_candidate": "比较基线", "shared_component": "DF神经参数演化；5D Fokker–Planck测试设置。", "claimed_difference": "加入零空间历史速度选择，而非只取最小范数解。", "basis": "target_paper_only", "target_locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p7、p9参考文献、p16附录B.4。", "prior_actually_read": false}, {"citation_as_printed": "Feischl, M., Lasser, C., Lubich, C., and Nick, J. Regularized dynamical parametric approximation. arXiv, 2403 (19234):1–38, 2024.", "identifier_if_present": "2403 (19234)", "relation_candidate": "比较基线", "shared_component": "病态DF参数动力学及正则化。", "claimed_difference": "作者强调真实零空间修正不引入Tikhonov式的残差最优性偏移。", "basis": "target_paper_only", "target_locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p2相关工作、p7基线、p10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Koch, O. and Lubich, C. Dynamical low-rank approximation. SIAM J. Matrix Anal. Appl., 29(2):434–454, 2007.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "DF动力学的gauge固定。", "claimed_difference": "本篇称前作使用矩阵因子专用正交条件；本作提出面向一般非线性参数化的历史驱动选取。", "basis": "target_paper_only", "target_locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p2相关工作、p10参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是有机制解释与特例支持的受约束动力学改造，超出局部调参；尚不足判为路线级新框架。", "central_increment": "前作已实现DF参数演化及正则化（本篇转述）；本作新增零空间中的滤波历史速度，支持证据为式(15)、命题A.1及表1–3；仍须界定截断近零方向带来的偏差。", "soundness_observation": "真实零空间下JP=0支持瞬时性质。命题A.1展示特例穿越路径，不证明一般轨迹唯一；逐点选定唯一速度也不等于证明秩变ODE良定。", "significance_observation": "可能改善local-in-time神经PDE求解的停滞与抖动；实际规模证据止于5D及数千参数。", "main_open_question": "实际tSVD将小非零奇值方向视作gauge时，残差偏移和有限步漂移能否被控制，同时保留稳定性收益？"}

limitations：[{"text": "不直接修复函数相关的小非零奇值方向；时间尺度参数依题目选择。真实零空间修正也只保证瞬时一阶性质，有限步可能产生高阶漂移。", "basis": "author_report", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p5 §3.2；p9 §6。"}, {"text": "近零截断时JPε通常不为零，因此原始残差最优性不能从精确gauge论证直接推出；配点最优也不自动等于连续L2最优。", "basis": "model_inference", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p6 §4.4。"}, {"text": "各法最优扫参结果与RSNG多次均值口径不同；TENG积分器也不同。表4固定β=0.2、λ∈[0.5,2.5]时误差跨7.75e−3至3.51e−2且无方差，不足认定免调参。", "basis": "model_inference", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p7、p18附录C.3、p19表4。"}, {"text": "相对同一SVD求解器，动量仅增加两次矩阵向量乘；但绝对成本未报。若按附录D使用稠密Gaussian sketch，形成JΓ和QᵀJ还需O(Nps)，其复杂度表述未计此项。", "basis": "model_inference", "locator": "TEXT_OR_aDPbUSUCwh_70cb3a23d080：物理p6 §4.5；p20附录D。"}]

minimal_check：{"question": "近奇异波碰撞中，DFO的收益是否伴随不可忽略的原始残差偏移？", "control": "固定四参数波例、初值、151配点和τ、λ，对照DF+tSVD与DFO，共用阈值并同步细化步长和截断阈值。", "observable_outcome": "记录是否穿越碰撞、解析解误差、未截断残差及‖JPεm‖，检查收益与残差偏移随细化的变化。", "resources": "四参数解析波例、SVD及小规模步长/阈值扫描；实际硬件和耗时未测。", "failure_or_stop_condition": "若细化后收益消失或原始残差明显增大，则不支持向原PDE无偏稳定性的外推。"}

missing_fields：["硬件、绝对耗时、峰值内存及完整调参预算。", "各主表最优τ/β、λ和完整搜索网格。", "5D时间步长、主表误差聚合细节及统计区间。", "Koch & Lubich条目的独立标识符；前作全文、原始图像和可执行代码未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

简单投影记忆具有可复用性和数值支持；继续阅读先厘清秩变解概念、截断残差及实际离散算法的一致性。

身份与零空间动量：完整题名和20页当前附件一致。eta_bar加lambda Pm只沿gauge方向补历史速度；精确JP=0确实保持当前函数导数，作者p5也承认有限步高阶漂移。实际Pepsilon使用tSVD，若丢弃小而非零奇值，JPepsilon一般不为零；其扰动范数至多|lambda| sigma_max_dropped ||m||，只是瞬时界，不是全局无偏或稳定保证。

核查定位：p001 title, p005, Eq13–15 and higher-order discussion, PDF physical page6, Section4.4/Algorithm1；identity_mechanism_and_exact_vs_truncated_scope_confirmed

碰撞命题的特殊条件与解概念：A.1明确rho0、c1、特定初值、m0=0及lambda=(1−exp(−2/tau))^−1；数值例另用tau=.5、lambda1。进一步逐点检查发现沿给定路径eta_bar只在t2由q变q−xi1，连续记忆被迫为(1−e^−t/tau)q，其t2导数与原记忆ODE右边差xi1/tau。lambda选择只修复theta方程。几乎处处解可忽略单点，但原文未说明该解概念，不能读成经典唯一穿越保证。推导另存。

核查定位：PDF physical page13, PropositionA.1/Eq22–28, local_check/collision_ode_scope.md；rank_change_solution_concept_gap_identified

主数值收益：原表1三个任务平均误差DFO .00210/.0123/.00395，DF+tSVD .00606/.0382/.0122；输运终点NIVP .0232优于DFO .0263，非全指标领先。原表2五维均值/协方差DFO .00447/.0526、DF .0146/.317，RDFO .00451/.0560并报半时间。图5显示所选维度DF突跳、DFO更平滑，但不能据单图证明任意动力系统稳定。

核查定位：PDF physical page8, Tables1–2/Figure5；decisive_empirical_values_and_scope_confirmed

阈值与调参范围：原表3五档阈值下调参DFO平均均值误差均较低；表4固定beta=.2时lambda.5–2.5的误差范围.00775–.0351，超过4倍，无方差条，不能据此称免调参。RSNG报五种子平均；低维TENG用Heun其余RK4，初值需50k/100k Adam步。

核查定位：p018, C.3, PDF physical page19, C.5–C.7/Tables3–4；tuning_and_comparison_protocol_confirmed

附加成本和总复杂度：同SVD基线复用V时动量只增加两次矩阵向量乘，附加成本小可成立；表中仅相对时间，未提供绝对硬件成本。附录D稠密Gaussian sketch形成J Gamma及Q^T J需O(Nps)，所报O(Ns²+ps²)遗漏这两次乘法；仍可能加速，但不是该式完整成本。

核查定位：PDF physical page6, Section4.5, p020, AppendixD；incremental_cost_supported_dense_sketch_accounting_incomplete

本地补充/限定：["新增A.1记忆方程在碰撞点的逐点一致性核查；需要澄清广义解而非直接接受经典穿越陈述。", "给出截断gauge导致的局部函数速度扰动界，明确不等于全局误差控制。"]

核查局限：["没有运行波碰撞、步长扫描、PDE求解或作者代码；本地代数说明仅针对给定特例。", "未证明一般广义解唯一性、全局误差或完整RK4收敛阶；未核读前作。", "第1页仅读标题；版本角色未核实。"]


## pro076 · SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics

论文 OR_ojwpa0wXo9；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_ojwpa0wXo9_0fbe7e861843", "source_url": "https://api2.openreview.net/pdf?id=ojwpa0wXo9\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "02913265a621634472a0509f1cfc1ee10c11578578942147c58f2e8076ae1913", "source_pdf_sha256": "0fbe7e861843402f601ff1643cc00ce82f2be5c22ba39c8bda5f886eb66113d0"}], "read_ranges": ["TEXT_OR_ojwpa0wXo9_0fbe7e861843：物理页1–24全部已提供文本，包括正文1–7页、致谢及参考文献8–10页、附录目录11页、附录A–F第12–24页；题名吻合，连续页标无缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–8不可见，未据图中文字残片推测图形。", "双栏文本存在串接，部分公式符号及表格排版可能失真；页标齐全不等于字符提取无损。", "未提供前作、代码、注册表及原始实验日志；未搜索、复现或核验公开发布状态。"]}

问题：如何识别实验室机器人完成任务却在途中溢液、过度接触或放置不稳，并提供可扩展的安全训练环境？

方法：LLM将指令转换为YAML，经语法、几何、因果及动态仿真核验；状态可见的专家生成安全示范。策略使用视觉、状态及任务输入，冻结BC基策略后叠加α=0.1的关节增量残差。奖励结合阶段完成奖与姿态、倾角、接触力代理惩罚；PBD流体用于校准，并非直接以液体损失训练。

作者主张：建立可生成、物理核验且支持交互安全学习的实验室基准。

论文证据：63个资产、9类64任务、6,400条筛选后专家轨迹；生成核验端到端通过率44%，最多三轮反馈修正。

模型推断：价值在组件贯通后形成可复用评测能力，而非新流体求解器。

定位：['TEXT_OR_ojwpa0wXo9_0fbe7e861843：p5图3说明；p14表6–7；p20§D.4。\n']

作者主张：终态成功显著高估实验室操作安全，轨迹级SSR能揭示该缺口。

论文证据：五种策略在三个域均存在超过30个百分点的SR–SSR差；另有代理校准及50次实物回放。

模型推断：支持既定安全定义下的系统性诊断，不等于真实危险发生率或部署保证。

定位：['TEXT_OR_ojwpa0wXo9_0fbe7e861843：p7表2；p17表12；p20–21附录E。']

作者主张：不重训基策略，以有界残差RL提高安全成功率。

论文证据：DP与π0.5的三域平均SSR分别增加43.0和33.1个百分点；提供残差幅度及约束RL对照。

模型推断：是有效的场景适配与接口示范，尚不构成新的通用RL算法。

定位：['TEXT_OR_ojwpa0wXo9_0fbe7e861843：p15–16表8–10；p19表14。']

key_results：[{"setting": "64任务；三种子，每任务每种子50回合，按原生输入协议评测。", "baseline": "DP、DP3、ACT、OpenVLA、π0.5。", "metric_or_guarantee": "SR / SSR，单位%。", "reported_values_and_units": "π0.5：Pour Liquid为91.2/52.4；Press Switch为93.4/54.8；Grasp Vessel为95.0/54.5。", "information_and_compute": "6,400条专家示范；π0.5全参微调10,000步、batch 256、8×A800 80GB。跨模型输入与训练预算不相等。", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p7表2；p19§D.3。\n"}, {"setting": "无额外测试扰动的名义评测；三种子，每任务每种子50回合。", "baseline": "冻结的DP或π0.5模仿策略。", "metric_or_guarantee": "Liquid / Actuation / Spatial三域SSR；增益为域均值差。", "reported_values_and_units": "DP：33.7/36.0/27.8%→73.2/74.5/78.9%，+43.0个百分点；π0.5：53.3/54.3/51.0%→86.0/87.4/84.5%，+33.1个百分点。", "information_and_compute": "残差训练报告10^7步、128并行环境；RL硬件、墙钟时间及计步粒度未报告。", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p15表9；p18表13。\n"}, {"setting": "Pour Liquid同时施加照明、物理与物体初始位姿扰动。", "baseline": "同一基策略，不添加残差RL。", "metric_or_guarantee": "SR / SSR，单位%。", "reported_values_and_units": "DP：58/24→77/65；π0.5：73/35→85/74。", "information_and_compute": "RL训练使用更广随机化；测试仍处于既定任务语法内。", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p23表22；p24表23。\n"}, {"setting": "12种容器几何、三种液位的仿真校准。", "baseline": "直接模拟溢液事件标签。", "metric_or_guarantee": "搬运倾角代理的召回率、精确率。", "reported_values_and_units": "阈值0.25 rad；召回率97%、精确率82%；距临界溢液角至少保留50%余量。", "information_and_compute": "校准扫描的轨迹总数及算力未报告。", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p17§C.3、表12。\n"}, {"setting": "50条PsiBot实物开环回放，按预测安全/不安全各25条分层抽样。", "baseline": "实物结果独立人工标注。", "metric_or_guarantee": "仿真标签一致率及不安全检测指标。", "reported_values_and_units": "TP/TN/FP/FN=23/20/2/5；一致43/50=86%；不安全召回82.1%；阴性预测值80%。", "information_and_compute": "双人独立标注κ=0.93，该值是标注者间一致性，不是仿真与实物的κ；不测试闭环策略迁移。", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p20–21附录E、表16。\n"}]

prior_work_candidates：[{"citation_as_printed": "Li, R., Hu, Z., Qu, W., Zhang, J., Yin, Z., Zhang, S., Huang, X., Wang, H., Wang, T., Pang, J., et al. LabUtopia: High-fidelity simulation and hierarchical benchmark for scientific embodied agents. In NeurIPSDB, 2025b.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "实验室流体仿真、透明资产及RL接口；仅功能对照。", "claimed_difference": "本作增加生成核验及RL可访问的轨迹安全约束。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p3表1、§2；p9参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Chen, T., Chen, Z., Chen, B., Cai, Z., Liu, Y., Li, Z., Liang, Q., Lin, X., Ge, Y., Gu, Z., et al. RoboTwin 2.0: A scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation. In ICML, 2026.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "以仿真核验生成任务的有效性。", "claimed_difference": "本作结合实验室流体、不可逆失败筛查及安全交互训练；未证明代码继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p3§2；p8参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Zhang, B., Zhang, Y., Ji, J., Lei, Y., Dai, J., Chen, Y., and Yang, Y. SafeVLA: Towards safety alignment of vision-language-action model via constrained learning. In NeurIPS, 2025a.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "安全约束学习；PPO-Lagrangian对照的方法来源线索。", "claimed_difference": "由文中转述的家庭导航转向流体及接触密集操作，默认采用残差惩罚式RL。", "basis": "target_paper_only", "target_locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p3§2；p10参考文献；p18§C.6。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可复用的安全评测和交互训练能力，不只是单项性能提升；尚不足支持路线级首创。", "central_increment": "前作已有流体实验室平台与生成核验组件（本篇转述）；本作在固定任务语法下将校准、核验、示范和轨迹安全训练贯通，证据为基准及对照结果；仍需排除代理合规与真实风险下降脱节。", "soundness_observation": "结果属于作者报告；残差幅度和软惩罚不提供形式安全保证。κ的含义可由附录澄清，后训练方差仍缺失。", "significance_observation": "对实验室操作预筛查有价值，工程集成贡献大于基础RL算法新意。", "main_open_question": "在独立事件标签及未参与校准的容器上，SSR提升是否仍对应实际溢液风险降低？"}

limitations：[{"text": "只筛查操作层安全，不涵盖化学、热学或部署认证；没有闭环实机迁移评测，也未模拟裂纹传播。", "basis": "author_report", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p6§4.1；p17表12；p21附录E。\n"}, {"text": "五次物理漏报集中于高瘦容器；分层抽样的86%一致率不能直接代表自然部署分布。", "basis": "model_inference", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p20–21附录E。\n"}, {"text": "跨模型输入不等：DP/DP3含真实目标坐标，DP3另用点云，OpenVLA仅单视角且无本体状态；与主文笼统排除特权信息的说法存在张力。", "basis": "model_inference", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p5§3.4；p19§D.1–D.2、表15。\n"}, {"text": "后训练同时增加随机化和交互，不能单独归因于残差结构或安全奖励；泛化仅针对既有任务语法内的扰动。", "basis": "author_report", "locator": "TEXT_OR_ojwpa0wXo9_0fbe7e861843：p14–15§B.1、§C.1。\n"}]

minimal_check：{"question": "残差带来的SSR改善是否同时降低独立模拟溢液事件率？", "control": "选一个液体搬运任务，固定初态、液位及评测种子，比较现有DP与DP+RL；直接液体逸出事件不采用倾角阈值定义。", "observable_outcome": "同时统计SSR、直接溢液率和执行时长，检查收益是否只存在于代理指标。", "resources": "需检查点、仿真器及逐步粒子或事件日志，无需复训；重评硬件及耗时未知。", "failure_or_stop_condition": "只有SSR改善而溢液未减少，则该检验不支持风险下降；缺少独立事件日志或统计样本不足时保留未知。"}

missing_fields：["生成LLM身份、采样参数、原始提案总数及生成成本。", "任务级力阈值、奖励权重、完整随机化范围及校准扫描样本量。", "RL硬件、墙钟成本、10^7训练步的计数及跨任务分配口径。", "表17只提供基策略SSR标准差，未给残差后训练对应方差和逐回合日志。", "三篇候选前作未印出可用DOI或预印本标识；原文均未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

轨迹级安全与终态任务成功的区别有实用评测价值；后续应优先核验独立溢液事件、未校准容器和闭环迁移。

身份、平台与基准范围：完整题名与24页附件匹配，所渲染页可读。63资产、64任务、6400条是筛选后接受的专家轨迹，不是生成尝试总数；测试仍在固定任务语法内重采样。系统增量是生成核验、轨迹安全及交互纠偏贯通，而非新流体求解或通用安全保证。

核查定位：p001 title, p005, Figure3/Section3.3, p015, scope paragraph, p020, D.4；identity_dataset_denominator_and_system_scope_confirmed

SR和SSR的数值口径：原表2 pi0.5 PourLiquid91.2/52.4、PressSwitch93.4/54.8、GraspVessel95.0/54.5%。SSR要全程满足适用限制；SM是含失败轨迹平均，空间诊断520mm不能与20mm成功阈值直接比较。倾倒阶段允许按容器/液位调整阈值，不能套用搬运.25rad恒定限制。

核查定位：PDF physical page7, Table2, p006, metric definitions, PDF physical page17, phase limits/SM scope；decisive_gap_and_metric_denominators_confirmed

残差效果和对照：原表9三域DP33.7/36/27.8→73.2/74.5/78.9，平均+43.0个百分点；pi0.5 53.3/54.3/51→86/87.4/84.5，+33.1。残差还加入交互和随机化，作者明确不是单因素归因。小/中/大偏差恢复88/52/17%，有界动作不等于形式安全。表17仅给基策略方差，不能据图4的引用认为后训练方差已完整提供。

核查定位：PDF physical page15, Tables8–9/C.1, PDF physical page21, Table17；posttraining_effect_and_missing_uncertainty_confirmed

代理校准与50次实物回放：12容器×3液位模拟校准报97%召回/82%精确率，力和空间仍是代理。实物为25预测安全+25预测不安全的开环分层回放，TP/TN/FP/FN23/20/2/5可复算43/50=.86、召回23/28=.821、NPV20/25=.8。按这些边际计算sim–real Cohen kappa=.72；文中.93是两位标注者的一致性，不能混用。五漏报集中高瘦容器，不代表自然部署分布风险率，也未做闭环策略迁移。

核查定位：PDF physical page17, Table12, p020, AppendixE, PDF physical page21, Table16；confusion_matrix_arithmetic_and_kappa_identity_confirmed

跨模型输入与训练预算：D.1/表15明确DP/DP3获真实目标坐标、DP3还用点云；OpenVLA单视角无本体状态。这是原生协议比较，非等输入榜单，与主文笼统排除特权信息句须一起读。pi0.5和OpenVLA虽均10k步/8A800，batch分别256/16，也非等训练预算。

核查定位：p005, observation paragraph, p019, D.1–D.3/Table15, p020, training continuation；input_and_compute_asymmetry_confirmed

本地补充/限定：["由实物混淆矩阵算得sim–real kappa=.72，与作者间kappa=.93分开；Pro原有区分得到进一步确认。", "渲染页正常可读，准备阶段PDF色彩配置警告未在所查页面造成可见缺失。"]

核查局限：["未运行仿真、残差训练或实体机器人；本地仅混淆矩阵算术及文图核对。", "未核读前作、代码、资产阈值注册表或发布完整性。", "第1页仅读标题开头，版本角色未确认。"]


## pro077 · Reflex: Real-Time Vision-Language-Action Control through Streaming Inference

论文 OR_XzsZK1hvpv；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_XzsZK1hvpv_64779006c30a", "source_url": "https://api2.openreview.net/pdf?id=XzsZK1hvpv\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "de5c8e31605c2c11b952d610a42f3d27077c66e2f81b33372d47bc7d01ac1563", "source_pdf_sha256": "64779006c30a57c5e2db08c789ac61211e85ac1e5c4fc63c3de2d8170b41541f", "note": "仅阅读所提供文本，未打开来源URL或PDF；不认定为最终出版版。\n"}], "read_ranges": ["TEXT_OR_XzsZK1hvpv_64779006c30a：物理页1–16连续完整；正文页1–9、参考文献页9–12、附录A–E页13–16。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–12的图像均未提供，不能核查曲线、注意力掩码图或完整柱状图数值。", "双栏文本存在串行混排，部分公式和表格布局有损；未发现物理页标缺失。"]}

问题：如何让迭代去噪VLA持续输出动作，同时减少观测到执行的延迟、错误缓存复用和混精数值失稳？

方法：输入图像、语言与本体状态，将上下文分为固定语言前缀、FIFO视觉历史和逐去噪步重算的动作后缀。视觉与策略双流共享缓存，以末次命令近似未来状态并自适应安排重叠推理；AdaRMSNorm用时间/状态门控及FP32统计稳定BF16，配合预分配和算子融合输出动作块。

作者主张：三分区缓存支持固定窗口下增量更新，并保持动态后缀注意力与全量计算等价。

论文证据：命题A.1给出分块注意力证明；§4.2称两模型、两基准固定输入比较均得MSE=0.00。

模型推断：分块代数成立不等于缓存跨窗口始终有效；时间步不变尚不足以排除驱逐导致的跨帧依赖变化。

定位：['TEXT_OR_XzsZK1hvpv_64779006c30a，页4，§3.1；页7，§4.2；页13，命题A.1。\n']

作者主张：AdaRMSNorm防止高频BF16流式部署中的数值崩溃。

论文证据：表5报告比BF16及仅FP32归一化更长的稳定步数，且附加延迟较低。

模型推断：支持有限压力测试中的稳定性改进，不支持无限时域保证。

定位：['TEXT_OR_XzsZK1hvpv_64779006c30a，页5，§3.2；页9，表5；页14，B.3。']

作者主张：异步视觉/策略流水线结合未来状态补偿和融合，实现低延迟50Hz持续控制。

论文证据：两基准、PiPer实机及附录SmolVLA实验报告加速、减少停顿和维持或提高成功率。

模型推断：具有部署价值，但50Hz动作执行不等于50Hz基于新观测的策略推理。

定位：['TEXT_OR_XzsZK1hvpv_64779006c30a，页5–8，§3.3–4.6；页15–16，D.6–D.7。']

key_results：[{"setting": "Pi0.5，LIBERO，RTX4090 24GB；视觉窗口10帧、动作块50、去噪10步、BF16。", "baseline": "Standard同步全历史重算。", "metric_or_guarantee": "动作块推理延迟、峰值显存、成功率与执行频率。", "reported_values_and_units": "作者报告135.2→52.4 ms，2.58×；8.42→6.15 GB；78.0%→79.5%。表9对应19.1 Hz，附录称通过动作插值实现50 Hz执行。", "information_and_compute": "每套10任务、每任务50回合；延迟预热100步后测1000次，但均值/P95口径不清。训练成本未报。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页14，表6、D.1–D.2；页15–16，表8–9、D.6。\n"}, {"setting": "Pi0 3.1B，LIBERO-Long。", "baseline": "Synchronous及Async-Naive。", "metric_or_guarantee": "观测到动作的反应延迟及stall rate。", "reported_values_and_units": "同步226.8 ms、Async-Naive 182.6 ms、Reflex 105.2 ms；Reflex较同步约降低54%；对应stall为100%、54%、0%。", "information_and_compute": "采用共同实验配置；stall分母与实际观测更新频率仍需核明。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页7，表1。\n"}, {"setting": "BF16流式稳定性压力测试，表5未单独明确模型与任务。", "baseline": "BF16及BF16＋FP32 norm-only。", "metric_or_guarantee": "稳定步数、NaN/Inf及附加延迟。", "reported_values_and_units": "BF16：120–220步；FP32 norm-only：700–1200步、+0.8 ms；AdaRMSNorm：>2000步、无观察到的NaN/Inf、+0.4 ms。", "information_and_compute": "重复次数、种子和测试总时长未报。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页9，表5。\n"}, {"setting": "AgileX PiPer：Pick-Place、Articulated、Dynamic Recovery。", "baseline": "Sync；另设Async-Naive。", "metric_or_guarantee": "实机成功率增量、反应延迟、stall。", "reported_values_and_units": "较Sync分别+11、+14、+17个百分点；Reflex延迟101、104、110 ms，stall均0%。", "information_and_compute": "作者称每方法每任务20回合，共180回合，使用与仿真相同checkpoint和超参数。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页7，§4.4；页8，表2。\n"}, {"setting": "Kinetix，Pi0.5及Pi0。", "baseline": "Standard。", "metric_or_guarantee": "推理加速与显存节约。", "reported_values_and_units": "分别2.41×、2.65×加速；峰值显存约降低24%。", "information_and_compute": "每任务100回合；任务清单、数量和VLA适配过程未报。图12绝对值不可核查。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页16，附录E正文。\n"}, {"setting": "SmolVLA 500M，LIBERO四套任务平均。", "baseline": "Standard。", "metric_or_guarantee": "跨模型推理加速与成功率。", "reported_values_and_units": "48.6→21.2 ms，2.29×；成功率72.4%→73.8%。", "information_and_compute": "附录沿用共同实验配置，未另报训练或适配成本。", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页16，D.7、表10。\n"}]

prior_work_candidates：[{"citation_as_printed": "Tang, J. et al. VLASH: Real-time VLAs via future-state-aware asynchronous inference. arXiv preprint arXiv:2512.01031, 2025.", "identifier_if_present": "arXiv:2512.01031", "relation_candidate": "背景引用", "shared_component": "未来状态条件化与异步推理。", "claimed_difference": "Reflex另处理去噪缓存有效性、混精稳定性和融合；未给完整直接对照。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页2，§1；页12，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Black, K., Galliker, M. Y., and Levine, S. Real-time execution of action chunking flow policies. arXiv preprint arXiv:2506.07339, 2025b.", "identifier_if_present": "arXiv:2506.07339", "relation_candidate": "背景引用", "shared_component": "flow policy动作分块的实时执行。", "claimed_difference": "作者强调服务环路与推理计算联合优化，而非仅调整执行。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页2，§1；页10，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Xu, S., Wang, Y., Xia, C., Zhu, D., Huang, T., and Xu, C. VLA-Cache: Efficient vision-language-action manipulation via adaptive token caching. In Belgrave, D., Zhang, C., Lin, H., Pascanu, R., Koniusz, P., Ghassemi, M., and Chen, N. (eds.), Advances in Neural Information Processing Systems, volume 38, pp. 164448–164473. Curran Associates, Inc., 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "复用视觉token计算。", "claimed_difference": "本篇转述前作按帧差划分token；Reflex按去噪时间依赖划分缓存。", "basis": "target_paper_only", "target_locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页3，§2.2；页12，参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心证据支持有价值的VLA部署整合与性能改善；尚未建立超出固定矩阵分块恒等的一般流式保证，也未证明新的控制机制。", "central_increment": "前作已涉及缓存、异步动作分块及未来状态条件化（仅本篇转述）；本作在时间步不变编码器条件下整合三分区缓存、数值稳定化与重叠执行，表1、5、7–10支持收益，仍待排除弱基线和缓存等价条件缺口。", "soundness_observation": "代数分块解释清楚，但滑窗缓存有效性证明不充分；数值与控制证据均为作者报告，未复现。", "significance_observation": "降低动作生成开销和执行停顿有实际意义；跨模型与实机结果增加适用性证据，但不能外推到全部VLA。", "main_open_question": "FIFO驱逐后，保留跨帧注意力和位置编码的多层缓存是否仍等价于重新计算当前有限窗口？"}

limitations：[{"text": "不覆盖时间条件进入视觉编码器的统一DiT；未来状态近似依赖命令跟踪；正式等价不覆盖异步调度、预测或混精。", "basis": "author_report", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页4，§3.1；页6，§3.3。"}, {"text": "O(1)针对固定窗口的增量操作，不能解释为注意力计算与窗口长度无关；作者在窗口消融中报告延迟随窗口增长。", "basis": "model_inference", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页4，§3.1；页9，Context Window Size。"}, {"text": "全历史重算和错误缓存对照不足以代表最强正确实现；未直接比较所引专用实时方法。", "basis": "model_inference", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页6，§4.1；页7–8，表1、3–4。"}, {"text": "D.2同时写平均延迟与P95，表格统计口径不明；实机称每组20回合却给76±7%等数值，跨重复聚合方式未解释，不能按单组原始成功次数理解。", "basis": "model_inference", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页8，表2；页14，D.2。\n \n"}, {"text": "有限稳定步数不支持无限时域结论；50Hz执行与19.1Hz动作块吞吐、实际新观测重规划频率需要区分。", "basis": "model_inference", "locator": "TEXT_OR_XzsZK1hvpv_64779006c30a，页9，表5；页15–16，D.6、表9。"}]

minimal_check：{"question": "滑窗首次及连续驱逐后是否仍保持缓存等价？", "control": "冻结checkpoint、帧序列、噪声、时间步、掩码及位置ID，关闭异步/预测，使用FP32；对比流式缓存与每次重新计算当前窗口。", "observable_outcome": "逐层保留token的KV差异及动态后缀输出最大误差、MSE，特别检查驱逐前后，不仅看两位小数。", "resources": "可按文中RTX4090 24GB配置测试；需取得checkpoint与实现，运行时间未知，本轮未执行。", "failure_or_stop_condition": "误差超过预设FP32容差则不支持该设置下的等价；缺少位置规则或可匹配checkpoint则停止并记录。"}

missing_fields：["图像及无法可靠恢复的图中绝对数值", "checkpoint标识、模型适配与AdaRMSNorm门控训练信息及成本", "Kinetix具体任务、任务数量、输入输出适配和所称平均回合长度结果", "随机种子、重复次数、统计聚合方式及明确的延迟统计口径", "独立前作全文与实验复现"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

系统优化有部署价值；继续阅读先验证首次/连续驱逐后逐层KV等价和实机统计口径，再采信更强正确性与控制频率陈述。

身份与系统增量：完整题名与16页附件相符，先前失败发送已恢复为唯一有效返回。三分区缓存、精度感知归一化、未来状态近似和异步执行组成系统；大部分组件已有，适用条件是视觉编码器不依赖去噪时间，统一DiT不在范围。未来状态直接近似上一次动作命令，依赖控制器跟踪。

核查定位：p001 title, PDF physical page4, Section3.1, p005, Eq2–3；identity_architecture_and_scope_confirmed

分块注意力与跨驱逐缓存等价：A.1在相同Q/K/V下的分块softmax代数成立，但时间步不变不能保证旧KV在视觉窗口驱逐后仍等于重算值。两层因果均值注意力例：旧[a,b]=[1,0]保留b的第二层V=.5；逐出a追加c0后，动作x0用旧缓存输出1/6，全窗口重算为0。例子满足时间步不变/FIFO，针对多层推广而非固定矩阵恒等式；具体实现须查逐层KV及位置规则。MSE打印0.00不证明逐位相等。

核查定位：PDF physical page13, PropositionA.1/B.1–B.2, PDF physical page8, Table4, local_check/eviction_scope_argument.md；fixed_matrix_identity_confirmed_streaming_extension_needs_extra_condition

速度、吞吐与反应延迟：原表7/8的Pi0.5 RTX4090总延迟135.2→52.4ms、2.58倍、显存8.42→6.15GB、成功78→79.5%。表9的19.1Hz是1000/52.4，p15明确动作插值执行50Hz，非50Hz基于全新观测重规划。Pi0 Long观察到动作延迟226.8→105.2ms与动作块推理延迟另计；固定窗口O(1)不代表对窗口长度常数，原图10延迟随窗口增长。

核查定位：p007, Table1, PDF physical page15, Tables7–8/D.6, p016, Table9, PDF physical page9, Figure10；latency_frequency_and_complexity_denominators_confirmed

稳定性与实际试验范围：原表5 BF16为120–220稳定步、norm-only700–1200、AdaRMS>2000且未观察NaN/Inf，额外延迟.4ms。没有无限时域保证或重复统计；新增门控MLP训练来源未交代。D.2同时写1000次平均与95分位，报告时保留统计口径未明。

核查定位：PDF physical page9, Table5, p014, B.3/D.2；finite_stability_test_and_timing_ambiguity_confirmed

实机与比较协议：原表2称每任务每方法20回合，却给76±7%、66±9%等非5%步长成功率，需解释重复聚合；不能据表反推单组成功次数。FullRecompute/AsyncNaive/错误缓存是主要对照，未见完整专用实时方法同条件比较。实机可行性证据与普遍跨模型优势分开。

核查定位：p007, Section4.4, PDF physical page8, Tables2–4, p016, SmolVLA scope；real_robot_aggregation_and_baseline_limits_confirmed

本地补充/限定：["把滑窗KV疑点具体化为两层因果注意力纸笔例；尚未运行真实实现，固定Q/K/V的分块恒等式保持成立。", "50Hz执行、19.1Hz块吞吐和观察到动作延迟分列。"]

核查局限：["未运行真实checkpoint、CUDA内核、机器人或作者代码；两层例仅代数构造。", "未核读所引用实时VLA前作，未独立确定AdaRMS训练及延迟统计。", "第1页仅读标题开头，其余页按所打印段落/原图核查，版本角色未确认。"]


## pro078 · RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

论文 OR_itonej9GIV；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_itonej9GIV_4c99e4dd93fd", "source_url": "https://api2.openreview.net/pdf?id=itonej9GIV\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_itonej9GIV_4c99e4dd93fd:p001–p027，页标连续，含正文、参考文献及附录A.1–A.23"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未发现缺页；未提供PDF图像，不能核验图示场景、曲线及视觉真实性。", "双栏顺序、公式布局和代码缩进存在提取损失；仅采用可明确对应的正文及表格文本。"]}

问题：如何规模化生成物理可执行、覆盖多种场景和机器人配置的桌面操作示范，并评测策略在环境变化下的泛化？

方法：输入任务描述、API、示例、几何约束与物体功能点；DeepSeek-V3生成程序，仿真每轮执行10次，结合日志和moonshot视觉诊断修复，成功率超过50%或连续失败5轮停止。通过抓取候选扰动与并行规划适配机器人，并随机化杂物、背景、灯光、桌高和语言；示范用于策略关节角回归。

作者主张：以物理执行验证和多模态反馈实现自主闭环专家程序合成。

论文证据：10个共有任务上，R2.0无反馈、日志反馈、多模态反馈的ASR依次为62.1%、66.7%、71.3%；全部50任务为43.34%。

模型推断：支持集成后的生成能力提升，但闭环指离线程序修复，不是策略在线自我学习，也不是执行正确性保证。

定位：['TEXT_OR_itonej9GIV_4c99e4dd93fd:p005，表1', 'TEXT_OR_itonej9GIV_4c99e4dd93fd:p017，表12']

作者主张：提供多样资产、可扩展数据生成器和50任务标准基准。

论文证据：报告731实例、147类别、11,000纹理及五类机器人支持；表6的平均数据收集成功率为52.2%→60.5%。

模型推断：具有可复用的系统与评测价值；五机器人数据生成支持不等于已证明学得策略跨机器人泛化。

定位：['TEXT_OR_itonej9GIV_4c99e4dd93fd:p002–p005，§1、§3', 'TEXT_OR_itonej9GIV_4c99e4dd93fd:p014，表6、A.8']

作者主张：强随机化合成数据改善少样本及零样本实机迁移。

论文证据：表3提供随机化预训练对照；表4、5分别展示RDT和π0实机收益。

模型推断：支持所测条件下的数据增强价值，不能据此推断可普遍替代大规模真实示范。

定位：['TEXT_OR_itonej9GIV_4c99e4dd93fd:p007–p008，表3–5']

key_results：[{"setting": "10个共有任务的程序生成；另报告全部50任务。", "baseline": "R1.0 + MM FB；R2.0 + FB。", "metric_or_guarantee": "ASR、平均修复轮数及代码长度。", "reported_values_and_units": "作者报告R1.0/R2.0 + MM FB：ASR 63.9%/71.3%，修复轮数2.42/1.76，代码长度1465.0/839.7 tokens；R2.0全部50任务ASR为43.34%。", "information_and_compute": "每轮10次仿真；候选程序数N未明确。另按3任务估算VLM每次观察6,894 tokens，不能把代码长度视为完整调用成本。", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p005，表1；p014–p017，A.9–A.10、表10–12"}, {"setting": "Aloha–AgileX上50任务；每任务50条干净示范，Easy/Hard各100次测试。", "baseline": "同一策略在无随机化与随机化测试环境中的表现。", "metric_or_guarantee": "任务平均成功率。", "reported_values_and_units": "作者报告Easy/Hard：RDT 34.5%/13.7%，π0 46.4%/16.3%，ACT 29.7%/1.7%，DP 28.0%/0.6%，DP3 55.2%/5.0%。", "information_and_compute": "VLA使用预训练权重；DP3额外使用1,024点云和理想背景/桌面分割，并非等输入信息比较。", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p006，§4.2；p013，A.5；p020，表15"}, {"setting": "32任务×300轨迹额外预训练，再用每任务50条干净示范适配；正文称5个新任务，表3实际列8个。", "baseline": "未增加RoboTwin预训练、增加Clean预训练。", "metric_or_guarantee": "随机环境下平均成功率。", "reported_values_and_units": "作者报告基线/Clean/Rand：RDT 18.8%/14.6%/24.8%；π0 22.5%/24.9%/29.1%。", "information_and_compute": "RDT预训练100,000步、8 GPU、每GPU batch 16；单任务微调10,000步、4 GPU。π0为100,000步预训练、30,000步LoRA微调，batch 32；GPU型号与耗时未报告。", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p006–p007，§4.3、表3；p013，A.5"}, {"setting": "COBOT-Magic上的RDT；Stack Bowls、Handover Block、Pick Bottle、Click Bell，交叉评测背景是否见过与有无杂物。", "baseline": "10条干净实机示范；对照加入1,000条随机化仿真轨迹或仅用仿真轨迹。", "metric_or_guarantee": "实机成功率。", "reported_values_and_units": "按作者表4等权重算：混合训练四配置均值17.0%→41.375%，增加24.375个百分点；仅仿真在两个未见背景配置均值33.0%，对应实机基线12.25%。这些汇总为本轮算术计算，非复现实测。", "information_and_compute": "zero-shot仅表示没有本实验目标实机示范；仍沿用预训练RDT。相机位置扰动≤1 cm；每格测试次数未报告。", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p007，§4.4；p008，表4"}, {"setting": "π0在Click Bell、Place Empty Cup、Stack Bowls Two的未见实机场景；每任务20次测试。", "baseline": "50条实机示范。", "metric_or_guarantee": "三任务平均成功率。", "reported_values_and_units": "作者报告50 real为8.3%；300 sim加0/10/30/50 real依次为15.0%/25.0%/36.7%/46.7%。", "information_and_compute": "固定300条随机化仿真示范改变实机数据量；该实机实验的完整训练成本未单独报告。", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p008，表5及§4.4"}]

prior_work_candidates：[{"citation_as_printed": "Mu, Y., Chen, T., Chen, Z., Peng, S., Lan, Z., Gao, Z., Liang, Z., Yu, Q., Zou, Y., Xu, M., et al. Robotwin: Dual-arm robot benchmark with generative digital twins. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2025.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "数字孪生、自动示范生成及双臂基准。", "claimed_difference": "新增视觉闭环、强随机化、资产规模及机器人配置支持。", "basis": "target_paper_only", "target_locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p003，§2.1；p011，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Hua, P., Liu, M., Macaluso, A., Lin, Y., Zhang, W., Xu, H., and Wang, L. Gensim2: Scaling robot data generation with multi-modal and reasoning llms. arXiv preprint arXiv:2410.03645, 2024.", "identifier_if_present": "arXiv:2410.03645", "relation_candidate": "背景引用", "shared_component": "多模态语言模型辅助机器人数据生成。", "claimed_difference": "本篇强调模拟执行与视觉诊断修复；未提供对GenSim2的直接等预算实验。", "basis": "target_paper_only", "target_locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p003，§2.1、§3.1；p010，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Wang, Y., Xian, Z., Chen, F., Wang, T.-H., Wang, Y., Fragkiadaki, K., Erickson, Z., Held, D., and Gan, C. Robogen: Towards unleashing infinite data for automated robot learning via generative simulation, 2023.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "生成式仿真与自动机器人学习数据。", "claimed_difference": "作者将相关管线描述为缺少闭环验证，本作增加失败反馈与程序修复；该前作描述未独立核验。", "basis": "target_paper_only", "target_locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p001，§1；p003，§3.1；p011，参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可复用生成系统、资源与有条件的新能力，超过单点提分；尚不足以认定路线级原创。", "central_increment": "RoboTwin 1.0已提供数字孪生生成与基准（本篇转述）；本作在标注资产和固定API条件下增加闭环修复、强随机化及多机器人适配，表1、4支持收益，尚待排除封装、额外数据和人工脚本的作用。", "soundness_observation": "实验支持集成系统有效，但诊断可靠性低、部分报告口径不一致，不能推出可靠自主质检或端到端收益归因。", "significance_observation": "对双臂数据生成和抗域偏移评测有实用价值；绝对成功率、自动任务覆盖及人工/计算成本仍限制扩展结论。", "main_open_question": "固定API、初始程序及执行预算后，视觉修复能否稳定增加有效轨迹，而非主要由重试和既有专家基础设施贡献？"}

limitations：[{"text": "作者将鲁棒性限定为场景布局和外观变化，而非任意外部扰动；所谓动态测试是在episode之间移动物体和更换背景。", "basis": "author_report", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p013，A.7"}, {"text": "作者报告VLM检测准确率43.1%，仅在40个正确识别失败样本中定位成功12个，即30%；明确承认姿态细节和不可见原因易漏检。", "basis": "author_report", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p015–p016，A.10.4"}, {"text": "混淆矩阵TP+FN=29对应成功样本，却将召回解释为失败检出；这与其正负类语义不符，削弱精准诊断论证，但不单独否定整体ASR收益。", "basis": "model_inference", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p015:L0043–L0064；p016:L0028–L0036"}, {"text": "摘要3.6×/2.2×未明确场景及增益口径，不能直接当总体成功率倍数；表3任务数与正文不一致，表6与表16的基线均值也略有差异。", "basis": "model_inference", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p001，摘要；p006–p008，§4.3、表3–4；p014、p021，表6、16"}, {"text": "下游轨迹的自动/人工来源未充分追溯；无等数据量的完整组件到实机消融。表8缺少全随机化对照列，也未独立消融语言随机化。", "basis": "model_inference", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p007–p008，§4.4；p013、p015，A.6、表8；p019，A.19"}, {"text": "A.1声称全程未使用LLM/AI，与方法中的模型使用存在声明范围冲突；A.16的负FID及由p90推断90%高相似覆盖也需核查，不能据此确认真实分布匹配。", "basis": "model_inference", "locator": "TEXT_OR_itonej9GIV_4c99e4dd93fd:p013，A.1；p014，A.10；p018–p019，A.16、表14"}]

minimal_check：{"question": "视觉反馈是否提供独立纠错收益？", "control": "固定R2.0 API、初始代码、场景种子和仿真次数，比较仅日志与日志加视觉反馈；用未参与修复的场景独立测试。", "observable_outcome": "有效轨迹成功率差、失败类型变化及完整调用tokens，而非仅比较生成代码长度。", "resources": "SAPIEN/CuRobo、原代码与指定语言/视觉模型接口；无需训练VLA。GPU配置、运行时间和费用未知。", "failure_or_stop_condition": "独立测试中增益消失、跨种子不稳定或实际预算不匹配，则不能确认视觉诊断的独立贡献。"}

missing_fields：["PDF图像、前作全文及最终出版版身份核验", "各配置候选程序数N、表4每格实机测试次数、训练种子与置信区间", "完整生成和训练成本、GPU型号、资产标注及筛选人时", "下游训练示范的自动生成、人工修改和人工专家程序来源比例"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

资产/API/仿真修复和随机化组合具有可复用价值；使用时先验证生成轨迹来源、真实失败观察器性能和独立场景测试。

身份、程序修复与范围：完整题名、27页同一PDF及规范化全文输入绑定。闭环是给定API/功能点/示例后的仿真程序修复，不是无基础设施自主学习。原表1共有10任务R2无反馈62.1%、日志66.7%、多模态71.3%；全50任务表12只有43.34%。代码长度839.7tokens不等于总调用成本，单次视觉观察另报6894tokens。

核查定位：p001 title, PDF physical page5, Table1, p016, Table10, p017, Table12, p019, A.20；identity_generation_denominator_and_budget_scope_confirmed

纠正VLM失败检测的正类语义：原文130例=29成功+101失败，TP16+FN13=29，因此印出的正类是成功。原.552召回为16/29成功召回，不是失败检出。按失败为正类重算召回40/101=39.6%、精确率40/53=75.5%；12/40=30%定位率仅针对已正确识别的失败，若相对所有101失败则12/101=11.9%。这不单独否定整体ASR提高，但不能据原召回解释可靠失败观察器。

核查定位：PDF physical page15, A.10.4/confusion matrix, p016, Error Localization；positive_class_misinterpretation_corrected

真实迁移数值及外推范围：原表4四配置均值由10实机基线17.0%到混合41.375%，+24.375个百分点；不是24.4%的相对改善。只有仿真的两个未见背景平均33.0%，但仍从公共预训练RDT初始化。表5 pi0三任务每任务20次，50real8.3%，300sim+0/10/30/50real为15/25/36.7/46.7%。不能由小规模任务推断普遍替代大规模真实示范。动态变化是在episode之间，不是执行途中任意扰动。

核查定位：PDF physical page8, Tables4–5, p007, Section4.4, p013, A.5/A.7；real_world_aggregate_arithmetic_and_scope_confirmed

随机化比较与输入限制：表3列8任务，RDT基线/Clean/Rand18.8/14.6/24.8，pi0为22.5/24.9/29.1%，并非每任务都改善。表8只有去掉单因素和全部随机化的列，缺完整随机化基线，不能独立恢复每项下降量。DP3使用理想背景/桌面分割点云，非等输入比较；五种机器人生成支持不等于策略跨机器人迁移。

核查定位：p007, Table3, PDF physical page15, Table8, p013, DP3 protocol, p019, A.19；ablation_and_embodiment_claims_bounded

纹理覆盖统计及声明冲突：原p18确将CLIP-FID−.36称数值噪声；FID理论非负，需核实现误差量级，不能据负数认证分布匹配。p90=.914表示约90%不高于该值，并不能推出90%达到.914；p10=.749才是近90%至少达到的分位参考，且阈值是否足够相似仍需定义。A.1的全程不用LLM声明与文中程序/语言生成范围冲突，应澄清而不推测作者意图。

核查定位：PDF physical page18, A.16, p019, Table14, p013, A.1, p005, language generation；quantile_direction_error_and_reporting_conflicts_confirmed

本地补充/限定：["将成功正类混淆矩阵转换为失败召回39.6%及条件定位率，保留分母。", "原纹理p90不能支持90%高相似覆盖；p10可给不同阈值的下侧覆盖参考。"]

核查局限：["未运行生成代理、作者代码、仿真或实机训练；混淆矩阵和均值仅本地算术。", "未核读RoboTwin1.0等前作或完整发布文件，未验证数据自动/人工来源比例。", "第1页仅读题名；输入修订仅文本传递规范化，PDF版本角色未确认。"]


## pro079 · PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs

论文 OR_PrM9JAYDF6；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_PrM9JAYDF6_1096a61c03f7", "source_url": "https://api2.openreview.net/pdf?id=PrM9JAYDF6\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "a6298d494dd4f8050ec6c3eacc0f6f42eab48df5609f3dbfee64da4457393bef", "source_pdf_sha256": "1096a61c03f7af0c0d3ede2401b4f9c294df71a09ccc003b9a8424c1688ca76b"}], "read_ranges": ["TEXT_OR_PrM9JAYDF6_1096a61c03f7：物理页1—21全部提供文本，含正文、参考文献及附录A—F；页标连续，题名匹配。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—2、附录C照片及案例空间真值不可核验。", "双栏文字存在错接，公式和表格排版可能失真；表1—12主要数值可读，但存在内部不一致。", "版本角色未核实；未提供前作全文、代码或实验日志，本轮未外查或复现。"]}

问题：无语义歧义的抽象几何监督，能否迁移到真实图像的关系、计数和深度判断，并检验监督不足这一瓶颈？

方法：随机生成彩色框、半透明圆或带字母的点，按几何真值产生关系、坐标、计数、最近点和颜色类比QA。将图元叠到原图并追加QA，保留原有问答；训练图像条目数不增加。已有MLLM另用5k纯灰底几何样本做LoRA-SFT，测试沿用真实图像基准。

作者主张：无需人工标注和架构修改，PGT即可改善真实图像细粒度理解，同时维持通用能力。

论文证据：表1覆盖四个LLM配置，表2覆盖五个现成MLLM；真实图叠加与灰底合成后训练均有迁移收益，7M训练数据下仍有效。

模型推断：贡献是可迁移监督配方及其实证，不是新网络或优化算法；通用指标大体稳定，但并非全部不下降。

定位：['TEXT_OR_PrM9JAYDF6_1096a61c03f7：p5—8，表1、2、4']

作者主张：二维距离任务促进三维理解，提示共享距离计算机制；PGT可诊断监督不足。

论文证据：删除距离任务后3D/Depth聚合准确率明显回落；附录C提供作者认定的捷径及纠错案例。

模型推断：支持距离监督的任务相关作用，但不能证明共享神经回路，也不能区分能力被唤起还是新学到，更不能排除其他视觉瓶颈。

定位：['TEXT_OR_PrM9JAYDF6_1096a61c03f7：p7，§5.1及表3；p16—20，附录C']

key_results：[{"setting": "LLaVA-v1.5-Instruct约0.6M；冻结CLIP-L/14@336px；Llama-3-8B。", "baseline": "相同骨干、原始指令训练数据。", "metric_or_guarantee": "作者报告的准确率及百分点变化，非复现实测。", "reported_values_and_units": "What’sUp 77.8%→97.4%（+19.6个百分点）；CV-2D 58.5%→71.8%（+13.3）；CV-3D 61.1%→70.8%（+9.7）。", "information_and_compute": "对齐1 epoch/8 GPU；指令训练2 epochs/16 GPU，batch 128、学习率2e-5。GPU型号及训练时长未报。", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p5，表1；p15，表6—7。\n"}, {"setting": "现成MLLM用5k灰底PGT后训练；不使用真实训练图像。", "baseline": "原模型；同为5k的Specialized Mix，来自TallyQA、VSR及Spatial-Ladder距离子集。", "metric_or_guarantee": "准确率。", "reported_values_and_units": "Qwen2.5-VL-3B：CV-2D 70.9%→74.4%，Mix为70.8%；CV-3D 71.5%→79.3%，Mix为79.9%。PGT并非所有指标占优。", "information_and_compute": "2 epochs，学习率1e-4，batch 64；LoRA r=8、alpha=32，仅训练语言模型Q/K/V低秩参数。GPU与时长未报。", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p6，表2；p16，§B.2及表10。\n"}, {"setting": "Llama-3-8B、LLaVA数据，逐项删除PGT任务。", "baseline": "常规训练及完整PGT。", "metric_or_guarantee": "3D/Depth聚合准确率。", "reported_values_and_units": "表3：基线60.8%，完整PGT 72.9%，删除Distance后61.7%；正文将完整PGT写为70.9%，存在冲突。", "information_and_compute": "沿用指令训练配置；删除任务后是否匹配token数及监督总量未说明。", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p7，§5.1及表3。\n"}, {"setting": "Llama-3-8B在Cambrian-7M上训练。", "baseline": "同一7M数据设置、不使用PGT。", "metric_or_guarantee": "分组平均准确率。", "reported_values_and_units": "Relational 69.7%→75.8%；3D/Depth 62.5%→70.3%。", "information_and_compute": "指令阶段1 epoch、16 GPU，batch 512、学习率4e-5；与0.6M设置同时改变数据来源和超参，不能只归因于规模。", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p8，表4；p15，表8—9。\n"}]

prior_work_candidates：[{"citation_as_printed": "Lei, X., Yang, Z., Chen, X., Li, P., and Liu, Y. Scaffolding coordinates to promote vision-language coordination in large multi-modal models, 2024.", "identifier_if_present": "arXiv:2402.12058", "relation_candidate": "背景引用", "shared_component": "在图像上加入显式空间标记。", "claimed_difference": "本篇将几何标记用于自动生成训练监督，而不只是混合提示。", "basis": "target_paper_only", "target_locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p3，§2；p11，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Wu, P., Zhang, Y., Diao, H., Li, B., Lu, L., and Liu, Z. Visual jigsaw post-training improves mllms, 2025.", "identifier_if_present": "arXiv:2509.25190", "relation_candidate": "比较基线", "shared_component": "无额外人工标注的视觉辅助任务后训练。", "claimed_difference": "本篇转述其使用拼图任务与RL；PGT采用几何QA和监督微调。", "basis": "target_paper_only", "target_locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p3，§2；p6，表2及§4.2；p12，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Fu, S., Bonnen, T., Guillory, D., and Darrell, T. Hidden in plain sight: Vlms overlook their visual representations, 2025.", "identifier_if_present": "arXiv:2506.08008", "relation_candidate": "背景引用", "shared_component": "语言模型未充分利用已有视觉表示的解释。", "claimed_difference": "PGT增加可操作的监督干预，但未直接复验前作的内部表示分析。", "basis": "target_paper_only", "target_locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p8，§6；p9，参考文献；p16，§C.1", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "核心价值是抽象监督向真实细粒度任务的非显然迁移，并有跨骨干、灰底训练和消融支持；不足以认定路线级新框架或已证实的共享机制。", "central_increment": "前作已有视觉标记和自监督视觉任务（仅本篇转述）；本作新增几何QA训练配方及迁移证据，尚待排除等预算替代监督和评测捷径。", "soundness_observation": "配对实验支持性能增益，但统计重复缺失、表文冲突及机制归因过强降低可信度。", "significance_observation": "可作为可复用训练干预和诊断对照；工程主要在数据生成与多模型验证，而非架构重造。", "main_open_question": "二维距离监督带来的提升，究竟是真实深度能力迁移，还是标记定位、输出格式及基准捷径适配？"}

limitations：[{"text": "当前任务仅为基础二维能力的概念验证；3D原语、视频与多步推理仍属未来工作。作者承认任务堆叠实验不严格检验真实背景遮挡。", "basis": "author_report", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p21，附录E—F"}, {"text": "同图像条目数不等于同token或算力。表11独立合成数据的3D/Depth为75.4%，高于叠加的72.9%，但缺少实测训练成本，效率优势尚未量化。", "basis": "model_inference", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p20，附录D及表11。\n"}, {"text": "表3删除关系/计数任务的降幅按表相减为9.7/3.7个百分点，正文写8.3/1.2；表1 Vicuna的SEED配对分数为62.1→64.3，却写提升1.2。原始PDF和结果日志需核验。", "basis": "model_inference", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p5，表1；p7，§5.1及表3"}, {"text": "未报告重复种子或置信区间。专门模型之间后训练预算不同；表2带星号的Spatial-Ladder结果来自原论文，不是同代码复测。", "basis": "model_inference", "locator": "TEXT_OR_PrM9JAYDF6_1096a61c03f7：p5—8，表1—5；p6，表2注释"}]

minimal_check：{"question": "距离监督是否独立改善真实深度判断？", "control": "固定Qwen2.5-VL-3B，比较完整5k PGT与将距离QA替换为同图颜色识别QA的对照；匹配答案分布、token预算、训练配置并重复种子。", "observable_outcome": "分别报告CV-Bench-3D距离/深度子集与BLINK-depth差异，并核查收益是否集中于有标记或位置捷径的题目。", "resources": "3B模型、PGT生成器、相关评测数据及GPU；所需显存、GPU时和额外样本核验成本未知。", "failure_or_stop_condition": "若等预算后优势不稳定，或仅改善标记定位/距离题而不改善深度子集，则不支持独立深度迁移解释。"}

missing_fields：["图像证据、原始结果日志及前作全文。", "GPU型号、训练时长、token/FLOPs开销及后训练GPU数量。", "随机种子、误差区间、完整评测解码设置及生成参数分布。", "附录A部分模板占位符异常的实际实现，以及表文数值冲突的权威更正。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

可自动核真值的几何监督有明确迁移收益，适合作为低成本研究对照；优先做同token替代监督和拆分深度子集的后续设计。

身份、训练机制与成本分母：完整题名与21页当前附件匹配。几何图元叠原图并追加QA，条目数不增加但token/监督量增加；另一设置以5k灰底图、2epochs、LoRAr8/alpha32只调语言Q/K/V，冻结视觉和投影器。无新增人工标签可成立，不能由同条目数推出同FLOPs或零训练成本。

核查定位：p001 title, p004, procedural generation, PDF physical page5, gray-background setting, p016, B.2；identity_mechanism_and_training_budget_scope_confirmed

主收益及非全面优势：原表1 Llama3-8B WhatUp77.8→97.4、CV2D58.5→71.8、CV3D61.1→70.8均确认。原表2 Qwen2.5VL3B PGT的CV3D79.3低于同5k SpecializedMix79.9，CV2D74.4则高于70.8。通用指标存在小幅下降，且无种子区间，不能称所有能力无损或所有对照都领先。

核查定位：PDF physical pages5–6, Tables1–2；decisive_table_values_and_tradeoffs_confirmed

消融值的表文冲突：原表3完整PGT的3D/Depth72.9，去Distance61.7，正文写完整70.9；关系75.7−66.0=9.7而正文8.3，计数55.2−51.5=3.7而正文1.2。表1 Vicuna SEED62.1→64.3应+2.2而印+1.2，Llama MMVP31.3→33.3应+2.0而印+1.2。保留原件，派生解释按配对值相减并标冲突，不猜测权威修正。

核查定位：PDF physical page7, Table3/Section5.1, PDF physical page5, Table1；source_arithmetic_and_text_table_conflicts_confirmed

二维到深度的机制证据：删除距离任务使混合CVBench3D/BLINKdepth指标下降，支持任务相关迁移；尚未做内部电路因果干预，不能证明共享神经距离回路、排除答题格式/标记定位适配或其他视觉瓶颈。p20原图确有精选纠错案例，但不能由三例建立总体机制；叠加多任务实验也明确未严格测试真实背景遮挡。

核查定位：PDF physical page7, grouped metrics and ablation, PDF physical page20, qualitative examples, p021, limitations；transfer_evidence_retained_mechanistic_claim_unverified

叠加与独立合成数据的取舍：原表11独立数据3D/Depth75.4高于叠加72.9，General62.8高于62.2；独立数据可能需更多训练，但未报实测GPU时或token匹配。PGT是有用可复用监督配方，效率与独特机制仍需等预算对照。

核查定位：PDF physical page20, Table11；overlay_accuracy_cost_tradeoff_confirmed

本地补充/限定：["额外核出Llama MMVP增量2.0与印出1.2不符；所有结论依据配对值并保留冲突。", "补看精选照片只支持案例展示，不升级为共享回路或总体空间真值证明。"]

核查局限：["未执行生成器、LoRA训练、benchmark复跑或前作核读。", "未独立裁决精选图像的深度标注，未取得原始成绩与重复种子。", "第1页仅读标题开头，当前附件出版角色未核实。"]


## pro080 · Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex

论文 OR_OQ6jQHJPTT；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6", "source_url": "https://api2.openreview.net/pdf?id=OQ6jQHJPTT\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6：物理页1–58全部所供文字，包括正文1–9、声明及参考文献10–14、附录A–K 15–58；页标连续，题名匹配。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图形、曲线与误差带不可见，不从坐标刻度推断数据点。", "双栏文字交错，式(3)等公式排版有损；主要表格可读，但不能据此确认原PDF排版及版本身份。"]}

问题：静态视觉模型的脑对齐受预训练规模、神经微调数据还是映射拟合数据限制？

方法：图像骨干特征经受试者/ROI读出预测神经响应，以噪声归一化Pearson r评估；训练集嵌套交叉验证选层及ridge系数。spvvs拟合尺度曲线、timm留出验证。微调先拟合并冻结读出，再交替用神经MSE和ImageNet分类更新骨干。共享读出使用16个潜在查询、384维单层cross-attention，保留受试者专属输出头。

作者主张：预训练对齐收益跨模态饱和；增加映射拟合样本带来较强、近似对数线性收益。

论文证据：600+模型覆盖8个神经基准，较大6个基准开展映射样本扫描；另报告随机投影及RSA/CKA稳健性分析。图中精确曲线不能核读。

模型推断：中心价值是统一刻画不同训练阶段的经验瓶颈，而非证明普适尺度定理。

定位：['TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p004–005,§4.1；p007,§4.7；p033,附录E.3。\n \n']

作者主张：神经微调提供互补收益，并可跨数据集及记录模态迁移。

论文证据：六个微调源、八个评测基准及置乱对照支持小幅收益；T-EEG1存在例外，ImageNet准确率下降。

模型推断：扩展了神经监督可迁移性的经验证据，但不说明认知机制相同或任务能力普遍增强。

定位：['TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p005–008,§4.3–4.6及§4.11；p043,附录G.3。\n \n']

作者主张：跨受试者共享注意力能以少约一个数量级的参数改善读出。

论文证据：表2中共享版本在六基准均优于单受试者注意力，但仅四个基准优于线性读出。

模型推断：属于有价值的紧凑读出改进，不能将cross-attention本身视为本篇首创。

定位：['TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p008,表2；p055–058,附录J–K。\n']

key_results：[{"setting": "§4.11汇总的ViT-S预训练至全数据神经微调", "baseline": "原始任务预训练ViT-S", "metric_or_guarantee": "平均rNC及ImageNet分类准确率，均无量纲", "reported_values_and_units": "作者报告：rNC由0.529升至0.535；准确率由0.783降至0.769，即下降1.4个百分点。", "information_and_compute": "AdamW，学习率1e-5，20个神经数据epoch；ImageNet/neural batch为512/256，3个种子，bf16。", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p008,§4.11；p043,表S3。\n \n"}, {"setting": "六个较大基准，以全部可用配对数据拟合读出", "baseline": "Linear-SS及Attention-SS", "metric_or_guarantee": "跨受试者、ROI和3个种子平均的rNC；读出参数数目", "reported_values_and_units": "表2按Linear-SS/Attention-SS/Attention-MS排序：平均rNC为0.516/0.503/0.527，参数为2.30e8/2.53e7/2.06e7。TVSD-EP为0.801/0.844/0.846；T-MEG为0.453/0.410/0.414，显示优势并不普遍。", "information_and_compute": "注意力batch256、10–30epoch；NSD学习率1e-3，其余1e-4；主干特征不随机投影。", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p008,表2；p058,表S5–S6。\n (20260929-195146)\n"}, {"setting": "ViT-S六个微调源×八个评测基准，共48种组合", "baseline": "全权重微调20epoch、学习率1e-5", "metric_or_guarantee": "相对预训练基线的平均ΔrNC", "reported_values_and_units": "全微调约0.0059，统一LoRA配置约0.0042；LoRA在21/48组合中更高。未采用逐数据集事后择优的上界结果。", "information_and_compute": "LoRA rank32、学习率1e-4、20epoch；分类头可训练，其余非适配骨干参数冻结。", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p008,§4.12；p052,附录I。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Gokce, A. and Schrimpf, M. Scaling laws for task-optimized models of the primate visual ventral stream. In Forty-second International Conference on Machine Learning, 2025.", "identifier_if_present": "OpenReview:WxY61MmHYo", "relation_candidate": "方法继承", "shared_component": "spvvs受控模型集与尺度曲线拟合", "claimed_difference": "本作扩展记录模态，并联合分析神经微调与映射阶段。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p011,参考文献；p022,附录B。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Dapello, J., Kar, K., Schrimpf, M., Geary, R. B., Ferguson, M., Cox, D. D., and DiCarlo, J. J. Aligning model and macaque inferior temporal cortex representations improves model-to-human behavioral alignment and adversarial robustness. In The Eleventh International Conference on Learning Representations, 2023.", "identifier_if_present": "OpenReview:SMYdcXjJh1q", "relation_candidate": "组件复用", "shared_component": "神经对齐训练路线及刺激抖动增强", "claimed_difference": "本作研究微调数据规模、架构依赖与跨记录模态迁移。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p010–011,参考文献；p043,附录G.1。\n \n \n", "prior_actually_read": false}, {"citation_as_printed": "Jaegle, A., Gimeno, F., Brock, A., Vinyals, O., Zisserman, A., and Carreira, J. Perceiver: General perception with iterative attention. In Meila, M. and Zhang, T. (eds.), Proceedings of the 38th International Conference on Machine Learning, volume 139 of Proceedings of Machine Learning Research, pp. 4651–4664. PMLR, 18–24 Jul 2021.", "identifier_if_present": "PMLR:139/jaegle21a", "relation_candidate": "组件复用", "shared_component": "潜在查询与cross-attention；附录K明确说明设计受其启发", "claimed_difference": "本作采用轻量单层探针、跨受试者共享及神经响应专属输出头。", "basis": "target_paper_only", "target_locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p012,参考文献；p058,附录K。\n (20260929-195146)\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是跨四类记录模态区分训练阶段的系统经验知识，超出单一基准性能改进；共享读出本身更接近L1，尚不足认定路线级首创。", "central_increment": "前作已研究任务优化视觉模型的尺度律（本篇转述）；本作在静态视觉条件下新增八基准、三阶段的统一分析，证据来自尺度扫描、迁移对照及表2。", "soundness_observation": "嵌套选层、独立模型验证和置乱控制提高可信度；未复现，图形区间不可核，数据量与优化预算仍有混杂。", "significance_observation": "有助于配置脑预测模型的训练资源；工程价值在统一评测和紧凑读出，不等于建立脑机制模型。", "main_open_question": "控制更新步数及ImageNet重放量后，神经微调的数据规模收益是否仍成立？"}

limitations：[{"text": "作者明示：仅静态视觉输入，时间结构被平均或展平；相关预测改善不证明机制对应。“多模态”指记录方式，不是多感官输入。", "basis": "author_report", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p009,Limitations。\n"}, {"text": "预训练C=D×单次前向FLOPs，不含epoch和反传；微调固定epoch随数据量增加也增加更新次数，不能据此建立严格等成本资源排序。", "basis": "model_inference", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p022,式(8)；p043,附录G.1。\n \n"}, {"text": "低秩/MLP先均值池化，参数接近不等于输入信息匹配，注意力优势的具体来源尚未完全分离。", "basis": "model_inference", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p055,附录J.1。\n"}, {"text": "所供文本中，NSD注意力SS/MS在表2为0.678/0.724、表S4为0.677/0.723；参数统计分别写平均及几何平均。差异原因未说明，不合并精确值。", "basis": "model_inference", "locator": "TEXT_OR_OQ6jQHJPTT_9384b8d1dbb6:p008,表2；p056,表S4。\n \n"}]

minimal_check：{"question": "神经样本规模效应是否独立于训练步数？", "control": "以T-fMRI和ViT-S比较10%/100%神经数据，共用仅在10%子集拟合的初始冻结读出；固定总更新数、ImageNet批次数及评测协议，与固定20epoch方案对照。", "observable_outcome": "三个种子下，等更新预算的100%数据仍有稳定正ΔrNC，同时记录ImageNet准确率变化。", "resources": "配对神经数据、ViT-S权重、ImageNet及训练设备；显存和运行时未报告，本轮未执行。", "failure_or_stop_condition": "优势消失或不确定区间覆盖零，则该检验不支持独立数据效应；无法核实数据划分或预算一致性时停止归因。"}

missing_fields：["图像及主要尺度曲线的完整系数、数值置信区间无法核读。", "硬件、总GPU小时、实际训练总FLOPs、神经记录获取成本及LoRA具体可训练参数数目未报告。", "前作全文、原始实验数据和代码未提供；未外部检索、复现或确认最终出版版本。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

跨记录方式拆分三个训练阶段的统一分析有研究价值；继续以等更新预算区分神经数据收益，并匹配读出信息后再谈资源配置。

身份、三阶段分析及多模态含义：完整题名及58页当前附件相符。跨EP/fMRI/EEG/MEG记录方式比较预训练、神经微调及读出拟合；输入仍全为静态视觉，非多感官模型。表S2主spvvs六族合计620检查点，另12个timm用于拟合外验证，不代表本轮从头训练632模型。相关预测改善不建立脑机制对应。

核查定位：p001 title, p004, Methods, p022, TableS2, p009, Limitations；identity_inventory_and_modality_scope_confirmed

主尺度趋势的原图核验：原图2/3显示所测预训练规模上的趋缓和高规模架构差距收窄；原图6映射样本扫描仍上升。四基准拟合渐近值1.0是模型外推，不是已观测完美预测或普适定理。原图5多数迁移正增益但T-EEG1等有负项，不能说所有迁移都改善。未从图轴猜测精确系数或置信区间。

核查定位：PDF physical page5, Figures2–3, PDF physical page7, Figure5/Section4.7, PDF physical page8, Figure6, p055, fitted asymptotes；visual_trends_confirmed_extrapolation_distinguished

对齐与任务性能取舍：原§4.11报告ViT-S平均rNC .529→.535仅+.006，ImageNet .783→.769为−1.4个百分点。全微调/统一LoRA跨48组合平均增益.0059/.0042，LoRA21/48更高；不采用逐数据集事后择优作为主结果。增强脑预测相关不等于全面任务能力增强。

核查定位：PDF physical page8, Sections4.11–4.12；decisive_gain_and_task_accuracy_tradeoff_confirmed

共享注意力读出：原表2平均LinearSS/AttentionSS/MS为.516/.503/.527，MS六基准均优于SS注意力，但仅四项优于线性；T-MEG .414低于线性.453、T-EEG2 .434低于.447。原附录K确认16查询、384维、单层跨注意力，受试者专属线性头；低秩/MLP先均值池化，参数匹配不等于输入token信息匹配。

核查定位：PDF physical page8, Table2, p055–p056, J.1, PDF physical page58, TablesS5–S6；readout_values_and_information_asymmetry_confirmed

计算尺度和统计口径：预训练compute proxy明确为数据条数×单次前向FLOPs，遗漏epoch/反传；神经微调固定20个数据epoch，扩大数据也扩大更新数及ImageNet重放量，不能从扫描独立识别数据效应或真实等成本资源优先级。表2参数称平均、S4称几何平均，NSD .678/.724与S4 .677/.723有.001差，不合并精确值。硬件总GPU时和记录采集成本缺失。

核查定位：p022, Eq8, p043, G.1/TableS3, PDF physical page8, Table2, p056, TableS4；compute_proxy_training_budget_and_reporting_scope_confirmed

本地补充/限定：["原图支持已测范围的趋势，拟合到1.0不等于实测；补充可核查模型清单为620个spvvs检查点加12个timm。", "读出参数汇总保留主表平均与附表几何平均的口径区别。"]

核查局限：["未重训视觉模型、拟合神经数据、重估尺度曲线或执行作者代码。", "未核读前作和原始数据；没有精确提取图中置信带或确认外推参数约束。", "第1页仅读标题开头，版本角色未确认。"]

