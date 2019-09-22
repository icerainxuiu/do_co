# 获得用户输入的用户名
# 用户在输入用户名时，去除用户两侧的空格
# 判断用户名是否全为字母
# 处理完毕，显示注册成功.

username = input('请输入您要注册的用户名：')
# strip 函数默认去除字符串两侧的空格
new_username = username.strip()
print(username)
print(new_username)
# isalpha 判断字符串所有元素是否都是字母
if new_username.isalpha():
    print('注册成功')
else:
    print('注册失败')
# print(new_username.isalpha())
# isdigit 判断是否是数字
