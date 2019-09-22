import random
import sys

# def main(num1, num2):
#     """
#     两数的加法和减法
#     :param num1: 被减数，加数
#     :param num2: 减数，加数
#     :return: 返回差值及和值
#     """
#     return num2 - num1, num2 + num1
#
#
#
#
# if __name__ == '__main__':
#     num1 = int(input("输入数1"))
#     num2 = int(input("输入数2"))
#     diff_num, add_num = main(num1, num2)
#     print("数1数2相加值为：", add_num)
#     print("数2减数1差值为：", diff_num)

# list1 = [random.randint(1, 100) for x in range(10)]
# # list1 = [0,1,1,2,3,4,4,0]
# print(list1)
# def set_extreme(local_list):
#     """
#     将列表中的最大值，最小值和0，1号位置的元素交换
#     :param local_list:
#     :return: 返回原0，1位置的元素
#     """
#     i = local_list.index(max(local_list))
#     j = local_list.index(min(local_list))
#     local_list[0], local_list[1], local_list[i], local_list[j] =\
#         max(local_list), min(local_list), local_list[0], local_list[1]
#     return local_list[i], local_list[j]
# z = set_extreme(list1)
# print(list1)
# print(z)


# def print_s(str1):
#     print("string", str1)
#
#
# def print_i(int1):
#     print("int1", int1)
#
#
# def print_info(f, values):
#     f(values)
#
#
# print_info(print_i, 8)


def num_add(num):
    if num == 1:
        return 1
    else:
        return num * num_add(num -1)

print(num_add(5))
# 判断 x 是否大于0
# f = lambda x: x > 0
# # 定义匿名函数两数相加
# f1 = lambda x,y : x + y
# f(1)
# print(f(0))
# f1(1,2)
# print(f1(1,2))