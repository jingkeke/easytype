#!/bin/bash

# EasyType 启动脚本 (macOS/Linux)

# 确保在项目根目录
cd "$(dirname "$0")"

# 检查 uv 是否安装
if command -v uv &> /dev/null; then
    echo "使用 uv 启动服务..."
    uv run python main.py
else
    # 检查 python3 是否安装
    if command -v python3 &> /dev/null; then
        echo "使用 python3 启动服务..."
        # 尝试安装依赖
        python3 -m pip install flask pyautogui pyperclip
        python3 main.py
    else
        echo "错误: 请先安装 Python 3 或 uv 包管理器。"
        exit 1
    fi
fi
