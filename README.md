# EasyType

手机输入实时推送到Windows剪贴板或直接输入的应用。

## 功能特点

- 📱 手机输入，实时推送到Windows
- ⌨️ 两种模式：直接输入或剪贴板
- 🎨 移动端优化界面
- ⚡ 实时同步，延迟低

## 快速开始

### 1. 安装依赖

确保已安装Python 3.12+和uv包管理器。

```bash
uv sync
```

或者使用pip：

```bash
pip install flask pyautogui pyperclip
```

### 2. 启动服务器

```bash
uv run python main.py
```

或者：

```bash
python main.py
```

服务器启动后，会显示本地IP地址，例如：`http://192.168.1.100:5000`

### 3. 手机连接

确保手机和电脑在同一个WiFi网络下。

1. 打开手机浏览器
2. 输入电脑上显示的IP地址和端口
3. 开始使用！

macos 的话 会要求权限授权


## 使用说明

### 模式选择

- **直接输入**：文字会直接在Windows上模拟键盘输入
- **剪贴板**：文字会复制到Windows剪贴板

### 输入区域

- 在输入框中输入文字，会自动同步到Windows
- 支持实时同步，无需手动发送

### 特殊按键

- **Enter**：发送回车键
- **Tab**：发送Tab键
- **Space**：发送空格键
- **Backspace**：发送退格键
- **Esc**：发送Escape键

### 清空输入

点击"清空输入"按钮可以清空当前输入框内容。

## 注意事项

1. 确保手机和电脑在同一网络下
2. Windows可能需要允许Python通过防火墙
3. 如果直接输入模式无效，尝试以管理员身份运行
4. 首次使用时，可能需要调整pyautogui的安全设置

## 技术栈

- **后端**：Flask
- **前端**：HTML5, CSS3, JavaScript
- **自动化**：PyAutoGUI
- **剪贴板**：Pyperclip

## 开发

### 项目结构

```
easyType/
├── main.py              # Flask应用主文件
├── templates/
│   └── index.html       # 移动端网页界面
├── pyproject.toml       # 项目配置
├── todo.md             # 开发计划
└── README.md           # 说明文档
```

### 运行开发服务器

```bash
uv run python main.py
```

## 许可证

MIT License

## 问题反馈

如有问题或建议，请提交Issue。
