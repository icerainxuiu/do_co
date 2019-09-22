import os

import requests

# 需求：使用requests库调用Tpshop登录功能的接口，完成登录操作，登录成功后获取“我的订单页面

# 获取验证码，服务器产生session，并返回cookie，

# 在requests中提供了session对象，该对象包含了cookies的提取组织与提交，可以简化cookie的应用

# 先创建session对象
session = requests.Session()

# 获取验证码
response = session.get(url="http://localhost/index.php?m=Home&c=User&a=verify")

# 输入登录帐号密码

my_data = {"username":"18828828888","password":"123456","verify_code":"8888"}  # 登录参数
# 将登录数据和cookies 一同提交
response2 = session.post(url="http://localhost/index.php?m=Home&c=User&a=do_login", data=my_data)

print(response2.status_code)
print(response2.text)

response3 = session.get("http://localhost/Home/Order/order_list.html")
print(response3.text)

path_v = os.path.abspath(__file__)
print(path_v)
print(os.path.dirname(path_v))
