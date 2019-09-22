import requests

# 根据id列表删除学院信息

# 设置url
url = "http://127.0.0.1:8000/api/departments/"
# 设置提交的数据

my_param = {"$dep_id_list":"T01,T18888"}
# 发送请求
response = requests.delete(url=url, params=my_param)
# 处理响应
print(response.status_code)
print(response.text)