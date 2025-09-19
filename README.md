# 京东自动化任务

这个项目提供了使用Trae AI的MCP Playwright工具在京东网站上执行自动化任务的指南，如搜索和浏览产品。

## 功能

- 自动打开京东网站
- 自动搜索指定产品（当前设置为搜索"牙膏"）
- 允许用户在浏览器中手动选择和浏览产品

## 使用方法

在Trae AI中，按照以下步骤操作：

1. 打开京东网站：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_navigate", args={"url": "https://www.jd.com/"})
```

2. 获取页面快照，找到搜索框：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_snapshot", args={})
```

3. 在搜索框中输入"牙膏"（需要替换搜索框的ref值）：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_type", args={"element": "搜索框", "ref": "搜索框的ref值", "text": "牙膏"})
```

4. 点击搜索按钮（需要替换搜索按钮的ref值）：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_click", args={"element": "搜索按钮", "ref": "搜索按钮的ref值"})
```

5. 查看搜索结果：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_snapshot", args={})
```

6. 完成后关闭浏览器：
```
run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_close", args={})
```

## 注意事项

- 使用此方法不需要安装任何依赖，因为它利用了Trae AI内置的MCP Playwright工具
- 在执行每个步骤后，您可以使用`browser_snapshot`工具查看当前页面状态
- 如果您想搜索其他产品，只需在第3步中将"牙膏"替换为您想要的产品名称