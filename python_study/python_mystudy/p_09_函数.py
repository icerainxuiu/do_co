# def 函数名():
#    一行或者多行代码
# define 定义函数
# def print_stars():
#     i =1    # 函数体 或 函数实现
#     while i <= 5:
#         print('*' * i)
#         i += 1
# print_stars()
# # 函数的好处： 减少代码的冗余 ，减少维护量
# # 函数不会自动执行，需要调用
#
# def my_add():
#     a = 10
#     b = 20
#     ret = a + b
#     print('a+b=',ret)
# my_add()
# # 函数内定义的变量，在函数外不能使用
# # 函数参数

# def my_addd(a,b):  # a 和 b 叫做形参
#     ret = a + b
#     return ret  # return 返回值关键字 将函数的值返回调用者
# my_addd(100,200)  # 100 和200 都是实参  位置参数
# my_addd(a=100,b=200) # 叫做关键字参数
# 函数的返回值
# 保存函数的返回结果

# ret = my_addd(10,20)
# final_result = ret + 100
# print('最终结果：', final_result)
# # return 语句  print 函数
# 编写一个函数用于计算从start 开始到 end 结束之间所有数字的累加和
# def leijia(start,end):
#     i = start
#     my_sum = 0
#     while i <= end:
#         my_sum += i
#         i += 1
#     return my_sum
# ret = leijia(88,200)
# print('ret:',ret)
# 编写一个函数根据传入的运算符，进行相应的 加减乘除 运算.
def my_caculator(left,right,operator):
     a = left
     b = right
     if operator == '+':
         ret = a + b
     elif operator == '-':
        ret = a - b
     elif operator == '*':
         ret = a * b
     elif operator == '/':
         ret = a / b
     else:
         print('您输入的操作符有误！')
         ret = None
     return ret
ret = my_caculator(10,20,'+')
print('ret:',ret)



