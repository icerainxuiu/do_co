import json


def data_login():
    data_list = list()
    with open('../data/data_for_login.json', encoding='utf-8') as f:
        for data_login_value in (json.load(f).values()):
            data_list.append((
                data_login_value.get("username"),
                data_login_value.get("password"),
                data_login_value.get("verify_code"),
                data_login_value.get("is_success"),
                data_login_value.get("expect")

            ))
    return data_list


def data_goods_join_cart():
    data_list = list()
    with open('../data/data_goods_join_cart.json', encoding='utf-8')as f:
        for data_goods_value in (json.load(f).values()):
            data_list.append((
                data_goods_value.get("goods_name"),
                data_goods_value.get("expect")
            ))
    return data_list


if __name__ == '__main__':
    print(data_login())
    print(data_goods_join_cart())