#这是注释

#你好 
print('')
print('(这是你好)')
print('你好，我的名字是迈克尔')
print('')

#变量和数据类型
print('(这是变量和数据类型)')
角色姓名 = '迈克'
角色年龄 = '18'
角色专业 = '计算机科学'
是男性 = True
print("你好，我的名字是 " + 角色姓名 , ',' '我今年 ' + 角色年龄 +' 岁' , ',' '我选择了 '+角色专业 + '专业。')

#字符串
print('')
print('(这是字符串)') 
print(" 长颈鹿 \n  学院")
print("迈克\"伯特")
print("迈克 \ 迈克尔")
print('')

#字符串变量
print('(这是字符串变量)' )
短语 = '长颈鹿'
print(短语)
print(短语 + ' 真是太酷了')
print('')

#函数可以修改和获取字符串信息
print('(这是可以修改和获取字符串信息的函数)')
 
 #关于修改的函数
print(短语.upper().center(35))

 #关于获取信息的函数 
print(短语.islower())

 #关于获取信息的函数 
print(短语.upper().isupper())
 
 #可以计算一行中有多少个字符的函数
print(len(短语))
 
 # 找出第一个字符是什么
print(短语[0]) 
print(短语[3])
 
 # 找出G在哪里 
print(短语.index("长"))
 
 # 我们可以替换单词 
print(短语.replace("长颈鹿","迈克的"))

 # 处理数字
print