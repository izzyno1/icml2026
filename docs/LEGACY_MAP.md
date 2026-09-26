# 历史包地图与冲突处理

本包包含前几轮所有提供的材料，按原始目录结构保存在reference/下，避免要求用户手动合并。

| 路径 | 可复用材料 | 本次应注意 |
|---|---|---|
| reference/v1/icml2026_audit/ | 10篇样本、来源、采集/解析起点、8项离线测试、schema与提示词 | API身份、原始投稿、审稿未完成全量核验；下载器未接入当前磁盘保护。旧AGENTS已改名AGENTS.original.md防止自动生效 |
| reference/v2/icml2026_genealogy_v2/ | 11节点8关系的局部图、分类规则、9项算法测试 | 历史人工核读说明未在本次重新审计；不可用于全会比例。build_bundle.py/浏览器测试含原环境依赖，不当Windows启动器 |
| reference/v3/icml2026_longrun_v3/ | 任务包/交接卡、恢复与单写入规范、容量工具及12项离线测试 | 调度器是待实现要求；默认双版本容量情景被当前按需单版本政策替代 |
| reference/CODEX_WINDOWS_LOW_STORAGE.md | 历史低存储、归档协议 | 价格是旧快照，采购前需再查；本轮不开户、不上传、不付费 |

当前规则入口只有根AGENTS.md、PROJECT_SPEC.md、configs/project_policy.json和用户选定的阶段提示词。
旧代码和旧SHA256清单只验证原包范围，不应当作整合包校验器。本包新增MANIFEST.sha256.json才记录整合包的交付字节。
旧Linux .sh不是Windows唯一入口，不因此要求装WSL；移植为Python或原生PowerShell。
历史文件按原文保留（仅AGENTS更名）；其中以前宣称通过的浏览器测试不是本次Windows验证。本次测试记录另见reports/BUNDLE_VALIDATION.json。

审查代码优先项：
1. V1下载器有单文档内存上限，但没有跨文件磁盘预算、流式写入和在途预留；真实批量下载前补齐。
2. V1解析/清单的部分write_text依赖默认编码，Windows执行应显式encoding='utf-8'；暂时使用python -X utf8不能替代正式修复。
3. 旧路径为原包工作目录，迁移时用__file__/显式root/config，不硬编码/mnt/data。
4. 旧代码只基于实际API某些字段，不自动证明全会范围正确；必须核对当前官方目录、字段和版本。
5. 旧图算法结构通过不表示引用支持每条边，不用它给创新贴金。
