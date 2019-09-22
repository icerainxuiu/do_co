# 2.	编写一个函is_leap_year(year)，判断参数year是不是闰年，如果year是闰年则返回1，否则返回0。
# 判断依据：如果某年份能被4整除，但不能被100整除，那么这一年就是闰年，此外，能被400整除的年份也是闰年。


def is_leap_year(year):
    """
    判断年份是否是闰年
    :param year: 整数年份
    :return:
    """
    return True if ((year % 4 == 0) and (year % 100 != 0)) or (year % 100 == 0 and year % 400 == 0) else False


if __name__ == '__main__':
    year_num = int(input("输入年份"))
    print(is_leap_year(year_num))

