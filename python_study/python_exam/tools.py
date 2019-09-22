class Animal(object):
    type = "狗"

    def __init__(self, name):
        self.name = name
        __age = 0

    def eat(self):
        print("狗吃骨头")


if __name__ == '__main__':
    dog = Animal("xiaotian")
    dog.eat()
