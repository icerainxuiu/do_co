# 导包
import requests

# 设置资源路径

url = "http://127.0.0.1:8000/api/departments/"

# 提交数据
my_json = {
    "data": [
        {
            "dep_id": "T01",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
    ]
}

response = requests.post(url,json=my_json)
# 打印响应代码
print(response.status_code)
# 打印响应体
print(response.text)
# post 提交的数据可以是json格式，也可以是键值对格式
# post(json=json, data=key_value)
print(response.cookies)