# import random

import re
card_list = list()
# list1 = ["a", 'b', 'c', 'd', 'e', 'f', 'g', '']
# list_name = [x*i for x in list1 for i in range(1, 10)]


def menu():
    star()
    print("欢迎使用【名片管理系统】".center(80, ' '))
    print("1.新建名片".center(80, ' '))
    print("2.显示全部".center(80, ' '))
    print("3.删除名片".center(80, ' '))
    print("4.修改名片".center(80, ' '))
    print()
    print("0.保存退出".center(80, ' '))
    star()


# 判断输入是否是数字
def decide_isdecimal(value_input):
    value_input = ''.join(value_input.split())
    return value_input if value_input.isdecimal else ""


# 判断输入是否是字母和数字
def decide_isalnum(value_input):
    value_input = ''.join(value_input.split())
    return value_input if value_input.isalnum else ""


def decide_gender(value_input):
    if value_input.strip() == "男":
        return "男"
    if value_input.strip() == "女":
        return "女"
    else:
        return ""


# 判断qq长度
def decide_qq_len(value_input):
    return int(value_input.strip()) if 6 <= len(value_input.strip()) < 11 else ""


# 判断姓名长度
def decide_name_len(value_input):
    return value_input.strip() if 2 <= len(value_input.strip()) < 12 else ""


def decide_age_len(value_input):
    return int(value_input.strip()) if 0 < len(value_input.strip()) < 4 else ""


# 姓名模块
def module_name(value_input):
    value_input = decide_isalnum(value_input)
    if value_input:
        if decide_name_len(value_input):
            return value_input
        else:
            return
    else:
        return


# 年龄模块
def module_age(value_input):
    value_input = decide_isdecimal(value_input)
    if value_input:
        if decide_age_len(value_input):
            return int(value_input)
        else:
            print("输入错误！")
            return
    else:
        print("输入错误！")
        return


# 性别模块
def module_gender(value_input):

    value_input = decide_gender(value_input)
    if value_input:
        return value_input
    else:
        return


# qq模块
def module_qq(value_input):
    value_input = decide_isdecimal(value_input)
    if value_input:
        if decide_qq_len(value_input):
            return int(value_input)
        else:
            return
    else:
        return


# 邮箱模块
def module_email(value_input):
    try:
        value_input = re.match("[a-zA-Z0-9]{4,16}@(qq|126|163|sina)\.com$", value_input).group()
        return value_input
    except:
        print("输入有误！")


# 创建名片
def create_card():
    while True:
        print("创建人员".center(100, "*"))
        star()
        person_msg = dict()
        value_input = input("请输入姓名,回车不添加：\n".center(80, ' '))
        if value_input:
            if module_name(value_input):
                person_msg["name"] = module_name(value_input)
            else:
                print("输入错误")
                break
        else:
            break
        age_input = input("请输入年龄,回车不添加：\n".center(80, ' '))
        if age_input:
            if module_age(age_input):
                person_msg["age"] = module_age(age_input)
            else:
                print("输入错误")
                break
        else:
            break
        gender_input = input("请输入性别,回车不添加：\n".center(80, ' '))
        if gender_input:
            if module_gender(gender_input):
                person_msg["gender"] = module_gender(gender_input)
            else:
                print("输入错误")
                break
        else:
            break
        qq_input = input("请输入qq,回车不添加：\n".center(80, ' '))
        if qq_input:
            if module_qq(qq_input):
                person_msg["qq"] = module_qq(qq_input)
            else:
                print("输入错误")
                break
        else:
            break
        email_input = input("请输入qq邮箱,回车不添加：\n".center(80, ' '))
        if email_input:
            if module_email(email_input):
                person_msg["email"] = module_email(email_input)
            else:
                print("输入错误")
                break
        else:
            break
        card_list.append(person_msg)
        if len(card_list) < 1:
            star()
            print("列表中无人员")
            break
        show_cards()
        save_card()
        choice1 = input("添加的人员已完成,是否继续，回车继续，'0'退出\n".center(80, ' '))
        if choice1 == '0':
            break


