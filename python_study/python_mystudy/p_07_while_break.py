# break 退出循环
print('循环开始...')
i = 0
while i <= 100:
    if i > 50:
        break
    print(i)
    i += 1
# break 执行，break后面的代码也不执行，并且马上终止循环
# continue 只能跳过本层循环里的本次循环
# break 只能终止本次循环