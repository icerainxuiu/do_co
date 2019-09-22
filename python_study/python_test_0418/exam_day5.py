# 练习：字典
# 1.
# 定义字典元素的列表：stds_list = [
#     {"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
#     {"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
#     {"id": 3, "name": "小东", "c_s": 79, "python_s": 83},
# ]
# 1)    显示学生信息：“学生id：学生姓名：小明，C语言成绩：85, Python成绩：78”。
# 2)    修改“小明”的Python成绩为90
# 3)    删除“小东”的信息

# stu_list = [
#     {"id": 1, "name": "小明", "C_s": 85, "python_s": 78},
#     {"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
#     {"id": 3, "name": "小东", "c_s": 79, "python_s": 83}
# ]
# dict1 = stu_list[0]
# dict2 = stu_list[1]
# dict3 = stu_list[2]
# print("学生ID:%s,学生姓名：%s,C语言成绩：%s,Python成绩%s" % (dict1["id"], dict1["name"], dict1["C_s"], dict1["python_s"]))
# dict1["python_s"] = 90
# dict3.clear()
# print(dict1)
# print(dict3)
#

# 2.
# 定义一个空列表，用于保存5个学生信息，一个学生信息包括三个属性：id、姓名、年龄
# 提示：列表元素是字典、向列表中添加数据用append()
#
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
# 练习 ：
# 1.
# 从键盘上获取信息，判断是否可转换为数字，如果是，转换为整数。

# n = input("请输入数字")
# if n.isdecimal():
#     print("n=", int(n))
# else:
#     print("输入有误")

# 2.
# 输入一行字符, 统计其中有多少个单词，每两个单词之间以空格隔开。如输入: This is a Python program.
# 输出：There are 5 words in the line
# str1 = input("输入一行英文单词")
# print("There are %s words in the line" % (str1.count(" ") + 1))
# 3.
# 计算字符串最后一个单词的长度，单词以空格隔开。（使用input()
# 输入一个句子）
#
# str1 = input("输入一行英文单词")
# str2 = str1.split(" ")
# print(len(str2[-1]))
# print(str2)

#
# 4.
# 从键盘输入一句话，输入的信息两端有空白字符。“  Life is short, you
# need
# python!   ”除去两端的空白字符，查找其中的python，将其替换为python3。
#

# s = input(" 输入一段前后含用空格的话")
# s1 = s.strip()
# print(s1)
# print("python's index is:", s.index("python"))
# s2 = s1.replace("python", "python3")
# print(s2)

# 5.
# 完成字符串的逆序以及统计：
# 现有字符串： str1 = '1234567890'，根据题目要求，将截取后的新字符串赋值给str2
# 截取字符串的第一位到第三位的字符
# 截取字符串最后三位的字符
# 截取字符串的全部字符
# 截取字符串的第七个字符到结尾
# 截取字符串的第一位到倒数第三位之间的字符
# 截取字符串的第三个字符
# 截取字符串的倒数第一个字符
# 截取与原字符串顺序相反的字符串
#
# str1 = '1234567890'
# str2 = str1[0:3]
# print(str2)
# str2 = str1[-3:]
# print(str2)
# str2 = str1[:]
# print(str2)
# str2 = str1[6:]
# print(str2)
# str2 = str1[:-3]
# print(str2)
# str2 = str1[2:3]
# print(str2)
# str2 = str1[-1:]
# print(str2)
# str2 = str1[::-1]
# print(str2)


# 6.
# 倒序遍历字符串”helloworld” (用三种方法实现)
# s = "helloworld"
# 方法 1 切片
# s1 = s[::-1]

# 方法2 列表逆序
# s3 = list(s)
# s3.reverse()
# s4 = ""
# for x in s3:
#     s4 += x
# print(s4)
# print(s1)

# 方法3 循环
# y = ""
# for x in range(len(s)-1, -1, -1):
#     y += s[x]
# print(y)

# 方法4 字符相加
# s = "helloworld"
# y = ""
# for z in s:
#     y = z + y
# print(y)
# 方法5 join反转连接
# s = "helloworld"
# y = (''.join(reversed(list(s))))
# print(y)

# 7.
# 请将s = 'aAsmr3idd4bgs7Dlsf9eAF'，字符串的数字取出，并输出成一个新的字符串
# s = 'aAsmr3idd4bgs7Dlsf9eAF'
# x = ''
# for i in s:
#     if i.isdecimal():
#         x += i
# print(x)

# 8.
# 定义字符串line = 'I am a beautiful girl'，变化为：girl beautiful a am I
# 进阶：如果句子尾端带有标点符号，例如I am a beautiful girl！ 带有叹号，则结果中的叹号也应该出现在句子的尾端
# girl beautiful a am I！
# line = 'I am a beautiful girl'
# x = line.split(" ")
# print(x)
# x.reverse()
# x = " ".join(x)
# print(x)
# line = 'I am a beautiful girl!'
# x = line[-1]
# y = line[:-1]
# y = y.split(" ")
# y.reverse()
# y = ' '.join(y)
# y = y + x
# print(x)
# print(y)
