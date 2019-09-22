# # 1.计算1-100之间的累加和，并且去除50.
#
# index = 0
# my_sum = 0
# while True:
#     if index >100:
#         break
#     if index == 50:
#         index += 1
#         continue
#
#     my_sum += index
#     index += 1
# print(my_sum)
# # 2.简易版的员工管理系统
# # 2.1 接收用户输入
# # 2.1.1 输入1：展示所有的员工信息
# # 2.1.2 输入2：新增一个员工信息
# # 2.1.3 输入3：修改一个员工信息
# # 2.1.4 输入4：删除一个员工信息
# # 2.1.5 输入5：退出员工管理系统
#
# # 显示系统菜单
# print('欢迎您使用【员工管理系统v1.0】')
# while True:
#     print('*' * 10 + '操作菜单' + '*' * 10)
#     print('1.展示所有员工信息')
#     print('2.新增一个员工信息')
#     print('3.修改一个员工信息')
#     print('4.删除一个员工信息')
#     print('5.退出员工管理系统')
#     print('*' * 27)
#     # 保存用户输入操作
#     user_opration = int(input('请输入您的操作：'))
#     if user_opration == 1:
#         print('姓名\t年龄\t性别')
#         print('如花\t59\t男')
#         print('小花\t19\t女')
#         print('狗剩\t20\t男')
#     elif user_opration == 2:
#         name = input('请输入新员工姓名：')
#         age = input('请输入新员工年龄：')
#         sex = input('请输入员工性别：')
#     elif user_opration == 3:
#         name = input('请输入您要修改的员工姓名：')
#         print('员工 %s 的信息修改成功' % name)
#     elif user_opration == 4:
#         name = input('请输入您要删除的员工姓名：')
#         print('员工 %s 的信息删除成功' % name)
#     elif user_opration == 5:
#         print('退出系统成功！')
#         print('欢迎再次使用本系统！')
#         break
#     else:
#         print('输入有误！')



import random
while True:
    user_quan = int(input('请出拳 石头(0)、剪刀(1)、布(2)、退出游戏(3):'))
    if user_quan == 3:
        print('欢迎您下次再玩猜拳游戏！')
        break
    computer_quan = random.randint(0,2)
    if (user_quan == 0 and computer_quan == 1) or \
            (user_quan == 1 and computer_quan == 2) or \
            (user_quan == 2 and computer_quan == 0):
        print('您赢了！')
    elif user_quan == computer_quan:
        print('平局')
    else:
        print('您输了！')