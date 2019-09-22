import json
import os

# host
BASE_URL = "http://ttapi.research.itcast.cn"

# login_url
LOGIN_URL = BASE_URL + "/app/v1_0/authorizations"

# get message_url
MESSAGE_URL = BASE_URL + "/v1_0/sms/codes/:"

# user channels url
CHANNELS_URL = BASE_URL + "/app/v1_0/channels"

# articles url
ARTICLES_URL = BASE_URL + "/app/v1_0/article/"

# collection url
COLLECTION_URL = BASE_URL + "/app/v1_0/article/collections"

# cancel collection url
CANCEL_COLLECTION_URL = BASE_URL + "/app/v1_0/article/collections/:"

# base_path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def data_for_login():
    data = list()
    with open(BASE_PATH + "/data/data_login.json", encoding='utf-8')as f:
        for values in json.load(f).values():
            data.append((
                values.get("mobile"),
                values.get("code"),
                values.get("status_code"),
                values.get("message")
            ))
    return data


if __name__ == '__main__':
    print(BASE_PATH)
    print(data_for_login())