import requests
url = "http://127.0.0.1:8000/api/departments/"

# 响应行
response = requests.get(url)

print(response.url)  # 响应的url
print(response.status_code)  # 响应码

# 响应头

print(response.encoding)  # 获取编码集

print(response.headers)  # 获取所有响应头
print(response.headers.get("Content-Type"))  # 响应指定响应头

# 响应体
print(response.text)  # 文本方式显示 响应体
# 以文本方式显示无法获取响应其中的数据
print(response.json().get("results"))  # 将响应体数据解析为JSON格式并获取数据
print(response.content)  # 获取图片或音频视频等非文本的二进制数据
# 如果响应体是非json数据，json() 函数调用会抛出异常
