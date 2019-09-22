# 1. 循环5次输入输出
# i = 1
# while i <= 5:
#     j = input("输入数")
#     print(j)
#     i += 1
#
#
# 2. 输出1-10之内的奇数
# i = 1
# while i <= 10:
#     if i % 2:
#         print(i, end='   ')
#     i += 1
#
# 3. 计算俩个数的累加和
# num_a = int(input("输入数1"))
# num_b = int(input("输入数2"))
# sum1 = 0
# if num_a < num_b:
#     while num_a <= num_b:
#         sum1 += num_a
#         num_a += 1
#     print(sum1)
# elif num_a == num_b:
#     sum1 = num_a + num_b
#     print(sum1)
# else:
#     while num_a >= num_b:
#         sum1 += num_a
#         num_a -= 1
#     print(sum1)

# 4. 输入1个大于等于0的整数，判断这个数是几位数
# num = int(input("请输入1个大于等于0的整数"))
# i = 1
# # 判断 该数对10的幂取商是否大于10
# while num / (10 ** i) >= 1:
#     i += 1
# print("这是个%s 位数！" % i)


# 5.输入两个数，计算两个数范围内的偶数和
# 方法1：
# num_a = int(input("数1"))
# num_b = int(input("数2"))
# max_num = 0
# min_num = 0
# result = 0
# if num_a >= num_b:
#     max_num = num_a
#     min_num = num_b
# if num_a < num_b:
#     max_num = num_b
#     min_num = num_a
# while min_num <= max_num:
#     if min_num % 2 == 0:
#         result += min_num
#     min_num +=1
# print(result)
# #
# 方法2：
# num_a = int(input("数1"))
# num_b = int(input("数2"))
# list1 = list()
# list1.append(num_a)
# list1.append(num_b)
# list1.sort()
# result = 0
# for i in range(list1[0], list1[-1] + 1):
#     if not i % 2:
#         result += i
# print(result)

# 方法3：
# num_a = int(input("数1"))
# num_b = int(input("数2"))
# result = 0
# while num_a <= num_b:
#     result += num_a if not (num_a % 2) else 0
#     num_a += 1
# print(result)

# 1 - 100 之间能被5 整除的数累加和
# n = 1
# sum1 = 0
# while n <= 100:
#     if n % 5 != 0:
#         n += 1
#         continue
#     sum1 += n
#     # print(n)
#     n += 1
# print(sum1)

# n = 1
# result = 0
# while n <= 100:
#     result += n if n % 5 == 0 else 0
#     n += 1
# print(result)

# 打印1-10 除5之外的数
# n = 0
# while n <= 10:
#     if n == 5:
#         n += 1
#         continue
#     print(n)
#     n += 1

# # 打印9行小星星

# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#     print()
#     row += 1

# row = 1
# while row <= 9:
#     print("*" * row)
#     row += 1
# 打印99乘法表
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%s*%s=%s" % (col, row, row * col), end="\t")
#         col += 1
#     print()
#     row += 1
#


# row = 1
# while row <= 9:
#     col = 9
#     while row <= col:
#         print("*", end=" ")
#         col -= 1
#     print()
#     row += 1

# n = 5
# for i in range(n):
#     for m in range(n-1-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("*", end="")
#     print()
# for i in range(n):
#     for m in range(i+1):
#         print(" ", end="")
#
#     for j in range(2*(n-i)-1):
#         print("*", end="")
#
#     print()
#
# for i in range(10):
#     for j in range(0, 10 - i):
#         print(end=" ")
#     for k in range(10 - i, 10):
#         print("$", end=" ")
#
#     print("")

# def sum_num(num1, num2):
#     """两个数求和"""
#     result = num1 + num2
#     print("%s+%s=%s" % (num1,num2,result))
#
#
# num1 = int(input("输入数1"))
# num2 = int(input("输入数2"))
# sum_num(num1, num2)
#


# 循环练习：
# 1.	从键盘上输入两个正整数，判断在这两个整数之间的范围内，哪些是奇数
# num1 = int(input("请输入正整数："))
# num2 = int(input("请输入正整数："))
# min_num = num1 if num1 <= num2 else num2
# max_num = num1 if num1 > num2 else num2
# while min_num <= max_num:
#     if min_num % 2 != 0:
#         print(min_num)
#     min_num += 1

