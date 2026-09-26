# 首篇证据关系图（模型初筛，非总体谱系）

```mermaid
flowchart TD
    H["Hedging · ICML 2026<br/>当前65页 / 投稿49页<br/>新颖性 U，人工审计未做"]
    M["Mansour等 · 2021<br/>正文12页 + 补充4页"]
    L["Lecué–Rigollet · 2014<br/>期刊全文14页"]
    Q["Mourtada等 · 2023<br/>仅2页扩展摘要"]
    H -->|"方法比较：条件需对齐"| M
    H -->|"证明组件复用：两边原文已核对"| L
    H -.->|"背景关系：全文仍缺"| Q
    click H "https://openreview.net/forum?id=J4wRLmh29t" "官方论文与版本"
    click M "https://proceedings.mlr.press/v130/mansour21a.html" "官方前作"
    click L "https://lecueguillaume.github.io/assets/AOS1190.pdf" "作者站点前作"
    click Q "https://proceedings.mlr.press/v195/mourtada23a.html" "官方扩展摘要"
```

箭头从本篇指向相关前作，表示图上写明的关系。比较和背景引用不计方法继承；
证明组件复用也不表示整篇等价或低价值。图中缺少父节点不能支持首创判断。

[逐项版本与证明核对](../papers/OR_J4wRLmh29t/version_checks_001.json)记录来源 ID、
物理页码、直接证据与推断。原始投稿和当前附件必须分别读取；正式定稿角色仍未知。
此前两轮 Pro 使用选页；新的146页完整文本审读等待真实返回，尚无完整论文闭环。
[来源和字节哈希](../evidence/P2_J4wRLmh29t.json)；[机器可读图](P2_J4wRLmh29t_partial.json)。
