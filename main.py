from flask import Flask, render_template, request, jsonify
import pyautogui
import pyperclip
import logging
import time
import ctypes
import sys
import os
import socket

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PyAutoGUI 安全设置
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/type', methods=['POST'])
def type_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        mode = data.get('mode', 'type')

        if not text and mode == 'type':
            return jsonify({'success': False, 'error': 'No text provided'}), 400

        if mode == 'type':
            logger.info(f"Injecting text via Clipboard: {text[:50]}...")
            pyperclip.copy(text)
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')
            logger.info("Injected successfully")
        
        elif mode == 'clipboard':
            pyperclip.copy(text)
            
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/key', methods=['POST'])
def press_key():
    """处理物理按键模拟"""
    try:
        data = request.get_json()
        key = data.get('key', '')
        
        if key == 'ctrl_enter':
            pyautogui.hotkey('ctrl', 'enter')
        else:
            # 标准按键映射
            key_map = {
                'enter': 'enter',
                'tab': 'tab',
                'backspace': 'backspace',
                'esc': 'esc',
                'space': 'space'
            }
            actual_key = key_map.get(key.lower(), key.lower())
            pyautogui.press(actual_key)
            
        logger.info(f"Simulated Key: {key}")
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def main():
    if not is_admin():
        script = os.path.abspath(sys.argv[0])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}"', None, 1)
        sys.exit(0)

    # 获取本地IP
    local_ip = "localhost"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except: pass

    print(f"\n{'='*40}")
    print(f"EasyType 运行中")
    print(f"请在手机浏览器访问: http://{local_ip}:5000")
    print(f"{'='*40}\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    main()