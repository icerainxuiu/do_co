def number_math():
    m = input('请输入第一个值')
    n = input('请输入第二个值')
    m = eval(m)
    n = eval(n)
    list1 = []
    list1.append(m + n)
    list1.append(m * n)
    list1.append(m % n)
    list1.append(m ** n)
    if m > n:
        z = m
        list1.append(z)
    else:
        z = n
        list1.append(z)
    for i in range(len(list1)):
        if i == 0:
            print('m和n的和为：', list1[i])
        elif i == 1:
            print('m和n的积为：', list1[i])
        elif i == 2:
            print('m对n取余为：', list1[i])
        elif i == 3:
            print('m的n次幂为：', list1[i])
        else:
            print('m和n中更大值为%s ' % z)

    # print(' ', tuple(list1))


number_math()
