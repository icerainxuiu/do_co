# 导包
import requests

# 设置url
url = "http://127.0.0.1:8000/api/departments/T01/"
# 设置提交的数据

my_json = {
    "data": [
        {
            "dep_id": "T01",
            "dep_name": "王者荣耀",
            "master_name": "鲁班七号",
            "slogan": "智商二百五"
        }
    ]
}
response = requests.put(url, json=my_json)
# 处理响应的结果
print(response.status_code)
print(response.text)
print(response.cookies)
print(response.headers)
