import time

# 定义一个猫类
class Cat(object):

    def __init__(self, name):
        self.name = name
    # 定义一个吃鱼的方法
    def eat(self):
        print("小猫%s爱吃鱼" % self.name)
    # 定义一个喝水的方法
    def drink(self):
        print("小猫%s爱喝水" % self.name)


# # 创建一个猫对象
# list1 = list()
# tom = Cat("Tom")
# tom.drink()
# tom.eat()
#
# name = input("")
# name = Cat(name)
# list1.append(name)
# list1[0].drink()
# print(list1)

# 定义一个学生类
# class Student(object):
#     # 定义一个初始化方法
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     # 定义一个学习方法
#     def study(self):
#         print("%s爱学习, 为祖国奋斗五十年" % self.name)
#     # 定义一个跑步方法
#     def run(self):
#         print("%s爱跑步, 强身健体保卫家国" % self.name)
#     # 定义一个睡觉方法
#     def sleep(self):
#         print("%s爱睡觉" % self.name)
#     def study_run(self):
#         self.study()
#         self.run()
#
#
# if __name__ == '__main__':
#     zhangpan = Student("张盼", 18, 178)
#     zhangpan.study_run()

# class HouseItem(object):
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#     def __str__(self):
#         return "[%s占地:%.2f平米]" % (self.name, self.area)
#
#
# class House(object):
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#         self.free_area = area
#         self.item_list = list()
#     def add_HouseItem(self, item):
#         if self.free_area < item.area:
#             print("%s房子剩余空间%s平米,小于%s空间不够,赚钱买大房子去!!!" %
#                   (self.house_type, self.free_area, item))
#         self.free_area = self.free_area - item.area
#         self.item_list.append(item.name)
#
#     def __str__(self):
#         return "[户型:%s][总面积:%.2f][剩余面积:%.2f]{家具名称列表:%s}" % \
#                (self.house_type, self.area, self.free_area, self.item_list)
#
#
# bed = HouseItem("席梦思", 78)
# chest = HouseItem("衣柜", 2)
# table = HouseItem("餐桌", 1.5)
# house = House("两居室", 80)
# print(bed, chest, table)
# house.add_HouseItem(bed)
# house.add_HouseItem(chest)
# house.add_HouseItem(table)
# print(house)

# class Gun(object):
#     def __init__(self, model):
#         self.model = model
#         self.bullet_count = 0
#     def add_bullet(self, count):
#         self.bullet_count = count
#     def shoot(self):
#         if self.bullet_count > 0:
#             self.bullet_count -= 1
#             print("%s开火...咻!!!.....子弹数量%s" %
#                   (self.model, self.bullet_count))
#         else:
#             print("枪没有子弹了！顺溜快跑！")
#             return
#
#
# class Soldier(object):
#     def __init__(self, name):
#         self.name = name
#         self.gun = None
#     def fire(self):
#         if self.gun is None:
#             print("顺溜没有枪，无法开火")
#             return
#         else:
#             print("顺溜冲啊！！！")
#             self.gun.shoot()
#             return
#
#
#
#
#
# gun = Gun("98K")
# soldier = Soldier("顺溜")
# gun.bullet_count = (50)
# soldier.gun = gun
# while True:
#     time.sleep(0.3)
#     soldier.fire()
#     if gun.bullet_count < 1:
#         break