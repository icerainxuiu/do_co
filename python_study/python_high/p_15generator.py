def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        # 如果一个函数中有yield 语句，那么这就不是
        # 函数，而是一个生成器模板
        a, b = b, a + b
        current_num += 1


# 再调用create_num 时，发现这个函数有yield，就是创建一个生成器对象

if __name__ == '__main__':
    obj = create_num(10)
    for num in obj:
        print(num)