import json
import pprint

import requests

# dict_data = {"dep_id": "T1888", "dep_name": "王者荣耀", "master_name": "鲁班七号",
#              "slogan": "智商二百五"}
# data_json = json.dumps(dict_data)
# print(data_json)

data_json = {
    "data": [
        {
            "dep_id": "T18888",
            "dep_name": "王者荣耀",
            "master_name": "鲁班七号",
            "slogan": "智商二百五"
        }
    ]
}
requests.post("http://127.0.0.1:8000/api/departments/", json=data_json)
response = requests.get("http://127.0.0.1:8000/api/departments/")
pprint.pprint(response.content.decode())
