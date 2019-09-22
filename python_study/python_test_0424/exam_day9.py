# 1.	定义一个Employee类：
# def __init__(self, name, job = None, pay = 0):
# 		pass
# #加薪的方法， percent为加薪比例，可能为0.1
# 	def giveraise(self, percent):
# 		pass
# 	def __str__(self):
#     		return '[Person: %s, %d]' % (self.name, self.pay)
# 再定义一个Manager类，实现其中的giveraise()方法，对于Manager来说，除了percent的固定加薪外，还要额外奖励bonus：
# 	def giveraise(self, percent, bonus = 0.1):
# 	pass
#


# class Employee(object):
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#
#     def give_raise(self, percent):
#         self.pay = self.pay * (1 + percent)
#
#     def __str__(self):
#         return "[Person: %s, %d]" % (self.name, self.pay)
#
#
# class Manager(Employee):
#     def give_raise(self, percent, bonus = 0.1):
#         self.pay = self.pay * (percent + bonus + 1)
#

# 2.	体验多态：定义Person类（该类中定义work()方法）
# 定义Employee类继承自Person类，Employee类中定义work()方法，表示员工工作，定义Stu类，
# 继承自Person类，Stu类中定义work()方法，表示学生实习
# 定义Company类，该类中定义do_work(self, who)方法，根据who传入对象的不同调用不同类中的work()方法
#
# class Person(object):
#     def work(self):
#         print("每个人都要工作")
#
#
# class Employee(Person):
#     def work(self):
#         print("员工工作")
#
#
# class Stu(Person):
#     def work(self):
#         print("学生实习")
#
#
# class Company:
#     @staticmethod
#     def do_work(self, who):
#         who.work()


# 3.		定义Stu类，该类中定义类属性count记录目前已有的学生的数量，要求在类外不可以直接打印count的值，
# Stu要提供查看count值的方法，当学生毕业的时候（对象消亡）的时候，减少count的数量。
# 进阶：定义Class类，该类中将记录属于本班级的学生，能够把学生的姓名都打印出来。

# class MyClass(object):
#     list1 = list()
#     @staticmethod
#     def count_stu():
#         for i in MyClass.list1:
#             print(i, end="")
#         print()
#
#
# class Stu(MyClass):
#     __count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Stu.__count += 1
#         MyClass.list1.append(self.name)
#
#     @staticmethod
#     def show_count():
#         print("学生数量%s" % Stu.__count)
#
#     def __del__(self):
#         Stu.__count -= 1
#         print("学生数量", Stu.__count)
#
#
# xiaoming = Stu("小明")
# xiaoli = Stu("小李")
# Stu.show_count()
# MyClass.count_stu()

# 4.	先定义一个父类SchoolMember，对象初始化时拥有name、age两个属性
# 父类定义一个print_info()方法，用于显示对象属性值。
# 再分别定义两个子类Teacher、Student
# Teacher子类对象除了拥有name、age属性外，还拥有salary属性
# Student子类对象除了拥有name、age属性外，还拥有stdid属性
# 两个子类中也定义print_info()方法，显示name、age及各自拥有的salary或stdid属性。
#
# class SchoolMember(object):
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         SchoolMember.count += 1
#
#     def print_info(self):
#         print("name: %s ,age: %s" % (self.name, self.age))
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         SchoolMember.count += 1
#
#     def print_info(self):
#         super().print_info()
#         print("%s 工资 %s" % (self.name, self.salary))
#
#
# class Student(SchoolMember):
#     def __init__(self, name, age, stdid):
#         self.name = name
#         self.age = age
#         self.stdid = stdid
#         SchoolMember.count += 1
#
#     def print_info(self):
#         super().print_info()
#         print("%s ID %s" % (self.name, self.stdid))
#
#
# xiaoming = Student("小明", "18", "33311")
# xiaoming.print_info()
# print(SchoolMember.count)

# 5.	在练习4的基础上进行修改，定义一个计数器，记录学校的总人数。


# 6.	自己编写单例模式。

# class Video(object):
#     current = None
#     obj = False
#
#     def __new__(cls, *args, **kwargs):
#         if cls.current is None:
#             cls.current = super().__new__(cls)
#         return cls.current
#
#     def __init__(self):
#         if not Video.obj:
#             print("初始化")
#             Video.obj = True
#         return
#
#
# video1 = Video()
# print(video1)
# video2 = Video()
# print(video2)


# 异常练习：
# 1.	定义函数func(a, b)，计算a/b，若传入的b为0，会报异常。实现调用func()函数的异常处理，
# 要求有两个except处理语句用于处理除零异常和接收所有异常。
# def func(a, b):
#     try:
#         ret = a/b
#     except ZeroDivisionError:
#         print("0不能做除数")
#     except:
#         print("请输入正确的值")
#
#
# func("a", "b")
# 2.	准备一个文件，内容为：
# When you are old and grey and full of sleep,
# And nodding by the fire,
# take down this book
# And slowly read, error info
# and dream of the soft look
# 定义一个函数read_file(f)，参数为文件对象，在函数中读取文件内容，若读到的某行信息中包含error字符串时，
# 抛出异常。在程序主流程中捕捉并处理该异常。
s = """ When you are old and grey and full of sleep, 
    And nodding by the fire," 
    take down this book" 
    And slowly read, error info " 
    and dream of the soft look"""
f = open("1.txt", "w")
f.write(s)
f.close()


def read_file(file):
    try:
        f1 = open(file, "r")
        s1 = f1.read()
        if "error" in s1:
            raise ValueError("ValueError")
    finally:
        print("Going to close the file")
        f1.close()


try:
    read_file("1.txt")
    print()
except ValueError:
    print("error is catch")
    # raise