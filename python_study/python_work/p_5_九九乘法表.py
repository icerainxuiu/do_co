# i = 0
# j = 0
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (j, i, i * j), end='\t')
# #     print()
# # 行与列的不同
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d" % (i, j, i * j), end='\t')
    print()
#

#
# def sum_b(num):
#     # for i in range(1, 10):
#     #     print(i * num, end=' ')
#         # print(i, end='')
#     # s1 = []
#     if num == 1:
#         return 1
#     temp = sum_b(num - 1)
#     return num * temp
#
#
# result = sum_b(5)
# print(result)
