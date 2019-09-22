# 1, 2, 3, 4 四个数字，可以组成多少位互不相同切无重复数字的三位数

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if(i != k) and (i != j) and (j != k):
                print(i, j, k)

