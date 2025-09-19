#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用MCP的playwright工具自动打开京东并搜索牙膏的脚本
"""

import json
import os
import sys

def main():
    print("此脚本将使用MCP的playwright工具来打开京东并搜索牙膏")
    print("请在Trae AI中运行以下命令：")
    print("\n1. 打开京东网站：")
    print("```")
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_navigate", args={"url": "https://www.jd.com/"})')
    print("```")
    
    print("\n2. 在搜索框中输入'牙膏'：")
    print("```")
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_snapshot", args={})')
    print('# 找到搜索框后，使用以下命令输入牙膏')
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_type", args={"element": "搜索框", "ref": "搜索框的ref值", "text": "牙膏"})')
    print("```")
    
    print("\n3. 点击搜索按钮：")
    print("```")
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_click", args={"element": "搜索按钮", "ref": "搜索按钮的ref值"})')
    print("```")
    
    print("\n4. 查看搜索结果：")
    print("```")
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_snapshot", args={})')
    print("```")
    
    print("\n5. 关闭浏览器：")
    print("```")
    print('run_mcp(server_name="mcp.config.usrlocalmcp.playwright", tool_name="browser_close", args={})')
    print("```")

if __name__ == "__main__":
    main()