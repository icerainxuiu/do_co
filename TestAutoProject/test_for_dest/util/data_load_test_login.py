# 从json文件读取测试登录模块的数据
import json


def data_login():
    data_list = list()
    with open('../data_json/login_data.json', encoding='utf-8')as f:
        # data_values = json.load(f)
        # print(data_values.values())
        # 按照字典的键读取其对应的值，并按照一组测试用例分开的方式添加进列表
        for data_value in (json.load(f).values()):
            data_list.append((
                data_value.get("username"),
                data_value.get('password'),
                data_value.get('verify_code'),
                data_value.get('is_success'),
                data_value.get('expect')
            ))
    return data_list


if __name__ == '__main__':
    print(data_login())
