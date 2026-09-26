# OpenReview 有界下载入口

默认入口仍为三篇四文件。`--reviewed-plan` 可读取本地已审阅清单，最多十篇/二十个
当前或原始投稿链接。清单必须绑定当前已验收目录任务、报告和实际来源字节；认证前、
认证后及每次传输前重核。精确 HTTPS GET 白名单限制 bearer，robots/其他路径/重定向
均不带认证。密码与 bearer 不保存，不从浏览器、环境变量或认证文件取出。

`tools/python-project.cmd tools/openreview_session.py --help`

`tools/python-project.cmd tools/openreview_session.py --plan --reviewed-plan exchange/download_plans/P2_pilot10_20260926_v2.json`

联网添加 `--run`，隐藏交互输入；先满足当前代码离线验收和40/50GB、每卷30GB保护。
克隆仓库不包含本地清单和账本，须先建立已核实来源任务。已有字节复用只证明本地哈希，
不声称重新下载或确认远端未变化。首次失败即停；旧分片和证据保留。目录变化需新计划。

本轮160项离线测试通过158项、跳过2项；扩展清单20项联网已成功，4项复用、16项新下载。
随后增加一条作者前作URL并重跑验收；旧清单绑定旧代码，恢复时不能直接重跑。
三篇/四文件旧入口实际成功另有本地回执。前作不计入目标十篇：必须显式注册为仅
`prior_work`；未知或混合角色仍计入，后续提升为目标也不得越界。该声明不等于取得或读过前作。

## 历史入口记录

# OpenReview API 登录与有限下载

官方 [Using the API](https://docs.openreview.net/getting-started/using-the-api)
当前明确要求 OpenReview 账号；API 使用与网站相同的账号和密码，但需要独立认证。
浏览器已登录不代表本地程序已认证。先前匿名 PDF 请求实际返回
`ChallengeRequiredError`，不是已验证的账号请求失败。

在项目根目录双击 `Login-OpenReview-and-Fetch.cmd`，在本地窗口输入邮箱、密码；
二者均隐藏显示，不要把它们发到聊天。账号启用 TOTP 或邮箱验证码时在同一窗口
输入验证码。程序直接向官方 API2 登录，临时会话仅保存在进程内，不写凭据文件，
不读取浏览器 Cookie、环境变量中的凭据、auth.json 或既有令牌。

标准库实现官方客户端公开的 `/login`、Bearer 和 MFA 协议，无新依赖。
文件复用受保护流式下载器，不使用全量缓冲的 PDF 接口。源码见
`src/icml_audit/openreview_session.py`。会话最多一小时，运行结束后清除引用并退出；
重新运行需要重新登录。没有全会任务、守护进程或后台承诺。

固定计划只有三篇已核对的主轨候选、最多四次 PDF 请求：首篇当前附件及原始投稿，
另外两篇当前附件。单并发、请求至少间隔五秒、每 PDF 最多 60 MB、请求超时 60 秒，
继续核查 robots、40/50 GB 预算、每卷 30 GB 留白、哈希和重复对象。
认证头只发给这四个精确官方 PDF URL，不发给 robots、其他域名或重定向。
登录响应最多 64 KiB。密码不出现在命令行参数、日志、Git 或结果回执。

验证挑战、权限拒绝或不支持的认证方式会停止，不自动重复登录。原始错误消息和
认证头不落盘，只留脱敏状态。passkey 流程尚未实现。现有文件可按哈希复核后复用。
下载成功只表示取得字节；原稿/定稿身份、正文核读和人类审计仍需分别验收。

```powershell
Set-Location -LiteralPath 'C:\Projects\icml2026'
.\tools\python-project.cmd tools/openreview_session.py --help
.\tools\python-project.cmd tools/openreview_session.py --plan
# 只在你自己的交互终端运行，不使用凭据参数或管道：
.\tools\python-project.cmd tools/openreview_session.py --run
```

状态文件为本地 `exchange/sync_receipts/openreview_api_session_latest.json`；每次还保存
带时间的独立回执。PDF 留在 `data/objects`。等待输入时不持有账本写锁或 running
租约。中断后运行既有 status/recover/preflight，再核对回执；不改旧任务哈希。

新增 14 项认证合成测试和一个精确作者 URL 测试。最新完整验收 **150 项：148 通过、
2 个既有 Windows 符号链接权限跳过、0 失败**，含四个实际强制中断恢复案例。

2026-09-26 修正后已再次完成真实登录与四个固定请求：前三份已存字节哈希复核一致，
第四份完整取得7,572,837字节、43页。旧中断分片保留，具体旧原因仍未知；不能倒填为
已证实超时。实际成功回执单独保存，程序结束且会话未持久化。

当前入口仍固定三篇四请求，不宣称已经支持其他候选。后续扩大需明确计划并保留同样保护。
首篇真实完整文本Pro返回已完成限定事实核对，第二篇正在审读。人工审计未做。
