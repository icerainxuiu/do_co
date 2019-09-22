import json
import os
from pprint import pprint

VERIFY_URL = "http://localhost/index.php?m=Home&c=User&a=verify"
LOGIN_URL = "http://localhost/index.php?m=Home&c=User&a=do_login"
ORDER_URL = "http://localhost/Home/Order/order_list.html"

path_data = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(path_data)


def data_json():
    data_list = list()
    with open(BASE_PATH + "/json_data.json", encoding='utf-8') as f:
        data_dict = json.load(f).values()
        for item in data_dict:
            data_list.append([item])
        pprint(data_list)
    return data_list


MY_DATA = {
    "username": "18828828888",
    "password": "123456",
    "verify_code": "8888"}

if __name__ == '__main__':
    data_json()
