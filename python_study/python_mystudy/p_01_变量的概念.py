# # 首先会申请一块内存  10
# # 变量存储程序需要临时数据
# # print('hello world')
# # a = 10  # 创建一个a的变量，并且赋值操作
# # a = 100  # 重新赋值
# # my_str = "d"
# my_str = "hello world!"
# # my_type = type(my_str)  # 赋值运算符，先看右边，再看左边
# print(my_str)
# print(10  +  20 )
# print(2 ** 9)
input_username = input('请输入您的用户名：')
input_password = input('请输入您的密码：')
correct_name = 'admin'
correct_pass = '123456'
if input_username == correct_name and input_password == correct_pass:
    # if input_password == correct_pass:
        print('欢迎 %s 登录系统！' % input_username)
    # else:
    #     print('您的用户名或密码错误！')
else:
    print('您的用户名或密码错误！')

