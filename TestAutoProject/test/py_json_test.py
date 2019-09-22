import json

dict_test = {
    "test1": {
        "username": "18828828881",
        "password": "123456",
        "verify_code": "8888"

    },
    "test2": {
        "username": "18828828881",
        "password": "123456",
        "verify_code": "8888"
    }

}
with open("./data_list.json", 'w', encoding='utf-8')as f:
    json.dump(dict_test, f)
# with open("./data_list.json", 'w') as f:
#     for d in dict_test.values():
#         json.dump(d, f)
#         f.write("\n")
