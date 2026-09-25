# 当前实现状态（2026-09-25 G0-02 本地实现）

G0-02 已新增 export-pro/import-pro：不可变证据包、waiting_external 无租约等待、
哈希命名隔离回传、300 秒本地验证 attempt、版本/来源/定位检查、幂等接收及同步回执。
结构通过仅为 awaiting_fact_check，不登记为论文验收结果。真实 Pro 往返尚未做。
协议见 contracts/pro_exchange.md。原 AGENTS.md 未改。

本轮完整离线套件 112 项：110 通过、2 跳过、0 失败；21 项新增交换测试，
共 4 项实际终止子进程后的新进程恢复。验收绑定见本地 state/offline_acceptance.json。
下方 91 项记录是修改前历史，不是当前实现的验收。

发布基线只包含活动源代码/测试及复用 V2 helper；旧十篇和示意图保留本地，
不作为本轮已核实数据发布。克隆后的活动测试入口：
`tools/python-project.cmd tools/run_offline_tests.py --active-only`。
完整 112 项需要原本地历史 fixtures，GitHub 不替代运行态备份。

本会话实际权限继承 full-access/no-approval，未修改权限、审批或执行策略。
项目配置仍要求 workspace-write/on-request；本轮不宣称当前桌面会话边界已验收。
恢复、开发与测试写入均限定当前项目目录，外部登记目录只读文件元数据计量。

当前根目录 `C:\Projects\icml2026`。统一交接入口为根目录 `ICML2026_正式工作交接.md`，机器验收见 `reports/setup_report.json`。旧 E 盘报告仅为历史，原文件保留在 backups。

P1 已有最小 SQLite 单写入账本、attempt/租约、版本绑定、持久输出与回执、幂等接收、局部 stale、强制结束恢复；受管理 PDF 下载器已有字节限额、预留与磁盘检查、SHA 去重和下载回执恢复。新补充 accounting.py 实时统计指定外部开发目录的文件元数据；内部版本别名去重、越界重解析点阻塞。无 OS 全局配额和归档清理器。

最新离线验收：91 项，89 通过、2 个符号链接权限测试跳过，0 失败；包括 3 个实际终止子进程后的新进程恢复，以及 Windows junction 计量边界测试。state/offline_acceptance.json 绑定实现与规则哈希。后续代码/规则改动需重新验收。

本机 Python/pip/Git、UTF-8、SQLite、允许的 HTTPS、内置网页搜索、现有 ChatGPT 缓存登录均通过。CLI 已完成一次极小非交互模型任务；独立 native sandbox :workspace 探针通过项目内写入/项目外拒绝。当前桌面会话本身继承 full-access，未改其设置；新窗口的项目权限/信任与完整退出桌面后的恢复未验收。原生具体 elevated 实现身份未单独证明。

P2 仍为零篇：仅有 3 条历史官方网页元数据来源，正文、前作、公开评审核读、贡献卡、真实图、人口统计均未完成。未安装论文依赖；未做真实下载联网集成。仍需实现受限题录采集、PDF 可定位解析、真实证据审核流程和输出。旧 V1 下载器不可绕过当前保护直接用于真实下载。

旧任务 P2_catalog_001 保留历史 blocked；新窗口应核对状态后使用 P2_catalog_002，不改旧任务版本哈希。项目政策仍为 40/50 GB 和每个使用卷至少 30 GB；旧 C20/E30 提议从未生效，现已标为失效。原始 AGENTS.md 保持字节不变。
