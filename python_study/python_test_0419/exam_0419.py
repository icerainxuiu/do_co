import random

# 1.	定义函数sum_nums(start, end)实现指定范围的数据的累加（数据范围的初始值和终止值由函数参数给出）。


# def sum_num(start, end):
#     if start < end:
#         list1 = [x for x in range(start, end+1)]
#         sum_add = sum(list1)
#         return "%s-%s之间的累加和是%s" % (start, end, sum_add)
#     else:
#         return "输入有误"
#
#
# print(sum_num(1, 100))

# 2.	全局变量的修改：定义全局变量g_num、g_bool（初值为False），定义函数mod_global_var()函数，
# 当g_num的值为奇数时，将g_bool修改为True， 当g_num的值为偶数时，将g_num的值修改为False。
# g_num = int(input("输入一个值"))
# g_bool = False
#
#
# def mod_global_var():
#     global g_num
#     global g_bool
#     if not g_num % 2:
#         print("g_bool:", g_bool)
#     else:
#         g_bool = True
#         print("g_bool:", g_bool)

# 3.	可变类型数据作为函数参数时，在函数中可能修改实参内容：随机生成一个拥有10个整数（范围1-100）的列表
# 。定义一个函数，实现将列表中的最大值放在列表的索引0位置。
# 如果传入函数的是一个元组，能够改变元组的内容吗？
# 提示：可以使用max()函数求列表中的最大值
# 		找到最大值的索引值
# 	   将最大值和索引0位置上的值交换

# def change_num():
#     list1 = [random.randint(1,100) for x in range(10)]
#     print(list1)
#     for i in range(len(list1)):
#         if list1[i] == max(list1):
#             print(i)
#             list1[i], list1[0] = list1[0], list1[i]
#     print(list1)
#
#
# change_num()

# 4.	写函数，检查传入列表的长度，如果大于2，那么仅保留前两个元素。

# def check_len():
#     list1 = [random.randint(1, 10) for x in range(random.randint(1, 10))]
#     print(list1)
#     list2 = []
#     if len(list1) > 2:
#         list2.extend(list1[:2])
#         print(list2)
#
#
# check_len()

# 5.	将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
# 提示：对字符串进行分割，拆成k:1的样子
# 	  对k:1再进行分割，冒号之前的内容作为键，冒号后的内容作为值
#
# str1 = "k:1|k1:2|k2:3|k3:4"
# str2 = str1.split("|")
# print(str2)
# list1 = []
# for i in str2:
#     str3 = i.split(":")
#     list1.append(str3)
# print(list1)
# dict1 = dict(list1)
# print(dict1)
