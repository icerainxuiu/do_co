import random


# var_list = [random.randint(1, 10) for i in range(10)]
# var_tuple = tuple(var_list)
# print("var_tuple:", var_tuple)
# m = list()
# n = int(input("请输入1个待查寻数字："))
# if var_tuple.count(n) > 0:
#     for x in range(len(var_tuple)):
#         if var_tuple[x] == n:
#             m.append(x)
#     print("result_index:%s" % m)
# else:
#     print("%s 在var_tuple 中不存在" % n)
#
# start = 0
# result_index = list()
# for i1 in range(var_tuple.count(n)):
#     index = var_tuple.index(n, start)  # 查询次数由出现次数决定，
#     # 查询起始位置由开始，第二次由找到的索引位置+1开始
#     result_index.append(index)
#     start = index + 1
# print("result_index:%s" % m)

# name_dict = {}

# name = input("输入学生姓名")
# age = int(input("输入学生年龄"))
# gender = (input("输入学生性别"))
# name_dict.setdefault("name")
# std_info.setdefault("age")
# std_info.setdefault("gender")
# name_dict["name"] = name
# std_info["age"] = age
# std_info["gender"] = gender
# std_info.update(name_dict)
# std_info = {'age': 35, 'gender': '男', 'name': '司马狗剩', "height": "18.9"}
# list1 = list()
# for item in std_info.items():
#     list1.append(item)
# for key_value in list1:
#     if key_value[1] == 35:
#         print(key_value[0])


# list1 = list()
# time = 3
# while time > 0:
#     dict_stu = {}
#     print(id(dict_stu))
#     name = input("输入姓名")
#     age = input("输入年龄")
#     gender = input("输入性别")
#     dict_stu["name"] = name
#     dict_stu["age"] = age
#     dict_stu["gender"] = gender
#     print(id(dict_stu))
#
#     list1.append(dict_stu)
#     print(id(list1[0]))
#     time -= 1
# print(list1)

# n = input("请输入数字")
# if n.isdecimal():
#     print("n=", n)
# else:
#     print("输入有误")

# s = "Life is short , you need python!"
# print("python's index is:", s.index("python"))
# s1 = s.replace("python", "python3")
# print(s1)
