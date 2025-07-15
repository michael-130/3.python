print("欢迎来到我的计算机Python项目！")

游戏 = input("你想要玩吗？ ")

if 游戏 != "是":
    quit()

print("好的！让我们开始玩吧 :)")
分数 = 0

#1
答案 = input("CPU代表什么？ ")
if 答案.lower() == "中央处理器" or 答案.lower() == "central processing unit":
   print("正确！")
   分数 += 20
else:
    print("错误！")
答案 = input("CPU代表什么？ ")
if 答案.lower() == "中央处理器" or 答案.lower() == "central processing unit":
   print("正确！")
   分数 += 20
else:
    print("错误！")
#2
答案 = input("GPU代表什么？ ")
if 答案.lower() == "图形处理器" or 答案.lower() == "graphics processing unit":
   print("正确！")
   分数 += 20
else:
    print("错误！")

#3
答案 = input("RAM代表什么？ ")
if 答案.lower() == "随机存取存储器" or 答案.lower() == "random access memory":
   print("正确！")
   分数 += 20
else:
    print("错误！")

#4
答案 = input("PSU代表什么？ ")
if 答案.lower() == "电源供应器" or 答案.lower() == "power supply":
   print("正确！")
   分数 += 20
else:
    print("错误！")

#5
答案 = input("PC代表什么？ ")
if 答案.lower() == "个人电脑" or 答案.lower() == "personal computer":
   print("正确！")
   分数 += 20
else:
    print("错误！")

# 简化版本
if 分数 >= 60:
   print("玩得很好！你得到了 " + str(分数) + " 分！") 
else: 
    print("不错的尝试！你得到了 " + str(分数) + " 分！")

print("你得到了 " + str((分数 / 5) * 100) + "%。")