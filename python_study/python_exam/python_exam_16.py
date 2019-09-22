def add_not_even():
    """
    求1-100间的奇数和
    :return: 总和
    """
    result = sum(i for i in range(1, 100, 2))
    return result


print(add_not_even())