# EasyType 开发完成

✅ 已完成：手机输入实时推送到Windows剪贴板或直接输入的软件

## 实现功能

1. ✅ Flask后端搭建
   - 处理文本输入请求http://127.0.0.1:5000http://127.0.0.1:5000
   - 处理特殊按键请求
   - 提供系统信息接口

2. ✅ 移动端网页界面
   - 响应式设计，适配手机屏幕
   - 大文本输入框
   - 模式切换按钮（直接输入/剪贴板）
   - 特殊按键按钮（Enter、Tab等）

3. ✅ Windows输入模拟
   - 使用PyAutoGUI模拟键盘输入
   - 实时同步输入内容
   - 支持特殊按键

4. ✅ 剪贴板功能
   - 使用Pyperclip复制文本到剪贴板
   - 模式切换支持

5. ✅ 实时通信
   - AJAX异步请求
   - 输入延迟优化（300ms）
   - 连接状态显示

6. ✅ 项目配置
   - 更新pyproject.toml依赖
   - 添加README文档
   - 配置.gitignore

## 使用方法

1. 安装依赖：`uv sync`
2. 启动服务器：`uv run python main.py`
3. 手机访问显示的IP地址
4. 开始输入，实时同步到Windows

## 技术栈

- 后端：Flask + PyAutoGUI + Pyperclip
- 前端：HTML5 + CSS3 + JavaScript
- 包管理：uv

