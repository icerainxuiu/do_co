import random
import time
from math import sqrt
# 一个整数， 它加上100后是一个完全平方数，再加上168又是一个完全平方数，问该数是多少
# x + 100 = n * n
# x + 100 + 168 = m * m
# m + n = i , m - n = j , i * j = 168
# m = (i + j)/2 , n = (i - j)/2
# i * j =168 ,j >= 2 , 1 < i < 168/2 + 1
# for i in range(1, 1000):
#     if 168 % i == 0:
#         j = 168 / i
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)
#
# 斐波那契数列


def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fib(10):
    print(x)

# 将一个列表的数据复制到另一个列表中
#
# list1 = [random.randint(1, 100) for x in range(random.randint(1, 10))]
# print("list1 ：%s" % list1)
# list2 = list1[:]
# print("list2 ：%s" % list2)

# 暂停一秒输出

# list1 = [random.randint(1, 100) for x in range(random.randint(1, 10))]
# print(list1)
# for i in list1:
#     print(i)
#     time.sleep(1)

# 暂停一秒输出，并格式化当前时间
#
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 判断101-200之间有多少个素数，并输出所有素数。

# for i in range(101, 201):
#     for j in range(2, int(sqrt(i))):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于
# 该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# for i in range(100, 1000):
#     j = str(i)
#     if int(j[0]) ** 3 + int(j[1]) ** 3 + int(j[2]) ** 3 == i:
#         print(i)
#
# for n in range(100, 1000):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)

# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示。
# x = int(input("输入1个数"))
#
# m = "A" if x >= 90 else ("B" if x >= 60 else "C")
# print(m)

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# x = int(input("请输入几个数相加"))
# m = random.randint(0, 9)
# list1 = [str(m) * (i + 1) for i in range(x)]
# print(list1)
# result = 0
# for i in list1:
#     result += int(i)
# print(result)

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？
# x = 100.00
# sum1 = 0.0
# for n in range(10):
#     sum1 += x
#     print("共经过%s 米" % sum1)
#     x /= 2
#     print("第%s次落地反弹%s 米 " % (n+1, x))

# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又
# 将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的
# 一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# x2 = 1
# for day in range(9):
#     x1 = (x2 + 1) * 2
#     x2 = x1
# print(x1)
