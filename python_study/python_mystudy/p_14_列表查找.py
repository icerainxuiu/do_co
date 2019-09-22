my_list = [10,20,30,40]
# index 用于根据值查询，如果查询失败，则会报错,查询成功返回值的位置
old_value = 20

new_value = 200
if old_value in my_list:
    pos = my_list.index(old_value)
    my_list[pos] = new_value
print(my_list)
# 列表2 插入列表1尾部
my_list2 = ['aaa','bbb','ccc']
my_list.extend(my_list2)
print(my_list)

 