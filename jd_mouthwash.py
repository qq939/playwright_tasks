#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用MCP的playwright工具自动打开京东并搜索漱口水的脚本
"""

import json
import os
import sys
import datetime

def main():
    print("此脚本将使用MCP的playwright工具来打开京东并搜索漱口水")
    
    # 1. 打开京东网站
    print("\n1. 打开京东网站：")
    print("```")
    print('mcp_playwright_browser_navigate({"url": "https://www.jd.com/"})')
    print("```")
    
    # 2. 在搜索框中输入'漱口水'
    print("\n2. 在搜索框中输入'漱口水'：")
    print("```")
    print('mcp_playwright_browser_snapshot({})')
    print('# 找到搜索框后，使用以下命令输入漱口水')
    print('mcp_playwright_browser_type({"element": "搜索框", "ref": "搜索框的ref值", "text": "漱口水"})')
    print("```")
    
    # 3. 点击搜索按钮
    print("\n3. 点击搜索按钮：")
    print("```")
    print('mcp_playwright_browser_click({"element": "搜索按钮", "ref": "搜索按钮的ref值"})')
    print("```")
    
    # 4. 查看搜索结果
    print("\n4. 查看搜索结果：")
    print("```")
    print('mcp_playwright_browser_snapshot({})')
    print("```")
    
    # 5. 分析搜索结果并提供选择
    print("\n5. 分析搜索结果并提供选择：")
    print("```")
    print("# 分析页面上的商品列表，提取品牌、价格、评分等信息")
    print('# 示例：提取前5个商品的信息')
    print('mcp_playwright_browser_evaluate({"function": "() => {')
    print('  const products = [];')
    print('  const items = document.querySelectorAll(\'.gl-item\');')
    print('  for (let i = 0; i < Math.min(5, items.length); i++) {')
    print('    const item = items[i];')
    print('    const title = item.querySelector(\'.p-name em\')?.textContent.trim();')
    print('    const price = item.querySelector(\'.p-price\')?.textContent.trim();')
    print('    const shop = item.querySelector(\'.p-shop\')?.textContent.trim();')
    print('    const link = item.querySelector(\'a\')?.href;')
    print('    products.push({title, price, shop, link});')
    print('  }')
    print('  return products;')
    print('}"})')
    print("```")
    
    # 6. 选择商品并进入详情页
    print("\n6. 选择商品并进入详情页：")
    print("```")
    print('# 假设用户选择了第一个商品')
    print('mcp_playwright_browser_click({"element": "第一个商品", "ref": "第一个商品的ref值"})')
    print('# 等待详情页加载')
    print('mcp_playwright_browser_snapshot({})')
    print("```")
    
    # 7. 立即购买
    print("\n7. 立即购买：")
    print("```")
    print('# 点击立即购买按钮')
    print('mcp_playwright_browser_click({"element": "立即购买按钮", "ref": "立即购买按钮的ref值"})')
    print('# 处理可能出现的登录请求')
    print('# 如果出现登录页面，记录状态')
    print('mcp_playwright_browser_snapshot({})')
    print("```")
    
    # 8. 处理结算页面
    print("\n8. 处理结算页面：")
    print("```")
    print('# 如果成功进入结算页面')
    print('# 选择配送方式和支付方式')
    print('# 点击提交订单按钮')
    print('mcp_playwright_browser_click({"element": "提交订单按钮", "ref": "提交订单按钮的ref值"})')
    print('# 获取订单号')
    print('mcp_playwright_browser_evaluate({"function": "() => {')
    print('  const orderNumber = document.querySelector(\'.order-num\')?.textContent.trim();')
    print('  return orderNumber;')
    print('}"})')
    print("```")
    
    # 9. 关闭浏览器
    print("\n9. 关闭浏览器：")
    print("```")
    print('mcp_playwright_browser_close({})')
    print("```")
    
    # 10. 记录购买信息
    print("\n10. 记录购买信息：")
    print("```")
    print('# 将订单信息记录到user_history.md文件中')
    print('# 包括订单号、商品信息、价格、预计送达时间等')
    print("```")

if __name__ == "__main__":
    main()