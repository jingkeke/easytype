@echo off
:: 切换到脚本所在目录
cd /d "%~dp0"
:: 执行启动命令
uv run main.py
pause