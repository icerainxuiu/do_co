import random
"""
生成1-100的顺序随机且不重复的100个数的列表
"""

list1 = list()
while len(list1) < 100:
    num_in_list = random.randint(1, 100)
    if num_in_list not in list1:
        list1.append(num_in_list)
