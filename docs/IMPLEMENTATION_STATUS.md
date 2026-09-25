# 当前实现状态（2026-09-25 本地 PDF 接收检查点）

最新完整离线验收 135 项：133 通过、2 跳过、0 失败。新增 11 项本地 PDF 接收
测试；四个既有实际强制终止/新进程恢复案例仍通过。`import-paper --help` 已实测。
接收限定 `exchange/manual_intake/<name>.pdf`，校验活动任务、代码/规则、精确
OpenReview 链接、文件上限、磁盘预留、路径/硬链接和复制期间变动；无联网、扫描
私人目录或删除用户原件。回执保留手动来源声明，入库版本与已读状态仍待核验。
中断回执也保留这些限制，格式通过不构成身份或科学验收。
首轮测试发现 Windows stat/fstat 的 ctime 差异，修正后 30 次重复检查通过，随后
运行完整套件。未新增依赖。说明见 MANUAL_PDF_INTAKE.md。

OpenReview 浏览器登录现已确认，本地原始投稿 PDF 请求仍为 HTTP 403。
浏览器下载未成功已由用户确认。下一任务 acquire_005 待真实文件后新建，
真实论文闭环仍为零。下方 124/117/91 项与待审核账号描述均属于历史。

前次完整离线验收 124 项：122 通过、2 跳过、0 失败。新增七项镜像/预印本测试。
预印本来源角色已实现；两个逐条核实的公开镜像 URL 使用原有保护下载路径，
无整站放行。无效角色在联网前拒绝，镜像不能标作原稿/定稿。规则未变，代码哈希
已重新绑定验收。下方 117/91 项属于先前实现历史。
网页检索服务可读取首篇的 70 页 PDF；本机 alphaXiv robots 拒绝、ResearchGate
HTTP 403，均未取得正文。详见 PUBLIC_SOURCE_ROUTES.md。P2 仍为零篇闭环，
下一任务 P2_J4wRLmh29t_acquire_004 需新的实际可用来源或访问变化。

G0-02 已新增 export-pro/import-pro：不可变证据包、waiting_external 无租约等待、
哈希命名隔离回传、300 秒本地验证 attempt、版本/来源/定位检查、幂等接收及同步回执。
结构通过仅为 awaiting_fact_check，不登记为论文验收结果。真实 Pro 合成往返已完成，格式与合成事实分别检查；人类审计未做。
协议见 contracts/pro_exchange.md。原 AGENTS.md 未改。

此前元数据入口版本完整离线套件 117 项：115 通过、2 跳过、0 失败；21 项交换测试和 5 项元数据保护测试，
共 4 项实际终止子进程后的新进程恢复。验收绑定见本地 state/offline_acceptance.json。
下方 91 项记录是修改前历史，不是当前实现的验收。

发布基线只包含活动源代码/测试及复用 V2 helper；旧十篇和示意图保留本地，
不作为本轮已核实数据发布。克隆后的活动测试入口：
`tools/python-project.cmd tools/run_offline_tests.py --active-only`。
完整套件需要原本地历史 fixtures，GitHub 不替代运行态备份。

本会话实际权限继承 full-access/no-approval，未修改权限、审批或执行策略。
项目配置仍要求 workspace-write/on-request；本轮不宣称当前桌面会话边界已验收。
恢复、开发与测试写入均限定当前项目目录，外部登记目录只读文件元数据计量。

当前根目录 `C:\Projects\icml2026`。统一交接入口为根目录 `ICML2026_正式工作交接.md`，机器验收见 `reports/setup_report.json`。旧 E 盘报告仅为历史，原文件保留在 backups。

P1 已有最小 SQLite 单写入账本、attempt/租约、版本绑定、持久输出与回执、幂等接收、局部 stale、强制结束恢复；受管理 PDF 下载器已有字节限额、预留与磁盘检查、SHA 去重和下载回执恢复。新补充 accounting.py 实时统计指定外部开发目录的文件元数据；内部版本别名去重、越界重解析点阻塞。无 OS 全局配额和归档清理器。

更早离线验收：91 项，89 通过、2 个符号链接权限测试跳过，0 失败；包括 3 个实际终止子进程后的新进程恢复，以及 Windows junction 计量边界测试。state/offline_acceptance.json 绑定当前实现与规则哈希。后续代码/规则改动需重新验收。

本机 Python/pip/Git、UTF-8、SQLite、允许的 HTTPS、内置网页搜索、现有 ChatGPT 缓存登录均通过。CLI 已完成一次极小非交互模型任务；独立 native sandbox :workspace 探针通过项目内写入/项目外拒绝。当前桌面会话本身继承 full-access，未改其设置；新窗口的项目权限/信任与完整退出桌面后的恢复未验收。原生具体 elevated 实现身份未单独证明。

P2 仍为零篇闭环。新增受保护元数据下载，官方范围说明和 venue 配置已取得；浏览器首屏保存十条候选，一篇身份与公开决定已查。题录 API 要求真人验证，PDF 403，arXiv robots 406，均保留失败。正文、前作、贡献卡、独立复核和真实图未完成。未安装论文依赖。见 docs/P2_CHECKPOINT.md；旧 V1 下载器不可绕过当前保护。

P2_catalog_001、P2_catalog_002 与单篇获取任务 _001、_002、_003 均保留 blocked。下一任务见本文开头，先解决实际访问限制，不改旧哈希。项目政策仍为 40/50 GB 和每个使用卷至少 30 GB；旧 C20/E30 提议从未生效。原始 AGENTS.md 保持字节不变。
