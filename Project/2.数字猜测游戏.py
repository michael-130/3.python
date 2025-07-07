import random

# r=random.randrange(-1 ,10) 用于随机数字，不包括10
# r=random.randint(-1 ,10) 用于随机数字，包括10

范围上限 = input('输入一个数字：')
if 范围上限.isdigit():
    范围上限 = int(范围上限)

    if 范围上限 <= 0:
        print("下次请输入一个大于0的数字。")
        quit()
else:
    print("下次请输入一个数字。")
    quit()

随机数字 = random.randint(0, 范围上限)
猜测次数 = 0

while True:
    用户猜测 = input("请猜一个数字：")
    if 用户猜测.isdigit():
        用户猜测 = int(用户猜测)
    else:
        print("下次请输入一个数字")
        continue
    
    猜测次数 += 1

    if 用户猜测 == 随机数字:
        print('你猜对了！')
        print(f'你总共猜了 {猜测次数} 次')
        break
    elif 用户猜测 > 随机数字:
        print('你猜的太大了')
    else:
        print('你猜的太小了')