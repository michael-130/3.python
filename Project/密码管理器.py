# 简单的密码管理器

import json
import os

密码文件 = "密码.json"

def 加载密码():
    """从文件加载密码"""
    if os.path.exists(密码文件):
        with open(密码文件, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def 保存密码(密码字典):
    """保存密码到文件"""
    with open(密码文件, 'w', encoding='utf-8') as f:
        json.dump(密码字典, f, ensure_ascii=False, indent=2)

def 添加密码(密码字典):
    """添加新密码"""
    网站 = input("输入网站名称：")
    用户名 = input("输入用户名：")
    密码 = input("输入密码：")
    
    密码字典[网站] = {
        "用户名": 用户名,
        "密码": 密码
    }
    
    print(f"已为 {网站} 添加密码！")

def 查看密码(密码字典):
    """查看保存的密码"""
    if not 密码字典:
        print("没有保存的密码。")
        return
    
    网站 = input("输入要查看的网站名称：")
    if 网站 in 密码字典:
        print(f"网站：{网站}")
        print(f"用户名：{密码字典[网站]['用户名']}")
        print(f"密码：{密码字典[网站]['密码']}")
    else:
        print("未找到该网站的密码。")

def 列出所有网站(密码字典):
    """列出所有保存密码的网站"""
    if not 密码字典:
        print("没有保存的密码。")
        return
    
    print("已保存密码的网站：")
    for 网站 in 密码字典.keys():
        print(f"- {网站}")

def 主程序():
    """主程序"""
    print("欢迎使用密码管理器！")
    密码字典 = 加载密码()
    
    while True:
        print("\n请选择操作：")
        print("1. 添加密码")
        print("2. 查看密码")
        print("3. 列出所有网站")
        print("4. 退出")
        
        选择 = input("输入你的选择 (1-4)：")
        
        if 选择 == "1":
            添加密码(密码字典)
            保存密码(密码字典)
        elif 选择 == "2":
            查看密码(密码字典)
        elif 选择 == "3":
            列出所有网站(密码字典)
        elif 选择 == "4":
            print("再见！")
            break
        else:
            print("无效的选择，请重试。")

if __name__ == "__main__":
    主程序()