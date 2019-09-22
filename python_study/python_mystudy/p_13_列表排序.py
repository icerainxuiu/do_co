import random

my_list = []

i = 0
while i < 10:
    random_number = random.randint(1,100)
    my_list.append(random_number)
    i += 1
print(my_list)
# 函数逆序
my_list.reverse()
print(my_list)
# 函数从小到大排序
my_list.sort()
print(my_list)
# 函数从大到小排序 关键字参数
my_list.sort(reverse=True)
print(my_list)
