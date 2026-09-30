# 单轮全文初评与有界本地核对 21–30

模型判断与本地更正分列；非人工审计、完整证明认证或实验复现。只读了本篇绑定版本，候选前作未穷尽核读；local_check相对定位对应本地留存证据。

## pro021 · Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards

论文 OR_LwB2EacVT6；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_LwB2EacVT6_73b4c6ec5981", "source_url": "https://api2.openreview.net/pdf?id=LwB2EacVT6\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "558f7e380bff95b401062b2fa6fee743a6a5c449800c638f3d10f484fa30bc8a", "source_pdf_sha256": "73b4c6ec5981a6ca64bed643abcabce65f86c911a018dd6c4bb746e50503e606"}], "read_ranges": ["TEXT_OR_LwB2EacVT6_73b4c6ec5981：物理页1—41全部所供文本；包括正文与Impact Statement（1—9）、参考文献（9—11）、附录A—O（12—41）。题名匹配，页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1—8仅能读取图注和残留标签，不能核读曲线、误差带或热图数值。", "双栏混排、根号、上下标及矩阵布局存在提取失真；表1—4主要文字可辨，但未经原版图像核对。", "附件版本角色未核实，不认定为最终出版版；未提供前作全文、完整实现或实验日志。附N伪代码和附O题目示例仅作为研究材料阅读，未执行。"]}

问题：验证器存在假阳性与假阴性时，RLVR何时只是学习变慢，何时会反向强化错误？

方法：将每个prompt独立抽象为正确/错误模式上的softmax bandit，以总体均值和方差代替组统计，对logit更新作小步长展开。概率漂移包含两次softmax Jacobian作用，再分解为错误总质量p及正确、错误类内组成y、z。

作者主张：J=TPR−FPR的符号决定学习方向；J>0时噪声改变收敛时钟而不改变正确方向。

论文证据：定理4.2及F.1给出错误质量在J>0时趋零、J<0时趋一、J=0时一阶漂移为零。推论4.3区分δFN>0时O(t⁻¹)与δFN=0时O(t⁻²)。

模型推断：价值在限定更新模型中的动力学保证，不在重新命名噪声相关性。

定位：['TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页4，Theorem 4.2、Corollary 4.3；物理页12，Appendix A。\n', 'TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页20，Theorem F.1、式(49)。']

作者主张：正确率提高可以同时伴随正确模式多样性坍缩。

论文证据：式(7a,b)及附录J/K表明：J>0时正确类内集中，通常由初始最大模式获胜；错误类内在原支撑上趋于均匀。碰撞项调节错误质量下降速度。

模型推断：比只追踪准确率增加了模式演化机制；但不能把普通logit梯度流直接等同于对原奖励作自然梯度更新。

定位：['TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页5，式(7)。\n', 'TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页29脚注1、32 Theorem J.11、37 Theorem K.6。\n']

key_results：[{"setting": "Qwen2.5-3B在过滤后的OpenR1 Python任务上进行GRPO训练，奖励由单测结果经合成噪声翻转获得。", "baseline": "同一初始模型及J=1的无噪声训练。", "metric_or_guarantee": "作者报告验证Pass@1；使用未注入噪声的单测，实际解码温度为0。", "reported_values_and_units": "表1的J/(FPR,δFN)→Pass@1：−0.1/(0.60,0.50)→0.16%；0/(0.50,0.50)→13.4%；0.3/(0,0.70)→16.0%；0.3/(0.70,0)→14.6%；0.7/(0.20,0.10)→18.6%；1/(0,0)→20.8%。无噪声配置较初始模型提升8.0个百分点。均为作者报告。", "information_and_compute": "训练10239、验证594个prompt；G=8，5个种子，2个epoch/1410步，全局batch=16；Adam学习率10⁻⁶，KL系数0。训练温度1，prompt/response各限4000 tokens。硬件及耗时未报告。", "locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页6—8 §6、Table 1；物理页39 Appendix M、Table 4。\n \n"}, {"setting": "DeepSeek-LLM-7B-chat在GSM8K上采用PPO，训练两轮并注入验证噪声。", "baseline": "文本报告初始化准确率约24%。", "metric_or_guarantee": "验证准确率；检验是否出现同方向的J符号转变。", "reported_values_and_units": "§6.2文字报告：正J约63—64%，近中性约21—22%，负J约1—3%。这些近似数值来自正文，不是从不可见曲线读取。", "information_and_compute": "包含token级信用分配；独立数据划分、种子数、PPO超参数和计算资源未单列。", "locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页7 §6.2、物理页9 Figure 6。\n"}]

