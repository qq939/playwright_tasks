# 用户规则

## 基本规则
- 优先使用mcp工具来完成任务
- 识别任务完成中的无效尝试和错误处理
- 更新项目规则: .trae/rules/project_rules.md
- 将user_rules.md文件中的所有规则都保存在：.trae/rules/user_rules.md中

## Git操作规则
- 如果有git仓库，先暂存本地修改，然后git pull，然后再继续下面的步骤
- 每次对话后都要git push(make sure success)，commit内容就是用户说的那句话
- git配置：user.email="939342547@qq.com", user.name="qq939"
- 远程仓库：remote=https://github.com/qq939/{to_be_create_as_this_projectName}, branch=master
- 可能需要创建远程仓库：gh repo create {to_be_create_as_this_projectName} --public
- 确保添加规则文件：git add .trae/rules/project_rules.md 和 git add .trae/rules/user_rules.md
- 如果git推送到远端失败，rebase并且push --force-with-lease

## 环境配置规则
- 创建Python虚拟环境：使用uv命令
- 安装requirements.txt中的Python包
- 所有对话存到项目文件夹下的user_history.md文件中
- 记录时间格式：按照工作笔记格式记录每个问题的时间

## 其他规则
- 适当增加mac的vscode快捷键提示
- 添加代码快速补全提示（如输入几个字母按tab键）
- 补充提示到tips.txt中
- 必须使用MCP完成购买任务
- 回答语言：使用中文回答用户问题