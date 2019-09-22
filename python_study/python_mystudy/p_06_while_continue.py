# 计算1-100之间的所有的数的累加和，50 不能累加
# 1 2 3 4 ...... 50 ...... 100

# index = 1
# my_sum = 0
# while index <= 100:
#     if index !=50:
#         my_sum += index
#     index += 1
# print('最终的结果:%s' % my_sum)

index = 1
my_sum = 0
while index <= 100:

    if index == 50:
        index += 1
        continue
    my_sum += index
    index += 1
print('最终的结果：%s' % my_sum)