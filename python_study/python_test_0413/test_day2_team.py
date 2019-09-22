# 编写一个程序，输入年月日三个数据，以年月日（及yyyy-mm-dd）的格式将其显示出来：
# 	Enter year:2019
# 	Enter month:04
# 	Enter day:13
# 	Today is 2019-04-10,I am happy！
# year = input("input year")
# month = input("input month")
# day = input("input today")
# print("\n\nToday is %s-%s-%s\nI am happy!" % (year, month, day))


# 2．print函数基本使用，分别使用后续格式控制字  %d  %x  %f  \t \n \b
# 将整形值7、100，以多种格式打印到屏幕
# %f练习，打印17.2365
# 打印字符串 %d、单引号、双引号

# a = 7
# b = 100
# print("%d   %x   %f   %d   %x   %f" % (a, b, a, b, a, b))
# c = 17.2365
# print("%.4f" % c)
# a = "%d"
# b = "'"
# c = '""'
# print("%s%s%s" % (a, b, c))
# print("%d" "'" '""')


# 3．编写程序，对用户录入的产品信息进行格式化。程序会话应类似下面这样：
# Enter item number: 583
# Enter unit price: 13.5
# Enter purchase date(yyyy-mm-dd):2019-04-10
# Item    Unit Price    Purchase Date
# 583     $13.50        2019-04-10

# item = input("enter item number:")
# unit_price = input("enter unit price:")
# purchase_date = input("enter purchase data(yyyy_mm_dd):")
# print("Item\tUnit Price\tPurchase Date\n%s\t\t$%s\t\t%s" % (item, unit_price, purchase_date))


# 4．编写程序，提示用户以区号、号码的格式输入电话号码，并以xxx.xxxxxxxx的
# 格式显示该号码：
# Enter zone number: 010
# Enter phone number: 65337309
# You entered 010. 65337309
# number = input("enter zone number：like 010")
# phone_number = input("enter phone number：like 65337309")
# print("Your entered is %s_%s" %(number, phone_number))

# 5. 输出两个字符串的连接结果：
# 	s1 = "hello"
# 	s2= "world"
#    进阶：键盘输入两个字符串，进行连接后输出
#
# s1 = "hello"
# s2 = "world"
# print(s1 + s2)
# s1 = input("请输入1")
# s2 = input("请输入2")
# print(s1 + s2)


# # 6. 重复输出5次“Life is short, you need python”
# #
# print('"Life is short , you need python"\n' * 5)


# # 7.	输入两个整数比较大小，输出哪个值大、哪个值小
# num1 = int(input("输入数1："))
# num2 = int(input("输入数2："))
# if num1 - num2 > 0:
#     print("较大值是数1：%s，较小值是数2：%s" % (num1, num2))
# elif num2 - num1 > 0:
#     print("较大值是数2：%s，较小值是数1：%s" % (num2, num1))
# else:
#     print("两数相等")


# # 8.	输入一个正整数，判断其是否为偶数
# num = int(input("输入一个正整数，可以判断是否是偶数："))
# if num % 2 == 0:
#     print("%s是个偶数" % num)
# else:
#     print("%s是个奇数" % num)


# # 9.	编写程序，输入3个整数找出最大值和最小值。
# Enter three integers: 10 8 49
# Largest: 49
# Smallest: 8

# 方法1：使用三目运算符
# a = int(input("输入数1"))
# b = int(input("输入数2"))
# c = int(input("输入数3"))
# max_num = a if a > b else b
# min_num = a if a < b else b
# max_num = max_num if max_num > c else c
# min_num = min_num if min_num < c else c
# print("max值是%s,min值是%s" % (max_num,  min_num))
#
# 方法2：使用 if else
# a = int(input("输入数1"))
# b = int(input("输入数2"))
# c = int(input("输入数3"))
# if a > b:
#     max_num = a
#     min_num = b
# else:
#     max_num = b
#     min_num = a
# if c > max_num:
#     max_num = c
# if c < min_num:
#     min_num = c
# print("max值是%s,min值是%s" % (max_num,  min_num))

# 方法3：使用列表
# list1 = []
# for i in range(0, 3):
#     j = int(input("请输入数字"))
#     list1.append(j)
# list1.sort()
# print("最大数是%s,最小数是" % list1[-1], list1[0])


# # 10.	 利用if嵌套语句编写一个程序，把用数字表示的成绩转化为字母表示的等级。
# # Enter numerical grade: 84
# # Letter grade: B
# # 使用下面的等级评定规则：A为90-100， B为80-89， C为70-79，D为60-69，F为0-59。如果成绩高于100或低于0显示“成绩有误”的信息。
# # 方法1：if elif
# grade = int(input("Enter your numerical grade:"))
# if 0 <= grade <= 100:
#     if 0 <= grade < 60:
#         print("Letter grade : F")
#     elif 60 <= grade < 70:
#         print("Letter grade : D")
#     elif 70 <= grade < 80:
#         print("Letter grade : C")
#     elif 80 <= grade < 90:
#         print("Letter grade : B")
#     elif 90 <= grade <= 100:
#         print("Letter grade : A")
# else:
#     print("成绩有误！")
#
# # 方法2：列表
# while True:
#     score = [0, 60, 70, 80, 90, 101]
#     grade = ['f', 'D', 'c', 'b', 'a']
#     a = float(input("输入分数"))
#     if 0 <= a <= 100:
#         for i in range(len(score)):
#             if (a >= score[i]) and (a < score[i+1]):
#                 print(grade[i])
#     else:
#         print("您的输入有误")
