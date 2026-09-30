# 单轮全文初评与有界本地核对 1–10

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro001 · ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning

论文 OR_FTC7najzZT；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_FTC7najzZT_7c6a943539d4", "source_url": "https://api2.openreview.net/pdf?id=FTC7najzZT\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_FTC7najzZT_7c6a943539d4：物理页1–8正文、9–10声明及参考文献、11–22附录A–E；全部所供文本已读，页标连续，未发现文本缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–18仅有题注和抽取文字，不能核验照片、几何示例、曲线或柱高；图16密集标签严重交错。", "部分双栏文字、公式(1)及Algorithm 1符号排版粘连；表1–14主体数据可辨，但颜色与视觉布局不可核验。", "未提供前作、其他版本、视频或代码；未搜索、未复现。当前附件不认定为最终出版版。"]}

问题：如何使视频空间QA的真值与模型实际看到的帧一致，避免把缺失证据或错误标注误判为空间推理失败？

方法：输入室内视频、网格与相机姿态，专家修正对象名、重力对齐OBB及房间多边形；记录可见性，重建16/32/64/all帧对应QA，并用去目标帧、重复帧和黑视频诊断证据依赖。不训练新模型。

作者主张：通过专家重标、问题重建与偏置控制，提高空间评测数据的准确性和多样性。

论文证据：表1报告381个场景、5365个对象、504种标签；VSI-Bench对应288、3185、65。

模型推断：有明确价值的数据重建；规模扩充本身不能证明标注误差已充分消除。

定位：['TEXT_OR_FTC7najzZT_7c6a943539d4：p4，§4.1、Table 1；p11，B.1–B.2。\n']

作者主张：按实际输入帧构建QA，保证问题可回答及真值正确。

论文证据：表7量化采样导致的失效；§5及B.5给出分预算真值、嵌套采样和帧索引方案。

模型推断：核心增量是将可观察证据纳入评测定义，不只是清洗更多数据。

定位：['TEXT_OR_FTC7najzZT_7c6a943539d4：p5–6，§5；p11，Table 7；p15，B.5']

作者主张：旧评测高估部分开源、专用模型；证据移除测试揭示先验依赖与幻觉。

论文证据：表3–6报告模型重评、基座对照及16帧dummy实验，显示显著行为差异。

模型推断：支持已测模型的视觉证据依赖不同，但不能据此确证训练污染或噪声监督的因果作用。

定位：['TEXT_OR_FTC7najzZT_7c6a943539d4：p6–8，§6、Tables 3–6']

