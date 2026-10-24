# 把这个Skill上传到GitHub（Windows新手图文操作的文字版）

## 你需要准备

- 一个GitHub账号：https://github.com/
- 推荐安装GitHub Desktop：https://desktop.github.com/
- 下载本聊天提供的 `geo-first-client-github-repository.zip` 并解压。

## 方案A：GitHub Desktop（推荐，能正确保留子文件夹）

1. 登录 https://github.com ，右上角 `+` → `New repository`。
2. `Repository name` 填 `geo-first-client`；`Description` 可以填 `GEO从零到第一单：78关训练与AI品牌可见度诊断 Agent Skill`。选 `Public`。创建时不勾选新的README、License、.gitignore（这些文件包里已经有）。点击 `Create repository`。
3. 启动GitHub Desktop，菜单 `File` → `Clone repository` → `URL`，输入新仓库地址 `https://github.com/你的用户名/geo-first-client.git`；选择本地文件夹并 `Clone`。
4. 打开克隆出的 `geo-first-client` 文件夹，把已经**解压后的仓库包内所有内容**（`skills` 文件夹、README.md、plugin.json 等）复制进去。注意不要多套一层同名文件夹。
5. 回到GitHub Desktop：左侧会显示新增文件。左下 `Summary` 填 `Initial release: GEO Agent Skill v1.0.0` → 点 `Commit to main`。
6. 点击 `Publish branch` 或 `Push origin`，然后打开 GitHub 仓库刷新，看到 `skills/geo-first-client/SKILL.md` 就成功了。

## 方案B：完全不用GitHub Desktop（浏览器上传）

1. 在GitHub创建一个 `Public` 空仓库 `geo-first-client`。
2. 打开仓库首页，选 `Add file` → `Upload files`。
3. **解压仓库zip**，将其中的文件和文件夹拖到上传区域（可将解压后的目录内容直接拖入）。确认预览中的路径有 `skills/geo-first-client/SKILL.md`，不是仅一个 `.zip` 文件。
4. 在页面下方写提交说明 `Initial release` 并提交。GitHub网页上传对浏览器支持和文件大小可能有限；若拖入文件夹失败，请使用方案A。

## 核查清单

- [ ] 仓库公开（Public），且没有客户隐私或密钥。
- [ ] `README.md` 能在首页显示中文说明。
- [ ] 浏览器能点开 `skills/geo-first-client/SKILL.md`。
- [ ] `references/curriculum-78.md` 和 `assets/templates/` 已上传。
- [ ] 未将第三方HTML、收费教程截图、真实客户数据或API Key提交公开仓库。
- [ ] 任选一种客户端安装测试，发送：`使用 geo-first-client，发布第00-01关`。

## 让别人安装

将仓库网址发给别人：`https://github.com/你的用户名/geo-first-client`。

Codex 用户可将 `skills/geo-first-client/` 整个目录复制到个人Skills目录或用其环境中已有的Skill安装器安装仓库路径。

WorkBuddy 用户可在GitHub Releases或你分享的文件中下载独立的 `geo-first-client-workbuddy-skill.zip`，从 WorkBuddy “添加技能 → 上传技能”导入；**普通仓库下载zip与技能专用zip不是同一个文件**。

## 如何更新版本

修改 `skills/geo-first-client/SKILL.md` 或参考资料，运行 `validate_skill.py`，提交并 Push；新增重要能力时再更改前置元数据版本号并更新发布说明。不要为了修改教材内容反复创建新仓库。
