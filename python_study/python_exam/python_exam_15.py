def func():
    """
    判断用户输入是否是9的倍数
    :return:是与否
    """

    try:
        a = int(input("请输入数字"))

    except ValueError:
        return "不是数字,请重新输入"

    else:
        if a % 9 == 0:
            return "是"
        else:
            return "否"


print(func())
