# # sum1 = 0
# # for i in range(0,101,2):
# #     sum1 = sum1 + i
# # print(sum1)
#
#
# def my_range():
#     print('计算偶数和,左闭右开区间：')
#     left = int(input('请输入起始数字：'))
#     print(id(left))
#     right = int(input('请输入结束数字：'))
#     print(id(right))
#     if left % 2 == 0:
#         sum1 = 0
#         print(id(sum1))
#         for i in range(left, right, 2):
#             print(id(i))
#             sum1 = sum1 + i
#         print(sum1)
#     else:
#         left = left + 1
#         sum1 = 0
#         for i in range(left, right, 2):
#             sum1 = sum1 + i
#         print(sum1)
#
#
# my_range()
# 计算奇数和偶数和


def sum_math():
    sum1 = 0
    left = int(input('输入值：'))
    right = int(input('输入值：'))
    for i in range(left, right + 1):
        if i % 2 == 0:  # 模3为0可以求逢三倍数之和
            continue  # 将continue 和else 去掉就是求偶数和
        else:
            sum1 += i
    print(sum1)


sum_math()