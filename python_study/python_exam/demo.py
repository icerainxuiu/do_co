import tools


class Dog(tools.Animal):
    def eat(self):
        tools.Animal.eat(self)
        print("吃完骨头瑶瑶头")


xiao = Dog("xiaotianquan")
xiao.eat()

