#!/usr/bin/env python3
"""
测试剪贴板模拟是否正常工作
用于验证剪贴板模拟是否正常工作
"""

import pyautogui
import pyperclip
import time
import sys
import os
import platform

IS_MAC = platform.system() == 'Darwin'
MODIFIER = 'command' if IS_MAC else 'ctrl'

def test_clipboard_paste():
    """测试剪贴板粘贴功能"""
    print("=" * 50)
    print(f"EasyType 粘贴功能测试 ({'macOS' if IS_MAC else 'Windows'})")
    print("=" * 50)

    # 测试文本
    test_text = "Hello from EasyType! 测试文本123"

    print(f"\n测试文本: {test_text}")
    print("\n请按照以下步骤操作:")
    print("1. 点击你想要输入文本的应用窗口（例如记事本或备忘录）")
    print("2. 确保输入框有光标在闪烁")
    print("3. 回到此窗口并按Enter键继续")

    input("\n准备就绪后按Enter键...")

    try:
        print("\n[1/4] 复制文本到剪贴板...")
        pyperclip.copy(test_text)
        time.sleep(0.1)
        print("✓ 文本已复制到剪贴板")

        print("\n[2/4] 等待应用准备...")
        time.sleep(1)
        print("✓ 等待完成")

        print(f"\n[3/4] 模拟按下 {MODIFIER.capitalize()}+V...")
        pyautogui.hotkey(MODIFIER, 'v')
        print(f"✓ {MODIFIER.capitalize()}+V 已发送")

        print("\n[4/4] 等待粘贴完成...")
        time.sleep(0.2)
        print("✓ 操作完成")

        print("\n" + "=" * 50)
        print("测试完成！请检查目标应用是否收到了文本。")
        print("=" * 50)

        return True

    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        return False

def test_keyboard_input():
    """测试键盘输入功能"""
    print("\n" + "=" * 50)
    print("键盘按键测试")
    print("=" * 50)

    print("\n测试将发送以下按键序列:")
    print("- Hello")
    print("- Enter键")
    print("- World")

    print("\n请确保目标应用已准备好接收输入")
    input("按Enter键开始测试...")

    try:
        pyautogui.write("Hello")
        pyautogui.press('enter')
        pyautogui.write("World")
        print("\n✓ 按键测试完成")
        return True
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        return False

def check_privileges():
    """检查权限"""
    if IS_MAC:
        print("\n⚠️  macOS 提示: 请确保在'系统设置 > 隐私与安全性 > 辅助功能'中允许了您的终端。")
        return True
    else:
        import ctypes
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except:
            return False

def main():
    """主测试流程"""
    print("EasyType 功能测试工具")
    print("=" * 50)

    # 检查权限
    if not check_privileges() and not IS_MAC:
        print("\n⚠️  警告: 当前没有管理员权限")
        print("   某些应用程序可能需要管理员权限才能接收模拟输入")
        input("\n按Enter键继续测试...")

    # 测试剪贴板粘贴
    success1 = test_clipboard_paste()

    # 询问是否测试键盘输入
    print("\n")
    response = input("是否测试键盘直接输入功能? (y/n): ")
    if response.lower() == 'y':
        success2 = test_keyboard_input()
    else:
        success2 = True

    # 总结
    print("\n" + "=" * 50)
    print("测试总结:")
    print(f"剪贴板粘贴测试: {'✓ 通过' if success1 else '✗ 失败'}")
    print(f"键盘输入测试: {'✓ 通过' if success2 else '✗ 失败'}")

    if success1 and success2:
        print("\n✓ 所有测试通过！EasyType应该可以正常工作。")
    else:
        print("\n✗ 部分测试失败，请检查错误信息。")
        print("\n建议:")
        print("1. 确保目标应用窗口是活动窗口")
        if IS_MAC:
            print("2. 检查‘辅助功能’权限设置")
        else:
            print("2. 尝试以管理员身份运行终端")
        print("3. 检查是否有安全软件阻止了模拟输入")

    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n测试已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n发生错误: {e}")
        sys.exit(1)
