import json
import os
from pprint import pprint

# 构造基础host域名
BASE_URL = "http://localhost"
# 构造验证码API
VERIFY_URL = BASE_URL + "/Home/user/login.html"
# 构造登录API
LOGIN_URL = BASE_URL + "/index.php?m=Home&c=User&a=do_login"

# 构造项目文件夹路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# print(BASE_PATH)


# 构造需要使用的数据并返回
def data_json():
    data_list = list()
    with open(BASE_PATH + "/data/data_json.json", encoding='utf-8') as f:
        data_j = json.load(f).values()
        for item in data_j:
            data_list.append((
                item.get("username"),
                item.get("password"),
                item.get("verify_code"),
                item.get("msg"),
                item.get("status")
            ))
    # pprint(data_list)
    return data_list


if __name__ == '__main__':
    pprint(data_json())
