import random
from os import sys
import time
# 1.	函数返回多个值：定义一个函数实现整数的四则运算calculate(num1, num2)，要求返回4个值，
# 返回值是 + - * /的结果。函数调用后分别用1个变量和4个变量接收函数的返回值。
# 进阶要求：定义四个函数分别实现整数的加、减、乘、除运算
#           定义一个函数cal(func, a, b)
# 		  四个参数的含义是：func：表示执行运算的函数名称
# 								a和b：执行运算的操作数
# 		通过调用cal()函数实现算数运算
# def calculate(num1, num2):
#     add_num = num1 + num2
#     diff_num = num1 - num2
#     by_num = num1 * num2
#     if num2:
#         div_num = num1 / num2
#     else:
#         print("除数不为0")
#     return add_num, diff_num, by_num, div_num
#
# def add_num(num1, num2):
#     return num1 + num2
# def diff_num(num1, num2):
#     return num1 - num2
# def by_num(num1, num2):
#     return num1 * num2
#
# def div_num(num1, num2):
#     if num2:
#         return num1 / num2
# def cal(fun, a, b):
#     return fun(a, b)


# 2.	lambda表达式：定义lambda表达式并调用：
# 1). 判断一个整数是奇数还是偶数
# 2). 实现对一个整数的乘以10操作
# 3). 实现两个整数的相加
# f = lambda x:x%2
# f1 = lambda x:x * 10
# f2 = lambda x, y:x +  y


# 3.	可变参数：编写函数，实现求多个数据的最大及最小值操作（mymax(*args)、mymin(*args)）
# ，要求：(不可调用max()、min()函数)
# o	求若干个数据中的最大、最小值（使用可变参数实现）
# def mymax(*args):
#     max_num = args[0]
#     for x in range(len(args)):
#         if args[x] > max_num:
#             max_num = args[x]
#     return max_num
#
# def mymin(*args):
#     min_num = args[0]
#     for x in range(len(args)):
#
#         if args[x] < min_num:
#             min_num = args[x]
#     return min_num
#
# list1 = [random.randint(1, 10) for x in range(10)]
# m = mymax(1,2,3,4,5)
# print(m)
# 进阶：
# 1.	可以使用函数名作为参数：定义三个函数
# 1).sum_even(n)：求0-n之间偶数的和
# 2). sum_odd (n)：求1-n之间奇数的和
# 3). sum_nums(func, n)：该函数可用于求取偶数或奇数的和。本函数第一个参数为函数，
# 表示要调用sum_even还是调用sum_odd，第二个参数为计算和值的变量。
# def sum_even(n):
#     sum_num = 0
#     for i in range(1,n+1):
#         if not i % 2:
#           sum_num += i
#     return sum_num
#
#
#
# def sum_odd(n):
#     sum_num = 0
#     for i in range(1, n+1):
#         if i % 2:
#             sum_num += i
#     return sum_num
#
# def sum_nums(func, n):
#     return func(n)
#
#
# print(sum_even(10))
# print(sum_odd(10))
#




# 2.	lambda表达式、可变参数、列表拆包：修改“编写函数，实现求多个数据的最大及最小值操作（mymax()、mymin()）”，
# 要求只定义一个函数就实现求最大及最小数操作。定义lambda表达式，完成数据比较。
# def max_min(*args):
#     max_num = args[0]
#     min_num = args[0]
#     for x in range(len(args)):
#         if args[x] > max_num:
#             max_num = args[x]
#     for x in range(len(args)):
#         if args[x] < min_num:
#             min_num = args[x]
#     return max_num, min_num

# def max_min(*args):
#     max_num = args[0]
#     min_num = args[0]
#     f = lambda x,y: x < y
#     for i in range(len(args)):
#         if f(max_num, args[i]):
#             max_num = args[i]
#         if f(args[i], min_num):
#             min_num = args[i]
#     return max_num, min_num
#
# list1 = [random.randint(1,100) for x in range(10)]
#
# print(max_min(*list1))
# 3.	变成实现print()的功能

def print_see(*objects, sep=None, end=None,file=None,flush=False):
    if sep is None:
        sep = " "
    if end is None:
        end = "\n"
    if file is None:
        file = sys.stdout
    file.write(sep.join(map(str, objects))+end)
    if flush:
        file.flush()
a = "0............a"
b = 1
a1 = {"a":"bm","b":"aa"}
print_see (a, "abc", sep="-")
print_see(("a", "b"))
print_see(a1)

