# # 1.计算偶数和
#  j = 0
# for i in range(1, 5):
#     if i % 2 == 0:
#         j += i
# print(j)
# # 2.判定年龄差
# my_age = int(input("输入你的年龄"))
# bro_age = float(input("输入弟弟的年龄"))
# print("你与你弟弟的年龄差为：%0.2f" % (my_age - bro_age))
# a = 2
# b = 3
# c = 4
# print("%02d\n%03d\n%06d\n" % (a, b, c))
#
# # 3.打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%s * %s = %s" % (j, i, i * j), end='\t')
#     print()
#
#
# # 4.格式化输出日期
# enter_year = input("输入年:")
# enter_month = input("输入月:")
# enter_day = input("输入日:")
# print("Today is %s-%s-%s, I am happy!" % (enter_year, enter_month, enter_day))
# try:
#     enter_year = int(enter_year)
#     enter_month = int(enter_month)
#     enter_day = int(enter_day)
#     print("Today is %d-%02d-%d, I am happy!" % (enter_year, enter_month, enter_day))
# except:
#     print("你的输入有误")
#
#  5.if while 练习
# # 定义一个变量记录年龄
# age = int(input("请输入你的年龄："))
# # 判断是否满了18岁
# if age >= 18:
#     # 如果满了18岁，可以进网吧嗨皮
#     print("可以进网吧嗨皮")
# # 没满18岁，不能进网吧
# else:
#     print("没满18岁,不能进网吧嗨皮")
#
# 6.三目运算符
# x = int(input(""))
# x += x if x % 2 == 1 else x
# print(x)

# 7.输入1 或0 的整数，1表示下雨 ，0表示不下，
# 根据输入的条件，当下雨时，输出带伞的信息
#
# try:
#     num = int(input("输入数值1或0:"))
#     if num == 1:
#         print("今天是个下雨天,记得带伞哟,亲！")
#     elif num == 0:
#         print("今天是个艳阳天,我们去游乐园吧！")
#     else:
#         print("老实在家看python！")
# except ValueError:
#     print("输入有误，你不是我的主人！")
#
# 8. 猜拳游戏
# 实现猜拳-石头剪刀布(人机大战)
# 步骤
# 基础：
# 1. 设定三个数字分别代表三种手势：1：石头、2：剪刀、3：布
# 2. 在程序中规定好计算机始终出"剪刀"：computer = 2
# 3. 从键盘接收输入，代表人出的手势：person = input() --- 注意类型转换
# 4. 判断：按照此规则编写判断条件
# 若满足如下条件之一，则机器获胜
# a. 如果computer == 1 并且 person == 2
# b. 如果computer == 2 并且 person == 3
# c. 如果computer == 3 并且 person == 1
# 若computer == person 则平局
# 否则人获胜
# 引入随机数
import random
# computer = random.randint(1, 3)
try:
    while True:
        computer = random.randint(1, 3)
        person = int(input("请出拳：（1：石头、2：剪刀、3：布）"))
        if person > 3:
            person = (person % 3 + 1)
        if (computer == 1 and person == 2) or \
                (computer == 2 and person == 3) or \
                (computer == 3 and person == 1):
            print("computer win")
        elif computer == person:
            print("dogFall")
        else:
            print("you win")
except ValueError:
    print("您的输入有误！游戏结束！")


