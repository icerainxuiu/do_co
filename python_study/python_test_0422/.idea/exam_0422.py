# 1.	创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
# 在类User中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 	class User(object):
# 		def __init__(self, first_name, last_name,  age, gender  =  “男”):
# 			对属性进行初始化
# 		def show_userinfo(self):
# 			显示用户信息
# 		def greet_user(self):
# 	根据用户性别，给出对应的问候
# class User():
#     def __init__(self, first_name, last_name, age, gender="男"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#     def show_userinfo(self):
#         self.greet_user()
#         print("姓名：%s%s\n年龄：%s\n性别：%s" %
#               (self.first_name,self.last_name,self.age,self.gender))
#     def greet_user(self):
#         if self.gender == "男":
#             print("%s先生您好！" % self.first_name)
#         else:
#             print("%s女士您好！" % self.first_name)
#
# zhang = User("张", "san", 18)
# li = User("李", "si", 19, gender="女")
# zhang.show_userinfo()
# li.show_userinfo()

# 2.	按照一下要求定义一个游乐园门票类，并尝试计算2个人平日票价
# 	平日票价100元
# 	周末票价为平日票价120%
#   class Ticket(object):
# 	def __init__(self, price):
# 		self.price = price
# 		self.weekend_price *= 1.2
# def compute(self,adultcount, isweekend):
# 		计算票价

# class Ticket():
#     def __init__(self, price):
#         self.price = price
#         self.weekend_price = price * 1.2
#     def compute(self, adultcount, isweekend=False):
#         if isweekend:
#             total_price = adultcount * self.weekend_price
#         else:
#             total_price = adultcount * self.price
#         return total_price
#
# ticket = Ticket(100)
# total_price = ticket.compute(2)
# print(total_price)

# 3.	定义一个学生类，要求包含以下属性：姓名、年龄、三门课程成绩（成绩用列表记录），定义实例方法：
# get_name()获取学生姓名、get_max_score()获取该学生的最高成绩、get_avg_score()获取学生三门课的平均成绩。

# class Student():
#     def __init__(self, name, age, *args):
#         self.name = name
#         self.age = age
#         self.socre_list = args
#     def get_name(self):
#         return self.name
#     def get_max_score(self):
#         return max(self.socre_list)
#     def get_avg_score(self):
#         return sum(self.socre_list)/len(self.socre_list)
#
# list1 = [random.randint(1,100) for x in range(3)]
# xiaoming = Student("小明", 19, *list1)
# print(xiaoming.get_name())
# print(xiaoming.get_avg_score())
# print(xiaoming.get_max_score())
# 4.	自定义一个类，模拟实现字典类的操作，要求具有属性data(为字典类型数据)，实现如下方法：
# 	get_dict(self, key): 获取字典中指定key对应的value值，若字典中不存在该key则提示未找到该内容
# 	del_dict(self, key): 删除字典中指定key对应的值，若字典中不存在该key则提示未找到该内容
# 	get_values(self): 获取字典键的列表
# class Dict1():
#     def __init__(self, data):
#         self.data = data
#         print(self.data)
#     def get_dict(self, key):
#         for x in self.data:
#             if x == key:
#                 return self.data[key]
#         else:
#             return "未找到该内容"
#     def del_dict(self, key):
#         for x in self.data:
#             if x == key:
#                 return self.data.pop(key)
#         else:
#             return "未找到该内容"
#     def get_values(self):
#         return list(self.data)
#
# dict1 = Dict1({"a":"1", "b":"1", "c":"1"})
# print(dict1.del_dict("d"))
# print(dict1.get_values())


# 5.	Joker买了一辆BMW X7（定义两个类：Person、Car）
# class Person(object):
# def __init__(self, name):
# 	初始化姓名
# 	def buy_car(self, car):
# 		打印买了什么型号的车
#

class Car(object):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.cai = None
    def buy_car(self, car):
        self.car = car
        print("%s买了%s" % (self.name, self.car.name))

car = Car("BMW X7")
joke = Person("Jack Ma")
joke.buy_car(car)

# 递归打印99乘法表
# def nine_multip(n):
#     if n < 1:
#         return
#     nine_multip(n - 1)
#     for m in range(1, n+1):
#         print("%s * %s = %s" % (n, m, m*n),end="\t")
#     print()
#
#
#
# nine_multip(9)