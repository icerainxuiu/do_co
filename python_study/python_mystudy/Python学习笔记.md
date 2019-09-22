

### 面向对象

#### 面向对象的三大特性

##### 封装

1. 封装 **根据** **职责** **将属性和方法封装到一个抽象的类中**
   * 定义类的准则

##### 继承

1. 继承 实现代码的重用，相同的代码不需要重复的编写
   * 设计类的技巧
   * 子类针对自己特有的需求，编写特定的代码

##### 多态

1. 多态 不同的子类对象 调用相同的父类方法，产生不同的执行结果

* 多态 可以 增加代码的灵活度
* 以继承和重写父类方法为前提
* 是调用方法的技巧，不会影响到类的内部设计

```python
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)
class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)
class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name,dog.name))
        dog.game()
```





