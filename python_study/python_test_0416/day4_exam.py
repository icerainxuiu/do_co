import random
import is_leap_year
# 1.	定义两个列表：list1 = ['life','is','short'],   list2 = ['you','need','python']，完成如下操作：
# 1)	输出python及其下标
# 2)	在list1的’is’后添加元素’so’，在list2的’you’后添加’really’
# 3)	将两个列表合并后，排序并输出其长度
# 4)	将list2中的 'python' 改为 'python3'
# 5)	移除之前添加的‘so’和’really’
#
# list1 = ['life', 'is', 'short']
# list2 = ['you', 'need', 'python']
# print("python index is", list2.index("python"))
# list1.insert(list1.index("is") + 1, "so")
# list2.insert(list2.index("you")+1, "really")
# list1.extend(list2)
# print(len(list1))
# n = list2.index("python")
# list2[n] = "python3"
# list1.remove("so")
# list1.remove("really")
# print(list1)

# 2.	先定义一个空列表，通过for循环，使用随机数（数据范围1-100）的生成办法，向列表中添加10个随机整数。累加和
#

# list1 = [random.randint(1, 100) for x in range(10)]
# print(list1)
# result = 0
# for i in list1:
#     result += i
# print(result)
# 3.	在一个拥有10个随机整数的列表中，查找某个整数是否出现，如果有显示该值的索引；若未出现，显示“数据未出现”的提示。
# list1 = [random.randint(1, 10) for x in range(10)]
# print(list1)
# n = int(input("输入1-100之间的数"))
# m = list1.count(n)
# if m == 0:
#     print("数据%s未出现 " % n)
# else:
#     for x in range(len(list1)):
#         if list1[x] == n:
#             print(x)
# 进阶要求：
# 			若数据多次出现，应打印每个数的索引
# 4．从键盘上输入数字（范围1---4），输入若干次，如果输入0，表示输入结束。统计1—4各数字出现的次数。
# 如：输入: 3 4 2 1 4 2 3 0
#          输出： 1:1   2:2   3:2    4: 2
# list2 = []
# while True:
#     n = int(input("输入数字范围1-4"))
#     if n == 0:
#         break
#     if 1 <= n <= 4:
#         list2.append(n)
#     else:
#         print("请重新输入")
# print("1:%s\t2:%s\t3:%s\t4:%s" % (list2.count(1), list2.count(2), list2.count(3), list2.count(4)))
#
# 5．寻找一维数组int num[5]中最大、最小及其坐标位置并打印输出。（数组值从键盘读取）
#
# n = 5
# list1 = []
# while n > 0:
#     m = int(input("输入数"))
#     list1.append(m)
#     n -= 1
# i = max(list1)
# j = min(list1)
# print("最大值是%s，位置是%s" % (i, list1.index(i)))
# print("最小值是%s，位置是%s" % (j, list1.index(j)))


# 6．编写程序，初始化一个double数组，然后把数组内容复制到另一个数组中。
# double source[5](数据从键盘获取)， dest[10]
#
# 方法 1

# n = 1
# list_double = []
# while n <= 5:
#     list_one = []
#     o = int(input("输入第%s组数第一个" % n))
#     p = int(input("输入第%s组数第二个" % n))
#     list_one.append(o)
#     list_one.append(p)
#     list_double.append(list_one)
#     n += 1
# list_three = []
# for a in list_double:
#     list_three.extend(a)
# print(list_double)
# print(list_three)

# # 方法 2
# list_double = [[0 for x in range(2)] for y in range(5)]
# print(list_double)
# n = 0
# for i in range(len(list_double)):
#     for j in range(2):
#         list_double[i][j] = int(input("输入数"))
# list_one = []
# print(list_double)
#
# for o in list_double:
#     list_one.extend(o)
# print(list_one)
#
# 7． 给定某年某月某日，将其转换成这一年的第几天并输出
# year = int(input("请输入年，格式为YYYY:"))
# month = int(input("请输入月:"))
# day = int(input("请输入日:"))
#
#
# day1 = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
# day2 = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
# month1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# if is_leap_year.is_leap_year(year):
#     for x in range(len(month1)):
#         if month == month1[x]:
#             print(day2[x] + day)
# else:
#     for x in range(len(month1)):
#         if month == month1[x]:
#             print(day1[x] + day)

#
# 8．编写程序检查某一个整数中是否有重复的数字，如检查2822中存在重复数字2
# i = str(random.randint(100000000, 1000000000))
# print(i)
# for m in range(10):
#     if i.count(str(m)) > 1:
#         print("重复数字是%s重复次数%s" % (m, i.count(str(m))))

# 9．改写上题，使其可以显示出哪些数字有重复。
# Enter a number: 939577
# Repeated digit(s) : 7 9
#
# 10．改写上题，使其打印一个列表，显示出每个数字在数中出现的次数：Enter a  number: 41271092
# Digit ：          0  1  2  3  4  5  6  7  8  9
# Occurrences:      1  2  2  0  4  0  0  1  0  1
#
# i = str(random.randint(100000000, 1000000000))
# list1 = []
# list2 = []
# for z in range(10):
#     list1.append(z)
# print("随机数i是：", i)
# list1.insert(0, "Digit:\t\t")
# for y in list1:
#     print(y, end='\t')
# print()
# for m in range(10):
#     list2.append(i.count(str(m)))
# list2.insert(0, "Occurrences:")
# for x in list2:
#     print(x, end="\t")

# 设一根铜管 317 15米 和27米 各最小1根，剩余残料最少
# list1 = []
# list2 = []
# for x in range((317 - 27) // 15):
#     # x是15米管数量，y是27米管数量
#     for y in range((317 - 15)//27):
#         if x * 15 + y * 27 < 317:
#             list1.append(x * 15 + y * 27)
#             if (x * 15 + y * 27) == max(list1):
#                 list2.append([x, y])
# print(max(list1))
# for i in range(len(list2)):
#     if (list2[i][0] * 15) + (list2[i][1] * 27) == max(list1):
#         print(list2[i])
# list1 = [[1,2,3],[7,8]]
# list2 = sum(list1,[])
# print(list2)
# list1 = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# list_name = [x+x*i for x in list1 for i in range(1, 10)]
# print(list_name)