prior_work_candidates：[{"citation_as_printed": "Cai, X.-Q., Wang, W., Liu, F., Liu, T., Niu, G., and Sugiyama, M. Reinforcement learning with verifiable yet noisy rewards under imperfect verifiers. arXiv preprint arXiv:2510.00915, 2025.", "identifier_if_present": "arXiv:2510.00915", "relation_candidate": "背景引用", "shared_component": "不完美验证器下的噪声RLVR问题。", "claimed_difference": "本篇强调J相线及全模式动力学，但未具体排除该作已覆盖相关结论。", "basis": "target_paper_only", "target_locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页2 §2、物理页10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Mroueh, Y. Reinforcement learning with verifiable rewards: Grpo’s effective loss, dynamics, and success amplification. arXiv preprint arXiv:2503.06639, 2025.", "identifier_if_present": "arXiv:2503.06639", "relation_candidate": "背景引用", "shared_component": "GRPO动力学及KL正则化；本篇仅在相关扩展处引用。", "claimed_difference": "未提供逐项定理比较，不能据此确认理论继承或新增范围。", "basis": "target_paper_only", "target_locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页6 §5.3、物理页10 References。\n", "prior_actually_read": false}, {"citation_as_printed": "Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.", "identifier_if_present": "arXiv:2402.03300", "relation_candidate": "组件复用", "shared_component": "GRPO组归一化及策略更新。", "claimed_difference": "本作分析其噪声与模式演化，不提出替代GRPO的训练算法。", "basis": "target_paper_only", "target_locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页2—3、物理页10 References。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "多模式解耦、收敛阶及集中机制构成实质理论解释，超过局部调参；不支持路线级首创判断。", "central_increment": "前作已有GRPO及噪声验证研究（仅本篇转述）；本作在类内对称均值场下新增J门控的质量—形状动力学，证据为式(7)、定理F.1和表1；尚待排除最近前作覆盖。", "soundness_observation": "主无KL漂移可由所给条件均值和Jacobian推导衔接；KL唯一性扩展按所给式(66)存在局部代数反例，见局限。未逐证全部定理或复现实验。", "significance_observation": "可解释验证器方向性与正确模式坍缩，但真实噪声校准、训练干预收益和长期相同终点尚未实证。", "main_open_question": "Cai与Mroueh是否已在可比假设下覆盖J相线及多模式动力学，从而改变中心增量归属？"}

limitations：[{"text": "作者明确忽略跨prompt和模式的参数共享；噪声在类内对称且实验为合成翻转。有限G、有限训练及非平稳判断器限制外推，主实验也未做KL扫描。", "basis": "author_report", "locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页3 §3、物理页8—9 §7。\n"}, {"text": "贪心单次通过率不直接测量训练采样分布中的错误质量p；未注入噪声的单测也未获独立语义正确性审计。短程结果更直接支持方向预测，而非渐近收敛阶。", "basis": "model_inference", "locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页7 §6.2、物理页39 Appendix M。\n"}, {"text": "按式(66)取K=M=1、J=1、β=0.1、pref=0.999，移项得h(p)=0.1[logit(p)−logit(0.999)]+2√(p(1−p))。局部代数检查给出h(0+)→−∞、h(0.5)≈0.3093、h(0.99)≈−0.0322、h(0.999)≈0.0632，因此至少有三个内点根，与H.7的无条件唯一性冲突。这针对所供公式下的KL扩展，不直接否定无KL主定理；仍需原PDF核对公式。H.3另明确普通logit梯度式(60)不同于正文式(9)采用的KL流。", "basis": "model_inference", "locator": "TEXT_OR_LwB2EacVT6_73b4c6ec5981，物理页24 Remark H.3、式(60)；物理页25 式(66)、Theorem H.7。\n \n"}]

minimal_check：{"question": "两臂情形下，H.7是否确有唯一且全局稳定的内点？", "control": "核对原式后固定上述参数，比较式(66)与普通logit梯度式(60)，并使用不同初始p。", "observable_outcome": "检查根数、根处漂移导数及不同初值的极限，区分两种更新几何。", "resources": "原PDF公式与CPU标量求根/ODE即可；无需LLM训练，本轮未运行，耗时未知。", "failure_or_stop_condition": "原PDF公式若与提取文本不同，先停止并修正；同一式(66)出现多个内点根即否定其唯一性，结论仅限KL扩展。"}

missing_fields：["原PDF图像、曲线与误差带的可核读数据。", "硬件型号/数量、运行时、GPU小时及实际token预算。", "PPO/GSM8K独立配置与种子统计；附M虽称适用于all experiments，但列出的是Qwen/GRPO配置，不能直接套用于DeepSeek/PPO。", "前作全文、完整代码、原始日志和真实验证噪声审计。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

无KL多模式分析仍值得读；使用KL扩展前必须先处理所印唯一性反例，并核对更新几何、稳定项和真实噪声对称性。

题名版本范围：首物理页题名及RLVεR记号与冻结目标一致；当前官方41页附件和Pro身份/哈希匹配。Pro完整读取提供文本，图像未见；本地核对关键公式原页。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

J门控理论的假设：§3明确每prompt独立、模式logit而非共享网络参数，所有好模式共享TPR、坏模式共享FPR；J=TPR−FPR。总体归一化无KL漂移可按J分方向，但不能把总体J>0推广到模式依赖或非平稳验证器。σ采用总体Bernoulli方差，渐近阶不能不加说明地沿用实际有限G与固定数值稳定项。

核查定位：p003:L0030-L0062, p004:Eq3-5, p012:AppendixA；mean_field_and_noise_symmetry_conditions_checked

实证数值及支持范围：p6为10239训练、594验证prompt；p7为G8、两epoch1410步、KL=0及5种子。Table1明确Pass@1百分比：J−0.1为0.16%，J0为13.4%，J0.3两噪声配置16.0/14.6%。不是0.16的概率值。作者也说明有限训练更直接支持方向预测，不是渐近终点与速率阶的实证证明。

核查定位：p006:L0053-L0063, p007:L0032-L0059, p008:Table1；units_and_experimental_scope_match

KL唯一性反例的原式确认：原PDF Eq66及TheoremH7确实声称任意β>0、固定类内分布下唯一稳定内点。取K=M=1、J1、FPR=FNR=0、β0.1、p_ref0.999，则σ=√(p(1−p))、s2+t2=2，移项为h(p)=0.1(logit p−logit0.999)+2√(p(1−p))。本地仅作标量算术复核：h(0+)趋−∞，h(0.5)=0.3093245，h(0.99)=−0.0321660，h(0.999)=0.0632139。连续性保证至少三个内点根，与所印无条件唯一性冲突。

核查定位：p025:Eq66,TheoremH7, local_check/p025.png, local_check/kl_equation66_sign_check.json；counterexample_to_printed_KL_uniqueness_verified

反例不可扩大适用范围：同类唯一性概括也出现在正文Eq9后，因此KL扩展需修正条件或结论；本次反例不直接否定无KL的J方向性结论，也没有证明真实共享参数GRPO存在三个稳态。未进行ODE数值积分。

核查定位：p006:Eq9 and following paragraph, p025:Eq66；counterexample_scope_explicit

本地补充/限定：[{"kind": "local_verification", "detail": "Pro提出的KL反例已对照原PDF并用独立标量运算确认符号；只据连续性得至少三个根，不声称完成整套动力学或实验复现。"}]

核查局限：["未逐证全部无KL收敛、类内集中定理或最近前作覆盖，L2仍为暂定贡献判断。", "只做公式的有限局部代数/算术核对，没有运行作者代码、训练或ODE实验。", "没有独立审计单元测试的语义完备性或真实LLM模式分布。"]


## pro022 · GRPO is Secretly a Process Reward Model

论文 OR_nMGaOCVlDW；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_nMGaOCVlDW_91379a381405", "source_url": "https://api2.openreview.net/pdf?id=nMGaOCVlDW\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "91379a381405b02a4471d5a574a6a991aaa09e55ff879a0c54d707951ed7b03c", "physical_pages": 16}], "read_ranges": ["TEXT_OR_nMGaOCVlDW_91379a381405：物理页1–9，摘要及§1–7。", "TEXT_OR_nMGaOCVlDW_91379a381405：物理页10–11，致谢、影响声明及参考文献。", "TEXT_OR_nMGaOCVlDW_91379a381405：物理页12–16，附录A–E，包括证明、实验配置、表3及图7–9的可提取节点文字。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["连续页标1–16齐全，但只有文本；图1–9的曲线、连边及配色不可见。", "双栏及公式存在错位；表1–3数值基本可辨。附录E长轨迹被作者截断，不能视为完整生成记录。", "未提供前作、代码或其他版本；不认定该附件为最终出版版。"]}

问题：仅有结局奖励的GRPO是否已隐式分配过程信用，以及如何缓解共享前缀频次失衡对训练的影响？

方法：按组内完全相同前缀构建作者所称的B(G)树；每段奖励为共享该前缀的轨迹集合λ的结局奖励均值，优势仍相对全组标准化。λ-GRPO把每个token的完整损失项(P_i,t·a_i−D_i,t)除以|λ(i,t)|，同时重加权策略项和KL项，不新增过程标签或rollout。

作者主张：GRPO与配备非平凡Monte Carlo PRM的过程奖励敏感目标等价。

论文证据：定理1及附录B通过共享前缀上的优势求和证明L_GRPO(G)=L_PRM(G)；另统计真实训练中的前缀重叠。

模型推断：实质增量是既有目标的过程级解释，而不是新训练一个奖励模型；代数等价不等于获得额外过程监督。

定位：['TEXT_OR_nMGaOCVlDW_91379a381405，p2§2.1、p4–5定理1、p12附录B。\n']

作者主张：λ-GRPO消除过程段频次放大，以极低开销改善推理训练。

论文证据：式9消去式8的|λ|乘数；六个合成配置均改善，真实任务20个比较单元中15个提高。

模型推断：是由机制分析导出的明确局部改进，但尚未独立排除梯度尺度及正则重分配带来的收益。

定位：['TEXT_OR_nMGaOCVlDW_91379a381405，p7式9及表1、p8表2。\n']

key_results：[{"setting": "DeepSeek-R1-Distill-Qwen-1.5B在OpenRS上的GRPO前缀结构统计。", "baseline": "平坦B(G)，作为无非平凡前缀结构的参照", "metric_or_guarantee": "平坦树计数及非平凡过程结构占比", "reported_values_and_units": "组大小6：6700组中仅12组平坦，约99.8%非平凡；组大小36：1100组中无平坦树。", "information_and_compute": "两组分别训练1675/275步，学习率6e-6/1e-6；batch=4，温度0.75，最多4096个新token。", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p6§3.2。\n"}, {"setting": "GPT-2-small遍历深度4二叉树；目标奖励+1，其他路径按共享前缀分配负奖励或+0.7。", "baseline": "标准GRPO", "metric_or_guarantee": "最后50训练步的目标路径频率，五种子均值", "reported_values_and_units": "n=1、rneg=-1时：GRPO为0.0000，λ-GRPO为0.7535；表1全部六个配置均提高。", "information_and_compute": "每配置、每方法五种子，每次250步；组大小16，学习率1e-5。另用5e-5时，两种方法所有配置均未收敛到目标。", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p7表1、p8§4.3及脚注2"}, {"setting": "Qwen-1.5B与Llama-3.2-1B-Instruct经OpenRS训练，评估AIME24、MATH-500、AMC23、Minerva、OlympiadBench。", "baseline": "同配置GRPO；另列未训练基座", "metric_or_guarantee": "五任务平均exact-match accuracy，0–1尺度", "reported_values_and_units": "GRPO→λ-GRPO：Qwen β=0为0.4837→0.5576，β=0.04为0.5394→0.5739；Llama β=0为0.0842→0.1001，β=0.04为0.0996→0.0973。20个单元中15胜、4负、1平，并非全面提升。", "information_and_compute": "每次1000步，组大小6、batch=4、温度0.75、最多4096新token；Qwen学习率1e-6，Llama随β为5e-7/1e-7。125题验证集每25步评估并选最佳检查点。", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p8表2及§5.1、p12附录C。\n"}, {"setting": "额外权重计算开销及验证集峰值效率。", "baseline": "标准GRPO", "metric_or_guarantee": "CPU秒/token、额外总秒数、达到验证峰值的训练步数", "reported_values_and_units": "Intel i7上，组大小6/36分别增加1.19e-7/1.21e-7秒/token，对应8.38/10.27秒。正文称平均验证准确率提高超过10%，峰值步数不足一半；图6不可见，无法核读各次峰值及增幅口径。", "information_and_compute": "构树复杂度O(k²n)；CPU计时使用§3.2轨迹。全部实验使用单张H100、24次梯度累积、generation batch=6；总GPU小时未报告，步数减少不能直接等同端到端时间减半。", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p7§4.2、p9§5.2、p12附录C。\n"}]

prior_work_candidates：[{"citation_as_printed": "Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., and Guo, D. Deepseek-math: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.", "identifier_if_present": "arXiv:2402.03300", "relation_candidate": "理论扩展", "shared_component": "GRPO组相对优势", "claimed_difference": "本篇转述前作提出GRPO；本作分析其隐式过程奖励并提出逆频次改法。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p2§2.1、p9§6、p11参考文献", "prior_actually_read": false}, {"citation_as_printed": "Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476, 2025.", "identifier_if_present": "arXiv:2503.14476", "relation_candidate": "组件复用", "shared_component": "token-level policy gradient objective", "claimed_difference": "本作使用其token归一化目标作为等价分析的前提，而非贡献该归一化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p2§2.1、p11参考文献", "prior_actually_read": false}, {"citation_as_printed": "Hou, Z., Hu, Z., Li, Y., Lu, R., Tang, J., and Dong, Y. TreeRL: LLM reinforcement learning with on-policy tree search. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 12355–12369, 2025.", "identifier_if_present": null, "relation_candidate": "背景引用", "shared_component": "树结构与Monte Carlo过程奖励", "claimed_difference": "按本篇转述，TreeRL显式分支采样并构造过程奖励；本作利用常规GRPO采样中已有的前缀重叠，不据此认定直接继承。", "basis": "target_paper_only", "target_locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p9§6、p10参考文献", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心是既有算法的非平凡机制解释，并据此导出可检验改法，超过单纯性能微调；尚不足以认定路线级新框架。", "central_increment": "前作已有GRPO和显式Monte Carlo过程奖励（仅本篇转述）；本作在特定未裁剪、token归一化条件下揭示目标等价与频次放大，并通过逆频次重加权改善部分训练结果。", "soundness_observation": "附录B的共享前缀求和恒等式可追踪。但按提取文本，B(G)定义允许n=0及任意子集，不能直接推出树；p5分区使用len(y)≤t也与有效token索引不符，需核对原公式。局部前缀受抑不充分保证整轨迹概率下降，未作全面证明审计。\n", "significance_observation": "可能帮助理解RL信用分配；实现改动轻量，但推广到大模型、多任务和显式PRM替代尚缺证据。", "main_open_question": "匹配整体更新尺度后，λ-GRPO是否仍有稳定优势，从而支持收益确由过程段频次重分配产生？"}

limitations：[{"text": "算力限制使真实任务仅覆盖1B/1.5B模型及一个训练数据集；作者称方法只充分处理其所述反探索效应，对反利用效应仅减轻。", "basis": "author_report", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p12附录A"}, {"text": "未明确真实任务重复训练种子数及置信区间定义，未提供梯度尺度匹配消融或显式PRM强基线；现有结果不能确立广泛统计优势。", "basis": "model_inference", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p8–9§5、p12附录C"}, {"text": "共享开场措辞也会产生非平凡树；结构出现率本身不能证明语义过程信用准确。等价分析亦不能无条件推广至多轮裁剪更新。", "basis": "model_inference", "locator": "TEXT_OR_nMGaOCVlDW_91379a381405，p2§2.1、p6§3.2、p14–16附录E"}]

minimal_check：{"question": "逆频次收益能否超越整体更新尺度变化？", "control": "在β=0、n=1、rneg=-1的二叉树任务比较GRPO、λ-GRPO及经标量缩放匹配更新范数的GRPO，保持种子和采样预算一致。", "observable_outcome": "五种子下最后50步目标频率及目标前缀概率变化。", "resources": "GPT-2-small，每臂五种子、每次250步；论文设备为单张H100，本检验实际耗时未知。", "failure_or_stop_condition": "若尺度匹配后优势消失或反转，则频次机制的独立收益未获支持。"}

missing_fields：["原始图像、各运行精确峰值及端到端训练耗时。", "真实任务重复种子数、置信区间方法与置信水平、完整测试解码设置。", "零奖励方差组处理、B(G)形式定义及分区不等式的原版核对。", "TreeRL参考条目未列独立标识；前作、代码及实验均未外部核读或复现。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

目标的过程级解释及轻量改法值得比较；下一优先问题是匹配更新范数和KL强度后，逆频次权重是否仍有独立收益。

身份和全文范围：首物理页题名匹配，官方当前16页附件与Pro身份、材料哈希一致；Pro完整读取所供文本并说明图像未见。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心等价的条件：§2.1明确改用DAPO全组token归一化，并取每批µ=1、忽略裁剪。附录B在共享前缀使P和KL项相同的条件下，将组均值优势求和重写为轨迹优势求和。该解释没有新增过程正确性标签，也不能不加条件推广到逐序列长度归一化或多轮裁剪更新。

核查定位：p002:L0044-L0057, p012:L0017-L0047；algebraic_grouping_and_assumptions_checked

实际方法重加权什么：Eq9把整个token损失(P*a−D)除以共享前缀数|λ|，KL项也变化，不仅改奖励均值。若要归因独立过程信用收益，还需区分整体梯度尺度及正则强度的改变。

核查定位：p007:L0043-L0059；policy_and_KL_reweighting_confirmed

关键数值和非全面优势：Table1的n1/rneg−1末50步目标频率为0→0.7535。原PDF Table2确认Qwen β0平均0.4837→0.5576，而Llama β0.04为0.0996→0.0973；20个任务/配置比较中15升、4降、1平，与Pro一致。点估计不能直接作跨种子的统计优势保证。

核查定位：p007:Table1, p008:Table2, local_check/p008.png；values_and_direction_counts_checked

计算开销口径：§4.2的1.19e−7/1.21e−7秒每token及8.38/10.27秒测量的是CPU附加权重计算；附录C另说明单张H100、24步梯度累积。不能将少于一半的峰值训练步数直接称完整训练墙钟减半。

核查定位：p007:L0043-L0047, p012:L0051-L0057；overhead_scope_checked

本地补充/限定：[]

核查局限：["未独立裁定Pro提出的B(G)形式定义和长度不等号疑点；不据这些疑点否定整个重写结果。", "未执行作者代码、重训或核验全部曲线；未全文核读前作。", "L2维持为Pro暂定判断，非历史首创认证。"]


## pro023 · Reuse your FLOPs: Scaling RL on Hard Problems by Conditioning on Very Off-Policy Prefixes

论文 OR_a5itZI3DeQ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_a5itZI3DeQ_c850e4c519d6", "source_url": "https://api2.openreview.net/pdf?id=a5itZI3DeQ\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_a5itZI3DeQ_c850e4c519d6：物理页1–33全部所供文本；包括p1–9正文、p10影响声明与致谢、p10–13参考文献、p14–33附录A–F及前缀示例。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["物理页标1–33连续，未发现所供文本缺页；未独立核验原PDF或终稿身份。", "图1–17图像均未提供，仅能阅读图题、正文和零散图中文字，不能恢复曲线端点、误差带或柱高。", "双栏文本交错，部分公式根号、上下标及裁剪运算排版失真；相关疑点按所供文本提出，不能排除提取错误。", "未提供前作全文、其他版本、代码或实验日志；未搜索、复现或逐一定理认证。"]}

问题：如何复用过去偶然获得的正确推理轨迹，使极低成功率数学题获得有效RL信号，并改善无前缀求解？

方法：每题拒绝采样保留一条验证正确轨迹，在其40%–80%位置固定随机截取三个前缀，作为assistant推理的未完成续写。将3000个带前缀题与1000个原题按3:1混合，用REINFORCE及组均值基线训练；仅在线续写token计策略损失，前缀不作监督目标。常规评测不提供前缀。

作者主张：把旧轨迹从监督目标改为条件上下文，稳定提高难题RL的算力效率。

论文证据：两种模型、同族与跨族前缀及PPO变体均有实验；计算比较明确纳入正确轨迹采集成本。

模型推断：状态重置本身已有前作；增量是推理模型中的具体实现与端到端收益，不能称为首次提出reset。

定位：['TEXT_OR_a5itZI3DeQ_c850e4c519d6:p6–8 §5；p14–15 §B；p30 §F.3–F.4']

作者主张：仅训练带前缀题也能改善无前缀行为，并放大或替换前缀中的策略。

论文证据：前缀长度带实验、相关与不相关题对照、策略关键词及NLL分析支持迁移；跨族长前缀的迁移较弱。

模型推断：支持不止逐字模仿或原路径拼接的行为变化；共享潜表示机制仍是假说。Dirichlet策略初始已有非零概率，不等于从零创造新策略。

定位：['TEXT_OR_a5itZI3DeQ_c850e4c519d6:p4–5 §4；p26–28 §E']

作者主张：PrefixRL目标保持原任务最优解，并有更好的样本效率及最坏情况分离。

论文证据：Theorem 3.2、3.3及Proposition 3.4，附录D给出证明。

模型推断：一致性依赖一个共同策略完美实现所有正确轨迹；样本界针对理想化NPG，不直接保证实际REINFORCE或解释back-generalization。

定位：['TEXT_OR_a5itZI3DeQ_c850e4c519d6:p3–4 §3.1；p16–25 §D']

key_results：[{"setting": "1000道DAPO及OMNI-MATH 6–8级题；Llama起点在512次采样中未成功，不代表真实成功概率为零。", "baseline": "SFT+RL、标准RL，含n=8与n=64设置", "metric_or_guarantee": "达到相同无前缀训练奖励所需估算FLOPs", "reported_values_and_units": "作者报告相对最强SFT+RL约2×算力效率。摘要另称最终奖励3×，正文称训练准确率提升>45%；缺少共同端点与清晰口径，不合并为同一数值。", "information_and_compute": "Llama-3.1-8B先经OpenThoughtsV3蒸馏，另测Qwen3-4B。主训练batch=128、n=8、学习率10^-6、通常400步；续写上限16384 token，总序列上限36000。Llama采集平均约650次/题、上限2500次，总约650k轨迹及0.7×10^20 FLOPs。F.2按2ND推理、6ND更新估算，D包含输入与输出token。", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p1摘要；p6 §5；p29 §F.1.2–F.2。\n"}, {"setting": "Llama-3.1-8B，无前缀AIME 2025与HMMT February 2025评测", "baseline": null, "metric_or_guarantee": "pass@1", "reported_values_and_units": "正文报告AIME 38.2%→61.3%，HMMT 29.2%→49.4%；未明确两组起点对应哪条基线，不能归为相对SFT+RL的增益。", "information_and_compute": "§5主实验n=8；F.2称pass@k用每题256次采样估计，测试温度0.7；该组数值的精确检查点FLOPs未列明。", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p7 §5；p29 §F.2。\n"}, {"setting": "相关图论题P2、P3；训练P2时把P3及完整解答置于上下文", "baseline": "仅在P2上进行标准RL", "metric_or_guarantee": "无上下文单题pass@4", "reported_values_and_units": "PrefixRL：P2为63%，未直接训练的P3为60%；标准RL在P2上为18%。", "information_and_compute": "§4.3的小规模机制实验，F.1.2列训练100步；独立种子数量与专属算力未报告。", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p5 §4.3；p26 §E.2。\n"}, {"setting": "满足D.1–D.3的PrefixRL-NPG，T轮、每轮N个critic样本", "baseline": "不接触离线轨迹的标准在线RL", "metric_or_guarantee": "作者声称的高概率次优界", "reported_values_and_units": "J*−J(π̄T) ≤ O(√(KL(μ‖π₀)/T)+√(log(T|F|/δ)/N))，概率至少1−δ；作为待核定理记录。", "information_and_compute": "算法采样离线轨迹状态，并混合离线动作与当前策略动作；离线成功轨迹获取成本不在该在线样本界内。", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p18 Algorithm 1；p21 Eq.D.42"}]

prior_work_candidates：[{"citation_as_printed": "Chang, J. D., Shan, W., Oertell, O., Brantley, K., Misra, D., Lee, J. D., and Sun, W. Dataset reset policy optimization for rlhf. arXiv preprint arXiv:2404.08495, 2024.", "identifier_if_present": "arXiv:2404.08495", "relation_candidate": "理论扩展", "shared_component": "dataset reset、critic拟合与NPG证明技术", "claimed_difference": "本文明确称沿用其证明技术，改用正确且最优可实现的reset轨迹，声称不再约束当前策略与SFT策略之间的KL。", "basis": "target_paper_only", "target_locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p10参考文献；p18 §D.2", "prior_actually_read": false}, {"citation_as_printed": "Zhang, X., Huang, Z., Li, Y., Ni, C., Chen, J., and Oymak, S. Bread: Branched rollouts from expert anchors bridge sft & rl for reasoning. arXiv preprint arXiv:2506.17211, 2025b.", "identifier_if_present": "arXiv:2506.17211", "relation_candidate": "比较基线", "shared_component": "利用已有解答引导在线探索", "claimed_difference": "本文将BREAD实现为显式专家提示，区别于assistant续写前缀，并报告后者迁移更强、较少绑定提示策略。", "basis": "target_paper_only", "target_locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p7–8 §5；p13参考文献", "prior_actually_read": false}, {"citation_as_printed": "Amani, M. H., Lotfi, A., Baldwin, N. M., Bengio, S., Farajtabar, M., Abbe, E., and West, R. Rl for reasoning by adaptively revealing rationales, 2025.", "identifier_if_present": "arXiv:2506.18110", "relation_candidate": "背景引用", "shared_component": "揭示部分推理来缓解探索困难", "claimed_difference": "据本文转述，AdaBack自适应搜索人工解答中的最小提示；本作固定随机截取模型轨迹，并研究back-generalization。", "basis": "target_paper_only", "target_locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p10参考文献；p14 §B", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "reset与部分解答引导并非新路线，但非逐字模仿的反向迁移现象及含采集成本的难题训练收益，构成实质机制知识候选；不足以判历史首创或L3。", "central_increment": "前作已有reset与hint引导（仅本篇转述），本作在可获取少量正确长轨迹时，以续写条件化复用旧算力，并展示无前缀迁移；尚待排除提示内容、上下文预算和基线实现差异。", "soundness_observation": "一致性论证在强可实现假设下有清晰依据。样本界中D.18/D.61的状态平均优势未显式带H，D.35–36又等同状态平均KL与轨迹KL；D.47称观察历史后隐藏目标串仍均匀独立，与失败排除候选串不一致。这些具体步骤需修订或澄清，不直接否定经验结果。", "significance_observation": "对稀疏奖励推理训练有实际意义；工程核心是数据构造与损失mask而非新架构，但长上下文采样及RL资源负担不低。", "main_open_question": "与BREAD或既有reset方法在相同前缀内容、总预算及充分调参下比较，无前缀迁移的独立优势是否仍稳定存在？"}

limitations：[{"text": "作者承认back-generalization机制未完全理解，实验限数学；跨族长前缀即使训练800步迁移仍弱，Llama→Qwen迁移也较不有效。", "basis": "author_report", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p9 Limitations；p27 §E.3；p30 §F.3"}, {"text": "理论使用全轨迹状态重置、混合动作critic及NPG，实际采用三个固定切点和REINFORCE；一致性也包含原题目标，不能当作仅前缀训练迁移的证明。", "basis": "model_inference", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p16–21 §D.1–D.2"}, {"text": "BREAD提示取思考后的解答段，PrefixRL取思考轨迹前缀，信息内容未严格匹配；离策略基线又采用有偏token权重与接受率近似，比较尚不能归因于条件化形式本身。", "basis": "model_inference", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p7 §5；p28 §F.1.1"}, {"text": "§4.3称基模pass@32<1%，E.2却列同组题pass@16为0.063–0.119；若同模型同采样条件则不相容，材料未解释差异。", "basis": "model_inference", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p5 §4.3；p26 §E.2"}, {"text": "FLOPs为近似而非墙钟；筛题、起点蒸馏、调参及达到2500次仍失败题目的处理成本不清楚。跨题置信区间不能代替独立训练种子方差；理论总时域与实际额外前缀预算也需区分。", "basis": "model_inference", "locator": "TEXT_OR_a5itZI3DeQ_c850e4c519d6:p6 §5；p29 §F.1.2–F.2。\n"}]

minimal_check：{"question": "续写式前缀是否比同内容的显式提示带来更强无前缀迁移？", "control": "在小固定数学题集上，将完全相同的正确轨迹片段分别置于assistant续写前缀和user提示；两组均只训练带条件题，匹配总序列预算、RL配置与实际计算量。", "observable_outcome": "比较多种子下无前缀pass@1/pass@k，并同时检查带条件任务是否已学会。", "resources": "一个Qwen3-4B起点、已有正确轨迹、答案验证器及至少三个训练种子；GPU数量与时长需实测。", "failure_or_stop_condition": "若两组均学会带条件任务但续写组的无前缀优势消失或跨种子不稳定，则其独立迁移优势未获支持。"}

missing_fields：["key_results[1].baseline：正文未明确38.2%与29.2%对应的基线。", "图中精确端点、完整误差带及各结果对应FLOPs。", "GPU配置、墙钟、完整种子统计与调参预算。", "采样上限失败题处理及完整生命周期成本。", "原PDF图像、前作全文及可执行实现；理论符号歧义尚未核清。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

复用已支付的成功轨迹且显式计算采集成本，有直接训练设计价值；继续读时优先做同内容前缀/提示、同总预算的对照。

身份版本范围：题名一致，官方当前33页附件和Pro ID及文本哈希匹配；Pro声明所有提供文本已读并保留图像/公式损失的说明。

核查定位：first_page_text.txt, text_delivery_manifest.json；pass_with_version_limit

中心机制及训练/测试条件：§3把旧成功轨迹作为条件上下文，并对离策略前缀mask梯度；§5从每题一条答案验证正确轨迹中在40%–80%处取三个前缀，3000带前缀题与1000原题组成训练，常规评测为无前缀。它区别于直接模仿旧动作，但正确终局轨迹不自动保证所有中间推理语义正确。

核查定位：p003:L0059-L0075, p006:L0023-L0030, p029:L0034-L0037；mechanism_and_no_prefix_evaluation_confirmed

决定性成本报告：原PDF及正文p6明确把拒绝采样采集计入比较：约650次/题、1000题、约650k轨迹、0.7×10^20 FLOPs，采样上限2500。约2倍相对SFT+RL效率是作者的估算FLOPs结果；F.2使用2ND前向、6ND更新，D含prompt和生成token，不能换算为墙钟或整个模型生命周期成本。

核查定位：p006:L0032-L0064, p029:L0034-L0059, local_check/p006.png；cost_inclusion_and_units_checked

稀有能力与额外上下文：任务筛选为基座pass@512观测零，不证明真实成功概率严格零。F.1.2给续写上限16384、总序列36000，前缀可长12k–14k；这是带额外状态/上下文信息的训练，不是无信息增益的免费搜索。

核查定位：p006:L0053-L0059, p029:L0013-L0024；finite_sample_and_context_budget_limits_checked

理论和实用算法不是同一保证对象：Assumption3.1需共同最优策略完美实现所收集正确轨迹；理论Algorithm1另以半概率选离线动作拟合可实现critic，再做NPG并返回混合策略。实际主实验用REINFORCE、三个固定切点，不能直接声称该实际更新已获同一最优样本界；一致性目标还含原题项。

核查定位：p003:L0023-L0031, p003:L0068-L0075, p018:Algorithm1,D.1-D.3, p029:L0013-L0024；theoretical_conditions_and_algorithm_difference_confirmed

本地补充/限定：[]

核查局限：["未核算完整采样、蒸馏、调参和未成功题处理成本；不独立确认2倍效率。", "Pro对附录时域归一化、条件概率及小题基线的疑点未在本地完成证明审计，保持待核。", "未运行作者代码、下载权重、核读前作或做新的训练/第二轮模型调用。"]


## pro024 · IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL

论文 OR_rEz2wdNZBJ；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7", "source_url": "https://api2.openreview.net/pdf?id=rEz2wdNZBJ\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed", "parent_pdf_source_id": "83dcb2aa8f8c75d0095d558b074385a3368ea015a28e33294e094bedf1bfcd57", "source_pdf_sha256": "20f3cfd661a703897acb660ce2ef5963a3de5e30562c25f5e6dd61dec20d042f"}], "read_ranges": ["TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：物理页1—21全部已提供文本；正文§1—7、致谢及影响声明位于页1—9，参考文献页9—11，附录A—J页12—21。页标连续，未见文本缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅有全文文本，未查看原PDF；图1—25图像不可见，不能核查曲线、误差条及图内拟合参数。表1、表2数值可读，部分公式和双栏文字存在排版损失。\n", "未提供前作或其他版本；未搜索、运行代码、复现实验或逐项证明理论推演。"]}

问题：固定模型、提示分布和采样预算时，如何在每题rollout数n、每批题数Bp和更新步数M间分配资源，使验证表现最好？

方法：以C=Bp·n·M计采样量；稳定训练后扫参，提取验证avg@4的分箱破纪录点，拟合单调奖励曲线并取上包络，再拟合log n*对log C的sigmoid。分别研究固定Bp、固定总批量B及三轴联合优化。

作者主张：计算最优n随预算增加后饱和；适中范围内Bp主要控制稳定性，剩余预算应分给M。

论文证据：主网格、联合优化及token口径分析报告相同定性趋势；附录另提供大模型、非数学任务和PPO/CISPO的稀疏实验。

模型推断：中心增量是预算约束下的可操作经验知识，而非新RL算法；“最优”限于已搜索配置，尚非普适外推定律。

定位：['TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页4—8§4—5、页15—18附录C—E。\n']

作者主张：较大n在Easy主要提高sharpening，在Hard主要扩展coverage，并缓解跨题干扰。

论文证据：正文报告best@4/worst@4的最优n不同；附录F固定Bp=128，比较训练/估计rollout数256/256、64/64、64/256，报告最佳验证奖励排序256/256 > 64/256 ≈ 64/64。

模型推断：支持收益不只来自更精确的组内基线；pass@1分布诊断及该消融尚不能独立证明“干扰缓解”或排除梯度估计差异。

定位：['TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页5—7§4.1、§5.1，页17—20附录F、H。\n']

key_results：[{"setting": "Qwen2.5-7B-Instruct、Guru-Math；正文按avg@16划分Easy约6000题、Hard约5000题，各300题同分布验证集。", "baseline": "同预算下较小n或更多更新；另比较训练集规模。", "metric_or_guarantee": "验证avg@4前沿及最优n的饱和。", "reported_values_and_units": "Easy正文报告n=512仍占据高预算前沿，扩大至2048未延伸前沿；数据量D从6000减至500时，报告饱和值由512降至256，继续用512出现退化。", "information_and_compute": "0/1结果奖励；主实验合计约120000 H200 GPU小时，非单次运行成本。温度0.6、top-p=1.0。", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页3—5§3—4.1、页8§5.2及图12、页12附录A。\n"}, {"setting": "附录C.2跨任务与模型规模实验。", "baseline": "n=8，对照n=64或128。", "metric_or_guarantee": "各配置最佳reward；并非统一预算终点比较。", "reported_values_and_units": "表1原值，括号为采样compute，K/M沿用原表：Qwen2.5-7B/Guru-Code，n=8/64/128为68.7(0.2M)/69.8(0.4M)/73.9(0.5M)；Guru-Logic为30.7(770K)/31.9(2.7M)/31.3(4M)；Qwen3-32B/SWE agent，n=8/64为35.9(118K)/43.5(147K)；K2-V2 70B/Guru-Math为85.0(389K)/87.1(1.3M)。reward表头未明示单位。", "information_and_compute": "Code/Logic使用1000训练样本和四个各200样本的留出划分；SWE使用R2E-Gym，最多50轮、64k tokens；70B数学实验也限64k tokens。单项GPU成本未报告。", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页15附录C.2、表1。\n"}, {"setting": "Qwen2.5-7B-Instruct/Guru-Math，PPO与CISPO。", "baseline": "较小n；各配置采样预算不同。", "metric_or_guarantee": "最佳reward及到达该值的compute；仅支持定性泛化。", "reported_values_and_units": "表2原值：PPO Easy，n=32/128/256为58.8(2.6M)/64.8(2.7M)/64.3(2.8M)；PPO Hard，n=32/128为15.7(1.1M)/17.9(1.8M)；CISPO Easy，n=32/256为61.3(3.1M)/69.4(4.6M)。reward单位未在表头明示。", "information_and_compute": "稀疏配置，不构成独立缩放律拟合；逐运行硬件和耗时未报告。", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页16附录C.3、表2。\n"}]

prior_work_candidates：[{"citation_as_printed": "Khatri, D., Madaan, L., Tiwari, R., Bansal, R., Duvvuri, S. S., Zaheer, M., Dhillon, I. S., Brandfonbrener, D., and Agarwal, R. The art of scaling reinforcement learning compute for llms. arXiv preprint arXiv:2510.13786, 2025.", "identifier_if_present": "arXiv:2510.13786", "relation_candidate": "背景引用", "shared_component": "RL奖励—compute的sigmoid趋势及稳定训练研究。", "claimed_difference": "由固定流程延长训练转向三轴预算分配。", "basis": "target_paper_only", "target_locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页8§6、页10参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Hu, J., Liu, M., Lu, X., Wu, F., Harchaoui, Z., Diao, S., Choi, Y., Molchanov, P., Yang, J., Kautz, J., et al. Brorl: Scaling reinforcement learning via broadened exploration. arXiv preprint arXiv:2510.01180, 2025a.", "identifier_if_present": "arXiv:2510.01180", "relation_candidate": "背景引用", "shared_component": "扩大并行rollout以拓展探索、突破训练平台。", "claimed_difference": "本作研究等采样预算下的机会成本与饱和，而非只增加探索宽度。", "basis": "target_paper_only", "target_locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页9—10参考文献、页19附录I。\n", "prior_actually_read": false}, {"citation_as_printed": "Li, Z., Chen, C., Yang, T., Ding, T., Sun, R., Zhang, G., Huang, W., and Luo, Z.-Q. Knapsack rl: Unlocking exploration of llms via optimizing budget allocation. arXiv preprint arXiv:2509.25849, 2025.", "identifier_if_present": "arXiv:2509.25849", "relation_candidate": "背景引用", "shared_component": "有限采样预算分配。", "claimed_difference": "前作据本篇转述自适应分配逐题资源；本作分析统一n、Bp和M的全局配置。", "basis": "target_paper_only", "target_locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页10参考文献、页19附录I。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "相较本篇转述的固定流程缩放和大rollout收益，新增三轴预算前沿、饱和边界及指标依赖，构成实质经验知识；不足以认定路线级首创。", "central_increment": "在固定模型、数据及稳定配方下，将“增加采样有益”细化为“何时增加n而非M或Bp”，证据来自系统扫参；尚待验证处方外推能力。", "soundness_observation": "实验对照覆盖较广，但主要前沿图不可核查，机制证据未充分解耦。附录G是单题tabular bandit推演，并非LLM/GRPO的严格收敛保证。", "significance_observation": "可指导后训练资源配置；工程难度主要在大规模稳定扫参，而非新算法实现。", "main_open_question": "低预算数据拟合出的规则，能否在独立验证集和未用于拟合的高预算上可靠选出接近最优的n？"}

limitations：[{"text": "Hard固定总批量时最优n可非单调；饱和受模型、数据量、指标及硬件搜索边界影响，极大Bp与n同时增大的区域未覆盖。", "basis": "author_report", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页6§4.2、页8§5、页12附录B、页17附录D。"}, {"text": "rollout数是采样成本代理，不等于端到端GPU成本；附录E支持token口径的定性趋势，但表1/2不同预算下的最佳值不能直接解释为等算力收益。", "basis": "model_inference", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页4§4、页15—17附录C—E。"}, {"text": "300题验证集上反复选配置、取破纪录点再单调拟合，可能产生选择偏差；可读文本未提供重复种子与拟合不确定性，无法量化。", "basis": "model_inference", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页3—4§3—4、页12附录A。"}, {"text": "难度分组正文使用avg@16，图2图注却写pass@16并解释为平均正确率，术语存在不一致；本提取按正文记录，不将其等同于至少一次成功概率。", "basis": "model_inference", "locator": "TEXT_OR_rEz2wdNZBJ_20f3cfd661a7：页3§3及图2。"}]

minimal_check：{"question": "缩放处方能否预测未见预算，而非仅描述已观测前沿？", "control": "固定Easy、Bp=32和配方，仅用低预算日志拟合并冻结规则；在预留高预算，与固定n=8及完整网格最优配置对照。", "observable_outcome": "等rollout预算下，独立留出题avg@4、预测所选n及相对网格最佳的奖励差，并估计抽样区间。", "resources": "原始日志、对应检查点及独立留出题；优先补评已有运行，所需GPU小时未知。", "failure_or_stop_condition": "若预留高预算上系统性选错n、显著落后网格最佳且不优于固定n，则外推处方未获支持；缺日志或检查点则停止该检验。"}

missing_fields：["图像、图内精确数值及拟合参数", "可读文本中的重复种子数、置信区间和外推误差", "逐运行GPU成本及部分附录实验的完整超参数", "表1/2明确标注的reward单位", "前作原文与版本身份核验"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可用于安排后训练采样预算，但继续读的关键是规则能否在独立预留预算和实际端到端成本下预测配置，而非重述拟合曲线。

身份、版本与阅读范围：核对官方 API 当前附件题名、21 页清单、PDF 与全文文本哈希及 Pro 返回绑定。Pro 初评覆盖所供 1—21 页文本，本地核查只覆盖所列页和两张原 PDF 页面；PMLR 页眉不单独作为最终出版版本认定。

核查定位：text_delivery_manifest.json, structured/pro024.json, p001:L0001, PDF physical pages 3,15；verified_with_scope_limit

核心经验前沿与预算定义：中心贡献是 C=Bp*n*M 约束下的已搜索配置前沿，采用验证集破纪录点、分箱、单调曲线及上包络拟合；并非给出对未见模型或预算已独立验证的普适最优律。主实验约 120000 H200 GPU 小时是总扫参开销，rollout 数不等于端到端成本。正文承认 Hard 固定总批量时 n* 可非单调。

核查定位：p002:L0017-L0045, p004:L0020-L0064, p006:L0003-L0012, p016:L0023-L0041, p017:L0026-L0039；confirmed_bounded_empirical_claim

难度分组及关键数值：原 PDF 第 3 页确认正文使用 avg@16，图 2 图注却印 pass@16 并解释为平均正确率。两者命名冲突不能把该分组当作至少一次成功概率。第 15 页表 1 确认 Guru-Code 68.7(0.2M)→73.9(0.5M)、SWE 35.9(118K)→43.5(147K)，各自是最佳 reward 与到达成本，不能读成同预算增益。第 16 页 PPO Easy n=128/256 为 64.8/64.3，亦非 n 越大越好。

核查定位：PDF physical page 3, Figure 2 and §3, PDF physical page 15, Table 1, p016:L0008-L0021；values_confirmed_interpretation_qualified

机制消融与可外推范围：附录 F 的 256/256、64/64、64/256 消融文字报告首者最佳、后两者近似，能约束纯基线精度解释；但 policy-gradient 样本量和训练内容仍变化，不能独立识别跨题干扰因果机制。图 20 的 AIME OOD 曲线在本地原 PDF 可见，这是任务分布外支持，不等于先冻结低预算规则再预测未见高预算的验证。

核查定位：p017:L0041-L0046, p018:L0012-L0027, PDF physical page 15, Figure 20, p020:L0041-L0049；mechanism_and_extrapolation_not_fully_identified

本地补充/限定：["保留 Pro 对经验性最优、预算不等及 avg@16/pass@16 命名冲突的限定；本地新增核看图 20，确认存在 AIME OOD 曲线，但没有把这一证据误写为预算外推验证。"]

核查局限：["没有重跑训练、取得原始日志或复核全部曲线；没有检查全部公式推演。", "未核读引用前作，L2 为当前 AI 初评而非已确证的历史新颖性。", "Pro 仅看全文文本、图像不可见；本地只渲染并观察第 3、15 页。", "验证集反复择优带来的偏差是方法风险，未用原始数据定量证明其大小。"]


## pro025 · A Critical Look at Targeted Instruction Selection: Disentangling What Matters (and What Doesn’t)

论文 OR_Dy5GeCd003；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_Dy5GeCd003_ae45600d74d4", "source_url": "https://api2.openreview.net/pdf?id=Dy5GeCd003\n", "version_role": "current_attachment_unverified_role", "version_note": "Official API current attachment acquired at recorded time; camera-ready identity not assumed"}], "read_ranges": ["TEXT_OR_Dy5GeCd003_ae45600d74d4：物理页1–36全部已提供文本；正文§1–8、参考文献、附录A–O。连续页标完整，题名与清单一致。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未提供PDF图像；图1–24仅有提取文字，曲线、误差条及混排热图数字无法可靠核读。表1–3文本可读，双栏交错及部分公式下标失真。", "物理p32图20面板题名为Llama 2 7B，图注却为Llama 3.2 3B，保留冲突，不自行修正。", "未提供前作全文、其他版本、作者代码或原始实验日志；未搜索、复现或执行作者代码。"]}

问题：如何利用少量有标注目标query，从指令—回答候选池选择B条训练数据，并辨明表示、选择器和预算分别影响什么？

方法：固定RR比较三种表示，固定LESS比较五种选择器；生成子集后SFT，分别测query交叉熵与测试集指标。新增UOT显式求运输计划，再按候选收到的总质量取top-B。

作者主张：解耦表示与选择算法，识别有效选择的条件。

论文证据：覆盖五任务、五基座、两个候选池；LESS距离较稳定关联query loss，但不保证下游最优。Tulu V2中的预算规律在Dolci不稳定。

模型推断：新增价值主要是跨设定的失效条件认识，而非证明梯度表示普遍占优。

定位：['TEXT_OR_Dy5GeCd003_ae45600d74d4：p4–7 §5；p25–36 附录M–O。\n']

作者主张：提出显式求解不平衡运输的UOT选择器。

论文证据：给出算法及实现；Tulu下部分大预算结果较强，Dolci下不存在一致优势。

模型推断：属于既有UOT在指令选择中的局部算法扩展。

定位：['TEXT_OR_Dy5GeCd003_ae45600d74d4：p6 §5.3；p18 附录F.2、算法1。\n']

作者主张：用集合距离最小化统一选择方法，并解释预算增加时收益递减。

论文证据：定理6.1给出两段Wasserstein距离、训练误差及联合误差构成的界；6.2给出含B^(-1/d)项的收益上界。

模型推断：是域适配与稳定性工具的任务化扩展，不是各选择器的近似比保证。

定位：['TEXT_OR_Dy5GeCd003_ae45600d74d4：p7–8 定理6.1–6.2；p22–24 附录L。\n']

key_results：[{"setting": "Llama 2 7B＋Tulu V2；RR排序后分10个距离分位，每分位选择500条。", "baseline": "RDS+(RR)、EMBED(RR)、LESS(RR)及未微调基座", "metric_or_guarantee": "query交叉熵、Spearman；BBH/GSM8K/MMLU-Pro的EM、Codex pass@10、TyDiQA F1", "reported_values_and_units": "正文报告：LESS在4/5任务上距离与下游表现强负相关；但EMBED在4/5任务下游优于LESS，尽管query loss更高。精确曲线值未可靠获得。", "information_and_compute": "上述任务query数依次为81/8/70/16/9；Codex采样温度0.8。query有参考回答，并非无标注选择。", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p4 §5.1；p14–15 附录B、表2。\n"}, {"setting": "Llama 2 7B＋约198K条Tulu V2候选；B=500、1000、2500、5000、10000。", "baseline": "随机抽样、未微调基座；表示比较固定RR，选择器比较固定LESS。", "metric_or_guarantee": "query交叉熵与各任务下游指标", "reported_values_and_units": "作者概括：LESS(RR)在BBH、TyDiQA、MMLU-Pro较优，RDS+(RR)在GSM8K较优；UOT的query loss在3/5任务最低。RR偏低预算占优，UOT/KNN-KDE偏高预算较强；不代表每个预算均胜出。", "information_and_compute": "预算实验每法3个训练种子，Random用3个独立子集。SFT为2 epochs、学习率2e-5、batch128、2048 tokens，单H100 80GB。LESS另用10000条预热4 epochs、4检查点及8192维投影；选择预算不含这些成本。", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p5–6 §5.2–5.3；p17–18 附录E.3、G。\n"}, {"setting": "定理6.2：有界直径Δ、维数d≥3、同预算B。", "baseline": "有放回均匀随机多重集Srnd，对比使query距离最小的子集S*。", "metric_or_guarantee": "测试损失差LT(θSrnd)−LT(θS*)的高概率上界", "reported_values_and_units": "概率至少1−2δ时，上界为C*·[Cd·Δ·B^(-1/d)+Δ·sqrt(log(1/δ)/(2B))+W1(P̂D,P̂Q)+W1(P̂S*,P̂Q)]，其中C*=K·Gθz/μ。", "information_and_compute": "依赖强凸风险、参数方向损失Lipschitz及数据方向梯度Lipschitz；并非计算复杂度界或实际LLM直接保证。", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p8 定理6.2；p22 引理L.2；p24 附录L.3。\n"}]

prior_work_candidates：[{"citation_as_printed": "Xia, M., Malladi, S., Gururangan, S., Arora, S., and Chen, D. LESS: selecting influential data for targeted instruction tuning. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024.", "identifier_if_present": "PG5fV50maR", "relation_candidate": "组件复用", "shared_component": "LESS梯度影响表示、DG及小模型代理思路", "claimed_difference": "改用逐query处理，拆开表示与选择器，并扩展预算和候选池比较。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p3、p17 E.3、p20 J；p13参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Ivison, H., Zhang, M., Brahman, F., Koh, P. W., and Dasigi, P. Large-Scale Data Selection for Instruction Tuning. ArXiv preprint, abs/2503.01807, 2025.", "identifier_if_present": "2503.01807", "relation_candidate": "组件复用", "shared_component": "RDS+、RR、Tulu V2候选池与评测流程", "claimed_difference": "新增梯度表示交叉比较、距离分位诊断及预算分析。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p3 §3–4；p14 A；p11参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Liu, Z., Karbasi, A., and Rekatsinas, T. TSDS: data selection for task-specific model finetuning. In Globersons, A., Mackey, L., Belgrave, D., Fan, A., Paquet, U., Tomczak, J. M., and Zhang, C. (eds.), Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, 2024b.", "identifier_if_present": "13848b5893119ff772b69812c95914fa", "relation_candidate": "组件复用", "shared_component": "KNN-Uniform、KNN-KDE及OT选择思路", "claimed_difference": "统一余弦距离，并另检验原L2方案；新增显式UOT求解。", "basis": "target_paper_only", "target_locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p3、p17–18 F、p21 K；p11–12参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是系统识别距离、query loss与下游表现之间的脱节及适用边界，超出单点提分；并非新表示或路线级框架。", "central_increment": "前作已有LESS、RDS+/RR及TSDS（仅据本篇转述）；本作在统一实验条件下拆分比较，并以跨模型、跨候选池结果揭示排序不稳定性。", "soundness_observation": "6.1称仅距离受S影响不严谨：训练误差及联合误差也可能变化；iid引理用于自适应选择子集的条件需复核。未逐项证明全部定理。\n", "significance_observation": "有助于避免把低query loss误当下游收益；工程量主要是系统实验，端到端成本证据不足。", "main_open_question": "在等训练token预算下，表示之间的下游排名差异是否仍成立，而非主要来自样本长度偏好？"}

limitations：[{"text": "作者指出候选池覆盖不足、query与测试分布失配或基座已很强时，选择及微调可能无益；Dolci下方法排序尤其不稳定。", "basis": "author_report", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p8 §6.1；p25 M；p31 O。\n"}, {"text": "按例数而非token比较，且LESS偏选短序列；换Dolci同时将长度上限2048改为4096，候选池效应未被单独隔离。", "basis": "model_inference", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p19 I；p31 O。\n"}, {"text": "不是完整的表示×选择器交叉实验；query同时用于选择和loss评估，且未微调基座不用chat template，不能完全归因于选择或训练本身。", "basis": "model_inference", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p5–6 §5.2–5.3；p18 G。\n"}, {"text": "6.2仅部分项随B衰减，池偏差不消失、最优子集残差可随B变化；图8仅一个LESS种子且平移曲线对齐，不能证明完整收益单调趋零或界的紧性。", "basis": "model_inference", "locator": "TEXT_OR_Dy5GeCd003_ae45600d74d4：p8 图8及定理6.2。\n"}]

minimal_check：{"question": "等token训练能否保留LESS低query loss但RDS+下游更优的现象？", "control": "固定Llama 2 7B、Tulu V2和GSM8K，比较LESS(RR)、RDS+(RR)、Random；从B=1000设置出发，控制实际训练token总量、模板和超参数，运行三种子。", "observable_outcome": "分别记录query loss、测试EM、实际token数及方法排名。", "resources": "需要候选数据、query、测试集及表示或检查点；参考作者单H100 80GB配置，用时与总FLOPs未知。", "failure_or_stop_condition": "若等token后排名反转或跨种子不稳定，停止将原排名差异归因为表示本身；若无法实现一致token预算，则该检验不成立。"}

missing_fields：["图中逐点性能、相关系数及标准误的可靠数值", "端到端选择与训练耗时、总FLOPs及显存峰值", "前作独立核读和当前附件最终出版身份"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

值得保留其解耦评测与代理目标失效证据，下一步应追问等 token、等总数据处理成本和一致模板后排名是否保留。

身份与材料范围：题名与当前官方附件、36 页文本清单和 Pro 材料哈希一致。Pro 初评覆盖全部所供文本；本地按列出的页面核查，并观察原 PDF 第 4、7、32 页。没有取得前作全文或运行作者代码。

核查定位：text_delivery_manifest.json, structured/pro025.json, p001:L0001-L0002；verified_with_scope_limit

核心经验结论与可见精确相关系数：原 PDF 第 4 页图 2 的 LESS 距离与 query loss Spearman，按 BBH/Codex/GSM8K/TyDiQA/MMLU-Pro 顺序为 0.92/0.99/0.94/1.00/0.95；图 3 下游相关为 -0.61/+0.72/-0.89/-1.00/-0.76，明确存在 Codex 反向例外。正文 4/5 负相关与图一致，低 query loss 不保证表示之间下游排名最优。这里是十个分位的相关描述，不是因果效果或独立显著性检验。

核查定位：PDF physical page 4, Figures 2–3, p004:L0027-L0057；central_claim_and_values_confirmed

预算、监督信息和比较条件：query 是含参考回答的小样本任务集合。LESS 另需 10000 条预热、4 epochs、四检查点和 8192 维投影；最终 SFT 为 2 epochs、2048 token 上限。按样本条数固定预算没有控制实际训练 token，作者也报告 LESS 选中序列更短。Dolci 实验同时将上限改为 4096，不能把差异全部归因于候选池；零样本基座不用同一 chat template 也已明确记载。

核查定位：p014:L0034-L0059, p017:L0034-L0051, p018:L0031-L0060, p019:L0041-L0050, p031:L0011-L0028；resource_and_information_scope_confirmed

理论条件与结论强度：核看原 PDF 第 7 页及附录 L：6.1 的损失条件并非一般 LLM 交叉熵；正文称仅 Wasserstein 子集距离随 S 改变，但训练误差 LS(thetaS) 显然也依赖 S，因此距离降低本身不保证整个右端收紧。6.2 明确要求强凸 ERM、Lipschitz 条件及有放回随机基线，且包含不随 B 必然消失的池失配与子集残差；不能据此证明实际收益单调趋零。iid 引理能否用于自适应子集及全部证明步骤保留未核实。

核查定位：PDF physical page 7, Theorem 6.1 and following paragraph, p008:L0012-L0020, p008:L0041-L0064, p022:L0007-L0037, p023:L0050-L0064, p024:L0003-L0059；theory_interpretation_qualified_not_full_proof_audit

图 20 模型标注冲突：原 PDF 第 32 页各面板标题为 Llama 2 7B，图注为 Llama 3.2 3B；确认是原文中存在的冲突而非文本提取错误。保存两种标注，不自行确定该页实际模型。

核查定位：PDF physical page 32, Figure 20；source_inconsistency_confirmed

本地补充/限定：["新增原图中可核的相关系数，并确认第 32 页模型标签冲突；Pro 原先的图像不可见声明仍保留。", "本地只确认 6.1 的训练误差依赖 S 足以限制该段解释，没有宣布整个定理被反证，也没有把尚未核实的 iid 问题当作已证伪结果。"]

核查局限：["本地未检查每个模型、任务、预算的全部图表，不概括为完整全交叉验证。", "没有重跑训练、复算原始 Spearman 或置信区间；相关系数为原图报告。", "没有核读前作或完成全部证明审计；新颖性等级保持 AI 暂评。", "Pro 只阅读全文文本，本地仅检查三个渲染页。"]


## pro026 · Large Language Model Agents Are Not Always Faithful Self-Evolvers

论文 OR_kTjSSqgqGf；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_kTjSSqgqGf_fe90a009facc", "source_url": "https://api2.openreview.net/pdf?id=kTjSSqgqGf\n", "version_role": "current_attachment_unverified_role", "parent_pdf_source_id": "7cdbb149186394eb999705625f45fd94d899ebc8beb25c1c7494e374b1d534b0", "source_pdf_sha256": "fe90a009facca6b4913f0dcbf0f7a36965176d41877a05d5110c543907c6ee6f"}], "read_ranges": ["TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页1–26全部已提供文本；包括正文§1–7、参考文献、附录A–D.8。连续页标完整。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未读取父PDF图像；图1–19不可见，抽取的图内数字不能可靠对应柱形或曲线，未据此补填数值。", "部分双栏顺序及公式排版失真；表1–7文字可读，案例表不是完整运行日志。", "未提供前作、其他版本或实验日志；当前附件的最终出版版本身份未经核实。"]}

问题：冻结参数、通过外部记忆适应任务的智能体，其性能收益是否真正依赖所检索经验的语义，尤其是压缩摘要？

方法：固定骨干与原框架流程，在检索后干预经验：raw采用Empty、Shuffle、Irrelevant；condensed采用Empty、Corrupt、Irrelevant、Filler。Empty保留提示模板，与彻底删除经验段区分。比较任务表现，再结合错误案例、梯度归因与任务类型分析。

作者主张：首次系统研究experience faithfulness，发现raw与condensed经验的利用不对称，且跨单/多智能体、规模和摘要独供设置存在。

论文证据：覆盖4框架、13骨干、9个主要基准；另有2个多跳问答诊断基准。作者报告原始轨迹干预在交互任务中影响较大，摘要语义干预影响较弱；知识任务存在例外。ReasoningBank在没有raw的情况下仍呈现后者。

模型推断：支持受测系统中两类记忆作用不对称这一经验性增量，但不能把总体成绩不变直接解释为行为无因果依赖。

定位：['TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页3–6 §3–4；物理页17–20 D.3–D.5。', '摘要独供结果：物理页5 §4.2。\n']

作者主张：摘要语义局限、模型内部处理偏置、预训练先验足以处理任务，共同导致不忠实利用。

论文证据：表1及表4–6归纳有害摘要案例；梯度代理分析报告摘要归因偏低；表2、7显示部分知识任务对两类经验干预均不敏感。

模型推断：提供可检验解释，但未独立操纵三个机制；不能据此确认其因果地位或相对贡献。

定位：['TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页7–8 §5；物理页20–26 D.6–D.8。']

key_results：[{"setting": "G-Memory／Qwen3-235B-A22B，ALFWorld；该基准使用134个可解任务。", "baseline": "同骨干、未干预的G-Memory。", "metric_or_guarantee": "任务成功率。", "reported_values_and_units": "作者正文报告：78.4%→47.8%，对应Ref-Raw Irrelevant，下降30.6个百分点；condensed Filler为77.6%。非本地复现实测。", "information_and_compute": "线上多智能体记忆；大模型通过API访问。具体检索k/M、总调用量和费用未报告。", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页19–20 D.5正文。\n \n"}, {"setting": "ExpeL，2Wiki-MultiHopQA与Musique；正文说明每基准抽取100题。", "baseline": "相应骨干的未干预ExpeL。", "metric_or_guarantee": "Exact Match；原表未显式标注百分号，以下保留表值。", "reported_values_and_units": "按两基准顺序：Qwen3-32B基线(62,48)，raw Empty(65,43)，condensed Filler(64,45)；Qwen3-14B基线(60,37)，raw Empty(58,42)，condensed Filler(56,44)。", "information_and_compute": "ExpeL设温度0、greedy decoding；这两个新增基准的具体检索和交互预算未单列。", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页8 表2；物理页26 表7。\n \n"}, {"setting": "ReasoningBank／Qwen3-14B，WebArena CMS的条件性错误子集。", "baseline": "筛选条件为无摘要成功、有摘要失败，并非全体任务。", "metric_or_guarantee": "Distraction／Reliance／Premature三类错误占比。", "reported_values_and_units": "86.7%／6.7%／6.7%；不能解释为总体错误率。", "information_and_compute": "每任务最多30步，检索top-3记忆；错误子集样本数、分类标注流程与一致性未报告。", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页7 表1；物理页15 附录C。\n"}]

prior_work_candidates：[{"citation_as_printed": "Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J., and Huang, G. Expel: Llm agents are experiential learners. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 19632–19642, 2024a.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "离线成功轨迹检索与自然语言insights。", "claimed_difference": "本作不新增该学习流程，而检验两类经验的实际作用。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页13 附录A；物理页12 参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Ouyang, S., Yan, J., Hsu, I., Chen, Y., Jiang, K., Wang, Z., Han, R., Le, L. T., Daruki, S., Tang, X., et al. Reasoningbank: Scaling agent self-evolving with reasoning memory. arXiv preprint arXiv:2509.25140, 2025.", "identifier_if_present": "arXiv:2509.25140", "relation_candidate": "比较基线", "shared_component": "从成功和失败中提炼、在线检索的摘要记忆。", "claimed_difference": "本作利用其摘要独供设置检验语义干预敏感性。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页5 §4.2；物理页11 参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. Measuring faithfulness in chain-of-thought reasoning. arXiv preprint arXiv:2307.13702, 2023.", "identifier_if_present": "arXiv:2307.13702", "relation_candidate": "背景引用", "shared_component": "区分表面解释与实际决策依据的faithfulness问题。", "claimed_difference": "本篇将研究对象转向动态、分类型的外部经验；直接方法继承尚未核实。", "basis": "target_paper_only", "target_locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页8–9 §6；物理页10 参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心贡献是跨系统的经验性新知识，而非新增训练算法；比单场景性能改进更实质，但不足以认定路线级框架。", "central_increment": "前作已展示经验记忆收益（本篇转述），本作在冻结参数条件下新增分类型干预证据；尚待排除格式效应、信息冗余与指标不敏感。", "soundness_observation": "操作性干预有价值，但主要证据支持边际效用差异，尚不足以推出完整的语义因果忠实性或三因素机制解释。", "significance_observation": "提示记忆收益不能自动归因于摘要语义。工程覆盖面广，但总成本与修复方案效果未给出。", "main_open_question": "固定记忆与环境、匹配长度位置并逐任务比较动作后，摘要语义的因果影响是否仍然弱？"}

limitations：[{"text": "作者因长上下文计算和内存限制，用最后一轮embedding梯度范数近似attention-level IG。", "basis": "author_report", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页20 D.7。\n"}, {"text": "该代理与主文逐头逐层定义、逐层曲线的对应未解释；末轮当前轨迹可能已承载早期记忆影响，低直接归因不能排除间接利用。", "basis": "model_inference", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页7 §5.2；物理页20–22 D.7。"}, {"text": "总体成功率不变可掩盖逐任务得失抵消或路径改变；忽略无关摘要未必不忠实，跟随错误摘要造成失败也可能体现真实因果依赖。", "basis": "model_inference", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页1 定义；物理页4–8 §4–5；物理页21–23 表4–6。"}, {"text": "干预未明确严格匹配token长度和位置；线上记忆快照、任务顺序及配对控制说明不足，且未报告重复运行、置信区间或显著性检验，不能确认小幅差异的可靠性。", "basis": "model_inference", "locator": "TEXT_OR_kTjSSqgqGf_fe90a009facc：物理页15–17 附录C、D.1–D.2；物理页4–8及17–26结果。"}]

minimal_check：{"question": "接近不变的平均成功率是否掩盖摘要导致的行为变化？", "control": "预选20个有可执行摘要的ALFWorld任务，固定ExpeL/Qwen3-14B、初始状态和记忆；比较原摘要、等长反事实摘要及Filler，其余输入一致，并重复原样条件估计波动。", "observable_outcome": "比较首次关键动作、轨迹分歧及逐任务成功转移，而不只比较平均成功率。", "resources": "模型推理设备、ALFWorld、ExpeL及可重置状态和记忆日志；显存、耗时与费用待测。", "failure_or_stop_condition": "无法固定状态或记忆则停止因果归因；组间差异不超过原样重复波动时，不支持存在可检出的摘要影响。"}

missing_fields：["全部图形原件及可机器核验的逐条件结果、逐任务轨迹。", "总API/token/GPU时、设备数量、经验构建总预算及费用；正文仅给出API或vLLM/A800部署方式。", "G-Memory实际k/M、随机种子、重复次数、统计区间、错误分类样本量及标注一致性。", "ReasoningBank同时写temperature=0.7与greedy decoding，实际采样方式待澄清；最终评测与记忆反馈中LLM裁判的分工不明。", "WebArena列举四域合计584任务与812总量的实际评测关系未明确。", "前作全文及历史首创核读；本轮未搜索、复现或执行作者代码。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

该工作值得作为记忆系统评测的约束性证据；继续阅读应围绕固定环境和记忆快照、等长等位置反事实与逐任务动作变化，而非仅比较成功率均值。

身份、版本和完整初评范围：核对题名、官方当前附件、26 页材料清单及 Pro 的 PDF/文本绑定。Pro 完成全部所供文本的一轮初评；本地仅核看列出的页面及原 PDF 第 8、20 页，未读取引用前作。

核查定位：text_delivery_manifest.json, structured/pro026.json, p001:L0001；verified_with_scope_limit

中心干预及 faithfulness 操作定义：论文定义为行为对经验的因果依赖，但主要呈现任务成功率。Empty 保留框架提示，区别于完全删除经验块；raw Shuffle 保留内容而改变顺序，condensed Filler 替换为占位字符。这支持受测条件下的边际效用与敏感性比较；平均成功率相近不能排除逐任务得失抵消、动作路径变化或合理忽略无关信息。冻结参数和各框架不同流程也明确限定结论。

核查定位：p001:L0039-L0047, p003:L0009-L0056, p015:L0005-L0041；intervention_confirmed_causal_interpretation_bounded

决定性数值及跨任务例外：原 PDF 第 20 页图 13 确认 Qwen3-235B-A22B/ALFWorld 基线 78.4、Ref-Raw Irrelevant 47.8、condensed Filler 77.6，下降分别为 30.6 和 0.8 个百分点。该图 FEVER 基线 65，若干 raw 条件仍为 65 或 64，不能把图注的明显下降概括为每个条件成立。第 8 页表 2 确认 32B 两个 100 题问答样本基线 62/48，raw Empty 65/43，Filler 64/45；没有把这些小差异称为已验证显著变化。

核查定位：PDF physical page 20, Figure 13, p019:L0063-L0067, PDF physical page 8, Table 2 and §5.3；values_confirmed_scope_narrowed

归因方法实际实施与错误分析分母：正文 §5.2 写逐头逐层 attention IG，附录 D.7 在原 PDF 第 20 页明确改用末轮 token embedding 梯度 L2 范数均值代理；其与逐层图的对应和对早期记忆间接影响的覆盖未建立。表 1 的 CMS 86.7/6.7/6.7 来自无摘要成功、有摘要失败的条件子集，不是总体错误率；跟随错误摘要导致失败本身可能说明摘要有因果影响。

核查定位：p007:L0003-L0039, p007:L0051-L0072, PDF physical page 20, D.7, p020:L0051-L0067；proxy_and_denominator_limits_confirmed

本地补充/限定：["本地新增核看图 13、图 7 和表 2；确认关键 ALFWorld 数字，并具体记录 FEVER raw 干预的反例条件，保留跨任务限定。", "没有将 embedding 梯度代理称为完整 attention IG，也没有用均值不变推出行为完全未使用经验。"]

核查局限：["未检查全部框架×模型×任务结果，也不宣称作者完成全交叉实验。", "未取得逐任务轨迹或运行实验；未重新计算统计区间。", "ReasoningBank 同时标 temperature=0.7 和 greedy 的实施细节仍不明确。", "原文历史首创及三因素机制未独立确认；Pro 仅看文本，本地只看两张 PDF 页面。"]


## pro027 · SimpleMem: Efficient Lifelong Memory for LLM Agents

论文 OR_oBgLvd5YC6；暂定 L1；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_oBgLvd5YC6_4eb778011acb", "source_url": "https://api2.openreview.net/pdf?id=oBgLvd5YC6\n", "version_role": "current_attachment_unverified_role", "physical_pages": 14}], "read_ranges": ["TEXT_OR_oBgLvd5YC6_4eb778011acb：物理页1—14全部提供文本，页标连续；包含正文、影响声明、致谢、参考文献、附录A的提示词及附录B的实现细节与实验。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["未发现物理页缺失；只读到全文提取文本，没有查看原PDF或图1—3图像。", "公式和表1—7主要内容可辨，但存在双栏交错、图中文字乱序；图形布局与未明确列出的图中数值不可核验。", "未提供前作全文；未核验当前附件是否为最终出版版本，未搜索或复现实验。"]}

问题：如何在有限上下文与token预算下，把长期对话转化为支持事实、时间和多跳问答的有效记忆？

方法：输入对话窗口、说话人与时间信息；LLM联合筛噪、指代消解和时间归一化，生成独立事实，写入前进行会话内合成。记忆建立语义、词法和符号三类索引；查询规划器生成三路查询及深度，各取Top-n后按ID并集去重，供回答模型使用。

作者主张：Semantic Structured Compression过滤冗余并保留任务相关语义，形成独立可检索的事实单元。

论文证据：表5中移除压缩后，Temporal F1由58.62降至25.40。

模型推断：支持结构化预处理的实用价值，不等于证明semantic lossless compression。

定位：['TEXT_OR_oBgLvd5YC6_4eb778011acb：p2 §2.1；p8表5；p11 A.1。']

作者主张：Online Semantic Synthesis在当前会话写入阶段合并相关片段，避免记忆碎片累积。

论文证据：表5中移除合成后，Multi-hop F1由43.46降至29.85。

模型推断：有会话内归并有效的消融证据，尚不能推出持续终身维护能力。

定位：['TEXT_OR_oBgLvd5YC6_4eb778011acb：p3 §2.2；p8表5；p12 A.3。']

作者主张：意图规划与多视图检索改善准确率、token使用和系统延迟。

论文证据：表1—4支持平均性能与效率优势；表5—6提供检索消融和深度敏感性结果。

模型推断：完整系统的收益证据强于动态深度本身的独立收益证据。

定位：['TEXT_OR_oBgLvd5YC6_4eb778011acb：p3—4 §2.3；p5—8表1—5；p14表6。']

key_results：[{"setting": "LoCoMo，GPT-4.1-mini。", "baseline": "Mem0、LoCoMo全上下文。", "metric_or_guarantee": "表列Average F1及Token Cost。", "reported_values_and_units": "SimpleMem：43.24 F1、531 tokens/query；Mem0：34.20、973；全上下文：18.70、16910。26.4%是该骨干相对Mem0的F1增幅，不是增加26.4分；约30×的token比较对象是全上下文。", "information_and_compute": "窗口20轮，正文检索范围3—20；规划和生成token是否全部计入未明确。均为作者报告。", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p4 §3.1；p5表1。\n"}, {"setting": "LongMemEval-S，GPT-4.1-mini与GPT-4.1骨干。", "baseline": "LightMem、Mem0。", "metric_or_guarantee": "表列Average正确率。", "reported_values_and_units": "GPT-4.1-mini：SimpleMem 76.87%、LightMem 68.67%、Mem0 59.81%；GPT-4.1：SimpleMem 83.97%、LightMem 76.86%。", "information_and_compute": "均由gpt-4.1-mini参考金答案判对错；未提供人审校准或重复实验方差。", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p5表2；p13 A.4。\n"}, {"setting": "LoCoMo-10，GPT-4.1-mini；每样本平均时间。", "baseline": "Mem0、LightMem、A-Mem。", "metric_or_guarantee": "建库/检索/总时间，单位s/sample。", "reported_values_and_units": "SimpleMem：92.6/388.3/480.9；Mem0：1350.9/583.4/1934.3；LightMem：97.8/577.1/675.9；A-Mem：5140.5/796.7/5937.2。", "information_and_compute": "表中单位是每样本而非单问延迟；硬件、并发及API限流条件未报告。", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p7表4。\n"}, {"setting": "LoCoMo，GPT-4.1-mini消融与检索深度实验。", "baseline": "完整SimpleMem及固定k配置。", "metric_or_guarantee": "Average F1。", "reported_values_and_units": "完整模型43.24；去压缩31.29、去在线合成38.24、去意图检索37.78。表6固定k=3/5/10分别为42.85/43.24/43.45。", "information_and_compute": "未报告各消融的匹配token预算；表5去规划与表6固定k的其余设置是否一致不明。", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p8表5；p14表6。\n \n"}]

prior_work_candidates：[{"citation_as_printed": "Dev, K. and Taranjeet, S. mem0: The memory layer for ai agents. https://github.com/mem0ai/mem0\n, 2024.", "identifier_if_present": "https://github.com/mem0ai/mem0\n", "relation_candidate": "比较基线", "shared_component": "结构化智能体记忆。", "claimed_difference": "本篇称其图更新开销较高，SimpleMem采用规范化、流线化写入。", "basis": "target_paper_only", "target_locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p7 §3.3；p9参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Fang, J., Deng, X., Xu, H., Jiang, Z., Tang, Y., Xu, Z., Deng, S., Yao, Y., Wang, M., Qiao, S., et al. Lightmem: Lightweight and efficient memory-augmented generation. arXiv preprint arXiv:2510.18866, 2025.", "identifier_if_present": "arXiv:2510.18866", "relation_candidate": "比较基线", "shared_component": "高效记忆增强生成。", "claimed_difference": "本篇报告更高平均准确率与更低检索时间，但未详细拆解二者机制差别。", "basis": "target_paper_only", "target_locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p5表1—2；p7表4；p9参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Xu, W., Liang, Z., Mei, K., Gao, H., Tan, J., and Zhang, Y. A-mem: Agentic memory for llm agents. ArXiv, abs/2502.12110, 2025. URL https://api.semanticscholar.org/CorpusID:276421617\n.", "identifier_if_present": "arXiv:2502.12110", "relation_candidate": "比较基线", "shared_component": "结构化记忆组织。", "claimed_difference": "本篇将其描述为存在迭代总结开销，本作强调写入时合成。", "basis": "target_paper_only", "target_locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p7 §3.3；p8 §4；p10参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L1", "confidence": "medium", "reason": "目前最强证据是既有记忆范式内有价值的流程和性能改进；新增组合机制的独立收益尚未充分隔离。", "central_increment": "前作已有结构化记忆与检索增强生成（本篇转述）；本作在长对话预算约束下联动事实规范化、会话内合成和意图检索；表1—6支持实用增益，尚待排除实现与预算差异。", "soundness_observation": "经验结果较丰富，但无损性没有形式保证；实现口径和动态深度归因需要复核。", "significance_observation": "对长期对话问答的准确率与成本有实际价值，尚不足以证明持续终身运行能力。", "main_open_question": "同一记忆库、同样查询改写且匹配总预算时，自适应深度是否仍优于固定k？"}

limitations：[{"text": "无逐事实保真审计；被筛掉的内容可能对未来问题重要，semantic lossless应视为设计目标而非已证保证。", "basis": "model_inference", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p1摘要；p2 §2.1；p11 A.1。"}, {"text": "文本中的实现口径未完全对齐：正文采用ID并集去重，表7称score fusion；窗口20、stride 5却标注25%重叠。需对照原PDF和实现核读，不能自行修正。", "basis": "model_inference", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p4式6；p14表7。\n"}, {"text": "写入、规划和回答的总token未拆分；表7指定gpt-4.1-mini建库和复杂度估计，小模型实验是否全流程使用小模型不明。", "basis": "model_inference", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p4 §3.1；p6表3；p14表7。"}, {"text": "平均优势不代表所有任务均胜出，如GPT-4o的SingleHop落后全上下文。LongMemEval判分提示允许仅触及相同主题即判对，可能偏宽松，未见校准验证。", "basis": "model_inference", "locator": "TEXT_OR_oBgLvd5YC6_4eb778011acb：p5表1；p13 A.4。\n \n"}]

minimal_check：{"question": "动态检索深度是否具有独立收益？", "control": "固定建库结果和三路查询表达，仅比较自适应深度与固定k；在独立调参部分匹配检索token预算后测试。", "observable_outcome": "配对比较F1、完整查询token及延迟，检查固定k是否持平或占优。", "resources": "需LoCoMo、作者实现、同一记忆库及GPT-4.1-mini调用日志；实际费用和硬件需求未报告。", "failure_or_stop_condition": "等预算固定k持平或更优，则不支持动态深度的独立优势；无法对齐其余设置时停止因果归因。"}

missing_fields：["图1—3原图及可核查图形内容。", "写入合成完整提示词、更新规则及各实验实际阶段模型。", "分阶段token、硬件、并发、重复次数与方差。", "三路Top-n与最终检索总量的映射，以及消融固定深度设置。", "LongMemEval-S具体样本数和明确汇总口径；所列Adversarial Success Rate的实验结果。"]

本地有界核查：bounded_check_completed；阅读取舍：stop_after_first_pass

保留作为结构化记忆工程方案与资源比较案例；当前证据不足以支持无损压缩、动态深度独立优势或更高层级理论新颖性，暂不投入前作全文或复现预算。

身份、版本与阅读范围：题名、14 页当前官方附件、全文文本和 Pro 返回材料哈希一致。Pro 初评覆盖所供全部文本；本地检查所列页面并观察原 PDF 第 13、14 页。当前版本角色仍是 current_attachment_unverified_role。

核查定位：text_delivery_manifest.json, structured/pro027.json, p002:L0001；verified_with_scope_limit

中心机制和支持强度：正文三阶段为规范化事实压缩、会话内写入合成、意图驱动三路检索。式 5 对每一路 Top-n，式 6 为并集去重，不等于最终恰好 n 条。表 5 支持整套流程和组件移除差异，但没有逐事实保真审计或终身持续运行保证；语义无损属于设计主张。A.3 提供的是回答生成提示词，不能拿它当写入合成的完整实施规范。

核查定位：p002:L0018-L0058, p003:L0024-L0078, p004:L0003-L0040, p008:L0003-L0014, p011:L0010-L0057, p012:L0036-L0067；mechanism_confirmed_guarantees_limited

性能、token 和时间的比较口径：表 1 中 GPT-4.1-mini 平均 F1 为 43.24 对 Mem0 的 34.20，约 26.4% 是相对增幅、绝对差为 9.04；531 tokens 对全上下文 16910 的约 30 倍比较使用另一个基线。表 4 的建库/检索/总时间 92.6/388.3/480.9 秒明确是 LoCoMo-10 每样本平均，不能报成单个问题延迟；规划、建库和回答全阶段 token 开销未拆明。GPT-4o 单跳 F1 45.41 低于全上下文 61.56，平均优胜不等于逐项优胜。

核查定位：p005:L0003-L0028, p007:L0042-L0051；values_and_denominators_confirmed

动态深度归因与实现冲突：原 PDF 第 14 页表 6 确认固定 k=3/5/10 的 F1 为 42.85/43.24/43.45，而完整模型表 5 为 43.24；其余配置未充分对齐，不能独立证明动态深度优于固定 k。表 7 确实同时写窗口 20、stride 5、25% overlap；按通常滑窗定义应重叠 15/20=75%，保留原文冲突而不修改参数。表 7 score fusion 与正文并集去重的口径也仍待实现澄清。

核查定位：PDF physical page 14, Tables 6–7, p008:L0010-L0014, p004:L0026-L0032；source_inconsistency_and_attribution_gap_confirmed

LongMemEval 裁判范围：原 PDF 第 13 页评测提示确有宽松的同主题判对规则，时间题又要求同一日期或时间段；因此保留人工校准和裁判可靠性缺口。该提示是论文中的实验材料，不是本任务指令；没有据此断言全部成绩无效。

核查定位：PDF physical page 13, Appendix A.4 / Listing 4, p005:L0040-L0056；evaluation_protocol_confirmed_limit_retained

本地补充/限定：["本地原 PDF 确认 stride/overlap、score fusion 和宽松裁判提示均为源文内容，不是提取导致的错误。", "明确区分 F1 相对改进与百分点、不同 token 比较基线，以及每样本实验时间与单问延迟；固定 k 结果只约束独立归因，不反证完整系统收益。"]

核查局限：["没有执行作者实现、重算评测、访问外部记忆服务或开展新的模型调用。", "未核对所有表格汇总权重、统计误差和小模型各阶段实际使用的后台模型。", "未核读前作；L1 是暂定阅读判断，不代表历史创新已被穷尽。", "Pro 只读文本，本地只渲染两页；其他图形未逐一验证。"]


## pro028 · The Appeal and Reality of Recycling LoRAs with Adaptive Merging

论文 OR_eibIUtU11k；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_eibIUtU11k_4fa95dc533ce", "source_url": "https://api2.openreview.net/pdf?id=eibIUtU11k\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "4fa95dc533cef0a11d44b1d1ed832e47b247de8e73b10ba3b13c5890d7fc5511", "parent_pdf_source_id": "46da6bf614e8e886cecec31bdd0b76c6478a06abbcc396e6bc0fe74aa64d4495"}], "read_ranges": ["TEXT_OR_eibIUtU11k_4fa95dc533ce：物理页1–9，摘要及§1–7正文。", "TEXT_OR_eibIUtU11k_4fa95dc533ce：物理页10–15，致谢、影响声明及参考文献。", "TEXT_OR_eibIUtU11k_4fa95dc533ce：物理页16–27，附录A–H及图表提取文字；页标连续，未发现缺页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["仅阅读全文文本，未查看PDF图像；可使用明确提取出的表格数值，不能恢复曲线、热图、分布及误差条。", "双栏文字交错、分式排版失真；式(1)与式(3)的A/B乘法顺序不同，未自行纠正。", "未提供前作原文、代码、运行日志或其他版本；当前附件不认定为最终出版版。"]}

问题：少量目标任务标注下，融合公共异构LoRA能否比用相同数据新训练一个LoRA更有效？

方法：按选择、系数粒度、激活、优化四轴组织设计空间。Ours评价候选并取top-k，冻结LoRA权重，零初始化模块级系数，经Leaky ReLU后加权融合；用80个训练样本优化100步，以20个验证样本选系数，推理时折叠为单模型。

作者主张：大规模检验真实公共LoRA回收，发现相对基座的收益明显，但相对同数据目标LoRA收益有限。

论文证据：958个Llama LoRA、62任务的比较，并补充1956个Qwen LoRA；表2和表6a支持该趋势。

模型推断：中心增量是纠正评测基线与适用范围，而非证明融合无效或历史首次。

定位：['TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页5–6§4–5、Table 2；页22Table 6a。']

作者主张：含目标LoRA时，回收选择影响很小，收益可能更接近结构正则化；正迁移依赖高度相关来源。

论文证据：保持目标LoRA不变，随机重初始化池接近真实池；正文还报告in-house池更优，排除高分来源后收益下降。图6精确数值不可恢复。

模型推断：削弱了收益必然来自跨任务知识的解释，但尚未证明正则化因果；相关性与统一训练带来的兼容性未解耦。

定位：['TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页7–9§5 Q3–Q5、Figures 3–6。']

作者主张：通过设计空间搜索得到实用自适应融合配置。

论文证据：20任务消融比较粒度、选择、激活与优化；纳入目标LoRA后，多数配置差距缩小。

模型推断：属于已有组件的局部组合改进，不是新的融合原理。

定位：['TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页20–22附录E、Figures 10–12、Table 5。']

key_results：[{"setting": "Llama 3.1 8B-Instruct，62任务，100样本；均为作者报告。", "baseline": "Zero-shot prompting与同数据target-task LoRA。", "metric_or_guarantee": "跨任务平均accuracy，0–1。", "reported_values_and_units": "Prompting 0.467；目标LoRA 0.657；Ours不含/含目标LoRA为0.652/0.675。后者较目标LoRA增加1.8个百分点，并非完全没有收益。", "information_and_compute": "80训练＋20验证；k=30，选池需评价958个候选。系数100步、学习率0.05；目标LoRA rank=64，基线5种子。作者使用单L40或H100，训练步数存在下述冲突。", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页6Table 2、页18–19附录C。\n"}, {"setting": "Llama主设置，Figure 3中k=30的选择与重初始化对照。", "baseline": "目标LoRA单独使用为0.657。", "metric_or_guarantee": "平均accuracy，0–1。", "reported_values_and_units": "含目标LoRA：评价选池0.675、随机选真实LoRA 0.675、随机参数池0.672；不含目标LoRA：评价选池0.650、随机参数池0.609。另Figure 4列出的dropout=0.5基线为0.659，未匹配随机池融合收益。", "information_and_compute": "随机化不改变目标LoRA；真实与随机参数对照保留原A/B标准差。", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页7Figure 3、页8Figure 4表格文字。\n"}, {"setting": "Qwen3-4B-Instruct-2507，1956个公共LoRA，62任务，100样本。", "baseline": "Prompting 0.578；目标LoRA 0.668。", "metric_or_guarantee": "平均accuracy，0–1。", "reported_values_and_units": "Ours不含/含目标LoRA为0.657/0.681；k=30时目标LoRA＋随机参数池为0.684。", "information_and_compute": "沿用主实验框架，k=30；不能由这两个均值证明统计等价。", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页6§5、页22Table 6a、页23Figure 13a表格。\n"}, {"setting": "10样本、62任务消融；基础模型与主实验的对应口径待核。", "baseline": "表6b列Prompting 0.578、目标LoRA 0.546。", "metric_or_guarantee": "平均accuracy，0–1。", "reported_values_and_units": "Ours不含/含目标LoRA为0.578/0.566；LoraHub含目标LoRA为0.587。加入目标LoRA不再一致有益。", "information_and_compute": "无验证集；系数和目标LoRA均训练100步。", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页22Table 6b、§F.2，页23§F.2续文。\n"}]

prior_work_candidates：[{"citation_as_printed": "Huang, C., Liu, Q., Lin, B. Y., Pang, T., Du, C., and Lin, M. Lorahub: Efficient cross-task generalization via dynamic lora composition. In First Conference on Language Modeling, 2024.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "少样本优化静态LoRA组合系数。", "claimed_difference": "本作改用真实异构池，补充同数据目标LoRA及随机参数对照；LoraHub需补零对齐异秩。", "basis": "target_paper_only", "target_locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页3§2.3、页12参考文献、页19–20附录D。", "prior_actually_read": false}, {"citation_as_printed": "Wu, C., Wang, T., Ge, Y., Lu, Z., Zhou, R., Shan, Y., and Luo, P. pi-tuning: Transferring multimodal foundation models with optimal multi-task interpolation. In International Conference on Machine Learning, pp. 37713–37727. PMLR, 2023.", "identifier_if_present": null, "relation_candidate": "比较基线", "shared_component": "任务相似性选池及LoRA与系数联合优化。", "claimed_difference": "缺少来源训练数据，采用Quasi-FIM替代FIM；因显存限制选择20个LoRA，非原方法严格复现。", "basis": "target_paper_only", "target_locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页3§2.3、页15参考文献、页20附录D。", "prior_actually_read": false}, {"citation_as_printed": "Yang, E., Wang, Z., Shen, L., Liu, S., Guo, G., Wang, X., and Tao, D. Adamerging: Adaptive model merging for multi-task learning. In The Twelfth International Conference on Learning Representations, 2024.", "identifier_if_present": null, "relation_candidate": "组件复用", "shared_component": "梯度优化细粒度融合系数。", "claimed_difference": "本作配置采用评价选池、Leaky ReLU及零初始化。", "basis": "target_paper_only", "target_locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页3Table 1、页15参考文献、页19§C.1。", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "真实池、强基线及随机化反事实提供了实质性经验认识；算法增量较局部，不足以据此判路线级L3。", "central_increment": "前作在受控池上实现融合迁移（本篇转述）；本作在真实异构池与同标注预算下发现，多数收益被目标LoRA吸收，随机参数亦可接近真实池；证据为表2、图3及Qwen补充实验，尚待排除额外目标适配混杂。", "soundness_observation": "多组对照支持有限范围内的结论，但文本未给核心差值置信区间；正则化解释仍属假说，未复现实验。", "significance_observation": "主要价值是改进回收研究的基线与评测方式；不意味着所有任务、池或动态路由方法均无正迁移。", "main_open_question": "排除目标LoRA额外模块重标定并匹配优化预算后，真实池与随机池是否仍表现接近？"}

limitations：[{"text": "公共训练元数据稀疏，难区分任务不相关、训练不兼容与选择失败；作者亦承认更好的选择方法仍可能有效。", "basis": "author_report", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页9§7。"}, {"text": "同数据不等于同计算。Table 3称目标LoRA训练100步，§C.2却写400步；含目标LoRA的融合还增加系数适配。§F.1所称相同π-Tuning学习率也与§C.1的第二个学习率不同，不能静默统一。", "basis": "model_inference", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页18Table 3、页19§C.1–C.2、页22§F.1。\n"}, {"text": "§3称评价选池使用训练集，§B.1则写100个样本；选择与验证的隔离口径不清。20任务设计搜索也未交代独立外层评测，不能据此直接认定测试泄漏。", "basis": "model_inference", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页3§3、页16§B.1、页20附录E。"}, {"text": "10样本组称重跑§5，但其Prompting为0.578，主Llama表为0.467，基础模型或基线口径需核对；改版π-Tuning等结果不能直接泛化为原方法普遍失效。", "basis": "model_inference", "locator": "TEXT_OR_eibIUtU11k_4fa95dc533ce，物理页6Table 2、页20附录D、页22Table 6及§F.2。"}]

minimal_check：{"question": "仅重标定目标LoRA是否已能复现随机池融合收益？", "control": "预先固定少量任务、目标LoRA和80/20划分，比较仅训练其模块系数、加入29个匹配随机LoRA、加入29个真实LoRA；均追加100步并采用相同验证规则及配对种子。", "observable_outcome": "独立测试集上的任务与种子配对accuracy差值及区间。", "resources": "对应权重和数据；参考作者单L40/H100配置，实际显存、工时未报告。", "failure_or_stop_condition": "若仅重标定已匹配随机池收益，则不能将该增益归因于新增随机方向的正则化作用。"}

missing_fields：["图6及其他未表列图形的精确数值、分布和误差条不可读。", "未报告端到端GPU时长、峰值显存、总搜索成本及完整配对统计。", "训练步数、π-Tuning学习率、选池数据划分及10样本组模型口径存在待核项。", "三篇候选参考条目未列独立DOI/arXiv标识；前作原文未提供。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

强目标基线与随机参数对照实质改变了知识回收增益的解释，值得继续核对逐任务配对结果和仅重标定目标 LoRA 的对照；当前不自动开展实验。

身份、版本与覆盖：题名、27 页官方当前附件、全文材料哈希及 Pro 返回绑定一致。Pro 阅读所有提供页面；本地围绕核心比较和实施预算核看列出的页面，并观察原 PDF 第 7、18、19 页。没有核读前作或下载适配器权重。

核查定位：text_delivery_manifest.json, structured/pro028.json, p003:L0001；verified_with_scope_limit

核心比较需要强基线：表 2 确认 Llama 62 任务平均准确率：零样本 0.467、同 100 条目标数据训练的 LoRA 0.657、Ours 不含/含目标 LoRA 为 0.652/0.675。后者仍比目标 LoRA 高 1.8 个百分点，不能概括为融合无收益。框架主要研究静态融合系数；按 token 或样本动态路由不属于同一个覆盖范围。

核查定位：p006:L0026-L0073, p003:L0018-L0034；central_values_and_domain_confirmed

随机池对照真正固定的对象：原 PDF 第 7 页图 3 与正文明确保留目标 LoRA 不变，随机化其他 A/B，分别匹配原矩阵标准差。k=30 含目标 LoRA：真实评价选池 0.675、随机真实选池 0.675、随机参数池 0.672；不含目标 LoRA：真实评价选池 0.650、随机参数池 0.609。只有保留目标模型的条件下才接近，不能读成随机权重普遍替代已学知识。均值接近不是统计等价，额外目标模块系数重标定也尚未隔离。

核查定位：PDF physical page 7, Figure 3 and Q3, p008:L0019-L0041；counterfactual_scope_confirmed

同标注预算不等于同训练与搜索开销：原 PDF 第 18 页表 3 把 target-task LoRA 列为 100 步，第 19 页 C.2 却明确写 rank 64、400 步；这是原文冲突，未自行选择一个值。Ours 还要评价全部 K 候选并追加 100 步融合系数训练，80/20 选参。因此同样 100 条标注并未建立端到端等算力比较。C.1 π-Tuning 的第二学习率 5e-5 与 F.1 所称同配方的 1e-5 也未对齐。

核查定位：PDF physical page 18, Table 3 and C.1, PDF physical page 19, C.1–C.2, p022:L0045-L0055；resource_scope_and_source_conflict_confirmed

跨设置结果与例外：Qwen 表 6a 的目标 LoRA 0.668、Ours 含目标 0.681，图 13a 随机参数加目标为 0.684，支持接近趋势而非唯一方法获胜。10 样本表 6b 的 Ours 不含/含目标 0.578/0.566，加入弱目标 LoRA 并非总有益；该组零样本 0.578 与主 Llama 表 0.467 的口径仍待澄清，不能自行指认模型或数据泄漏。

核查定位：p022:L0014-L0034, p022:L0063-L0067, p023:L0019-L0039；replication_scope_and_exception_retained

本地补充/限定：["确认原 PDF 中训练步数 100/400 的冲突；保留为未澄清实施口径，未改写真实实验配置。", "强调随机池接近真实池以目标 LoRA 保持不变为前提，不能延伸为所有模型融合无用或已证明正则化机制。"]

核查局限：["没有核验所有任务、候选池元数据、图 6 精确数值或统计等价。", "未执行作者代码、下载权重或重跑融合；机制解释仍为假说。", "未完整检查式 1/3 的矩阵顺序和全部实现改造；未核读被比较前作。", "Pro 仅看文本，本地仅观察三个渲染页；L2 保持 AI 暂评。"]


## pro029 · Monitoring Monitorability

论文 OR_b82fgbMVpz；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_b82fgbMVpz_66752bfc1a12", "source_url": "https://api2.openreview.net/pdf?id=b82fgbMVpz\n", "version_role": "current_attachment_unverified_role", "source_pdf_sha256": "66752bfc1a123fa189578cf0f288aa4571844a8dc765a86575afbc8cb2cd72d6"}], "read_ranges": ["TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页1–9，正文§1–8。", "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页10–12，致谢、影响声明及参考文献。", "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页13–65，附录A–J，包括全部可见提示词、示例和图题；1–65页标连续。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["只读到全文提取文本，未见PDF图像；图1–34绘图区、曲线数值和误差条不可核读。", "双栏文本存在交错，部分公式符号和表格排版有损；表2–4主要文字可辨。", "未提供前作全文、其他版本、原始实验数据或代码；未搜索、复现或执行论文指令，未确认最终出版版本身份。"]}

问题：如何测量监控器从模型轨迹中识别行为属性的能力，并追踪其随训练、计算预算及追问而发生的变化？

方法：比较CoT-only、Action-only和All-messages监控。干预双臂估计TE，令Reffect=TE/P(Y=1|X=1)、p=P(Z=1|X=1,Y=1)，以min(1,p/Reffect)乘√(TNR0·TNR1)评分；过程评估仅纳入正确解并置TNR=1；结果属性由执行结果或裁判标注。采用分层bootstrap和图内共同筛选。

作者主张：提出干预、过程和结果属性三类评估及可比较的监控指标。

论文证据：提供164道专家标注过程题、864条干预退化评估数据，并用混淆RL检验套件能否发现退化。

模型推断：实质增量在可操作的测量与诊断体系，而非首次提出CoT监控或g-mean。

定位：['TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页38，表4。\n', 'TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页43，附录F.2；物理页46–56，附录H。\n']

作者主张：CoT、代理推理预算及监控器能力影响可监控性，存在monitorability tax。

论文证据：文字报告CoT通常优于仅动作；匹配能力时，小模型配长推理往往更可监控，但总推理计算更高。

模型推断：提供预算配置的新实证认识，尚非普适缩放定律。

定位：['TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页6–8，§4–5、图4–5对应正文。']

作者主张：追问原代理并监控新增CoT可提高可监控性。

论文证据：多次通用追问接近单次定制追问；新增CoT通常比仅新增答案有用，但Scruples及部分模型效果较差。

模型推断：属于有价值的局部增强，不证明追问准确恢复了原始决策原因。

定位：['TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页8，§6；物理页58–65，附录J。']

key_results：[{"setting": "固定GPT-5 Thinking代理，提升o4-mini监控器的reasoning effort。", "baseline": "最低effort；同时比较CoT与仅动作观测。", "metric_or_guarantee": "g-mean²变化", "reported_values_and_units": "最低到最高effort：可见CoT约提升12%，仅动作约提升4%；原文未明确是相对百分比还是百分点。", "information_and_compute": "报告effort变化，未提供对应绝对FLOPs或费用。", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页7，§5.2。\n"}, {"setting": "不同预训练规模模型，经数学、科学和代码RL后比较。", "baseline": "较大模型、较低推理effort；分别匹配能力或计算预算。", "metric_or_guarantee": "可监控性—能力—推理计算权衡", "reported_values_and_units": "最大模型预训练计算超过最小模型100倍；具体可监控性增益和能力损失无法从缺失绘图区读取。", "information_and_compute": "每规模一个seed；推理计算定义为FLOPs/token×生成tokens；未计延迟。", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页7–8，§5.1、图4。\n"}, {"setting": "GPT-5 Thinking、o3、o3-mini和o4-mini的追问实验。", "baseline": "重建日志后重新运行的不追问监控，以及仅提供追问答案的监控。", "metric_or_guarantee": "g-mean²", "reported_values_and_units": null, "information_and_compute": "多追问版本为同一追问的10次独立续写；新增生成和监控成本未量化。", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页58，附录J.1；物理页61–65，图30–34。\n"}, {"setting": "o4-mini规模模型的定向CoT混淆RL，Coding-impossible-tasks的solution length子集。", "baseline": "标准RL对照；正文召回变化未逐点标明训练检查点。", "metric_or_guarantee": "监控召回率", "reported_values_and_units": "作者报告召回率从0.85降至0.70。", "information_and_compute": "属于两项主混淆训练之一；无广泛消融，绝对训练预算未报告。", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页46，附录H；物理页50，H.1。\n"}]

prior_work_candidates：[{"citation_as_printed": "Baker, B., Huizinga, J., Gao, L., Dou, Z., Guan, M. Y., Madry, A., Zaremba, W., Pachocki, J., and Farhi, D. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. arXiv preprint arXiv:2503.11926, 2025.", "identifier_if_present": "arXiv:2503.11926", "relation_candidate": "方法继承", "shared_component": "CoT恶行监控及混淆训练压力。", "claimed_difference": "扩展为跨原型测量、计算预算分析和追问实验。", "basis": "target_paper_only", "target_locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页1、8–9，§1、7；物理页10，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Chen, Y., Benton, J., Radhakrishnan, A., Uesato, J., Denison, C., Schulman, J., Somani, A., Hase, P., Wagner, M., Roger, F., Mikulik, V., Bowman, S. R., Leike, J., Kaplan, J., and Perez, E. Reasoning models don’t always say what they think, 2025.", "identifier_if_present": "arXiv:2505.05410", "relation_candidate": "方法继承", "shared_component": "通过提示答案干预检测未被CoT表达的影响。", "claimed_difference": "纳入随机采样、最低归因标准及更自然的干预。", "basis": "target_paper_only", "target_locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页3–4，§3.1；物理页10，参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Kutasov, J., Sun, Y., Colognese, P., van der Weij, T., Petrini, L., Zhang, C. B. C., Hughes, J., Deng, X., Sleight, H., Tracy, T., et al. Shade-arena: Evaluating sabotage and monitoring in llm agents. arXiv preprint arXiv:2506.15740, 2025.", "identifier_if_present": "arXiv:2506.15740", "relation_candidate": "组件复用", "shared_component": "正常任务与恶意侧任务配对环境。", "claimed_difference": "复用其中14个环境比较观测范围，并另建真实代码库破坏任务。", "basis": "target_paper_only", "target_locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页6、28–31，§3.3、D.3.2；物理页11，参考文献。\n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是实质性的测量方法与计算配置知识，超出单一基准性能改进；不足以据此确认路线级首创。", "central_increment": "前作已用CoT检测奖励黑客和提示影响（本篇转述）；本作新增随机干预指标、综合套件及预算/追问证据，尚待排除代理指标和筛选策略造成的高估。", "soundness_observation": "分层bootstrap和退化对照有价值，但指标不等于真实因果召回，部分协议存在文内歧义；本轮未复现。", "significance_observation": "可为训练及部署提供监控回归测试，不构成CoT忠实性或系统安全保证。", "main_open_question": "校正各原型随机基准后，该分数是否仍支持不同模型监控能力的可靠比较？"}

limitations：[{"text": "每规模单seed、能力评估限于分布内且未计延迟；主监控器来自OpenAI，可能存在同源偏差；人工退化负例也可能留下分布特征。", "basis": "author_report", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页6–7，§4–5；物理页44–46，F.4。"}, {"text": "ShadeArena和OAI-repo-sabotage剔除有侧任务指令但未判阳性的样本；跨图纳入集合不同，且未按部署低误报率校准，不能直接外推真实告警表现。", "basis": "model_inference", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页17，附录C；物理页28、30，D.3.1–D.3.2。\n"}, {"text": "图1称随机监控器基准为0.25，但依本文定义，公平随机监控器在过程评估中的总体分数为0.5，干预分数还依赖Reffect及负例支持；统一随机基准需核查。", "basis": "model_inference", "locator": "TEXT_OR_b82fgbMVpz_66752bfc1a12：物理页2，图1图题；物理页4，式(3)–(5)；物理页5，§3.2。\n"}]

minimal_check：{"question": "统一0.25随机基准是否适用于该混合套件？", "control": "固定图内纳入实例，以独立公平随机预测替换监控器输出，按三类原公式及聚合规则评分。", "observable_outcome": "分原型随机分数、原监控器超随机增益，以及校正前后的跨模型排序。", "resources": "原始双臂标签、监控日志与指标实现；仅需离线重算，不需训练，具体运行成本未知。", "failure_or_stop_condition": "若排序主要依赖原型基准或Reffect差异，需收窄可比性主张；无原始日志则停止实证重算。"}

missing_fields：["图中完整分数、误差条及追问实验的具体增益。", "各环境完整有效实例数、重复采样数、绝对训练/推理算量、GPU时和费用。", "跨模型采样配置：G.1写GPT-5/o3使用medium，图20–21图题写maximum，未能消解。", "Anti-scheming实际数据集数：正文写5，D.3.4写6。", "H.1所列定向提示未明确体现H节声称的三个目标主题，定向奖励配置无法完整复原。"]

本地有界核查：bounded_check_completed；阅读取舍：read_further

三类测量框架与计算权衡有实用研究价值；后续应优先核实各原型随机基准、低误报部署指标和固定实例集比较，而非直接引用聚合分数为安全保证。

身份与材料范围：题名、官方当前 PDF、65 页全文清单及 Pro 返回哈希一致。Pro 一轮初评覆盖全部提供文本；本地检查所列方法与预算页，并观察原 PDF 第 2、4、5 页。第 38、43、50 页的 164/864/0.85→0.7 只做关键词定位，不计为整页阅读或数值复核。

核查定位：text_delivery_manifest.json, structured/pro029.json, p001:L0001；verified_with_explicit_read_scope

中心测量对象及原公式：论文明确区分可监控性与完整 CoT 忠实性。原 PDF 第 4 页确认 Reffect=TE/Pr(Y=1|X=1)，TPRmc=min(1,p/Reffect)，干预分数再乘 sqrt(TNR0*TNR1)；其评价触发是否达到最低可归因比例，未获得逐轨迹真实因果标签。TE≤0 的实例排除，空负例支持另有约定，因此不是普通二分类召回率。

核查定位：p001:L0009-L0039, p002:L0047-L0069, PDF physical page 4, equations 1–5, p017:L0007-L0021；metric_definition_confirmed

随机基准的有限解析核查：原 PDF 第 2 页图 1 图注确写随机监控器为 0.25；第 5 页却对过程题只保留正确答案、令 TNR=1。将独立公平二元随机预测代入总体概率公式，过程分数为 0.5；干预两类负例支持非空时为 0.5*min(1,0.5/Reffect)，Reffect=1 时为 0.25、Reffect≤0.5 时为 0.5。故统一 0.25 不适用于所有原型的这些定义。这里只做公式代入，没有原始日志重算；有限样本截断偏差、空支持约定和聚合权重仍会影响实际随机得分，不能据此宣布已校正图中排名。

核查定位：PDF physical page 2, Figure 1 caption, PDF physical page 4, equations 3–5, PDF physical page 5, §3.2, p017:L0014-L0021, p017:L0053-L0062；population_formula_baseline_mismatch_confirmed_not_empirical_reproduction

计算权衡与可比性边界：§5.2 确实报告弱监控器有 CoT 时约 12%、仅动作约 4% 的改善，但未在该段明确相对百分比还是百分点，保留原口径。每个预训练规模只有一个 seed，能力来自分布内数学/科学/代码，推理计算定义为 FLOPs/token×生成 token 且未计延迟。附录 C 的图内共同剔除策略不保证跨图绝对值可比；bootstrap 同时重采实例与实例内轨迹，不能把所有轨迹视作独立样本。

核查定位：p007:L0026-L0055, p008:L0007-L0011, p013:L0013-L0051, p017:L0023-L0058；reported_effect_and_resource_scope_confirmed

追加追问的实际协议：附录 J.1 是从日志重建对话，同一追问抽取十个独立续写，并非十轮连续追问；工具环境未完整恢复，基线重新运行。新增 CoT 的帮助不等于恢复原始决策真实原因，且新增生成与监控预算未等额控制。正文还保留 Scruples 下降和模型差异，不能说追问普遍提高可监控性。

核查定位：p058:L0007-L0034, p008:L0021-L0041；protocol_and_exception_confirmed

本地补充/限定：["把 Pro 对随机基准的疑问推进为有明确假设的总体概率公式代入结论，保留实际有限样本分数与排序尚未重算。", "不把图 1 随机线问题扩大为整个监控方案无效，也不把 TPRmc 当作真实个体因果召回。"]

核查局限：["没有运行监控器、恶意任务、训练、作者代码或原始日志重算。", "未核读全部附录案例和所有图形，也未验证全部人数、数据量或退化曲线。", "没有核读引用前作或确定历史首创，L2 为 AI 暂评。", "Pro 仅读全文文本，本地只观察三个 PDF 页面；公式核查不是完整证明或部署安全审计。"]


## pro030 · Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning

论文 OR_9hzK071Z3R；暂定 L2；medium。

阅读范围：{"visible_sources": [{"source_id": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce", "source_url": "https://api2.openreview.net/pdf?id=9hzK071Z3R\n", "version_role": "current_attachment_unverified_role"}], "read_ranges": ["TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页1–22全部已读，连续无缺页标；正文及声明为1–9页，参考文献为10–12页，附录A–C为13–22页。"], "material_form": "full_text", "figures_visible": false, "missing_or_unreadable": ["图1–12仅有图题及正文转述，曲线、散点、热图及其中数值不可见；不能独立核读注意力和D2A相关图。", "双栏文本顺序交错，部分公式尤其式(9)、(11)排版失真，未据此重建精确代数形式；表格文字可读。", "未提供前作全文、其他版本、代码、检查点或原始实验记录；不认定当前附件为最终出版版。"]}

问题：没有监控奖励的RLVR何时提升CoT可监控性？这种提升与能力、训练数据及内部行为有何关系？

方法：对已完成长CoT冷启动的DS-1.5B和Qwen3-4B进行GRPO，输入题目、输出草稿与答案；奖励为任务正确性加0.1倍格式奖励。数学、代码、IF各5000条，科学3600条。用提示干预和外部监控器测g-mean2，并跟踪能力、逐token熵、段间注意力及D2A。

作者主张：可监控性增益依赖数据分布；IF及多域训练更有效，任务能力提升并不保证可监控性提高。

论文证据：等更新预算下，表3的+IF相对w/o IF提高0.09和0.06；正文报告能力与监控指标的相关方向随模型、任务变化。

模型推断：新增价值是限定free gift的训练条件并提供IF级联策略，而不是首次发现该现象；不支持将orthogonality理解为严格统计独立。

定位：['TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页3–6，§3.1、§4，表3。\n']

作者主张：监控增益主要联系到分布收尖及面向Prompt的注意力，而非更强的Answer→Reasoning依赖；探索后收尖优于过早塌缩。

论文证据：表4提供clipping切换实验；表8显示困难数据降熵更快却监控更差。注意力与D2A的相关结论有正文叙述，但图内数据不可见。

模型推断：支持低熵并非充分条件及训练路径重要这一条件性认识；尚不能确立熵或注意力变化的独立因果作用。

定位：['TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页6–8，§5–6；物理页20，表8。\n \n']

key_results：[{"setting": "两主模型的matched-data IF比较，各800步；+IF为400步w/o IF后接400步IF。", "baseline": "IF、ALL、w/o IF，与+IF比较；不是未训练基座分数。", "metric_or_guarantee": "作者报告的峰值平均g-mean2，无量纲；±的统计含义未说明。", "reported_values_and_units": "按IF/ALL/w/o IF/+IF顺序：Qwen3-4B为0.60±0.02/0.63±0.02/0.54±0.03/0.63±0.02；DS-1.5B为0.39±0.02/0.50±0.02/0.42±0.02/0.48±0.02。", "information_and_compute": "全局batch128，每题16个rollout，训练输出上限4096、温度1.0；监控评测输出上限8192、温度0.6、top-p 0.95。硬件和时长未报。", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页5，表3；物理页13，A.2、B.1。\n \n"}, {"setting": "DS-1.5B训练800步；High Ent使用上clip 0.28，Collapse在400步后切回0.2。", "baseline": "始终采用标准clipping或始终采用较高clipping。", "metric_or_guarantee": "最终g-mean2与平均token熵；熵单位未注明。", "reported_values_and_units": "Math的Standard/High Ent/Collapse分别为0.36(0.71)/0.34(0.87)/0.38(0.77)；IF分别为0.39(0.71)/0.33(0.80)/0.37(0.70)。括号内为熵；Collapse并非均优于Standard。", "information_and_compute": "数据和奖励不变，从高熵400步检查点分支；未报告跨训练种子的差值不确定性。", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页7，表4。\n"}, {"setting": "DS-1.5B在固定数学数据上训练400步，改变训练输出上限。", "baseline": "4096 tokens。", "metric_or_guarantee": "总体g-mean2及能力汇总分。", "reported_values_and_units": "4096/6144/8192 tokens对应g-mean2为0.36/0.34/0.29，能力分为39.73/41.41/41.05；能力分原表未注明单位。", "information_and_compute": "更新步数相同，但训练生成预算不同；能力评测中的代码生成另用16384 tokens和16次采样。", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页8，表5；物理页22，表11。\n \n"}, {"setting": "DS-1.5B数学训练难度消融，400步。", "baseline": "Medium混合难度。", "metric_or_guarantee": "g-mean2及平均token熵。", "reported_values_and_units": "Easy/Medium/Hard分别为0.39(0.77)/0.36(0.78)/0.21(0.72)；困难训练的熵最低但监控分最低。", "information_and_compute": "难度依据16次生成的正确次数划分；额外准备Easy和Hard各5000条，硬件成本未报。", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页9，§7；物理页20，表8。\n"}]

prior_work_candidates：[{"citation_as_printed": "Guan, M. Y., Wang, M., Carroll, M., Dou, Z., Wei, A. Y., Williams, M., Arnav, B., Huizinga, J., Kivlichan, I., Glaese, M., et al. Monitoring monitorability. arXiv preprint arXiv:2512.18311, 2025.", "identifier_if_present": "arXiv:2512.18311", "relation_candidate": "方法继承", "shared_component": "g-mean2、提示干预、Sycophancy与Sandbagging评测。", "claimed_difference": "本篇新增实践训练域比较、IF级联与训练期长度消融，而非仅研究推理期长度。", "basis": "target_paper_only", "target_locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页3、8、10，§3、§7及参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "Chen, Y., Benton, J., Radhakrishnan, A., Uesato, J., Denison, C., Schulman, J., Somani, A., Hase, P., Wagner, M., Roger, F., et al. Reasoning models don’t always say what they think. arXiv preprint arXiv:2505.05410, 2025a.", "identifier_if_present": "arXiv:2505.05410", "relation_candidate": "方法继承", "shared_component": "提示影响是否在CoT中被承认的干预评估，以及早期RLVR监控增益现象。", "claimed_difference": "本篇强调多训练域、匹配预算及机制消融。", "basis": "target_paper_only", "target_locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页1–3及10，§1–3与参考文献。\n", "prior_actually_read": false}, {"citation_as_printed": "MacDermott, M., Wei, Q., Djoneva, R., and Ward, F. R. Reasoning under pressure: How do training incentives influence chain-of-thought monitorability? arXiv preprint arXiv:2512.00218, 2025.", "identifier_if_present": "arXiv:2512.00218", "relation_candidate": "背景引用", "shared_component": "RL训练配置与CoT可监控性的受控实验。", "claimed_difference": "本篇将前作概括为长度惩罚、KL等训练变体研究，自身关注实践数据分布、泛化和内部机制；未核实这一覆盖边界。", "basis": "target_paper_only", "target_locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页2，§2；物理页11，参考文献。\n \n", "prior_actually_read": false}]

assessment：{"ai_verdict": "L2", "confidence": "medium", "reason": "中心增量是可监控性形成条件的实证新知识，而非新算法或路线级框架；等步数比较与反例消融超过单纯复述既有现象。", "central_increment": "前作已观察free gift并提供评测工具（仅本篇转述）；本作在无监控奖励GRPO下增加IF级联和熵轨迹、长度、难度边界，证据为表3–6、8；尚待排除指标与提示服从性的混淆。", "soundness_observation": "附录补充双监控器、提示类型及Llama-8B检查，增强部分稳健性；机制因果识别仍弱，且正文存在与表格不一致的优越性表述。\n \n", "significance_observation": "可指导RLVR数据配置和阶段切换，但不构成安全或真实推理忠实性的保证；工程上涉及多检查点训练与大监控器评测，成本未量化。", "main_open_question": "固定评测样本并排除提示服从和末句复述后，IF增益是否仍对应模型自身CoT对答案更强的因果作用？"}

limitations：[{"text": "作者承认注意力变化不证明真实信息整合，输入干预可能产生虚假的可监控感；DS-1.5B部分通用任务的D2A与g-mean2并不一致。", "basis": "author_report", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页8，§5.2–6。\n"}, {"text": "D2A使用外部生成或既有草稿并改写结论，可能测到草稿服从；Draft Reliance的两种回答协议输出相等，也不能单独证明答案由草稿决定。", "basis": "model_inference", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页8，§6；物理页18，B.8。\n \n"}, {"text": "按TE跳题和过滤测试集，可能使不同检查点的评分样本组成变化；峰值选择、少量采样以及未说明的种子数和±定义限制差异解释。", "basis": "model_inference", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页5，表3；物理页15，B.2。\n"}, {"text": "正文称+IF超过ALL，但表3中Qwen3-4B只是持平，DS-1.5B则为0.48低于0.50；只支持相对w/o IF的提升。", "basis": "model_inference", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页5，表3及§4.1。\n \n"}, {"text": "B.1称提示干预的无干预对照采样8次，B.2却称4次；MedQA的200条抽样与表1的184条关系未说明，不自行调和。", "basis": "model_inference", "locator": "TEXT_OR_9hzK071Z3R_8a7ac7d0a7ce：物理页3表1、13 B.1、14 B.2。\n \n \n"}]

minimal_check：{"question": "IF级联是否提升对自身推理内容的因果依赖，而不仅是提示影响的显式承认？", "control": "比较800步w/o IF与+IF检查点，固定GPQA子集及解码条件；对各自生成的草稿进行关键推理反事实改写，对照原稿和等长无关措辞改写，避免直接植入目标答案。", "observable_outcome": "比较答案对关键推理改写的特异性响应，以及该差异是否与g-mean2增益一致。", "resources": "两个检查点、固定题集、逐样本草稿与重复推理资源；检查点未提供，显存和运行时长未知。", "failure_or_stop_condition": "若增益仅体现提示承认或结论复述，不支持更强因果忠实性的解释；检查点不可得则无法执行。"}

missing_fields：["图1–12的图内数值、D2A完整数值及部分公式原始排版。", "训练种子数、表3误差条含义、匹配数据流具体组成及关键增益的重复实验统计。", "训练与评测硬件、时长、总token和费用；表11能力分单位。", "对照采样数与MedQA最终样本数口径；前作全文、代码和原始实验记录。"]

本地有界核查：bounded_check_completed；阅读取舍：read_with_specific_question

可保留 IF 数据与训练路径的条件性经验知识，进一步阅读应检查固定评测实例集、等总生成预算、训练重复数和不植入答案的草稿干预。

身份、版本与阅读范围：题名、22 页官方当前附件、全文哈希和 Pro 返回绑定一致。Pro 初评覆盖全部提供文本；本地只核看列出的页和三个 PDF 渲染页。Monitoring Monitorability 同时入选本阶段且已有独立初评与有限核查，这一项目级交叉阅读不回写为本篇 Pro 已核读前作。

核查定位：text_delivery_manifest.json, structured/pro030.json, p003:L0001, pro/OR_b82fgbMVpz/bounded_local_check.json；verified_with_cross_paper_scope_distinction

核心训练干预、预算与数据：两主模型已具备长 CoT 冷启动。IF、ALL、w/o IF 各 800 更新步，+IF 为 400 步 w/o IF 再加 400 步 IF；同更新步数不等于同 token、验证成本或 FLOPs。奖励 Rtask+0.1Rformat 含显式推理格式项，只能说没有直接监控分数奖励，不能说完全无过程格式约束。训练输出上限 4096，监控评测 8192，代码能力评测还另用 16384 与 16 次采样。

核查定位：p003:L0027-L0055, p013:L0005-L0033, p013:L0044-L0053；training_information_and_resource_scope_confirmed

表 3 的实际增益与正文冲突：原 PDF 第 5 页表 3 是峰值平均 g-mean²，+IF 对 w/o IF 为 Qwen 0.63−0.54=0.09、DS 0.48−0.42=0.06。但 +IF 相对 ALL 为 0.63=0.63 和 0.48<0.50，正文声称超过 ALL 不受该表支持。保留峰值选择与 ± 含义未说明的局限，不把该表改写为统一终点或显著性证明。

核查定位：PDF physical page 5, Table 3 and IF booster paragraph；values_and_source_overstatement_confirmed

熵机制的关键反例：原 PDF 第 7 页表 4：Math 800 步 Standard/High Ent/Collapse 为 0.36/0.34/0.38，IF 为 0.39/0.33/0.37；切换策略并非在两域都优于 Standard。第 20 页表 8 的 Hard 熵最低 0.72、监控也最低 0.21，相比 Easy 的 0.77/0.39 和 Medium 的 0.78/0.36，约束了低熵充分性的解释。改变 clipping 同时改变优化轨迹，注意力相关图不能独立确定因果方向。

核查定位：PDF physical page 7, Table 4 and Figure 5, PDF physical page 20, Table 8, p008:L0019-L0042；conditional_mechanism_claim_confirmed

指标、D2A 与因果忠实性：附录 B.2 沿用 Reffect 归一化及两臂 TNR，按 TE 排除实例并过滤测试集；该条件分数不是模型内在独立于监控器的保证。D2A 部分草稿来自更强模型或既有数据，改写末尾结论；两种回答协议输出相同也可发生于模型都忽略草稿，故不能仅凭 Draft Reliance=1 断定草稿完全决定答案。B.1 的无干预采样 8 次与 B.2 的 4 次确有文本冲突，仍待实施澄清。

核查定位：p003:L0003-L0005, p013:L0044-L0047, p014:L0003-L0013, p015:L0010-L0039, p008:L0043-L0069, p018:L0022-L0045；measurement_and_causal_interpretation_qualified

本地补充/限定：["原 PDF 确认 +IF 超过 ALL 的文字与表 3 不符，及 Collapse 在 IF 上低于 Standard 的例外。", "补充说明训练含 0.1 格式奖励；无监控奖励不等于没有任何推理格式约束。", "把 Draft Reliance 输出相等不能推出因果决定的逻辑局限明确保留，没有对实际模型构造或执行新的反例实验。"]

核查局限：["未执行训练、评测、作者提示或代码；未取得原始生成与检查点。", "未核看全部 D2A、注意力或能力曲线，也未复算统计显著性。", "其他引用前作未独立核读；同阶段相邻论文的比较仅覆盖各自已核查的范围。", "Pro 仅看全文文本，本地只观察三页 PDF；L2 仍为 AI 暂评。"]

