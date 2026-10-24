# GEO 从零到第一单 — `geo-first-client` Agent Skill

> 适用于 Codex、腾讯 WorkBuddy 及支持 Agent Skills 格式的智能体。**78关新手陪练 + GEO品牌可见度诊断 + 内容与渠道SOP + 合规商业交付。**

本仓库是技能包，不是自动“操纵大模型排名”的工具；AI能否引用、推荐由第三方平台决定，不能保证。

## 两种模式

| 模式 | 示例指令 | 产出 |
|---|---|---|
| 🧑‍🏫 教练 | `使用 geo-first-client，开营，从第00-01关开始` | 每轮一关，提交证据、100分制评分、85分晋级、训练存档 |
| 🛠️ 执行 | `使用 geo-first-client，为一家设备企业做GEO只读诊断` | 问题库、测试协议、数据汇总、来源分析、报告草稿、报价边界 |

**重要：** 没权限时只做公开研究或草稿；发布、改站、报价发送、付款、联系真实客户都要用户授权。原始AI回答和业务事实必须留证据；不制造虚假评测、排名或投毒内容。

## 文件结构

```text
geo-first-client/
├── README.md                       # 仓库首页说明
├── HOW_TO_PUBLISH_GITHUB.md        # Windows小白上传教程
├── LICENSE                         # MIT（只适用于本仓库的原创文件）
├── plugin.json                     # 可选：OpenAI Agent Plugin清单
├── AGENTS.md                       # 给Codex读的仓库协作规则
├── skills/
│   └── geo-first-client/
│       ├── SKILL.md                # 核心技能入口，先读它
│       ├── references/            # 78关课程与测试/交付规范
│       ├── assets/templates/      # 13张空CSV+4份Markdown模板
│       └── scripts/               # 离线任务查询、汇总、校验
└── examples/                       # 不包含真实客户资料
```

## Codex 安装（Windows PowerShell）

先下载或克隆本仓库，在仓库**根目录**打开 PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Path ".\skills\geo-first-client" -Destination "$HOME\.codex\skills" -Recurse -Force
```

重新打开 Codex 对话，发送：`请使用 geo-first-client 技能，先读取 SKILL.md，开营发布第00-01关。`

若你已使用其它自定义技能目录、工作区级技能或新版插件安装器，可按自身环境将同一个 `geo-first-client` 技能文件夹放进去。**目录必须包含 `SKILL.md`**。

## WorkBuddy 安装

用仓库发行的 `geo-first-client-workbuddy-skill.zip`（内部第一层为 `geo-first-client/SKILL.md`），打开 WorkBuddy → 专家·技能·连接器 → 技能 → 添加技能 → 上传技能 → 选择该zip。不要把整个**GitHub仓库备份ZIP**当作WorkBuddy技能包。

官方WorkBuddy说明：https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market

## 脚本（可选，不联网、不依赖外部库）

```bash
python skills/geo-first-client/scripts/validate_skill.py
python skills/geo-first-client/scripts/task_lookup.py 04-02
python skills/geo-first-client/scripts/visibility_summary.py --input 你的采样记录.csv --output sample_summary.json
```

`visibility_summary.py` 只计算**本地CSV里人工已经核实的**描述统计，不负责向豆包、DeepSeek等平台自动提问，也不能代替原始截图与引用URL核验。

## 课程地图

| 阶段 | 主题 | 关数 |
|---|---|---:|
| LV0 | 建营与建档 | 3 |
| LV1 | GEO基础与AI原理 | 7 |
| LV2 | 选市场与双路线 | 8 |
| LV3 | 买家问题与测试设计 | 7 |
| LV4 | 基线测试与竞品溯源 | 9 |
| LV5 | 事实证据与内容制作 | 10 |
| LV6 | 渠道与网站可发现性 | 9 |
| LV7 | 复测、归因与报告 | 7 |
| LV8 | 产品化、报价与合作边界 | 7 |
| LV9 | 客户开发实战 | 6 |
| LV10 | 首单与复盘 | 5 |
| **合计** | | **78** |

## 授权与来源

本仓库仅分发独立撰写的技能指令、复写后的知识方法、空白模板和代码，**不附带第三方教程原始HTML、文章图片或未经授权案例**。参考文章中的未经核实数字不会变成“平台算法定律”。详细见 `skills/geo-first-client/references/sources-and-rights.md`。

开源协议MIT适用于本仓库由贡献者有权授权的原创内容，不会使外部引用网站或他人文章自动转成MIT。真实客户数据、凭证、API密钥切勿提交至公开仓库。

## 开始

安装后说：**`使用 geo-first-client，开营`**。

详见 [上传 GitHub 指南](HOW_TO_PUBLISH_GITHUB.md)。如果想把此项目作为OpenAI可安装Plugin提交公共目录，仓库还提供符合新规范的可选 `plugin.json`；**推送到GitHub不等于自动上架Plugin商店**。
