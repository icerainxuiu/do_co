#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# 一行代码打印九九乘法表
print('\n'.join([" ".join(["%2s x %2s = %2s" % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]))

# 一行代码打印迷宫
print("".join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))

# 一行代码表白爱情
print(''.join([''.join([("LOVE"[(x -y )% len('LOVE')]if ((x*0.05)**2 + (y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0
                         else" ")for x in range(-30, 30)])for y in range(30, -30, -1)]))