key_results：[{"setting": "VSI-Bench均匀采样；假定all-frame标注正确，仅考察可见性", "baseline": "原全帧真值", "metric_or_guarantee": "采样后原GT仍正确的题数／总题数", "reported_values_and_units": "计数：16帧432/565，64帧533/565；Appearance Order：16帧174/618，64帧431/618。", "information_and_compute": "基于对象可见性核查，不是模型推理成绩；人工成本未量化。", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p3，§3；p11，Table 7。\n"}, {"setting": "零样本评测，VSI-Bench→ReVSI", "baseline": "同一模型在旧基准的成绩，非同题配对", "metric_or_guarantee": "任务均分，百分制；NQ为MRA，MCQ为Acc", "reported_values_and_units": "Qwen3-VL-32B-Instruct：61.8→53.3；Gemini 3 Pro：60.5→60.9。", "information_and_compute": "Qwen使用64帧全量评测；Gemini使用1fps，ReVSI仅1093题tiny子集，旧基准使用官方tiny集；非等预算比较。", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p7，Table 3；p19，D。\n \n"}, {"setting": "32帧下Qwen2.5-VL-7B-Instruct与SpaceR-7B比较", "baseline": "对应未微调基座", "metric_or_guarantee": "七任务均分，百分制", "reported_values_and_units": "基座→SpaceR：VSI-Bench为37.7→43.5，ReVSI为33.9→30.5。", "information_and_compute": "使用发布模型及其评测设置；不是本篇重新训练的受控实验。", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p8，Table 4。\n"}, {"setting": "16帧dummy计数，表注报告997题，GT均为0", "baseline": "Query-Drop与Black输入对照", "metric_or_guarantee": "Exact Match正确率，不使用零分母MRA", "reported_values_and_units": "Query-Drop/Black：Qwen3-VL-32B为50.5%/100.0%；InternVL3.5-38B为9.1%/1.2%；Spatial-MLLM-4B-820k均为0.0%。", "information_and_compute": "移除目标帧或替换为黑帧；具体推理资源未报告。", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p8，Table 5。\n"}, {"setting": "16帧尺寸估计，Real与Black对照", "baseline": "同模型真实视频输入", "metric_or_guarantee": "相对原尺寸GT计算MRA，百分制", "reported_values_and_units": "Real/Black：Qwen3-VL-32B为68.6/0.3；InternVL3.5-38B为70.2/48.6。", "information_and_compute": "黑视频没有尺寸视觉证据，但评分真值并非0；未报告运行成本。", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p8，Table 6。\n"}]

prior_work_candidates：[{"citation_as_printed": "Yang, J., Yang, S., Gupta, A. W., Han, R., Fei-Fei, L., and Xie, S. Thinking in space: How multimodal large language models see, remember, and recall spaces. In Proceedings of the Computer Vision and Pattern Recognition Conference (CVPR), 2025a.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "VSI-Bench任务、模板、QA生成及指标。", "claimed_difference": "从全场景固定GT改为视频纠错与按帧预算构建GT，增加去偏和证据移除诊断。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p4–6，§4–6；p10，References；p15–17，B.6–B.8。\n", "prior_actually_read": false}, {"citation_as_printed": "Zhang, J., Chen, Y., Zhou, Y., Xu, Y., Huang, Z., Mei, J., Chen, J., Yuan, Y., Cai, X., Huang, G., Quan, X., Xu, H., and Zhang, L. From flatland to space: Teaching vision-language models to perceive and reason in 3D. arXiv preprint arXiv:2503.22976, 2025a.", "identifier_if_present": "arXiv:2503.22976", "relation_candidate": "背景引用", "shared_component": "SPAR-Bench：由3D标注构造视频空间QA，本篇转述。", "claimed_difference": "ReVSI强调标注与实际视频输入一致；本篇未对SPAR-Bench实施同等规模的错误审计。", "basis": "target_paper_only", "target_locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p2–3，§2–3；p10，References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献包含输入条件化评测协议及可操作的证据依赖诊断，超出局部扩充数据；尚不足以认定路线级首创。", "central_increment": "前作已提供空间视频QA（仅本篇转述）；本作按实际可见帧调整问题和真值，并用证据移除揭示旧分数掩盖的行为差异。", "soundness_observation": "全文支持诊断现象，但因果解释、独立标注准确性及部分实现口径仍待验证；全部实验数字均为作者报告。", "significance_observation": "可能改变空间VLM比较及训练数据质量判断；主要工程难度是专家几何标注与逐帧核验，而非新网络训练。", "main_open_question": "固定同一批问题、帧、提示和答案分布后，仅纠正GT是否仍会改变基座与微调模型的相对表现？"}

limitations：[{"text": "专家人工标注昂贵，限制扩展到训练规模；当前数据范围为室内场景。", "basis": "author_report", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p8，Limitations & future work"}, {"text": "重标、类别扩展、模板与答案分布同时改变；闭源tiny集及不同帧预算进一步混杂，不能将排名变化完全归因于原GT错误。", "basis": "model_inference", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p4–8，§4、Tables 3–4；p19，D"}, {"text": "长距离在相对误差MRA下容许更大绝对误差；16帧又少两类任务，跨设置均分不能直接解释为能力差异。", "basis": "model_inference", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p6，§6.1–6.2；p22，Tables 12–13"}, {"text": "135k→820k训练量对应表4均分40.5→40.9，正文却称约3%；该文字不能直接作为ReVSI增益引用。", "basis": "model_inference", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p7，§6.2；p8，Table 4。\n \n"}, {"text": "方向任务最小间距正文写1m、B.8写1.5m；5%覆盖自动可见规则与B.4全人工判定的表述也需核对实际实现。", "basis": "model_inference", "locator": "TEXT_OR_FTC7najzZT_7c6a943539d4：p5，§4.2；p6，§5.1；p15，B.4；p16，B.8"}]

minimal_check：{"question": "仅更换正确GT，是否足以消除SpaceR的计数优势？", "control": "选两版共有场景、32帧内目标仍可见的原始计数题，固定提示和两模型输出，仅以旧GT和双人盲核的帧内GT重新评分。", "observable_outcome": "基座与SpaceR的配对MRA差及其按场景重采样区间是否改变符号。", "resources": "共有题、固定帧索引、两模型预测及人工复核；缺少预测时需推理，硬件和工时未知。", "failure_or_stop_condition": "优势仍保留则不支持将其消失单独归因于GT纠错；无法建立共享题或可靠独立GT则停止。"}

missing_fields：["原PDF图像、前作全文、其他版本及当前附件出版身份未核实。", "GPU配置、推理时长、API总费用、标注工时未报告。", "独立标注误差率、一致性统计、重复运行区间及人工dummy评测细节未报告。", "128帧和FPS输入对应逐题真值的可复核映射细则不足。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得继续读评测定义与控制设计；下一关键问题是固定共享题、帧、提示和预测，仅改经独立核验的GT是否仍使模型相对优势翻转。

题名、版本及完整材料：首物理页完整题名与冻结名单一致；来源为官方API当前附件，出版/定稿身份未确认。Pro明示读完1–22页文本，图像未供给；本地附件预览逐块完整匹配输入，22个页标和末尾标记齐全。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro001_attachment_preview_full.txt；pass_with_stated_version_limit

中心增量及适用条件：§4.1重标对象及几何，Table1为381/5365/504与288/3185/65。§5.1明确按16/32/64/all-frame重建QA；p6可见性超过画面5%时自动判可见、否则人工标注，16帧排除房间面积和路线。支持输入条件化评测机制；并不自动保证所有几何量从可见帧唯一可定。

核查定位：p004:L0003-L0009, p004:L0032-L0073, p005:L0073-L0086, p006:L0003-L0036；supported_with_scope_conditions

决定性模型比较：p8原PDF Table4确认32帧下基座旧/新均分37.7/33.9，SpaceR为43.5/30.5。模型相对优势改变为作者报告，非同题只改GT的随机干预，不能将因果归因于训练污染或纠错单因素。

核查定位：p008:Table4, p008:L0016-L0017, local_check/p008.png；reported_numbers_match_causal_limit_retained

dummy指标及跨模型预算：原PDF Table5确认997题Exact Match：Qwen32B Query-Drop/Black=50.5/100.0，InternVL38B=9.1/1.2；Table6是尺寸MRA，Qwen68.6/0.3、Intern70.2/48.6。Pro正确区分两种指标。p19 D确认专有模型仅1093题tiny，Gemini用FPS采样；Table3跨模型不属严格等预算。

核查定位：p008:Tables5-6, p019:L0008-L0028, p007:L0016-L0024；numbers_and_critical_metric_distinction_match

采样有效性统计：Table7作者报告计数正确题16帧432/565、64帧533/565，出现顺序174/618与431/618，和Pro引用一致；正文/附录的作者核验不等于独立人工审计。

核查定位：p011:Table7, p011:L0034-L0054；fractions_match

本地补充/限定：[]

核查局限：["仅有界核查列出的正文、表格与条件，未复核所有22页或所有图像。", "未核读VSI-Bench等前作；不存在独立历史首创裁决。", "没有运行作者代码、重新标注视频或复现实验；Pro L2仍为未校准模型判断。", "UI原始返回中的Pasted text及换行是可见引用标记，未当作论文来源内容。"]


## pro002 · Vision Language Models Cannot Reason About Physical Transformation

论文 OR_1xZeIkqDPs；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_1xZeIkqDPs_999a3e237024", "source_url": "https://api2.openreview.net/pdf?id=1xZeIkqDPs\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_1xZeIkqDPs_999a3e237024：物理页1—9，正文§1—6。", "TEXT_OR_1xZeIkqDPs_999a3e237024：物理页10—15，影响声明、致谢、参考文献。", "TEXT_OR_1xZeIkqDPs_999a3e237024：物理页16—29，附录A—P，包括表2—6、图注和提取出的图中文字。全部提供文本已读，页标连续。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像或原视频；图1—18的视觉内容均未核读，不能验证实际动作、曲线或热图。", "双栏文本存在交错；表2—6基本可读，部分图中数字与标签对应不可靠。图6跨基准相关系数、图16—17完整机制分析数值不可恢复。", "未提供前作全文、其他版本、逐题预测或作者代码；未搜索、复现或执行作者代码，不认定本版本为最终出版版。"]}

问题：VLM能否在数量、长度、液体体积和橡皮泥Size的外观变换中，区分目标量保持与实际改变，而非默认回答相同？

方法：录制192个守恒视频及192个匹配非守恒控制；3种抽帧方式×5种帧数（3/5/7/9/16）×4种提示形成60条件。112个VLM接收时序多图与三选一问题；选项反平衡，规则匹配失败后由4个LLM评审，至少3个一致才接受，否则FAIL计错。统计普通准确率和配对双题全对率，另做白图、纯文本及单模型注意力分析；未训练新模型。

作者主张：提出以变换不变量为目标的认知启发基准ConservationBench。

论文证据：四属性各48对视频，384视频展开为23,040个输入条件实例；人类864题子集准确率98.35%。

模型推断：明确价值是成对控制和可系统变化的任务设计；23,040不是独立物理场景数量，也不是新物理原理。

定位：['TEXT_OR_1xZeIkqDPs_999a3e237024，物理页3—5，§3—4.2；物理页16、19，附录A—B、G。']

作者主张：模型依赖数量不变先验，不能可靠整合变换证据；增加帧数、提示和精选帧不能恢复稳健能力。

论文证据：112模型的守恒与非守恒准确率呈负相关r=-0.510；62模型视觉移除控制显示回答向相同迁移。多因素实验未发现随帧数增加的稳定收益。

模型推断：匹配反例提供了超出总准确率的实质行为诊断；但不能将跨模型相关解释为因果权衡，也不能据此断言所有物理变换推理均不存在。

定位：['TEXT_OR_1xZeIkqDPs_999a3e237024，物理页5—8，§4.3—4.5；物理页23—26，附录J—N。']

作者主张：非守恒任务中的错误相同判断来自首帧锚定及状态更新不足。

论文证据：Qwen2.5-VL-7B-Instruct的NC same error比NC correct更自信，且第20—27层更偏向首帧；仅能依据正文和附录文字确认作者报告。

模型推断：这是相关性失败特征，不是架构瓶颈的因果证明。

定位：['TEXT_OR_1xZeIkqDPs_999a3e237024，物理页8—9，§4.7；物理页27—28，附录O。']

key_results：[{"setting": "112模型，四属性、守恒/非守恒及60输入条件的汇总。", "baseline": "6名人类参与的864题子集，并非模型全量题集；按192:192标签构造，本轮推得恒答相同的单题基线为50%。", "metric_or_guarantee": "守恒准确率、非守恒准确率、二者平均及严格配对准确率。", "reported_values_and_units": "作者表5报告gemini-2.5-pro依次为94.33%、43.88%、69.11%、41.20%；人类依次为98.55%、98.15%、98.35%、96.72%。", "information_and_compute": "推理集群为8×NVIDIA H100 80GB，按模型大小使用1—8卡；总GPU时、商业API费用和实际总调用量未报告。", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页5，§4.2；物理页18，附录E；物理页20，表5。\n"}, {"setting": "62个支持图文及纯文本输入的模型，固定7帧对应条件，保持问题文本不变。", "baseline": "真实图像输入，对照为全白图像和完全无图像。", "metric_or_guarantee": "图3图注定义的原预测→控制预测转移比例，不等同真值准确率。", "reported_values_and_units": "白图条件：原相同→相同85.7%，原两类不相同→相同71.5%/75.4%；纯文本对应73.7%、69.1%/68.2%。", "information_and_compute": "仅62模型子集；未给出可重算各条件平衡准确率的逐题输出。", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页6，§4.3、图3图注。\n"}, {"setting": "以112模型为重复测量单位，分别分析Number/Length与Volume/Size。", "baseline": "4提示、5帧数和3抽帧方式；其余因素先取平均，成对比较使用Bonferroni校正。", "metric_or_guarantee": "准确率主效应与成对差异。", "reported_values_and_units": "帧数效应p分别为0.416和0.032，后者仅7帧优于9帧。Number/Length上Continuous优于Direct，校正p=0.0191，CoT更差；Volume/Size上Uniform优于人工及SEVILA抽帧，校正p=0.0006/0.0014。", "information_and_compute": "结果支持无稳定增帧收益，不支持所有提示或抽帧完全无影响；相应准确率效应量未在可读正文列出。", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页7，§4.4。\n"}]

prior_work_candidates：[{"citation_as_printed": "Li, Y., Gao, Q., Zhao, T., Wang, B., Sun, H., Lyu, H., Hawkins, R. D., Vasconcelos, N., Golan, T., Luo, D., and Deng, H. Core knowledge deficits in multi-modal language models. arXiv preprint arXiv:2410.10855, 2025a.", "identifier_if_present": "arXiv:2410.10855", "relation_candidate": "组件复用", "shared_component": "核心知识评测、两阶段答案评分及概念解释提示。", "claimed_difference": "本篇聚焦连续变换中目标量保持与改变的匹配诊断。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页4、7，§4.1、4.4；物理页12，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Sun, H., Yu, S., Li, Y., Gao, Q., Lyu, H., Deng, H., and Luo, D. Probing perceptual constancy in large vision language models. arXiv preprint arXiv:2502.10273, 2025.", "identifier_if_present": "arXiv:2502.10273", "relation_candidate": "背景引用", "shared_component": "恒常性与视觉推理缺陷的邻近评测主题；不据引用推定继承。", "claimed_difference": null, "basis": "target_paper_only", "target_locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页3，§2；物理页13，参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Zheng, Z., Yan, X., Chen, Z., Wang, J., Lim, Q. Z. E., Tenenbaum, J. B., and Gan, C. Contphy: Continuum physical concept learning and reasoning from videos. arXiv preprint arXiv:2402.06119, 2024.", "identifier_if_present": "arXiv:2402.06119", "relation_candidate": "背景引用", "shared_component": "从视频评估物理概念和材料动力学。", "claimed_difference": "本篇将相关工作概括为偏结果预测或描述推断，并强调自身对变换不变量的检验；未给出逐任务覆盖比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页2—3，§2；物理页15，参考文献。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "最有价值的是匹配反例揭示的跨模型不对称行为，而不只是新增榜单。可暂列实质经验认识，但不能升级为普遍失能或已确立的架构机制。", "central_increment": "前作已有核心知识和恒常性评测（本篇转述）；本作在四域受控视频条件下新增守恒/非守恒成对诊断，揭示高守恒得分可伴随违反条件识别失败；尚待排除评分口径及普通感知混杂。", "soundness_observation": "两道三选一若独立均匀猜测，严格全对机会率应为1/9≈11.11%，不是正文33.3%。据表5—6逐项计数，27款点估计超过11.11%，并非仅3款；这不等于统计显著。另图3的85.7%按原预测条件化，不能直接和真实守恒准确率约60%比较，更不能证明视觉降低平衡准确率。\n", "significance_observation": "适合作为状态跟踪的诊断测试；大规模评测有工程价值，但未展示修复方法、因果机制或下游机器人收益。", "main_open_question": "按真实标签对齐控制结果并修正配对零假设后，真实视觉究竟改善还是损害成对任务表现？"}

limitations：[{"text": "仅四属性和实验室条件；机制分析仅一个模型，跨家族因果验证及规划、工具使用、机器人影响均未完成。", "basis": "author_report", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页9，§4.7、§6。"}, {"text": "未见首末帧、末帧或时间乱序基线，不能充分隔离静态感知与时序更新瓶颈；Size题用size提问却以总质量描述真值，存在术语歧义。", "basis": "model_inference", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页2—4，§3；物理页16，表2。"}, {"text": "附录K同一白图相关系数出现0.678与0.578；附录L的n=10、r=0.591/0.362与p<0.0001需核查统计单位。高FAIL模型排除阈值、名单和评分映射错误率未报告。", "basis": "model_inference", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页4、18，§4.1、附录F；物理页25，附录K—L。"}, {"text": "跨模型尺寸相关和单个Cosmos Reason结果不能推出受控扩模或各种后训练都无效；人类子集与模型全量评测也不是完全相同的抽样范围。", "basis": "model_inference", "locator": "TEXT_OR_1xZeIkqDPs_999a3e237024，物理页5、8，§4.2、4.5；物理页26，附录N。"}]

minimal_check：{"question": "视觉有害结论能否通过真值对齐的重评分审计？", "control": "使用同一62模型、7帧对应条件的实图/白图/纯文本输出，固定视频对、提示及真值；重算平衡准确率和严格配对率，以独立均匀猜测1/9作明确参照。", "observable_outcome": "报告实图相对两控制的配对准确率差，并按视频对聚类估计不确定性，而非使用预测类别转移率代替准确率。", "resources": "需要逐题输出、真值和配对ID；取得已有输出后可用CPU统计，无需重训，实际耗时未知。", "failure_or_stop_condition": "若实图并未稳定低于控制，视觉降低平衡表现的强结论不成立；缺少原始输出则停止数值判定。"}

missing_fields：["prior_work_candidates[1].claimed_difference：正文未给出与该前作的明确逐项差异。", "原视频、图像及机制图完整数值缺失；前作覆盖关系未核读。", "逐题预测、评分审计、FAIL排除细则及重复运行不确定性未提供。", "总GPU时、API费用、逐模型实际推理预算及完整调用快照未报告。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

保留成对诊断设计的价值；采用强失能或视觉损害结论前，应重算明确零假设下的配对统计和按真实标签分组的控制准确率。

身份、版本与范围：首物理页完整题名匹配；官方API当前附件与29个物理页文本绑定。Pro声明正文、参考文献、附录均读且未见视频/PDF图像，和实际传递相符；没有认证最终出版身份。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro002_attachment_preview_full.txt；pass_with_material_limits

中心配对设计：四种属性各48个守恒视频及匹配非守恒控制，输入条件展开不能当成独立物理场景数。正文定义严格配对正确需两题都对，能揭示高守恒成绩伴随非守恒识别失败；跨模型相关不能单独证明架构因果机制。

核查定位：p003:L0049-L0057, p005:Figure2 caption, p005:L0032-L0043；paired_design_and_scope_supported

严格配对机会率：每题三选一、两题独立均匀猜测时全对概率为1/9=11.111%，而非正文用于严格配对的33.3%。按Tables5–6完整112个模型行（唯一排名1–112）复算，严格点估计高于1/9者27个，高于33.3%者3个，与Pro所述一致。这不构成27个显著高于机会，也不声称独立均匀猜测是唯一合理基线。

核查定位：p004:§4.1 Evaluation, p005:L0032-L0043, p020:Table5, p021:Table6, local_check/pairwise_chance_recalculation.json；null_baseline_mismatch_confirmed_under_explicit_null

图3与视觉损害结论：原PDF图注明确行是完整视觉下的预测、列是控制条件预测；同页正文又按任务真值讨论85.7%并直接比较约60%真实守恒准确率，轴标签也写Task。本地确认这一口径冲突。若按图注，85.7%是条件转移比例，不能直接作真值准确率；没有原始预测，不能确定实现究竟采用哪个分母，更不能认定视觉损害了平衡准确率。

核查定位：p006:Figure3 and caption, p006:L0039-L0053, local_check/p006.png；conditioning_ambiguity_confirmed_implementation_unverified

本地补充/限定：[{"kind": "qualification", "detail": "Pro将图3解释为原预测条件化有图注依据；本地补充正文和轴标签使用任务措辞，应报告内部口径冲突，不能仅凭图注确认真实计算实现。"}]

核查局限：["未查看原视频、逐题输出或作者代码，不能复算真实任务准确率或判定机制。", "112行计数是论文表中点估计的派生统计，未进行显著性检验或多重比较校正。", "未核验所有消融p值、跨家族机制泛化或人类抽样代表性；无独立前作审读。"]


## pro003 · SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads?

论文 OR_0pyFbZSfbT；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_0pyFbZSfbT_aba2323d1597", "source_url": "https://api2.openreview.net/pdf?id=0pyFbZSfbT\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "3e046e1a1c6769ef02d6d0a0305fbca50e2c46df84d2afb0f0a13068243853b4", "source_pdf_sha256": "aba2323d15976761a5049359d55b114c981a75def7e7e75d3b12415544be9b82", "note": "仅提供全文提取文本；题名匹配，物理页标1—39连续；未核定为最终出版版。"}], "read_ranges": ["TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页1—9，正文、结论及影响声明。", "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页10—11，参考文献。", "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页12—39，附录A—N，包括提示词、代码示例、表格及图注文本。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；分布图、曲线及火焰图不可视觉核读，图注与代码提取文本不等于看过原图。", "双栏文字、表2/3及附录I公式局部混排；主结果交叉读取较清晰的表6/7，不推测未提取的图形数值。", "未提供前作全文、作者评测代码、完整任务数据或模型轨迹；未搜索、执行代码或复现实验。"]}

问题：给定完整仓库与固定慢负载，代理能否自行定位瓶颈和相关测试，修改库代码实现加速，同时维持既有测试通过？

方法：筛选性能PR，结合动态覆盖与静态符号展开选取覆盖gold diff的测试，人工编写负载并验证前后性能。代理仅获仓库、负载及构建/测试命令，不获gold patch或评测测试名单。有效补丁SR=SpeedupLM/Speedupgold=Tgold/TLM，下限0.001；空补丁或测试失败回退为max(1/Speedupgold,0.001)，全量取调和均值。

作者主张：提出更贴近真实调查式性能工程的498任务、9仓库基准。

论文证据：任务将固定性能负载与仓库原有正确性测试分离，允许不同于专家的优化方案。

模型推断：增量是任务信息边界与验收协议的组合，而非首次提出仓库级优化。

定位：['TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页3表1、页4§2.2—2.3、页17表5。\n']

作者主张：提供可扩展、可复现的数据构建和评测流水线。

论文证据：96,457个PR经筛选至9,257、1,041，最终498任务；1,041项负载标注约耗200作者小时。

模型推断：具有实质工程价值，但环境配置与负载标注是半自动过程。

定位：['TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页18—23附录E。\n']

作者主张：代理总体远落后于专家，主要表现为误定位、捷径偏好和提前停止。

论文证据：报告15模型的SR与正确性结果，并以5种配置的profiling归因和补丁案例分析失败模式。

模型推断：支持给定协议下存在性能差距，但不足以把误定位确认为主要因果机制。

定位：['TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页6—9§4、页28—31附录I、页38—39补丁示例。']

key_results：[{"setting": "498任务，OpenHands，15模型；以下均为作者报告。", "baseline": "对应专家补丁SR=1.0×；原始代码作为耗时基线。", "metric_or_guarantee": "SR调和均值，以及通过正确性检查且快于专家的任务比例。", "reported_values_and_units": "Claude 4.5 Opus：0.225×；GPT-5：0.157×；GPT-5.2：0.148×。GPT-5.2仍有52%任务正确且快于专家，11%测试失败，说明低SR不等于低成功率。", "information_and_compute": "n2-standard-64主机：64 vCPU、256GB；每worker 4 vCPU、16GB。每题3小时、100动作，每步30分钟；OpenHands无美元上限，SWE-agent另限每题1美元，不能直接作等预算框架比较。", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页5§3、页26表6、页27表7。\n"}, {"setting": "附录I的5种模型—框架配置，仅保留正确且speedup≥1的实例。", "baseline": "gold补丁的函数性能归因。", "metric_or_guarantee": "ERCfile、ERCfunc。", "reported_values_and_units": "ERCfile为0.519—0.630，ERCfunc为0.246—0.314；这是归因质量覆盖，不是任务误定位概率。", "information_and_compute": "每配置分析193—252个实例；额外profiling成本未报告。", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页30表9、页31表10。\n"}, {"setting": "固定gold补丁，对比人工与Gemini 2.5 Flash生成负载。", "baseline": "人工标注负载。", "metric_or_guarantee": "暴露性能增量的大小及显著性。", "reported_values_and_units": "人工负载在76%案例中显示更大增量；47%的模型负载未显示显著增量。", "information_and_compute": "模型仅获diff与修改前文件，人工还获得PR描述及讨论；作者承认信息不对等，不能归因为纯粹能力差异。", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页31—33附录K。\n"}, {"setting": "附录H.3早期100题SWE-FFICIENCY LITE、OpenHands实验，不与全量结果合并。", "baseline": "Gemini 2.5 Flash。", "metric_or_guarantee": "SR、总token费用、累计请求延迟。", "reported_values_and_units": "Pro/Flash分别为SR 0.008×/0.007×，费用509.52/98.83美元，累计请求延迟9.03/6.29小时。", "information_and_compute": "费用含prompt caching；延迟为各请求之和，不是并行作业墙钟时间。", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页27表8。\n"}]

prior_work_candidates：[{"citation_as_printed": "Shetty, M., Jain, N., Liu, J., Kethanaboyina, V., Sen, K., and Stoica, I. Gso: Challenging software optimization tasks for evaluating swe-agents, 2025.", "identifier_if_present": "arXiv:2505.23671", "relation_candidate": "背景引用", "shared_component": "真实仓库性能优化任务；作为任务设计对照，非同场实测基线。", "claimed_difference": "本作公开性能负载，不提供GSO式正确性oracle。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页1引言、页7—8§5、页10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Fan, Z., Huang, Y., Yuan, Z., Ma, Z., Liu, Q., et al. SWE-Perf: Can language models optimize code performance on real-world repositories? arXiv, 2025.", "identifier_if_present": "arXiv:2507.12415", "relation_candidate": "背景引用", "shared_component": "仓库级优化及原有单元测试。", "claimed_difference": "本作不指定优化函数，并将正确性与性能负载分离。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页1引言、页7§5、页10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. R. SWE-bench: Can language models resolve real-world github issues? In The Twelfth International Conference on Learning Representations, 2024.", "identifier_if_present": "OpenReview:VTF8yNQM66", "relation_candidate": "方法继承", "shared_component": "GitHub任务采集与仓库评测基础设施。", "claimed_difference": "反转测试修改筛选条件，转向pass-to-pass性能任务，并新增覆盖测试选择和负载标注。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页2§2.1、页10参考文献、页19附录E.2。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "核心价值是将代码理解、瓶颈定位和测试定位纳入可执行的大规模评测，而不只是增加题量；尚不足以判断为路线级首创。", "central_increment": "前作已做到仓库级性能优化评测（本篇转述）；本作在公开固定负载、不提供目标函数或测试名单的条件下新增调查式协议，498实例支持其可操作性；尚待排除gold导向验收的盲区。", "soundness_observation": "环境与筛选工程较充分，但测试通过不等于语义等价，归因和部分数值存在下列核验问题。", "significance_observation": "对性能工程代理有实用研究价值；新意主要属于数据与协议，非新训练或优化算法。", "main_open_question": "当代理修改gold范围之外的代码时，固定的gold覆盖测试是否系统性漏检回归？"}

limitations：[{"text": "作者明确限定于9个主要Python/Cython库；非CPU硬件、更长负载及多目标性能尚待扩展。", "basis": "author_report", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页8§6。"}, {"text": "测试按专家diff选择，却允许代理任意修改库代码；因此覆盖专家改动不能自动保证覆盖代理引入的全部风险。", "basis": "model_inference", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页17表5、页20附录E.3。"}, {"text": "按可读公式，I.3的专家mass重新汇总选中文件内各函数的累积耗时差，而非仅使用I.2的非重叠函数集，可能重复计入调用链；低ERC不能直接解释为误定位主因。", "basis": "model_inference", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页29附录I.2—I.3。\n"}, {"text": "正文GPT-5 Mini的0.019×与表2/6的0.039×不一致；表11重测分数与主表亦未对齐，不能据此认定全部主实验及轨迹生成均稳定。", "basis": "model_inference", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页5§4.1、页26表6、页37附录N表11。"}, {"text": "附录L.2先称spawn，后文及示例使用fork；示例按repeat隔离但每个进程仍执行number=5次调用，未证明逐次调用均无缓存复用。", "basis": "model_inference", "locator": "TEXT_OR_0pyFbZSfbT_aba2323d1597：物理页34—36附录L.2。\n"}]

minimal_check：{"question": "gold覆盖测试是否漏掉代理其他改动造成的回归？", "control": "抽取现有判为正确、但修改超出gold范围的补丁，对照原测试集与覆盖gold和代理diff并集的扩展测试；原始代码及gold补丁须先通过。", "observable_outcome": "仅代理补丁新增的可重复测试失败，以及失败回退后的SR变化。", "resources": "需任务Docker、保存的补丁及覆盖数据；可沿用每worker 4 vCPU、16GB，无需新模型采样，耗时与费用未知。", "failure_or_stop_condition": "发现一项稳定漏检即可否定该补丁的正确性判定；基线或gold也失败则剔除该测试；零漏检仅支持所查子集。"}

missing_fields：["原始图像及局部公式、双栏排版的视觉核对条件缺失。", "全量评测总token费用、逐任务原始结果及不同结果表的运行批次对应关系未提供。", "前作全文、实际评测实现与反作弊误检/漏检验证数据未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得读任务协议及测试选择。优先问题是代理编辑超出gold覆盖范围时，验收是否漏检功能回归；其次看SR分布而非只看调和均值。

身份版本范围：首物理页题名一致，官方当前附件哈希与39页输入绑定。Pro说明全文1–39页文本已读且图像未见；范围与实际传递一致。当前版不自动认证为camera-ready。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro003_attachment_preview_full.txt；pass_with_version_limit

中心协议与正确性限制：§2.3只提供完整代码库和性能工作负载，允许不同于gold的改动；covering_tests不得给代理。p20按专家PR修改区域选择覆盖测试。这支持调查式任务增量，同时测试通过只约束所选测试，不能保证任意替代改动全语义等价。

核查定位：p004:L0024-L0049, p017:L0044-L0049, p020:L0008-L0025；supported_and_scope_limit_confirmed

SR及成功率不可混用：§2.3将单题SR定义为模型加速除以专家加速，聚合为调和均值并截断极小值；失败或空补丁按原始实现回退。Table6确认0.225、0.157、0.148。p27原PDF Table7确认GPT-5.2在52%任务上通过测试且快于专家、11%测试失败；因此0.148不是14.8%成功率，正文少于四分之一等概括也不能代替该表。

核查定位：p004:L0037-L0052, p005:L0003-L0006, p026:Table6, p027:Table7, local_check/p027.png；numbers_match_metric_interpretation_checked

计算预算与旧子集成本：p5为64vCPU/256GB主机、每worker4vCPU/16GB，3小时、100动作、每步30分钟；OpenHands不设美元上限而SWE-agent限1美元。p27 Table8确认100题早期LITE的0.008/0.007、509.52/98.83美元、9.03/6.29小时；表注明延迟是请求时长总和，不能当全量并行墙钟。

核查定位：p005:L0023-L0055, p026:L0040-L0056, p027:L0034-L0065；cost_scope_and_values_match

本地补充/限定：[]

核查局限：["本地未核算全部498实例、ERC归因公式或全部消融。", "没有运行仓库、Docker、作者脚本或复现实验；硬件和价格均为论文报告。", "前作只从目标论文获知，未独立核读；L2仍是Pro暂定判断。"]


## pro004 · Constructing Industrial-Scale Optimization Modeling Benchmark

论文 OR_0Q7adIsv6p；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_0Q7adIsv6p_79223f28025f", "source_url": "https://api2.openreview.net/pdf?id=0Q7adIsv6p\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_0Q7adIsv6p_79223f28025f：物理页1–44全部提供文本，包括正文、影响说明、参考文献、目录和附录A–J；页标记连续，未发现缺页标记。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；只读到图注及部分提取标签。图18–19的细分占比、图内统计检验结果不可见。", "多栏文字及表1、8、9部分相邻模型行粘连，公式上下标和求和排版有损；未引用不能可靠对齐的单元格。", "未提供原始MPS、发布的数据与代码工件、逐例验证日志或前作全文；未搜索、运行代码或复现实验。"]}

问题：如何构造可核验的工业尺度评测，检验LLM把自然语言需求与外部数据转成数学优化模型及可执行代码的能力？

方法：专家依据MPS命名、系数结构及元数据恢复变量组和循环约束族，设计确定性NL蓝图并可选润色；模型与数值数据分离。随后多模型各最多8次独立回构，未通过者进入专家交互修订，产出NL、数学模型、代码对齐样本。

作者主张：发布223个与MIPLIB原实例一一对应、数学内容保持不变的工业尺度NL-to-Opt样本。

论文证据：245候选中163通过初级回构；82进入人工复查，保留60、剔除22。

模型推断：形成有实质价值的新评测范围，但不等于收集了223个原始真实业务需求。

定位：['TEXT_OR_0Q7adIsv6p_79223f28025f，物理页7，§3.4–3.5。\n', 'TEXT_OR_0Q7adIsv6p_79223f28025f，物理页5，§3.3；物理页29，§D.4。']

作者主张：通过显式循环骨架和结构保持的逆向生成，兼顾描述紧凑性与模型保真。

论文证据：给出恢复、蓝图及验证流程；报告文件压缩中位数6.5倍、最大293277倍。

模型推断：属于构建方法的有效细化，不是首次逆向生成、全自动结构恢复或新求解算法。

定位：['TEXT_OR_0Q7adIsv6p_79223f28025f，物理页4–6，§3；物理页23–24，§C.3。\n']

作者主张：工业结构暴露了旧基准掩盖的性能缺口和不同失败模式。

论文证据：横评显示准确率下降；失败实例中建模、执行、超时分别占48.3%、45.0%、6.7%。

模型推断：支持存在新的困难分布，尚不能证明规模本身是失败的原因。

定位：['TEXT_OR_0Q7adIsv6p_79223f28025f，物理页8–9，§4；物理页35–37，附录G。\n']

key_results：[{"setting": "14系统横评10个旧基准与MIPLIB-NL；后者实际有效分母未澄清。", "baseline": "同批系统在MAMO-E、NLP4LP等既有基准上的结果。", "metric_or_guarantee": "Pass@1/8：至少一次生成模型的求解目标值与参考最优值相对误差不超过10^-6。", "reported_values_and_units": "作者报告MIPLIB-NL平均Pass@1为17.85%、Pass@8为21.87%；MAMO-E与NLP4LP平均Pass@1分别91.78%、90.97%。GPT-5.1在MIPLIB-NL分别为39.05%、42.38%。", "information_and_compute": "温度0.6，最多8次独立生成，Python/Gurobi执行；主评测固定求解时限的具体值、硬件及token预算未报告。", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页8表1、物理页35 §F.3、物理页38表8及结果说明。\n \n"}, {"setting": "Qwen2.5-7B-Instruct的family-held-out LoRA实验：179训练、44测试，作者称家族零重叠。", "baseline": "未微调Base-7B；同一44例上的GPT-5.1作为能力参照。", "metric_or_guarantee": "可执行实例数与正确实例数。", "reported_values_and_units": "Base→LoRA：可执行1/44→14/44，正确0/44→5/44；GPT-5.1分别31/44、20/44。", "information_and_compute": "LoRA超参数、训练算力及该切分对不可行/未决实例的处理未交代。", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页39，附录H、表10。\n"}]

prior_work_candidates：[{"citation_as_printed": "Gleixner, A., Hendel, G., Gamrath, G., Achterberg, T., Bastubbe, M., Berthold, T., Christophel, P., Jarck, K., Koch, T., Linderoth, J., et al. Miplib 2017: data-driven compilation of the 6th mixed-integer programming library. Mathematical Programming Computation, 13(3):443–490, 2021.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "原始MILP实例、MPS代数表达与参考求解结果。", "claimed_difference": "新增自然语言、外部数据和高层结构接口，而非新增原始优化问题。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页2 §1、物理页10参考文献。", "prior_actually_read": false}, {"citation_as_printed": "Lu, H., Xie, Z., Wu, Y., Ren, C., Chen, Y., and Wen, Z. Optmath: A scalable bidirectional data synthesis framework for optimization modeling. In Forty-second International Conference on Machine Learning, 2025.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "明确沿用九类应用分类；表2称其已有MIPLIB逆向生成。", "claimed_difference": "本作强调原实例工业规模与逐例结构保真；具体模板和覆盖差异待核读。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页10参考文献、物理页13表2、物理页29 §D.4。\n", "prior_actually_read": false}, {"citation_as_printed": "Wang, Z., Zhu, Z., Li, Z., Chen, C., Han, Y., Lin, Y., Lin, Z., Gu, A., Hu, X., Sun, R., and Tian, D. Orgeval: Graph-theoretic evaluation of llms in optimization modeling. arXiv preprint arXiv:2510.27610, 2025.", "identifier_if_present": "arXiv:2510.27610", "relation_candidate": "比较基线", "shared_component": "Bench4Opt部分源于MIPLIB，并采用模型–数据分离。", "claimed_difference": "本作主张更大规模、专家结构恢复及更完整的逐例对齐。", "basis": "target_paper_only", "target_locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页11参考文献、物理页13表2、物理页34 §F.1。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是工业结构保留的评测材料及其揭示的能力缺口，而非逆向生成概念首创；足以形成实质性数据贡献，但保真与统计口径有重要疑点。", "central_increment": "前作已有MIPLIB逆向生成和数据分离（本篇转述）；本作新增223个结构化配对样本，并把评测推进到明显更大的求解模型。", "soundness_observation": "目标值相同不能证明可行域等价，§3.5的完全保真强于所述验证。C.1信息论论述也未给出接近Kolmogorov下界的证明。", "significance_observation": "有助于研究结构建模和数据绑定，价值主要来自数据整理与验证投入，不是新优化算法。", "main_open_question": "223个配对是否具有可审计的逐例结构或可行域等价证据，而不仅是单个目标值匹配？"}

limitations：[{"text": "依赖专家并优先选择可恢复结构；缺语义名称、重预求解及验证困难造成排除，且包含合成模型和补拟场景。", "basis": "author_report", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页5 §3.3、物理页29 §D.4、物理页39–40附录I。"}, {"text": "规模口径冲突：A.1/F.1称达到或超过10^7；C.3却报告最大变量283648、最大约束1050112。不把较大规模主张作为已确认事实。", "basis": "model_inference", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页14 §A.1、物理页23 §C.3、物理页34 §F.1。\n \n"}, {"text": "223−8−15应为200，但表1的39.05%不能对应200例单次成功计数。表8 OptMATH-32B在NL4Opt为32.24%，低于表1的79.44%；分母、抽样关系或排印问题未解释，不能擅自修正。", "basis": "model_inference", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页7 §3.4、物理页8表1、物理页38表8。\n \n"}, {"text": "不同数据集提示模板不完全一致；MIPLIB模板给出绝对路径示例又禁止绝对路径，可能混入执行错误，缺少等接口对照。", "basis": "model_inference", "locator": "TEXT_OR_0Q7adIsv6p_79223f28025f，物理页41–44附录J，尤其物理页43。\n"}]

minimal_check：{"question": "目标等值通过的样本是否确实保持了原模型语义？", "control": "从初级通过和人工修订组各抽1个可解实例，独立盲审NL与数据，以原MPS及发布参考模型为对照。", "observable_outcome": "建立变量映射，比较变量域、目标和约束族；对结构差异寻找可行域不等价的反例。", "resources": "需原MPS、发布工件、验证日志、独立OR审阅者及Gurobi环境；工时和内存需求未知。", "failure_or_stop_condition": "发现遗漏规则但目标值仍匹配，则不支持验证充分性；工件不足时停止。两个样本通过不代表全库保证。"}

missing_fields：["主评测实例清单、有效分母及Pass@1/8抽样关系", "逐例等价审计记录、专家工时与构建成本", "求解器版本、主评测具体时限、硬件和token预算", "LoRA配置、训练成本及不可行/未决实例处理", "细分错误原始计数和显著性检验明细", "MIPLIB 2017与OptMath参考条目的独立标识未提供"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得读结构恢复与模型—数据接口；优先要求逐例等价证据、主评测分母及Pass@1/8采样关系，再用其结果比较建模能力。

身份和范围：完整题名匹配，官方当前附件哈希绑定44页文本；Pro声明全部页文本已读并保留图表排版局限，与实际输入一致。没有把当前附件称为已确认camera-ready。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro004_attachment_preview_full.txt；pass_with_version_limit

中心增量与验证强度：p6流程先结合MPS代数行及外部证据恢复结构，初级验证要求多个LLM之一最多8次中有一次目标值或求解状态匹配；失败再做专家结构审查，明确不是穷尽核验。p7有163+60=223个保留、22丢弃。支持新自然语言接口与验证工程的价值，不能把单目标值一致当成可行域等价证书，也不能说作者完全没有结构核对。

核查定位：p006:Figure4 caption, p006:L0029-L0063, p007:L0006-L0020；protocol_supported_exact_equivalence_unverified

主指标及数值：F.3定义生成模型目标值相对误差≤1e-6且N次中至少一次成功，温度0.6，求解时限未给具体值。原PDF Table1确认总体17.85%、GPT-5.1为39.05%；Table8总体21.87%、GPT为42.38%。两张表都为作者报告；目标值达标不是完整模型语义等价。

核查定位：p035:L0013-L0023, p008:Table1, p038:Table8, local_check/p008.png, local_check/p038.png；values_match_metric_limit_retained

分母和表间疑点：p7明确223中8不可行+15open排除主评测，字面推出200；39.05%不对应200个实例单次二元成功的整数计数，故需澄清实际分母或重复估计。原PDF也确认OptMath-32B在NL4Opt的Table1为79.44%、Table8为32.24%。若是相同嵌套样本的Pass@N则反常；若独立试验或其他口径仍需说明，不能擅自改数。

核查定位：p007:L0022-L0034, p008:Table1, p038:Table8；published_discrepancies_confirmed_cause_unknown

家族留出小模型结果：p39 Table10为179训练/44测试、作者声明家族无重叠；可执行1/44→14/44、正确0/44→5/44，GPT-5.1为31/44与20/44。Pro记录一致；该子集与主评测不可行/open的处理关系尚未说明。

核查定位：p039:L0007-L0025；counts_match_split_scope_unresolved

本地补充/限定：[{"kind": "qualification", "detail": "保真质疑应同时保留作者的前期结构检查和后期专家审查；未获得逐例证书，不能缩写成整个流程只匹配一个目标值。"}]

核查局限：["未取得或运行MPS、求解代码和逐例验证日志；未证明任何两个优化模型完全等价。", "未复核规模10^7与附录最大变量/约束数的另一项Pro疑点，本地不把它列为已确认事实。", "未重算全部系统均值、错误类型或来源论文；L2为未校准Pro判断，不代表数值全部可靠。"]


## pro005 · Security–Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense

论文 OR_vTJmIhNvC3；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_vTJmIhNvC3_3db86fced549", "source_url": "https://api2.openreview.net/pdf?id=vTJmIhNvC3\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_vTJmIhNvC3_3db86fced549：物理页1–34全部所供文本，包括正文§1–7、影响声明、参考文献及附录A–F；页标连续，未发现整页缺失。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–4仅有图题及抽取文字，未核读图形、曲线或颜色编码。", "双栏文字局部串行，公式排版及部分字符失真；主要公式和表格可据文本辨读，但数值或口径冲突无法对照原始页面消解。", "未提供前作全文、其他版本、逐例预测与评测实现；未搜索、运行代码或复现实验。"]}

问题：模型处理不可信文本时，能否既不执行其中的指令，又保留任务要求处理的内容？

方法：为可信指令与受污染数据预制EXECUTED、PROCESSED、IGNORED三种可区分参考输出。签名答案检测执行；实体集合、计数及参考嵌入相似度判定数据处理。Security=1−Executed，Fidelity=1−Ignored；严格安全处理另定义为Pr[PROCESSED∧¬EXECUTED]，不能把四个报告率当互斥分类。进一步用处理优于忽略、忽略优于执行的偏好信号调优SECALIGN。

作者主张：SECFID使未执行背后的忠实处理与内容抑制分别可测。

论文证据：构造1168条核心样例：提取310、计数307、翻译278、编辑273；另有252条工具使用场景。正文给出同一任务下不可辨识与可辨识探针的对照。

模型推断：增量在评测可辨识性，而不只是扩大攻击集合；Fidelity这一具体代理指标仍有缺陷。

定位：['TEXT_OR_vTJmIhNvC3_3db86fced549：p3，§3.1；p21，表7–8；p27，§D']

作者主张：相似安全性可通过修复或抑制两种不同方式取得。

论文证据：在Llama 3.1 8B原先执行的574条样例上，SECALIGN修复54.0%、抑制36.6%；DefensiveTokens分别为26.8%、60.3%，残余执行分别为1.2%、3.0%。

模型推断：同基座、同样例配对支持行为差异，但不是对模型内部机制的因果识别，也不是不可突破的安全—保真下界。

定位：['TEXT_OR_vTJmIhNvC3_3db86fced549：p6，§4.2；p31，表24。\n']

作者主张：Fidelity-aware DPO可减少过度过滤，同时保留低执行率，并迁移到未训练的编辑任务。

论文证据：按结构锚点划分训练与测试；141条核心留出及273条全留出编辑任务均报告处理率提高。

模型推断：是既有DPO与安全检查点上的有价值局部改进；关键新增是偏好信号，而非优化算法。

定位：['TEXT_OR_vTJmIhNvC3_3db86fced549：p29、32–33，§E，表27–28']

key_results：[{"setting": "1168条核心样例，48个模型／防御／推理配置；以下均为作者报告", "baseline": "未防御Llama 3.3 70B", "metric_or_guarantee": "Security／Fidelity，均为百分比", "reported_values_and_units": "基座47.8／96.5；SECALIGN-70B为99.3／71.0；SECALIGN-8B为99.3／73.9。表22另报95% Wilson区间。", "information_and_compute": "默认temperature=0；闭源API、开源本地推理。硬件、总耗时及推理token预算未报告。", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p24，§B.1；p30，表22。\n"}, {"setting": "DPO：核心留出N=141；编辑任务迁移N=273", "baseline": "SECALIGN-8B", "metric_or_guarantee": "Executed／Ignored／Processed，均为百分比", "reported_values_and_units": "核心：0.0／17.7／73.8→0.0／9.2／83.0；编辑：1.1／53.5／43.2→0.7／16.8／80.6。", "information_and_compute": "754条训练样例生成2894偏好对；RS-LoRA秩96，β=0.1，学习率2×10^-6，序列上限3072，有效批量16，bfloat16，1轮／181步；GPU和时间未报告。", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p32，§E.3；p33，表27。\n \n"}, {"setting": "252条InjecAgent改造场景，直接危害与窃取数据各126条", "baseline": "未防御Llama 3.3 70B", "metric_or_guarantee": "Security／Fidelity，均为百分比", "reported_values_and_units": "基座72.2／44.0，SECALIGN-70B为98.0／31.7；Gemini 3 Flash为100.0／72.6。", "information_and_compute": "探针位于首次良性工具观测；两阶段窃取链使用预计算攻击者工具响应，避免外部副作用。", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p8，表3；p27，§D。\n"}, {"setting": "固定模糊输入及后验α∈(0,1)，正安全与保真成本", "baseline": "PROCESS与FILTER两种动作", "metric_or_guarantee": "命题F.1的部署成本依赖", "reported_values_and_units": "L(PROCESS)=αCsec，L(FILTER)=(1−α)Cfid；α>Cfid/(Cfid+Csec)时过滤更优。不存在对所有正成本对都Bayes最优的部署无关确定性策略。", "information_and_compute": "直接比较预设损失；未估计实际部署成本，不覆盖保留内容但剥离权限等动作。", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p34，命题F.1、§F.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Zverev, E., Abdelnabi, S., Tabesh, S., Fritz, M., and Lampert, C. H. Can LLMs separate instructions from data? and what do we even mean by that? In ICLR, 2025a.", "identifier_if_present": null, "relation_candidate": "方法继承", "shared_component": "§3.3明示采用相似的指令、数据、探针实例组织。", "claimed_difference": "新增处理与忽略必须产生不同答案的构造要求；前作覆盖程度未核读。", "basis": "target_paper_only", "target_locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p3，§3.3；p13，参考文献", "prior_actually_read": false}, {"citation_as_printed": "Chen, S., Zharmagambetov, A., Wagner, D., and Guo, C. Meta secalign: A secure foundation llm against prompt injection attacks. arXiv preprint arXiv:2507.02735, 2025b.", "identifier_if_present": "arXiv:2507.02735", "relation_candidate": "组件复用", "shared_component": "8B／70B防御检查点及安全偏好训练思路；8B也是新增调优起点。", "claimed_difference": "不仅奖励不执行，还奖励处理优于忽略。", "basis": "target_paper_only", "target_locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p6–7，§4.3；p10，参考文献；p24，§B.1", "prior_actually_read": false}, {"citation_as_printed": "Zhan, Q., Liang, Z., Ying, Z., and Kang, D. InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents. Findings of the Association for Computational Linguistics: ACL 2024, pp. 10471–10506, Bangkok, Thailand, August 2024. Association for Computational Linguistics.", "identifier_if_present": "doi:10.18653/v1/2024.findings-acl.624", "relation_candidate": "组件复用", "shared_component": "252个工具使用场景。", "claimed_difference": "改造为可从最终答案或工具参数辨识保留／过滤探针的任务。", "basis": "target_paper_only", "target_locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p12–13，参考文献；p27，§D", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可识别的评测设计及修复／抑制诊断，属于实质性知识增量；不是新DPO算法，也未证明普遍不可兼得定理。", "central_increment": "前作已研究指令—数据分离及安全调优（本篇转述），本作在可疑文本本身须被处理的条件下新增可观测分解；配对诊断和留出迁移提供支持，尚待排除判分偏差。", "soundness_observation": "二元成本推导成立，但汇总存在内部疑点：表15翻译Processed=64.2%、Exec.+proc.=12.7%，按同分母定义safe processing应为51.5%，却报53.0%；差异超过舍入，需原始标签核验。\n \n", "significance_observation": "对翻译、编辑和工具观测处理有诊断价值；多任务构造与防御适配体现工程工作量，但未量化真实部署损失。", "main_open_question": "统一并独立验证联合标签后，改用严格安全处理指标，防御比较与DPO迁移结论是否仍成立？"}

limitations：[{"text": "作者明确只测固定探针；二元成本模型不覆盖完整防御动作空间，不能外推为所有架构的能力上限。", "basis": "author_report", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p9，Limitations；p34，§F.1"}, {"text": "Fidelity=1−Ignored并非正确保留率：被判OTHER且未执行的全拒绝输出可同时取得满Security与Fidelity。因此两轴前沿必须结合安全处理率和失败率解释。", "basis": "model_inference", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p4，§3.4–3.5"}, {"text": "翻译人工样本仅99条；89.9%准确率来自同样本阈值扫描择优，并非固定0.5阈值的独立验证。编辑缺少对应人工校验；表7将编辑计入程序检查，与§3.4及E.4的嵌入判分描述需核对。", "basis": "model_inference", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p21，表7；p24，§B.2；p32，§E.4。\n"}, {"text": "跨防御平均值覆盖不同基座，不能当统一条件排名；DPO只有一个起点与一个留出任务，尚不足证明跨模型普适改善。", "basis": "model_inference", "locator": "TEXT_OR_vTJmIhNvC3_3db86fced549：p6，表1说明；p33，§E.5"}]

minimal_check：{"question": "编辑迁移的处理率提升是否也是人工确认的安全处理提升？", "control": "对同273题的SECALIGN-8B与DPO输出隐去模型名，独立标注执行与内容处理，并与固定评测器配对比较。", "observable_outcome": "重建联合标签，检查safe processing=Processed−Executed∩Processed，并报告两模型人工安全处理率之差及配对区间。", "resources": "需两模型原始输出、参考答案、评测器及双人盲标；不需重训，标注工时未知。", "failure_or_stop_condition": "缺少原始输出则无法开展；若联合率无法重建或人工安全处理增益消失，不确认对应迁移结论。"}

missing_fields：["版本出版角色未核实；图像及前作全文未提供。", "逐例预测、联合标签和评测实现未提供，表格一致性问题未解决。", "训练／评测硬件、耗时、API费用、推理token预算及多次训练方差未报告。", "固定阈值独立验证、编辑人工判分验证及偏好组成消融未报告。", "Zverev et al. (2025a)独立检索标识未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得继续读安全与忠实性联合标签定义；采用数值前优先核查逐例联合标签及Table15等表的分母和恒等关系。

题名与材料范围：首物理页题名与旧候选、当前冻结名单一致；本次只取官方API当前附件。Pro声明读完1–34页文本且未见图像，与传递清单一致；旧候选本次首次全文初评占本阶段名额。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro005_attachment_preview_full.txt；pass_with_version_limit

中心增量：§3.1以相同提取任务对比处理/忽略输出是否可区分；ProbeB使忽略、作为数据处理和执行有不同输出。支持行为可辨识的测量设计，不能从输出分类直接识别模型内部机制。

核查定位：p003:L0008-L0017, p003:L0042-L0061；supported_with_mechanistic_limit

Pro提出的表15数值疑点：原PDF p25 C.1明确所有率按48配置的model–example cells计，Processed包括同时执行者，Safe proc为处理且不执行；Table15翻译行64.2−12.7=51.5，却报53.0。差1.5个百分点不能由一位小数舍入解释。编辑行也有45.4−20.9=24.5而报27.4，差2.9点。本地确认出版页面本身如此，尚不能确定是列定义、实现或抄表错误。

核查定位：p025:L0007-L0010, p025:Table15, local_check/p025.png；source_internal_inconsistency_confirmed_unresolved

DPO与留出范围：Table27确认核心N141处理率73.8→83.0且执行0→0；编辑N273处理43.2→80.6、执行1.1→0.7。正文明确无编辑偏好训练、仅一个初始化和构造，支持该设定内增益，不等于跨部署普遍安全。处理率不是严格安全处理率；不能忽略多标签口径。

核查定位：p033:Table27, p033:L0052-L0059；reported_values_match_joint_label_caveat_retained

理论条件：F.1固定同一模糊输入、后验alpha∈(0,1)、二元PROCESS/FILTER和正成本，损失alpha*Csec与(1−alpha)*Cfid的比较得到成本依赖阈值。F.1后明确剥离权限等中间动作可缓解权衡，所以它不是现实全部防御的不可兼得定理。

核查定位：p034:L0003-L0036, p034:L0039-L0046；binary_algebra_and_scope_checked

本地补充/限定：[{"kind": "corroborating_local_extension", "detail": "在Pro指出翻译行冲突之外，本地原PDF核查也发现编辑行存在相同集合恒等式冲突；保留原Pro不改写。"}]

核查局限：["未取得逐例标签或作者实现，不能判定冲突根因或重算防御排名。", "未重算全部48配置、Wilson区间、条件N574的配对结果。", "无前作全文核读、人工审计、攻击复现或额外模型调用；L2暂定不代表数值已完全可靠。"]


## pro006 · Measuring Agents in Production

论文 OR_mWxEAgz3xu；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d", "source_url": "https://api2.openreview.net/pdf?id=mWxEAgz3xu\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：物理页1—47全部提供文本，包括正文§1—8、参考文献、附录A—G、完整问卷及流程图提取文字。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["物理页标记连续，未见缺页；未提供PDF图像。双栏正文及部分图表文字串行。", "图16—17、26、28—29的图形结构不可核验；其他图仅能读取明确提取的标签和正文报告值，置信区间端点不可读取。", "未提供原始逐项问卷、访谈记录、生产日志或前作全文；未搜索、复现或执行作者代码。"]}

问题：真实部署的agents为何被采用，采用哪些模型、架构和评测方法，主要工程障碍是什么？

方法：2025年4—11月开展20项访谈并收集306份问卷，主分析筛出86份生产/试点记录。访谈由至少3人独立编码；47题问卷分支呈现，领域标签经LOTUS归并与人工裁定，平均κ=0.636；分类比例采用1000次bootstrap，形成17维画像。

作者主张：首次大规模系统研究生产agents，提供17个设计维度的一手技术证据。

论文证据：20项案例、306份问卷及86份部署子集；附录披露问卷、访谈提纲、汇总统计和全样本比较，而非逐记录原始数据。

模型推断：增量是跨组织经验知识与可沿用的调查工具，不是新agent算法；历史首次尚未核验。

定位：['TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p2，贡献列表；p24—45，附录C—G。\n']

作者主张：生产可靠性主要通过简单、可控的系统设计实现，而非模型级或算法级进步。

论文证据：记录结构化工作流、提示工程、人工审核及只读/沙盒限制；访谈解释其维护与风险动机，但没有可靠性干预实验。

模型推断：支持实践模式及从业者解释，不能证明这些措施优于后训练，或是部署成功的因果原因。

定位：['TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p8—9，§7—8。\n']

key_results：[{"setting": "20项访谈案例：14项正式生产、6项试点。", "baseline": null, "metric_or_guarantee": "工程实践采用比例；非性能保证。", "reported_values_and_units": "14/20（70%）不做权重后训练；16/20（80%）采用结构化工作流；15/20（75%）没有正式benchmark集。", "information_and_compute": "每次访谈30—90分钟；没有统一训练或推理成本测量。", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p5—7，§5.2、5.4、6.1；p23，§C.2.1。\n"}, {"setting": "部署子集自主步数问题，有效N=60。", "baseline": null, "metric_or_guarantee": "要求用户输入前的自主步数分布。", "reported_values_and_units": "作者报告约68%至多10步、47%少于5步；正文部分位置写成“<10”，但QN10选项是“Ten or fewer”，应保留≤10口径。", "information_and_compute": "自报而非轨迹实测；问卷中的user也可能是软件，不能全部等同人工介入。", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p6—7，§5.4/图7a；p35，QN8—QN10。\n"}, {"setting": "部署子集验证方法问题QO1，有效N=31，多选。", "baseline": null, "metric_or_guarantee": "验证方法的采用率。", "reported_values_and_units": "人工类23/31（74.2%）；模型类16/31（51.6%）。模型类包含LLM-as-a-Judge等多个子类，不能据此确定其单独采用率。", "information_and_compute": "多选不测量各方法的主次、审核工作量或准确率。", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p8，图8；p37，QO1。\n"}, {"setting": "部署子集延迟容忍度问题，有效N=53。", "baseline": null, "metric_or_guarantee": "可接受的端到端延迟，非实测延迟。", "reported_values_and_units": "作者报告66%可容忍分钟及以上或未设限，其中17%未设置明确上限。", "information_and_compute": "包含无上限回答；未提供对应token、GPU或API预算。", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p5，§4.4/图4。\n"}, {"setting": "部署子集开发优先级问题QO2，有效N=29。", "baseline": "其他开发优先级类别，非受控性能基线。", "metric_or_guarantee": "排名第一的回答比例。", "reported_values_and_units": "Core Technical Performance获11/29（37.9%）首位；该类同时包含可靠性、扩展性、延迟及资源限制，不能拆出可靠性的独立排名。", "information_and_compute": "测量主观开发优先级，并未测量长期失败概率。", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p19，图11/表2；p38，QO2。\n"}]

prior_work_candidates：[{"citation_as_printed": "LangChain. State of AI agents, 2024. Survey of 1,300+ professionals on agent adoption, use cases, controls, and challenges.", "identifier_if_present": "https://www.langchain.com/stateofaiagents\n", "relation_candidate": "背景引用", "shared_component": "从业者调查、采用动机与挑战。", "claimed_difference": "本作强调生产系统及工程级技术细节，而非单纯增加调查规模。", "basis": "target_paper_only", "target_locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p2，§2；p11，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Challapally, A., Pease, C., Raskar, R., and Chari, P. The GenAI divide: State of AI in business 2025. Technical report, MLQ.ai and Project NANDA, July 2025.", "identifier_if_present": "https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf\n", "relation_candidate": "背景引用", "shared_component": "组织引入AI的实证调查。", "claimed_difference": "按本篇转述，前作偏管理者视角的经济可行性，本作偏直接开发者的技术决策。", "basis": "target_paper_only", "target_locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p2，§2；p10，参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心价值是跨组织一手生产经验，形成实质性描述知识；没有提出路线级框架或新可靠性保证。", "central_increment": "前作已调查采用与商业价值（本篇转述）；本作在2025年生产/试点样本中新增工程实践画像，证据来自访谈与问卷；尚待排除样本选择及编码口径造成的表象。", "soundness_observation": "问卷及编码流程披露有助于检查，但采用率、主要依赖程度和因果效果不可互换；部分统计存在内部不一致。", "significance_observation": "可为评测、有限自主和模型迁移研究提供需求证据。工作难点主要是部署团队准入、保密协调与材料整理，而非训练计算。", "main_open_question": "对系统去重、分开正式生产与试点并核对各题分母后，有限自主这一中心画像是否仍稳健？"}

limitations：[{"text": "作者承认团队地域偏美洲、专业网络及参与意愿带来选择偏差，且跨月采集存在时间偏差；不应解释成全球固定普及率。", "basis": "author_report", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p4，§3.3。\n"}, {"text": "附加题回答数远小于86；受访者可为不同系统重复提交，系统/组织去重及两类样本重合未充分披露。bootstrap不消除自选、缺答和幸存者偏差。", "basis": "model_inference", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p3，§3.2；p31，§G.1；p36，SEP。\n"}, {"text": "访谈85%自建框架与问卷60.7%使用外部框架方向不同；不能仅据两个迁移案例推断所有系统成熟后都会转向自建。", "basis": "model_inference", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p16—17，§B.2.1。\n"}, {"text": "文本中图6标N=53，但25人对应44.6%的分母不一致；§C.1写生产/试点占82%，图14b却列50+36人、N=111。缺原始数据，无法区分统计、选项处理或排版问题。", "basis": "model_inference", "locator": "TEXT_OR_mWxEAgz3xu_df6e0a6cbf0d：p6，图6；p22，图14b/§C.1。\n"}]

minimal_check：{"question": "至多10步的多数性是否在正式生产且服务人类用户的子集中保持？", "control": "统一QN10编码并去重，对比原生产/试点合并组与QN5正式生产、QN8人类用户子集。", "observable_outcome": "报告各组有效N、≤10步比例及缺答数量；核对原报告约68%。", "resources": "脱敏QN5/QN8/QN10、系统与组织去重标识及统计环境；数据访问成本、人时未知。", "failure_or_stop_condition": "原比例不能重建或严格子集不再占多数，则该概括不能通过此检查；缺原始数据则停止。通过也不证明因果或全球代表性。"}

missing_fields：["原始逐题回答、访谈编码记录、去重及样本重合信息未提供。", "图像、置信区间端点及统计不一致的解释缺失。", "逐系统训练、推理及人力审核成本未报告。", "key_results中null基线表示没有统一受控性能对照；本篇没有新模型训练实验。", "前作全文及目标附件最终出版版本身份未核验。"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

对当前贡献研究，一轮已足够将其用作2025年部署实践背景和评测需求线索；不继续投入时间把自选样本推广为行业比例，除非能获得可去重的原始记录。

身份版本及全文范围：首物理页题名匹配；本次首次全文初评的官方当前附件为47页，Pro声明正文、参考文献和附录全部已读文本、图像未提供，和传递清单一致。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro006_attachment_preview_full.txt；pass_with_version_limit

一手经验增量与样本范围：§3为2025年20访谈和306有效问卷，访谈专业网络起步加滚雪球，问卷由会议、MOOC和专业网络分发；86数据点筛入生产/试点。全部问题可选，动态分支，至少3人独立编码访谈后讨论。C.2.1明确案例14生产+6试点，组织多系统时优选不同用例，不能把20+86直接当106独立正式生产系统或全球概率样本。

核查定位：p003:L0016-L0067, p023:L0018-L0035；descriptive_evidence_and_selection_limits_confirmed

自主步数：Figure7a标N60，前两档28和13，即41/60约68.3%至多10步；QN10选项Ten or fewer、QN8/9明确user可能是软件。Pro保留≤10并不等同全部人类介入，修正了正文Finding9的<10/human概括。

核查定位：p007:L0003-L0016, p035:QN8-QN10；threshold_and_denominator_checked

验证方法采用率：原PDF Figure8为N31多选：人工23/31=74.2%，Model Based16/31=51.6%，规则12/31=38.7%。QO1把多种模型/估计方法放在同类，不能把51.6%拆成LLM-as-a-judge单项采用率，也不测方法主次。正文规则42%与图38.7%不一致，本地引用图中明确值。

核查定位：p008:Figure8, p037:QO1, local_check/p008.png；reported_counts_match_category_limit_and_text_discrepancy_recorded

本地补充/限定：[{"kind": "additional_local_observation", "detail": "Figure8规则方法为38.7%(12/31)，同页正文写42%；本地不以正文42%作为核验值。"}]

核查局限：["未重新编码访谈、核对系统/组织去重或复算全部47问分布。", "Pro提到的图6及图14其他分母疑点未在本地进一步核验，不能列为本地已确认结果。", "图表置信区间和从业者自报不消除自选、未答与时间偏差；无人工审计或因果干预。"]


## pro007 · Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models

论文 OR_phHnze3Nfm；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_phHnze3Nfm_cfaf982d6ccb：物理页1–21全部可见文本，包括正文1–9、致谢及参考文献10–11、附录A–E所在12–21；页标连续，未见缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–14原图均未提供；仅阅读图题及抽取标签，未核验曲线、分布形状或奖励景观。", "双栏文字交错，公式及图内标签有排版损失；公式主要机制和表1–12数值可辨，但未作PDF图像复核。"]}

问题：数学推理PRM在静态扰动、主动攻击和RL优化下，能否持续区分高分文本与真正正确的解答？

方法：三层诊断：八类静态扰动测ΔR；优化连续嵌入或熵正则Gumbel-Softmax离散token以抬高错误轨迹奖励；GRPO训练后比较奖励、真值准确率及保语义改写效果。Skywork取末步奖励并后缀注入，Qwen取最小步奖励并在解答前插入。

作者主张：提出三层诊断框架和PRM-BiasBench，揭示流畅性与逻辑检测脱节。

论文证据：八类扰动实验及双LLM校验；保语义编辑的判断一致率93.5–95.7%。GenPRM另测每类1000例，保语义编辑的判定翻转率20.5–22.8%。

模型推断：提供有价值的压力测试协议，但不能由有限模型直接断言所有PRM只是流畅性检测器。

定位：['TEXT_OR_phHnze3Nfm_cfaf982d6ccb p3–4/§4；p15–16/表3–5']

作者主张：短token触发器可跨轨迹抬高奖励，优化位置附近存在宽高分区域。

论文证据：Skywork-1.5B呈强攻击及跨集迁移；7B效果较弱。表2报告其100-token盆地指标约为随机位置的2.2倍。

模型推断：主要是既有攻击范式的PRM适配；漏洞见证成立不等于获得最坏情况保证。

定位：['TEXT_OR_phHnze3Nfm_cfaf982d6ccb p5–7/§5及表2；p18–20/附录D']

作者主张：普通RL能自行发现PRM漏洞，Skywork约43%的奖励增益来自风格利用，Qwen则坍缩为空洞输出。

论文证据：奖励与准确率分离、改写降分，以及扩展网格中正确性奖励基线明显更好。

模型推断：静态风格不变性不保证优化对齐，是中心知识增量；Qwen案例也暴露任务完成度奖励缺失。

定位：['TEXT_OR_phHnze3Nfm_cfaf982d6ccb p8–9/§6；p20–21/附录E']

key_results：[{"setting": "PRM-BiasBench；Qwen和Skywork均为7B PRM。", "baseline": "同一原始轨迹未施加扰动。", "metric_or_guarantee": "ΔR均值±标准差，无量纲奖励分。", "reported_values_and_units": "改写：Qwen −0.01±0.03、Skywork −0.02±0.05；问题打乱：分别−0.32±0.35、−0.20±0.25。", "information_and_compute": "LLM生成及语义检查；标量PRM各扰动的确切样本数未报告。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p15/表3。\n"}, {"setting": "8条AIME24错误轨迹优化100个离散token，迁移至8条AIME25轨迹。", "baseline": "k=0，无攻击token。", "metric_or_guarantee": "训练最佳奖励及迁移平均奖励，不是准确率。", "reported_values_and_units": "Skywork-1.5B训练0.237→0.954、迁移0.305→0.924；Skywork-7B迁移0.320→0.377；Qwen-7B迁移0.287→0.245。", "information_and_compute": "白盒Adam优化1000次，学习率0.1，种子42；攻击硬件未报告。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p7/表2；p16/表6。\n"}, {"setting": "30条AIME24轨迹优化，100-token触发器迁移至全部AIME25、MATH-500和MATH-Hard。", "baseline": "相同轨迹不加触发器。", "metric_or_guarantee": "平均奖励变化ΔR。", "reported_values_and_units": "按上述数据集顺序，Skywork-1.5B为+0.429、+0.166、+0.280；Qwen-7B为+0.076、−0.012、+0.050，均按表中报告值保留。", "information_and_compute": "迁移不重优化；MATH-500为500题，MATH-Hard为1324题；未明确这些迁移轨迹是否全部错误。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p19–20/表7、9、10。\n \n"}, {"setting": "Qwen2.5-1.5B-Instruct在AIME24训练并监测该集准确率。", "baseline": "训练初始策略。", "metric_or_guarantee": "PRM奖励与真值准确率变化。", "reported_values_and_units": "Skywork-1.5B奖励约0.1→大于0.8，准确率峰值3–4%；Qwen-7B PRM奖励在前100步内升至1.0，准确率降至0%。", "information_and_compute": "GRPO共1000步，每题8次采样，KL=0，输出上限2048 token；每跑8×H100 80GB，耗时未报告。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p8/§6.2；p21/表12。\n \n"}, {"setting": "Skywork-1.5B对AIME25上的base、GRPO及改写后GRPO轨迹评分。", "baseline": "base策略及未经改写的GRPO输出。", "metric_or_guarantee": "平均奖励与改写消除的奖励增益比例。", "reported_values_and_units": "base=0.246、GRPO=0.641、改写后=0.472；下降0.169，占总增益0.395的约43%，不是准确率提升比例。", "information_and_compute": "依赖保语义改写；干预样本量、分步边界保持情况未充分报告。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p8/§6.3。\n"}, {"setting": "扩展GRPO：7B策略/AIME、1.5B策略/MATH-500，各1000步。", "baseline": "正确性奖励基线分别达到63%、81%。", "metric_or_guarantee": "mean@8准确率；独立测试划分未明确。", "reported_values_and_units": "使用Skywork-1.5B/7B轨迹奖励时，AIME准确率20%/23%，MATH-500为62%/65%；AIME步级奖励均为17%。六组最终PRM奖励0.82–0.94。", "information_and_compute": "基线额外使用答案真值；均KL=0、每题8次采样，硬件见表12。扩展表仅写AIME，未注明年份。", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p20/表11；p21/表12。\n"}]

prior_work_candidates：[{"citation_as_printed": "Xu, Y., Dong, H., Wang, L., Xiong, C., and Li, J. Reward models identify consistency, not causality. arXiv preprint arXiv:2502.14619, 2025.", "identifier_if_present": "arXiv:2502.14619", "relation_candidate": "背景引用", "shared_component": "奖励模型依赖浅层一致性线索的诊断。", "claimed_difference": "本篇称新增主动攻击、受控干预及闭环RL。", "basis": "target_paper_only", "target_locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p2/§2.2；p10/参考文献", "prior_actually_read": false}, {"citation_as_printed": "Zheng, C., Zhang, Z., Zhang, B., Lin, R., Lu, K., Yu, B., Liu, D., Zhou, J., and Lin, J. Processbench: Identifying process errors in mathematical reasoning. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1009–1024, 2025.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "数学推理轨迹及过程错误评测数据。", "claimed_difference": "扩展八类受控扰动，评估优化压力下的可利用性。", "basis": "target_paper_only", "target_locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p3/§4；p11/参考文献", "prior_actually_read": false}, {"citation_as_printed": "Gao, L., Schulman, J., and Hilton, J. Scaling laws for reward model overoptimization. In International Conference on Machine Learning, pp. 10835–10866. PMLR, 2023.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "代理奖励提高但真实目标恶化的过优化现象。", "claimed_difference": "将分析转到PRM，并用改写干预刻画风格相关增益。", "basis": "target_paper_only", "target_locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p2–3/§2.4；p10/参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心价值是多层干预形成的可利用性与失效机制证据，而非新攻击算法；超过单一性能改进，但不足以认定路线级框架。", "central_increment": "前作已讨论浅层线索及奖励过优化（本篇转述）；本作在数学PRM、纯PRM奖励且KL=0条件下，展示静态风格稳定不保证优化后稳定；支持来自改写干预及正确性奖励对照，尚待排除评分结构混杂。", "soundness_observation": "跨集与真值奖励对照增强可信度，但数表与部分概括存在张力。Qwen空洞输出得高分主要暴露完成度缺口，不能直接否定其局部检错能力。", "significance_observation": "对将PRM作为唯一RL目标及部署前压力测试具有实际价值；不能推广为PRM所有训练和推理用途均无效。", "main_open_question": "固定数学内容、步骤边界和终止规则后，改写是否仍消除约43%的GRPO奖励增益？"}

limitations：[{"text": "Skywork和Qwen训练目标及末步/最小步聚合不同，奖励绝对值不可直接横比。", "basis": "author_report", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p3/§3；p5–6/§5.3"}, {"text": "正文强调Skywork更能惩罚问题错配，但表3平均降分反而Qwen更大；峰值与均值不同，不能直接判定数据错误，须原图和逐样本数据核对。D.1称Qwen抵抗攻击，表7却报告迁移+0.076，亦不支持绝对化表述。", "basis": "model_inference", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p4/§4.2；p15/表3；p18–19/D.1及表7"}, {"text": "43%是改写奖励差的比例，尚未隔离步骤边界等评分结构变化；剩余奖励增益也不能直接认定为推理能力提升。", "basis": "model_inference", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p8/§6.3"}, {"text": "全部RL关闭KL且集中于数学和1.5B/7B策略；未提供多种子误差，不能外推至带完成约束或混合奖励的训练。特定攻击失败也不是鲁棒性保证。", "basis": "model_inference", "locator": "TEXT_OR_phHnze3Nfm_cfaf982d6ccb p5–7/§5；p20–21/表11–12"}]

minimal_check：{"question": "43%的纯风格归因能否通过结构保持的配对改写检验？", "control": "同题base和GRPO轨迹均改写；冻结数学式、答案、错误内容、分步及终止标记，并盲审语义等价。", "observable_outcome": "比较两类轨迹改写前后的配对奖励降幅及差分置信区间，检验优化轨迹是否仍额外明显降分。", "resources": "既有AIME25轨迹、Skywork-1.5B及改写和盲审资源；仅需推理，具体硬件与工时未定。", "failure_or_stop_condition": "匹配后差异消失或主要由内容/步骤变化解释，则不支持原43%纯风格归因；无法取得原轨迹则停止。"}

missing_fields：["原图、原始逐样本数据及前作全文未提供；部分前作无显式标识符。", "标量PRM扰动样本数、改写干预配对规模、扩展迁移轨迹正确性筛选未充分报告。", "扩展RL训练/独立评测划分及多种子不确定性未明确。", "白盒攻击硬件、各实验GPU小时、盆地半径及积分细节未报告；版本最终出版身份未核验。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

三层压力测试对奖励模型采用决策有直接价值，值得继续读干预设计与聚合规则；重点核查等步骤边界/完成度约束下43%结果是否保持。

题名版本范围：首物理页题名匹配，官方当前附件与21页连续文本绑定；Pro声明全部文本已读、图像未见，与输入一致。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro007_attachment_preview_full.txt；pass_with_version_limit

核心诊断与评分结构：§3明确静态扰动、白盒优化、闭环RL三层；Skywork轨迹奖励取末步、Qwen取最小步，不能把绝对分数横比。自然轨迹上保语义改写稳定与RL优化轨迹改写降分并不逻辑矛盾，优化后分布不同。

核查定位：p003:L0014-L0039, p003:L0041-L0065, p008:L0039-L0057；mechanism_and_noncomparability_confirmed

43%的确切含义：原PDF Figure8及§6.3给base0.246、GRPO0.641、改写后0.472；本地复算(0.641−0.472)/(0.641−0.246)=0.42785，即约43%。它是奖励增益中被该干预移除的比例，不是准确率或普遍风格投机比例；纯风格归因依赖数学内容、分步边界等评分结构保持。

核查定位：p008:Figure8, p008:L0016-L0036, local_check/p008.png；numbers_and_arithmetic_match_causal_assumption_explicit

决定性训练条件：Table12明确KL=0无参考模型、每题8rollouts、1000步、响应上限2048token、每跑8×H10080GB。p8 Figure7与正文显示奖励上升而准确率低，Qwen空洞输出的高奖励不能直接否定局部错误检测全部用途；结论限该纯PRM训练设置。

核查定位：p021:Table12, p008:Figure7, p008:L0031-L0042；conditions_checked_no_general_robustness_claim

本地补充/限定：[]

核查局限：["未运行攻击、RL、作者代码或独立校验改写语义；没有检查所有表格与多种子稳定性。", "本地没有证明漏洞普遍存在，也没有将某个攻击失败视为鲁棒性保证。", "前作仍仅为目标论文提供的候选线索，未核读。"]


## pro008 · Reasoning Models are Test Exploiters: Rethinking Multiple Choice

论文 OR_IvoZENu6qG；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1", "source_url": "https://api2.openreview.net/pdf?id=IvoZENu6qG\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_IvoZENu6qG_7e3ecee77eb1：物理页1–9，正文§1–5。", "TEXT_OR_IvoZENu6qG_7e3ecee77eb1：物理页10–12，致谢续文、影响声明及参考文献。", "TEXT_OR_IvoZENu6qG_7e3ecee77eb1：物理页13–22，附录A–F，包括提示词、模型表、判分与过滤代码文本、行为探测说明及图表提取文本。22页标记连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–13仅有题注及部分图中文字，不能复核柱高、曲线、热图或图5–6中的代码画面。", "物理页5公式分式、括号及部分双栏顺序有损；四选一猜测基线采用物理页6明确写出的公式。", "附录A提示框与标签对应关系可疑，不能确认属于原文错误还是提取错位。未提供前作、其他版本或实际运行日志。"]}

问题：选择题高分能否代表无选项问题求解能力，模型选中的错误选项能否诊断其推理错误？

方法：改变同题中选项与CoT的出现时序，比较仅选项、仅问题、问题加选项及两阶段格式。四选一用0.75×A_FT+0.25校正猜测，并以仅选项表现和两格式取并集的super-scoring控制部分选择误差；另对生成Python进行200组输入扰动，以输出哈希比较错误行为。

作者主张：推理模型特别擅长利用选项，通常的MCQA不能可靠代理其自由作答能力。

论文证据：正文称覆盖15基准、27模型；校正猜测和部分映射误差后仍报告选项增益，Qwen3关闭第二阶段thinking的对照仍显示较大QMC残差。

模型推断：中心增量是推理模型条件下解耦失效的系统证据，而非首次发现选择题偏差。

定位：['TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页6–7，§4–4.1。\n \n']

作者主张：NOTA削弱部分捷径，而更难、更多的干扰项不能可靠消除选项利用。

论文证据：报告NOTA干预及MMLU/MMLU-Pro归一化仅选项比较；NOTA也明显改变模型的选择偏好。

模型推断：提供选项设计的适用边界，不构成通用修复方案。

定位：['TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页8，§4.2。\n']

作者主张：可执行CoT能揭示错误选项诊断遗漏的共同及家族性错误。

论文证据：程序行为相似度与MCQA错误选择相似度没有显著线性相关，并报告家族内错误聚类。

模型推断：增加了外显程序行为的诊断分辨率，但不证明内部推理过程相同。

定位：['TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页5、8–9，§3.2、§4.3。\n']

key_results：[{"setting": "基准套件的CoT-extractable子集，比较QMC-CoT与Q-CoT。", "baseline": "同模型Q-CoT；另列四选一猜测增强基线Q-CoT+k。", "metric_or_guarantee": "pass@1准确率差", "reported_values_and_units": "正文报告约50B以上模型的原始差为30–40个百分点；这不是扣除猜测后的exploitation数值。", "information_and_compute": "作者报告总计4.92 GPU年、OpenAI API 2146.51美元；开源使用1–4张L40。通常每基准开源/闭源评测5000/1000题，STEER-ME为5800/1160题；各配置最终有效样本数和token预算未齐报。", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页2、6，§1、§3.4、§4。\n \n \n"}, {"setting": "仅提供选项、含NOTA的MCNA-CoT诊断。", "baseline": "非推理模型；文中该比较的NOTA真实正确率为25%。", "metric_or_guarantee": "NOTA选择率", "reported_values_and_units": "推理模型55.82%，非推理模型30.05%；这些是选择率，不是准确率或exploitation降幅。", "information_and_compute": "复用NOTA随机替换干预；各组聚合权重与不确定性区间未充分说明。", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页8，§4.2。\n"}, {"setting": "CoT-executable基准上的模型对错误相似度分析。", "baseline": "扣除随机一致基线的MCQA错误选择相似度。", "metric_or_guarantee": "行为哈希相似度与MCQA相似度的Pearson相关", "reported_values_and_units": "r=0.090，p=0.513；54.5%的模型对在行为哈希下相似度更高。不能将不显著相关解释为已证明相互独立。", "information_and_compute": "每个程序200组确定性扰动，浮点输出舍入至6位小数后哈希；无需为每个扰动重新调用模型。", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页5、9，§3.2、§4.3。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Raman, N. K., Lundy, T., Amouyal, S. J., Levine, Y., Leyton-Brown, K., and Tennenholtz, M. STEER: Assessing the Economic Rationality of Large Language Models. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024.", "identifier_if_present": "nU1mtFDtMX", "relation_candidate": "方法继承", "shared_component": "Q-CoT-MC-1T，即hidden两阶段协议；NOTA干预。", "claimed_difference": "研究第二阶段不能直接输出1T的推理模型及其残留选项利用。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页4，§3.1；参考文献物理页11–12。\n", "prior_actually_read": false}, {"citation_as_printed": "Balepur, N., Ravichander, A., and Rudinger, R. Artifacts or abduction: How do LLMs answer multiple-choice questions without the question? In Ku, L.-W., Martins, A., and Srikumar, V. (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 10308–10330, Bangkok, Thailand, August 2024. Association for Computational Linguistics.", "identifier_if_present": "10.18653/v1/2024.acl-long.555", "relation_candidate": "方法继承", "shared_component": "隐藏题干、仅提供选项以测量可利用信号。", "claimed_difference": "本篇称前作限制1T，本作重点测量CoT推理选项后的表现。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页4，§3.1；参考文献物理页10。\n \n", "prior_actually_read": false}, {"citation_as_printed": "Raman, N., Lundy, T., Amin, T., Perla, J., and Leyton-Brown, K. STEER-ME: Assessing the Microeconomic Reasoning of Large Language Models, 2025.", "identifier_if_present": "arXiv:2502.13119", "relation_candidate": "组件复用", "shared_component": "STEER-ME基准、程序生成选项；已有plug-and-chug现象线索。", "claimed_difference": "扩展到跨基准、模型类型和CoT时序的系统比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页2–3，§1–2；参考文献物理页11。\n \n \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是关于推理模型评测失真的实质性实证知识，而非新模型或路线；其普遍性及因果解释仍受协议与报告缺口限制。", "central_increment": "前作已有选项探测、hidden/NOTA和plug-and-chug观察（本篇转述）；本作新增推理模型对选项及CoT时序的系统依赖证据，支持来自多格式残差比较，尚待排除评分与预算混杂。", "soundness_observation": "猜测、最近选项和映射控制有价值；但格式收益不自动等于虚假推理，正文与附录的实现、模型清单和协议描述亦需审计。", "significance_observation": "直接关系到用MCQA推断开放作答能力及据错项诊断模型错误的可靠性。", "main_open_question": "采用独立盲评和等额二次推理预算后，推理模型特有的选项增益是否仍然保留？"}

limitations：[{"text": "作者承认转换会遗漏可用题目，且真实任务本来要求候选选择时，选项感知推理可能合理；不能外推为所有MCQA无效。", "basis": "author_report", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页2–3，§1–2.1。\n \n"}, {"text": "1T在两种Answer前缀间按正确token概率择优，属于带金标签信息的诊断基线。附录C.1形参与内部变量不一致，且按小数位而非正文所称有效数字舍入；无法据此确认实际判分实现。", "basis": "model_inference", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页6，§3.4；物理页15，附录C.1。\n \n"}, {"text": "200个一致输出不足以证明函数或内部推理等价；统一在[-1000,1000]扰动可能越出具体题目的有效定义域。", "basis": "model_inference", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页5，§3.2；物理页16–17，附录D。\n \n"}, {"text": "正文模型数量、表5与图4模型阵容不一致；表7还列出正文称无法运行1T的推理模型。附录A的Prompt1标签也与Q-CoT定义不符，需核对原件和运行配置，不能自行调和。", "basis": "model_inference", "locator": "TEXT_OR_IvoZENu6qG_7e3ecee77eb1，物理页5–6表4及§3.4、物理页8图4提取标签、物理页13–15附录A–B、物理页21表7。\n \n"}]

minimal_check：{"question": "第二阶段选项收益是否只是多一次推理或判分差异？", "control": "固定同一Qwen3-8B的首轮Q-CoT轨迹，同题比较无选项复查与加入选项的第二轮推理，给予相同token上限；预先固定不查金标签的解析器，并独立盲评自由答案。", "observable_outcome": "报告配对准确率差、置信区间及因答案解析而改变判定的比例。", "resources": "一个预注册题目子集、模型权重、首轮轨迹、推理GPU与盲评人力；具体显存、GPU时和费用未知。", "failure_or_stop_condition": "若等预算且修正判分后增益消失或反转，则第二阶段选项捷径的解释明显削弱；若两组解析失败率失衡，先停止机制归因。"}

missing_fields：["原图及仅在图中呈现的精确结果。", "统一模型清单、逐配置有效样本数、输出token预算和完整运行配置。", "行为探测失败、异常及有效样本比例；家族聚类显著性检验的完整细节。", "前作全文、其他版本、实际评测代码和运行日志；本轮未外部核读或复现。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得继续读评分和等预算控制；关键是独立盲评、匹配二次推理预算后，剩余选项增益是否仍可与合法候选验证区分。

身份版本范围：首物理页题名匹配；官方当前附件的22页文本与Pro题名、paper/review ID及哈希一致。Pro说明只读文本，图像未提供，范围匹配。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro008_attachment_preview_full.txt；pass_with_material_limits

中心协议与适用题集：Tables1–4分别规定只有选项、题干+选项、NOTA及一/两阶段作答；第二阶段可再推理时不等同于机械映射。§2.1过滤依赖选项或不可判分题，原数据部分只保留62.81%。所以结论限CoT-extractable等子集，不能外推为所有选择题都不能测能力。

核查定位：p003:L0003-L0025, p003:§2.1, p004:Tables1-3, p005:Table4；design_and_selection_scope_checked

原始差、校正与NOTA数值：p6明确约50B以上模型QMC-CoT相对Q-CoT高30–40个百分点，这一数值是原始差；四选一猜测增强为0.75*Q-CoT+0.25，不能把原始差直接称纯选项利用量。p8报告NOTA选择率55.82%与30.05%，真实正确率25%，这些也不是准确率。

核查定位：p006:L0041-L0059, p008:L0031-L0039；reported_values_and_metric_distinctions_match

行为诊断的保证边界：p5为生成程序在确定性扰动下探测200组、5秒沙箱；p9明确r=0.090、p=0.513和54.5%模型对比较。有限输入上输出一致不能证明函数等价或内部推理相同；不显著线性相关也不是独立性的证明。

核查定位：p005:L0022-L0043, p009:L0018-L0036；diagnostic_numbers_match_equivalence_limit_retained

本地补充/限定：[]

核查局限：["未执行附录判分函数、生成程序或探测；未逐项确认模型清单/提示框的其他Pro疑点。", "未从图中重估各模型效应量或重新检验相关显著性；未核读前作。", "本地只核查上述来源，L2仍是模型暂定贡献判断。"]


## pro009 · CUARewardBench: A Benchmark for Evaluating Reward Models for Computer-Using Agents

论文 OR_Xj7V0wKlE5；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7", "source_url": "https://api2.openreview.net/pdf?id=Xj7V0wKlE5\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：物理页1–20全部所供文本，包括正文、参考文献及附录A.1–A.10。清单和连续页标均为20页；消息另提22页，不据此认定本版缺两页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–2的图形不可见，图3–6仅提示词提取文本可读。双栏文字有交错，表3公式排版有损。", "未提供前作全文、原始预测或实验日志；主附表部分数值冲突，无法判断是原文还是提取问题。"]}

问题：如何可靠评测基于截图的CUA奖励模型对任务成功及关键动作正确性的判断？

方法：筛选OSWorld-verified轨迹，经独立标注、交叉复核和共识处理形成结果与关键步骤标签；评测12模型和3模板的适用组合。UPE组合不同模型/提示，只有全部判断同为正或同为负时才输出，否则弃权。

作者主张：首个同时系统评测CUA结果奖励与过程奖励的综合基准。

论文证据：覆盖10类软件、7种策略模型；272条轨迹含139成功、133失败，346个关键步骤含182好、164坏。

模型推断：提供有价值的桌面多粒度测试集，但并非对全部步骤作密集标注。

定位：['TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p4–5 §2.2–2.3、表1–2。\n']

作者主张：UPE提高正负奖励信号的可靠性，优于单模型及多数投票。

论文证据：表4–5展示严格一致和异质提示组合的收益，同时报告召回率、特异度下降。

模型推断：属于带拒判的可靠性改进；同二成员多数票对照中precision不变，不能称所有指标同时提升。

定位：['TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p7–9 §3.4、表4–6。\n']

作者主张：视觉推理是CUA奖励评估的核心瓶颈。

论文证据：GLM-4.5V-106B配sewsm的53个ORM错例中，推理错误19例（35.8%），视觉理解错误16例（30.2%）。

模型推断：支持该模型错例的诊断，不足以证明专门训练损伤推理能力的因果机制。

定位：['TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p19 A.8、表9。\n']

key_results：[{"setting": "272条轨迹的ORM；Qwen3VL-32B-T/sewsm与Qwen3VL-235B-T/zerogui组合。", "baseline": "相同成员的多数投票；两票分歧判负。", "metric_or_guarantee": "Precision / NPV / Recall / Specificity", "reported_values_and_units": "作者报告UPE为88.0/95.3/79.1/75.9%；多数票为88.0/80.3/79.1/88.7%。", "information_and_compute": "输入指令及截图轨迹，使用两路模型配置；实际token、耗时和费用未报告。", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p7 表4。\n"}, {"setting": "346个关键步骤的PRM；Qwen3VL-32B-T/sewsm与Qwen3VL-235B-T/opencua reflector组合。", "baseline": "相同成员的多数投票。", "metric_or_guarantee": "Precision / NPV / Recall / Specificity", "reported_values_and_units": "作者报告UPE为83.1/86.2/53.8/45.7%；多数票为83.1/63.2/53.8/87.8%。", "information_and_compute": "sewsm看完整轨迹；reflector只看截至当前动作的信息，并含代码及坐标标记。计算成本未报告。", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p8 表5；p7 §3.3；p16 图6提示词。\n"}, {"setting": "Impress单域SFT；在OSWorld原始47个Impress任务上各评测10次。", "baseline": "未经过该轮SFT的Qwen3VL-7B-Thinking。", "metric_or_guarantee": "任务成功率", "reported_values_and_units": "作者报告34.68%→46.10%，增加11.42个百分点，约33%相对提升。", "information_and_compute": "Qwen3VL-32B-Thinking为437任务各生成10条轨迹并判奖；4370条中判成功2243条，再按任务难度筛至1532条训练7B模型。硬件及训练预算未报告；此实验使用单奖励模型而非UPE。", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p17–18 A.6。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Lu, X. H., Kazemnejad, A., Meade, N., Patel, A., Shin, D., Zambrano, A., Stanczak, K., Shaw, P., Pal, C. J., and Reddy, S. AgentRewardBench: Evaluating automatic evaluations of web agent trajectories. arXiv preprint arXiv:2504.08942, 2025.", "identifier_if_present": "arXiv:2504.08942", "relation_candidate": "背景引用", "shared_component": "智能体轨迹自动评估器的基准评测。", "claimed_difference": "本篇称其聚焦Web，而本作覆盖桌面操作及ORM/PRM。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p10 References；p11 A.1。", "prior_actually_read": false}, {"citation_as_printed": "Yang, C., Su, S., Liu, S., Dong, X., Yu, Y., Su, W., Wang, X., Liu, Z., Zhu, J., Li, H., et al. ZeroGUI: Automating online GUI learning at zero human cost. arXiv preprint arXiv:2505.23762, 2025a.", "identifier_if_present": "arXiv:2505.23762", "relation_candidate": "组件复用", "shared_component": "ORM提示词及多数投票参照。", "claimed_difference": "UPE要求正负判断均全票一致，分歧时弃权，并混合提示。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p5 §3.1；p7–8 §3.4；p10 References。", "prior_actually_read": false}, {"citation_as_printed": "Sun, Z., Liu, Z., Zang, Y., Cao, Y., Dong, X., Wu, T., Lin, D., and Wang, J. SEAgent: Self-evolving computer use agent with autonomous learning from experience. arXiv preprint arXiv:2508.04700, 2025.", "identifier_if_present": "arXiv:2508.04700", "relation_candidate": "组件复用", "shared_component": "SE-WSM提示词及专门训练的奖励模型基线。", "claimed_difference": "本作在多软件、多策略轨迹上评测其泛化，并将提示纳入UPE。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p5–6 §3.1–3.2；p10 References；p12 A.3。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "中心是有明确价值的桌面多粒度评测扩展，附带可靠性优先的拒判策略；尚未隔离覆盖率选择效应，也未建立新的因果机制结论。", "central_increment": "前作已有Web轨迹奖励评测（本篇转述）；本作新增经人工复核的桌面结果与关键动作评测，表2、4–5支持其诊断价值。", "soundness_observation": "主要证据为作者报告的离线分类实验；输入条件、拒判指标及主附表一致性仍需核对。", "significance_observation": "对训练数据筛选有实用意义；单域SFT增益不能证明基准排序能预测下游收益，更不能验证UPE或PRM的RL收益。", "main_open_question": "相同覆盖率和推理预算下，UPE是否仍优于单模型拒判？"}

limitations：[{"text": "作者未记录初始标注分歧率；截图也无法验证文件大小等不可见系统状态。", "basis": "author_report", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p12 A.2；p20 A.8。\n \n"}, {"text": "成功失败平衡、难度筛选和争议剔除改变了样本分布；precision与NPV不能直接外推到真实部署。", "basis": "model_inference", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p4–5 §2.2–2.3；p11–12 A.2。"}, {"text": "PRM模板比较同时改变了未来信息、动作代码和坐标提示，并非仅措辞对照；SE-WSM首错输出如何映射任意关键步骤标签，以及弃权如何计入R/S/OA分母，未充分说明。", "basis": "model_inference", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p5 表3；p7 §3.3；p8 表5–6；p14、16提示词。"}, {"text": "主附表冲突未校正：Qwen3VL-235B-T/sewsm的ORM NPV在表4/7为78.6%/73.6%；GPT-5/sewsm的PRM R在表5/8为64.8%/89.0%；GUI-OWL-32B/sewsm的PRM R为89.0%/86.8%。", "basis": "model_inference", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p7–8 表4–5；p17–18 表7–8。\n \n \n \n"}, {"text": "SFT缺少未过滤及等量随机过滤对照，无法分离过滤、额外训练和难度筛选的贡献；未报告任务去重、置信区间及端到端成本。", "basis": "model_inference", "locator": "TEXT_OR_Xj7V0wKlE5_a9cacb9edba7：p17–19 A.6–A.7。"}]

minimal_check：{"question": "UPE的ORM优势是否超出拒判带来的样本选择效应？", "control": "在未用于配置选择的任务上，对比UPE与等推理预算单模型置信拒判；仅用开发集调阈值，匹配覆盖率。", "observable_outcome": "比较precision、NPV、保留率及每条可用标签成本，并按任务重采样估计不确定性。", "resources": "需完整截图、标签及模型预测/置信分数；缺失时需重新推理，硬件和费用未知。", "failure_or_stop_condition": "若同覆盖、同预算下无稳定优势，则不能支持UPE具有超出拒判筛选的独立方法收益。"}

missing_fields：["训练和推理硬件、token、耗时、费用及完整采样配置", "初始标注一致性及标注工时", "SE-WSM步骤标签映射、无效输出处理、弃权指标分母", "主附表冲突的可核验正确值", "独立开发测试划分、SFT任务去重和统计不确定性"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

当前贡献比较已有足够信息把它定位为GUI奖励评测和拒判策略的局部价值；暂不继续投入，除非后续研究需要GUI奖励，届时先做等覆盖率、等信息和等计算对照。

身份范围及实际输入异常：题名、ID、哈希匹配官方当前20页附件，附件预览完整匹配。实际发送说明夹有另一草稿的22页字样，真实消息已保存在raw/pro009_ui.txt及回执。Pro明确依据清单和连续页标读完20页，不据错误包装文字虚构缺页；本地核查支持此范围，未重发。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro009_attachment_preview_full.txt, raw/pro009_ui.txt；full_material_correct_wrapper_anomaly_preserved

贡献边界及样本构成：§2.3明确只标注关键好坏动作而非全部步骤，并大体排除冗余动作；计139成功+133失败轨迹、182好+164坏动作。支持桌面多粒度评测扩展，不是密集全轨迹标注或部署样本分布。

核查定位：p005:L0003-L0045；scope_and_counts_match

一致投票与关键指标：原PDF Table6显示两票分歧：多数票判负而严格一致弃权。Table5同二成员PRM组合的P/R均83.1/53.8，NPV63.2→86.2而S87.8→45.7；Table4的ORM组合P/R也不变，NPV80.3→95.3、S88.7→75.9。Pro数值正确，不能说全部指标同时提升；可靠性收益伴随覆盖损失。

核查定位：p007:Table4, p008:Tables5-6, local_check/p008.png；values_and_abstention_tradeoff_checked

未来信息混杂：§3.3明确OpenCUA reflector只看当前步骤以前，SE-WSM看完整轨迹。它们比较不仅改提示措辞，也改变可用未来信息；离线回看评价不能直接等价为在线过程奖励。

核查定位：p007:L0070-L0084；information_scope_difference_confirmed

本地补充/限定：[]

核查局限：["未本地核查单域SFT全部数据或主附表的其他冲突，保留为Pro提出的未决项。", "未复查专家分歧、长轨迹泛化或真实部署基率；没有新增模型测试或作者代码执行。", "Pro仅收到文本，关键表5/6由本地另行视觉核查。"]


## pro010 · NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents

论文 OR_wqQam1muOQ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_wqQam1muOQ_a43b7b406703", "source_url": "https://api2.openreview.net/pdf?id=wqQam1muOQ\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_wqQam1muOQ_a43b7b406703：物理页1–20全部提供文本，包括正文、参考文献及附录A–Q。题名与清单一致；清单与连续页标均为20页，并非用户重复语句中的22页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未发现文本缺页；未查看原PDF或图1–8的图像。图4各轮数预算下的精确曲线值不可核验。", "部分双栏文字交错，图中文字位置关系丢失；仅采用正文明确报告或表格可明确对齐的数值。"]}

问题：智能体能否从单份需求说明和空工作区出发，自主生成可安装、通过上游测试的完整Python库？

方法：人工反向工程需求文档，经AST清单核对、专家审查及试生成修订；原库须在专用Docker环境通过全部测试。智能体生成期间不直接获得源码或测试，完成后执行上游pytest，宏平均各仓库测试通过率。注意文档仍明确提供完整目录、API签名与依赖，并非没有结构先验。

作者主张：建立从自然语言、空工作区生成完整仓库的严格可验证长程评测。

论文证据：104个Python库、9类任务，平均输入约18,800 tokens；提供标注、环境校验和多模型基线。

模型推断：实质增量是评测资源与输入条件组合，不是新生成算法；“无骨架”应限定为没有实体代码骨架，不能扩大为没有架构信息。

定位：['TEXT_OR_wqQam1muOQ_a43b7b406703：物理页3–5，§3；物理页13，附录C.3。\n']

作者主张：长程失败涉及过早结束、被动等待、规划不足及跨文件不一致，增加上下文或交互次数不足以解决。

论文证据：报告终止行为分类，并提供移除task tracker、开放测试和限制交互轮数的实验。

模型推断：支持规划工具与测试反馈的局部作用；不足以证明内部推理导致过度自信，或大上下文是成功的必要条件。

定位：['TEXT_OR_wqQam1muOQ_a43b7b406703：物理页7–9，§4.3–4.4；物理页17–20，附录M–Q。']

key_results：[{"setting": "104任务，单次生成；Overall为每仓库测试通过率的宏平均，Pass@1为全部测试通过的仓库数。", "baseline": "表2各模型与框架配置。", "metric_or_guarantee": "平均测试通过率；完整通过仓库数。", "reported_values_and_units": "作者报告：Sonnet-4.5/Claude Code为40.2%、3/104；Sonnet-4.5/OpenHands为39.9%、3/104；Sonnet-4/OpenHands为37.0%、5/104；GPT-5/OpenHands为21.7%、1/104。最高平均分配置不是完整通过数最多的配置。", "information_and_compute": "主实验不限制工具使用和交互轮数；平均需求约18,800 tokens；总token、耗时及费用未报告。", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页5–6，§4.1、表2。\n"}, {"setting": "Claude-Sonnet-4.5/Claude Code，开发阶段是否开放全部上游测试。", "baseline": "仅需求文档。", "metric_or_guarantee": "平均测试通过率；完整通过仓库数。", "reported_values_and_units": "40.2%→59.4%，增加19.2个百分点；3/104→18/104。", "information_and_compute": "干预同时增加规格信息与可执行反馈；重复次数、额外运行成本未报告，不是严格性能上界。", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页19，附录O、表10。\n"}, {"setting": "OpenHands-CodeAct中禁用task tracker，其余设置按作者说明保持不变。", "baseline": "启用task tracker。", "metric_or_guarantee": "平均测试通过率。", "reported_values_and_units": "GPT-5：21.7%→18.7%；Claude-Sonnet-4：37.0%→34.0%；均下降3.0个百分点。", "information_and_compute": "仅两个模型；对应重复试验及置信区间未报告。", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页15–17，附录J、表7。\n"}]

prior_work_candidates：[{"citation_as_printed": "Zhao, W., Jiang, N., Lee, C., Chiu, J. T., Cardie, C., Gall´e, M., and Rush, A. M. Commit0: Library generation from scratch. In The Thirteenth International Conference on Learning Representations, 2024.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "从零生成软件库的评测问题。", "claimed_difference": "本篇称Commit0提供工程结构和函数签名；本作不提供实体骨架，但仍以文字提供结构及签名。不能据此认定方法继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页3，§2.1；物理页11，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., et al. Paperbench: Evaluating ai’s ability to replicate ai research. In Forty-second International Conference on Machine Learning, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "文档驱动的长程仓库构建评测。", "claimed_difference": "按本篇转述，PaperBench针对论文复现并常用LLM评判；本作针对Python库行为重建，以原项目测试执行评分。", "basis": "target_paper_only", "target_locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页3，§2.1；物理页10，参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心价值在可执行的仓库生成评测资源及能力缺口刻画；具有实质评测增量，但不足以认定路线首创或新的长程推理机制。", "central_increment": "前作已做从零库生成和文档驱动复现（本篇转述）；本作在结构化说明、空工作区、隐藏测试条件下新增104库评测；支持证据为任务构建及表2、7、10，尚待排除文档不足和测试特异约束。", "soundness_observation": "原库全测试校验与环境隔离合理，但AST清单覆盖不等于行为语义完备；汇总数据及机制归因存在待核问题。未复现实验。", "significance_observation": "适合评估需求到多文件实现的持续执行能力；不能直接外推至无架构提示、交互式需求发现或一般软件开发。", "main_open_question": "低通过率中，有多少真正来自长程协调不足，而非说明遗漏或未明示的上游测试约束？"}

limitations：[{"text": "作者承认导入、依赖及测试接口对齐失败；同时放宽文档、许可证等非功能构建要求，因此分数不等于原始发布流程完全合规。", "basis": "author_report", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页4，Environment Building；物理页20，附录Q。"}, {"text": "存在汇总一致性疑点：按表4的26/46/32任务数加权表2中Sonnet-4.5/OpenHands的55.3/43.0/21.4，得到约39.43%，而非所列39.9%；差异超出一位小数舍入范围，需原始结果核对。", "basis": "model_inference", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页6、12，表2、4。\n \n"}, {"text": "Early Termination按不足100轮调用finish定义，未要求实际测试失败；Non-Finish混合等待用户和系统超时，不能分别直接等同于过度自信与缺乏自主性。", "basis": "model_inference", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页17–18，附录M。\n \n"}, {"text": "三次复跑仅覆盖三个开源模型，报告标准差3.5–4.2个百分点；跨框架小差异和规划消融缺少对应重复统计。上下文容量与模型能力混杂，不能由跨模型相关性推出因果。", "basis": "model_inference", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页15，表6；物理页19–20，附录P。\n"}, {"text": "仓库公开且工具包含网络访问；未见训练污染或目标源码下载审计，不能确认“初始不提供源码”等于全程未接触源码。", "basis": "model_inference", "locator": "TEXT_OR_wqQam1muOQ_a43b7b406703：物理页12，附录B、C.1。"}]

minimal_check：{"question": "文档缺项是否解释部分所谓长程失败？", "control": "选3个失败任务，独立核对需求与失败测试；同模型、框架和预算下，对比原文档与仅补齐确认缺项的文档，不公开测试。", "observable_outcome": "每条件重复3次，比较配对通过率及被修复失败项；结论限定于抽查任务。", "resources": "任务文档、测试、Docker镜像、语义审查人员及18次生成调用；实际token、工时和费用未知。", "failure_or_stop_condition": "无法确认文档缺项则停止该干预；若补齐后主要失败消失，则削弱这些任务上的长程能力归因，不能推广为全基准结论。"}

missing_fields：["原始逐任务结果及可执行任务文件未随附件提供。", "精确模型/API与框架版本、采样和推理配置、超时上限及有效上下文管理细节不完整。", "总token、硬件、耗时、API费用及标注工时未报告。", "前作全文、独立文献标识、污染审计及行为分类一致性统计未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得比较完整库生成协议，但用低成功率归因长程协调前，先核验文档行为完备性、测试隐藏约束和逐任务汇总。

身份、范围与发送说明异常：题名和绑定ID/哈希符合官方当前20页附件，全部输入预览核验通过。真实消息含重复的22页及20页包装语，已保留原件；Pro明确以清单及页标为准读完20页，未虚构额外页。附件及学术v2正文未改变，无第二轮调用。

核查定位：first_page_text.txt, text_delivery_manifest.json, browser/pro010_attachment_preview_full.txt, raw/pro010_ui.txt；complete_material_correct_wrapper_conflict_documented

空工作区不等于无架构信息：§4.1从只有任务说明的空目录开始；C.3要求说明提供整体设计、主要组件、完整目录结构、依赖及全部功能节点名称签名位置。支持没有实体代码骨架的评测，不能称完全无架构先验。

核查定位：p005:L0019-L0033, p013:L0030-L0064；input_scope_checked

两种指标与主结果：p5定义每仓库测试通过率后宏平均；原PDF Table2确认Sonnet4.5/ClaudeCode40.2%且3/104全过，Sonnet4为37.0%但5/104全过。最高均分与最多完整通过并非同一配置。

核查定位：p005:L0030-L0033, p006:Table2, local_check/p006.png；numbers_and_metric_distinction_match

汇总一致性：原PDF Table4分桶任务数26/46/32，Table2 Sonnet4.5/OpenHands分数55.3/43.0/21.4。按论文宏平均定义复算39.428846%，而Overall印39.9%，差约0.471点，超过一位小数舍入可解释范围。原因可能为分桶、聚合或数据版本，缺逐任务记录不能选定根因，也不能替作者改表。

核查定位：p006:Table2, p012:Table4, local_check/p006.png, local_check/p012.png, local_check/weighted_mean_recalculation.json；printed_aggregate_inconsistency_confirmed

公开测试干预：Table10报告文档到文档+测试40.2→59.4%、全过3→18；这同时增加行为规格信息与可执行反馈，不能单独证明只缺长程推理，亦不是严格能力上界。

核查定位：p019:L0032-L0044；values_match_intervention_limit_retained

本地补充/限定：[]

核查局限：["未检查全部104份说明、仓库、测试或污染来源，未运行作者代码。", "未复核其他消融全部数字、行为终止分类或上下文容量的因果作用。", "本地确认的是所印数据及定义之间的差异，未得到原始任务结果；L2仍为Pro暂定判断。"]

