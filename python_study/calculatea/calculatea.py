g_result = 0


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        return "除数不能为0"


if __name__ == '__main__':
    g_result = add(1, 2)
    print(g_result)
    g_result = sub(1, 2)
    print(g_result)
    g_result = mul(1, 2)
    print(g_result)
    g_result = div(1, 2)
    print(g_result)