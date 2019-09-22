class Fibonacci(object):

    def __init__(self, num):
        self.num = num
        self.content = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.content < self.num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.content += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    fibonacci = Fibonacci(10)
    for i in fibonacci:
        print(i)