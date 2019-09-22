import requests


select_url1 = "http://127.0.0.1:8000/api/departments/"
response = requests.get(select_url1)
print(response.status_code)  # 查看状态码
print(response.text)  # 查看响应文本

text = response.content.decode()  # 将响应文本进行转码
print(text)
# 根据id列表查询学院信息，可以使用字典格式保存提交的数据
myParams = {"$dep_id_list": "/sddfs,T18888"}
response = requests.get(select_url1, params=myParams)
print(response.status_code)
print(response.text)