# 2.	判断一个正整数有多少位，例如375有3位， 1000有4位， 0有1位
# num = int(input("请输入1个大于等于0的整数"))
# i = 1
# # 判断 该数对10的幂取商是否大于10
# while num / (10 ** i) >= 1:
#     i += 1
# print("这是个%s 位数！" % i)

# 3. 统计一个自然数的二进制表示形式中有多少个 1
#
# num = int(input("输入1个自然数"))
# n = 0
# while num > 0:
#     if num % 2 == 1:
#         n += 1
#     num = num // 2
# print(n)

# 4. 判断1-100的数字里有多少个9
# n = 1
# i = 0
# while n <= 100:
#     if n % 10 == 9:
#         i += 1
#     if n / 10 == 9:
#         i += 1
#     n += 1
# print(i)
#
# 练习：break continue练习
# 	基础：
# 1.	循环输入若干个数，当输入0时，停止输入。
# 提示：使用循环结构，在循环结构中判断数据为0时，通过break退出循环。
# 进阶要求2：在停止输入时，输出读取到的数中的最大值。
# max_num = 0
# while True:
#     num = int(input("输入一个大于0的数，为'0'退出:"))
#     if num == 0:
#         print("最大值是%s" % max_num)
#         break
#     max_num = num if num > max_num else max_num

# 2.	计算1-10的累加和时不把5计算在内。
# n = 1
# result = 0
# while n <= 10:
#     result += n
#     if n == 5:
#         n += 1
#         continue
#     n += 1
# print(result)
#
# 进阶：循环嵌套
# TODO
# 1.	求1-100的素数：只有1和其本身为约数的数就是素数，最小的素数是2
#
# i = 2
# while i <= 100:
#     j = 2
#     while j <= i - 1:
#
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         print(i)
#     i += 1

# 函数练习：
# 基础：
# 1.	定义一个函数is_even(n)，判断数据n是否为偶数，若是偶数，函数的返回值为True，若不是偶数，则函数的返回值为False

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# n = is_even(99)
# print(n)
# 进阶：
# 2.	编写一个函is_leap_year(year)，判断参数year是不是闰年，如果year是闰年则返回1，否则返回0。
# 判断依据：如果某年份能被4整除，但不能被100整除，那么这一年就是闰年，此外，能被400整除的年份也是闰年。
# def is_leap_year(year):
#     if ((year % 4 == 0) and (year % 100 != 0)) or (year % 100 == 0 and year % 400 == 0):
#         return 1
#     else:
#         return 0
#
#
# a = is_leap_year()
# print(a)
# 综合练习：
# 	基础：
# 1.	编写函数judge_arr(start, end)用于判断start到end范围中的数据哪些是偶数
# 		要求在该函数中调用is_even(n)函数判断某个数是不是偶数
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def judge_arr(start, end):
#     while start <= end:
#         n = start
#         m = is_even(n)
#         print("%s是不是偶数%s" % (n, m))
#         start += 1
#
#
# judge_arr(10, 20)


# 2.	定义函数实现如下功能，读若干整数，直到输入0停止读取。停止输入后，程序报告输入的偶数（不包括0）总个数以及偶数的平均值，奇数的个数及平均值。
# 提示：会用到break关键字
# def fun():
#     n, i, j, sum1, sum2, avg1, avg2 = 1, 0, 0, 0, 0, 0, 0
#     while n > 0:
#         m = int(input("输入数，输入0停止输入"))
#         if m == 0:
#             print("偶数个数为%s，平均值为%s" % (i, avg1))
#             print("奇数数个数为%s，平均值为%s" % (j, avg2))
#             break
#         if m % 2 == 0:
#             sum1 += m
#             i += 1
#             avg1 = (sum1 / i)
#         if m % 2 != 0:
#             sum2 += m
#             j += 1
#             avg2 = (sum2 / j)
#         n += 1
#
#
# fun()

# 练习：
# 把自己写的is_even(n)、is_leapyear(year)函数放到一个模块文件中，供应用程序使用
#
