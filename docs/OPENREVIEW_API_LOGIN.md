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

2026-09-26 已完成真实登录：三次 PDF 请求成功（65 页当前版、49 页投稿版、另一篇
23 页论文），第四次中断并保留分片；不能把会话整体写成四份下载全成功。首次当前版
按哈希复用了已有对象。登录成功证明官方认证路径可行；后续批次仍需各自验收。
首次会话使用前一版下载器；本次 1 MiB 流式读取降低重复存储计量的开销，仍在每次
读取前后检查预算/时间/大小，新增精确脱敏错误分类。旧失败回执无法确定具体原因，
不把推测倒填为已证实原因。修正后作者站点的前作 PDF 已成功受保护下载；第四份
OpenReview 文件尚未用修正版重新实测。程序退出后不保留或恢复登录令牌。

代码更新后，旧 Pro 包保留历史 stale；新 `P2_J4wRLmh29t_evidence_gaps_001` 已核对
原返回字节与新增版本身份。新的补充 Pro 包使用新代码基线；科学验收仍须真实返回
后的短任务完成。人工审计未做。
