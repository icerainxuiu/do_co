import requests

from data_base import VERIFY_URL, LOGIN_URL


# 封装登录的API接口
class Login:

    # 登录的API接口类的初始化
    def __init__(self):
        # 创建一个session实例对象
        self.session = requests.Session()
        # 获取cookie的url地址，从测试数据文件中导入
        self.verify_url = VERIFY_URL
        # 获取登录的地址
        self.login_url = LOGIN_URL

    # 创建获取cookie的方法，并返回获取到的响应
    def get_verify_cookie(self):
        response = self.session.get(self.verify_url)
        return response

    # 创建获取登录页面的方法，并返回响应
    def login(self, data):
        response = self.session.post(url=self.login_url, data=data)
        return response

    # 创建关闭session的方法
    def close_login(self):
        self.session.close()
