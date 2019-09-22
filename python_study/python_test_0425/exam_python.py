# 1.	从键盘上读取若干字母字符，全部转化为大写字符后存入文件dest.txt，当输入exit时停止输入。
#
# f = open("1.txt", "w")
# while True:
#     s = input("输入")
#     if s == "exit":
#         break
#     s1 = s.upper()
#     f.write(s1 + "\n")
#
# f.close()
#
# 2.	实现文件的复制（三种方法实现文件复制：read()、readline()、readlines()）。
#
# f1 = open("1.txt", "r")
# f2 = open("2.txt", "w")
# s1 = f1.read()
# f2.write(s1)
# f1.close()
# f2.close()
#
# f1 = open("1.txt", "r")
# f3 = open("3.txt", "w")
# s2 = f1.readline()
# f3.write(s2)
# f1.close()
# f3.close()
#
#
# f1 = open("1.txt", "r")
# f4 = open("4.txt", "w")
# s3 = f1.readlines()
# print(s3)
# f4.write(str(s3))
# f1.close()
# f4.close()


# os模块练习：
# 1.	创建一个目录newdir并切换到该目录下，切换完成后调用getcwd()显示以下工作目录的信息。
# import os
# os.mkdir("./new_dir")
# os.chdir("./new_dir")
# print(os.getcwd())


# 2.	手动在newdir目录下创建3个文件test_1.txt、test_2.txt、test_3.txt，修改文件名称，
# 在三个文件名前均添加“bkup_”信息。
# import os
# print(os.listdir("./"))
# if not os.listdir("./"):
#     for i in range(3):
#         filename = "test_%d.txt" % i
#         open(filename, "w")
# else:
#     for file in os.listdir("./"):
#         os.rename(file, "backup_" + file)

# os.chdir("./new_dir")
# with open("test_1.txt", "w") as f:
#     f.write("hello")
# with open("test_2.txt", "w") as f1:
#     f1.write("hello")
# with open("test_3.txt", "w") as f2:
#     f2.write("hello")
#
# os.rename("test_1.txt", "bkup_test_1.txt")
# os.rename("test_2.txt", "bkup_test_2.txt")
# os.rename("test_3.txt", "bkup_test_3.txt")

# 选做：文件操作—文件的缓冲类别
# 文件操作时，会将文件从磁盘读入内存，为了提高操作效率，在内存中会开辟缓存，保存文件数据，
# 实际加工的数据其实是内存中的数据，若对文件进行写操作，其实也是写入内存，
# 当满足某个条件时再对实际文件更新（即更新实际的文件有更新条件的）
# 文件缓冲区的类别决定了更新时机，文件缓冲常见的有两种：
# 1.	行缓冲：当要写入文件的数据中包含换行符时，将进行更新，如果不包含换行符，将数据留存在内存中不向实际文件更新。
# 标准输入文件是行缓冲文件，即print()输出的内容不包含’\n’时是不会自动将内容写到屏幕上的。
# 2.	全缓冲：当缓冲区满后，再进行文件更新。普通的文件是全缓冲文件。
# 上面说到的是两类缓冲形式是对应文件默认的更新操作，若想主动更新文件，可以通过flush()方法实现，
# 即若想主动将缓冲区中的内容更新到文件可以使用文件对象f调用flush()方法：f.flush()
# 3.	向日志文件存储数据。日志文件中存储的数据如下：
#       ID year-month-day hour:mintue:second
# 1) 若日志文件不存在则id从1开始，每隔一秒向文件写入一条信息并且向屏幕显示数据
# 2) 若日志文件已经存在则本次运行程序写入的内容中id值应该累加
# 第一次运行：
#     1  2019-04-20  10:10:20
#     2  2019-04-20  10:10:21
# 第二次运行：
#     3  2019-04-20  10:20:19
#     4  2019-04-20  10:20:20
# 提示：使用time模块中的strftime()函数获取当前时间信息，使用time模块中的sleep()函数实现延时1秒，参考代码如下：
# # 导入time模块
# import time
# # 调用strftime()显示时间信息
# time.strftime("%Y-%m-%d %H:%M:%S")
# # 调用sleep()暂停1秒
# time.sleep(1)
#
# import time
#
# f = open("day_log.txt", "a+")
# list1 = f.readlines()
# id_num = len(list1)
# while True:
#     id_num += 1
#     now_time = time.strftime("%Y-%m-%d %H:%M:%S")
#     f.write(str(id_num) + "\t" + now_time + "\n")
#     f.flush()
#     print(str(id_num) + "\t" + now_time + "\n", end="")
#     time.sleep(1)
#
#
#
# print(time.strftime("%Y-%m-%d %H:%M:%s"))
# s = time.strftime("%Y-%m-%d %H:%M:%S")
# print(s)






#
#
# class Animal(object):
#     type = "狗"
#
#     def __init__(self, name):
#         self.name = name
#         __age = 0
#
#     def eat(self):
#         print("狗吃骨头")