# 显示名片
def show_cards():
    if len(card_list) < 1:
        print("列表中无人员".center(80, ' '))
    else:
        print("名片列表".center(80, "*"))
        star()
        print("%-14s%-14s%-14s%-14s%-20s%-20s" % ("ID", "姓名", "年龄", "性别", "QQ号","qq邮箱\n"))
        for i_index in range(len(card_list)):
            print("%-14s%-14s%-16s%-15s%-18s%-20s" % (str(i_index + 1), card_list[i_index]["name"],
                                                      card_list[i_index]["age"],
                                                      card_list[i_index]["gender"],
                                                      card_list[i_index]["qq"],
                                                      card_list[i_index]["email"]))


# 删除名片
def del_card():
    while True:
        print("删除人员".center(80, "*"))
        show_cards()
        del_id = input("请输入你要删除的人员编号,不输入退出删除\n".center(80, ' '))
        if del_id.strip().isdecimal():
            del_id = int(del_id)
            if del_id in range(len(card_list)+1):
                card_list.pop(del_id-1)
                show_cards()
                choice1 = input("删除人员已完成,是否继续，'0'退出\n".center(80, ' '))
                if len(card_list) < 1:
                    print("名片中已无人员".center(80, ' '))
                    break
                if choice1 == '0':
                    break
            else:
                print("输入有误".center(80, ' '))
        else:
            break


# 修改名片
def update_card():
    show_cards()
    while True:
        id_update = input("请输入你要修改的人员编号\n".center(80, ' '))
        if ''.join(id_update.split()).isdecimal():
            id_update = int(id_update)
            if (id_update - 1) in range(len(card_list)):
                name_update = input("请输入姓名,回车不修改：\n".center(80, ' '))
                if name_update:
                    if module_name(name_update):
                        card_list[id_update - 1]["name"] = module_name(name_update)
                    else:
                        print("输入有误")
                age_update = input("请输入年龄,回车不修改：\n".center(80, ' '))
                if age_update:
                    if module_age(age_update):
                        card_list[id_update - 1]["age"] = module_age(age_update)
                    else:
                        print("输入有误！".center(80, ' '))
                gender_update = input("请输入性别,回车不修改：\n".center(80, ' '))
                if gender_update:
                    if module_gender(gender_update):
                        card_list[id_update - 1]["gender"] = module_gender(gender_update)
                    else:
                        print("输入有误")
                qq_update = input("请输入qq,回车不修改：\n".center(80, ' '))
                if qq_update:
                    if module_qq(qq_update):
                        card_list[id_update - 1]["qq"] = module_qq(qq_update)
                    else:
                        print("输入有误")

                email_update = input("请输入qq邮箱,回车不添加：\n".center(80, ' '))
                if email_update:
                    if module_email(email_update):
                        card_list[id_update - 1]["email"] = module_email(email_update)
                        print("修改信息".center(100, "*"))
                        show_cards()
                        save_card()
                        choice1 = input("人员修改已完成,是否继续，'0'退出\n".center(80, ' '))
                        if choice1 == '0':
                            break
                else:
                    show_cards()
                    save_card()
                    choice1 = input("人员修改已完成,是否继续，'0'退出\n".center(80, ' '))
                    if choice1 == '0':
                        break
            else:
                print("输入有误".center(80, ' '))
                break

        else:
            print("你的输入有误, 请重新输入！".center(80, ' '))


# 打印星星
def star():
    print("*" * 80)


# 保存到本地
def save_card():
    global card_list
    f = open("save_list", 'w', encoding="utf-8")
    f.write(str(card_list))
    f.close()


# 打开本地保存
def local_card():
    global card_list
    try:
        f = open("save_list", "r", encoding="utf-8")
        card_list = eval(f.read())
        f.close()
    except Exception:
        pass


# 主函数，选项功能
def main():
    local_card()
    while True:
        menu()
        choice = input("请输入你要执行的操作\n".center(80, ' '))
        if choice == '0':
            save_card()
            print("欢迎您下次使用\n".center(80, ' '))
            break
        if choice == "1":
            create_card()
        if choice == "2":
            show_cards()
        if choice == "3":
            del_card()
        if choice == "4":
            update_card()


if __name__ == '__main__':
    main()
