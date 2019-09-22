# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("都要吃饭")
#
#     def sleep(self):
#         print("在家睡觉")
#
#
# class Students(Person):
#
#     def study(self):
#         print("%s要学习" % self.name)
#
#     def sleep(self, is_at_home=True):
#         if is_at_home:
#             super().sleep()
#             super(Students, self).sleep()
#         else:
#             print("在教室睡觉")
#
#
# stu = Students("张三")
#
# stu.eat()
# stu.sleep()
# stu.study()

#
# class Master(object):
#     def __init__(self, name):
#         self.name = name
#
#     def make_cake(self):
#         print("%s传统方法制作煎饼" % self.name)
#
#
# class School(object):
#     def __init__(self, name):
#         self.name = name
#
#     def make_cake(self):
#         print("%s 现代方法制作煎饼" % self.name)
#
#     def make_pizza(self):
#         print("%s 制作pizza" % self.name)
#
#
# class Prentice(Master, School):
#     def make_cake(self, selection=True):
#         if selection:
#             super().make_cake()
#         else:
#             School.make_cake(self)
#
#
# class Restaurant(object):
#     def __init__(self, name):
#         self.name = name
#
#     def make_cook(self, obj):
#         obj.make_cake()
#
#     def make_pizza(self, obj):
#         obj.make_pizza()
#
#
# lanxiang = School("蓝翔")
# laowang = Master("老王")
# xiaoming = Prentice("小明")
# # xiaoming.make_cake(False)
# xiaoming.make_pizza()
#
# chinese_restaurant = Restaurant("中餐馆")
#
# chinese_restaurant.make_cook(laowang)
# chinese_restaurant.make_cook(xiaoming)
# chinese_restaurant.make_cook(lanxiang)
# chinese_restaurant.make_pizza(lanxiang)
# chinese_restaurant.make_pizza(xiaoming)


class Game(object):
    top_score = 0

    @staticmethod
    def show_welcome_info():
        print("welcome play game")

    def __init__(self, name):
        self.name = name
        self.score = 0
        Game.show_welcome_info()
        Game.show_top_score()

    @classmethod
    def show_top_score(cls):
        print("目前最高分是%s" % cls.top_score)

    def play_game(self, score):
        self.score = score
        print("%s得分是%s" % (self.name, self.score))
        if self.score > Game.top_score:
            Game.top_score = self.score
        Game.show_top_score()


joke = Game("joke")
joke.play_game(300)

