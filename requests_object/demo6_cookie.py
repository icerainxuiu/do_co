from pprint import pprint

import requests

response1 = requests.get(url="http://localhost/index.php?m=Home&c=User&a=verify")  # 验证码接口

print(response1.status_code)  # 查看响应状态码
cookies = response1.cookies  # 查看响应回的cookies
pprint(cookies)
cooki_value = cookies.get("PHPSESSID")
pprint(cooki_value)
cook = {"PHPSESSID":cooki_value}
my_data = {"username":"18828828888","password":"123456","verify_code":"8888"}  # 登录参数
# 将登录数据和cookies 一同提交
response2 = requests.post(url="http://localhost/index.php?m=Home&c=User&a=do_login",data=my_data,cookies=cook)
# 查看响应码
print(response2.status_code)
# 查看响应头
pprint(response2.json())
response3 = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookies)

print(response3.text)