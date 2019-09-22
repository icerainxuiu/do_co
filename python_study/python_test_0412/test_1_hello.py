# print("*" * 30)
# print(50 // 3)
# print(50 % 3)
# print("*" * 30)

# list1 = [1, 2, 3, 4]
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# 先定义 a 早餐单价
# b 天数
# 30天后 打9折
# 总价 c
# a = 5
# b = 30
# c = a * b
#
# # 第31 天 单价
# a = a * 0.9
# # 31 天后总价
# c = c + a
# print(c)


def main():
    try:
        while 1:
            day = float(input("输入天数"))
            price = float(input("输入单价"))
            if day >= 0 and price > 0:
                if day > 30:
                    money = price * 30
                    price = price * 0.9
                    money = money + (day - 30) * price
                    print("money =%f" % money)
                elif day >= 0:
                    print("money =%f" % (day * price))
            else:
                print("输入正确的单价或天数！")
    except ValueError:
        print("您的输入有误，退出游戏！")


if __name__ == '__main__':
    main()