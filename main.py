from flask import Flask, render_template, request, jsonify
import pyautogui
import pyperclip
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

@app.route('/')
def index():
    """Main page for mobile input"""
    return render_template('index.html')

@app.route('/type', methods=['POST'])
def type_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        mode = data.get('mode', 'type')

        if not text:
            return jsonify({'success': False, 'error': 'No text provided'}), 400

        if mode == 'type':
            # 方案：直接灌入文字（使用Ctrl+V模拟粘贴）
            logger.info(f"Using 'Paste' injection for text: {text[:50]}...")

            # 1. 先把文字放入剪贴板
            pyperclip.copy(text)
            logger.info("Copied text to clipboard")

            # 2. 等待一小段时间确保剪贴板准备就绪
            time.sleep(0.1)  # 100ms延迟

            # 3. 模拟按下 Ctrl+V 进行粘贴
            logger.info("Simulating Ctrl+V keystroke...")
            pyautogui.hotkey('ctrl', 'v')

            # 4. 等待粘贴完成
            time.sleep(0.05)  # 50ms延迟
            logger.info("Successfully injected text via clipboard paste")
        
        elif mode == 'clipboard':
            pyperclip.copy(text)
            
        return jsonify({'success': True, 'mode': mode})
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/key', methods=['POST'])
def press_key():
    """Press special keys (enter, tab, etc.)"""
    try:
        data = request.get_json()
        key = data.get('key', '')

        if not key:
            return jsonify({'success': False, 'error': 'No key provided'}), 400

        # Map common keys
        key_map = {
            'enter': 'enter',
            'tab': 'tab',
            'space': 'space',
            'backspace': 'backspace',
            'escape': 'esc'
        }

        actual_key = key_map.get(key.lower(), key.lower())
        pyautogui.press(actual_key)
        logger.info(f"Pressed key: {actual_key}")

        return jsonify({'success': True, 'key': actual_key})

    except Exception as e:
        logger.error(f"Error pressing key: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/paste', methods=['POST'])
def paste_from_clipboard():
    """Paste text from clipboard using Ctrl+V"""
    try:
        logger.info("Starting paste operation...")

        # 确保剪贴板内容已经准备就绪
        time.sleep(0.1)  # 100ms延迟

        # 模拟按下 Ctrl+V 进行粘贴
        logger.info("Simulating Ctrl+V keystroke...")
        pyautogui.hotkey('ctrl', 'v')

        # 等待粘贴完成
        time.sleep(0.05)  # 50ms延迟
        logger.info("Successfully pasted from clipboard")

        return jsonify({'success': True})

    except Exception as e:
        logger.error(f"Error pasting from clipboard: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/info')
def get_info():
    """Get server info"""
    return jsonify({
        'status': 'running',
        'modes': ['type', 'clipboard'],
        'special_keys': ['enter', 'tab', 'space', 'backspace', 'escape']
    })

def main():
    """Run the Flask app"""
    print("Starting EasyType server...")
    print("Access from your mobile device using the local IP address")
    print("Example: http://192.168.1.100:5000")

    # Get local IP for display
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"Local IP: http://{local_ip}:5000")
    except:
        print("Could not determine local IP")

    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
