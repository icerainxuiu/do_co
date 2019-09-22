# 1.	编写函数judge_arr(start, end)用于判断start到end范围中的数据哪些是偶数
# 		要求在该函数中调用is_even(n)函数判断某个数是不是偶数


def is_even(n):
    """
    判断是否偶数
    :param n: 输入整数
    :return: True 是偶数,False 是奇数
    """
    if n % 2 == 0:
        return "%s is 偶数 ,is %s" % (n, True)
    else:
        return "%s is 奇数 ,is %s" % (n, False)


def is_even1(n):
    """
    判断是否偶数
    :param n: 输入整数
    :return: True 是偶数,False 是奇数
    """
    return not (n % 2)


if __name__ == '__main__':
    x = 2
    z = is_even(x)
    print(z)