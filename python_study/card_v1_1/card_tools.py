import time
import os
card_list = list()


# def menu():
#     while True:
#         print_star()
#         print("欢迎使用【名片管理系统】".center(80, ' '))
#         print("1.新建名片".center(80, ' '))
#         print("2.显示全部".center(80, ' '))
#         print("3.删除名片".center(80, ' '))
#         print("4.修改名片".center(80, ' '))
#         print()
#         print("0.退出系统".center(80, ' '))
#         print_star()
#         choice = input("请输入你要执行的操作\n".center(80, ' '))
#         if choice == '0':
#             print("欢迎您下次使用\n".center(80, ' '))
#             break
#         if choice == "1":
#             create()
#         if choice == "2":
#             show_cards()
#         if choice == "3":
#             del_card()
#         if choice == "4":
#             update_card()
def menu():
    print_star()
    print("欢迎使用【名片管理系统】".center(80, ' '))
    print("1.新建名片".center(80, ' '))
    print("2.显示全部".center(80, ' '))
    print("3.删除名片".center(80, ' '))
    print("4.修改名片".center(80, ' '))
    print()
    print("0.保存退出".center(80, ' '))
    print_star()


def create():
    time_sleep()
    while True:
        print("创建人员".center(100, "*"))
        print_star()
        person_msg = dict()
        name_update = input("请输入姓名,回车不添加：\n".center(80, ' '))
        name_update = name_update.strip()
        if name_update.isalnum():
                person_msg["name"] = name_update
        else:
            break
        age_update = input("请输入年龄,回车不添加：\n".center(80, ' '))
        if age_update.strip().isdecimal():
            person_msg["age"] = int(age_update)
        else:
            print("输入有误！".center(80, ' '))
            break
        gender_update = input("请输入性别,回车不添加：\n".center(80, ' '))
        if gender_update.strip().isalnum():
            person_msg["gender"] = gender_update
        else:
            break
        qq_update = input("请输入qq,回车不添加：\n".center(80, ' '))
        if qq_update.strip().isdecimal():
            person_msg["qq"] = int(qq_update)
        else:
            print("输入有误！".center(80, ' '))
            break
        card_list.append(person_msg)
        if len(card_list) < 1:
            print_star()
            print("列表中无人员")
            break
        show_cards()
        choice1 = input("添加的人员已完成,是否继续，回车继续，'0'退出\n".center(80, ' '))
        if choice1 == '0':
            break


def show_cards():
    if len(card_list) < 1:
        print("列表中无人员".center(80, ' '))
    else:
        print("名片列表".center(80, "*"))
        print_star()
        print("%-14s%-14s%-14s%-14s%-20s" % ("ID", "姓名", "年龄", "性别", "QQ号\n"))
        for i_index in range(len(card_list)):
            print("%-14s%-14s%-16s%-15s%-18s" % (str(i_index + 1), card_list[i_index]["name"],
                                                 card_list[i_index]["age"],
                                                 card_list[i_index]["gender"],
                                                 card_list[i_index]["qq"]))
        print_star()


def del_card():
    while True:
        time_sleep()
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


def update_card():
    time_sleep()
    show_cards()
    while True:
        id_update = input("请输入你要修改的人员编号\n".center(80, ' '))
        if id_update.strip().isdecimal():
            id_update = int(id_update)
            if (id_update-1) in range(len(card_list)):
                name_update = input("请输入姓名,回车不修改：\n".center(80, ' '))
                if name_update.strip().isalnum():
                    card_list[id_update - 1]["name"] = name_update
                age_update = input("请输入年龄,回车不修改：\n".center(80, ' '))
                if age_update.strip().isdecimal():
                    card_list[id_update - 1]["age"] = int(age_update)
                else:
                    print("输入有误！".center(80, ' '))
                gender_update = input("请输入性别,回车不修改：\n".center(80, ' '))
                if gender_update.strip().isalnum():
                    card_list[id_update - 1]["gender"] = gender_update
                qq_update = input("请输入qq,回车不修改：\n".center(80, ' '))
                if qq_update.strip().isdecimal():
                    card_list[id_update - 1]["qq"] = int(qq_update)
                    print("修改信息".center(100, "*"))
                    show_cards()
                    choice1 = input("人员修改已完成,是否继续，'0'退出\n".center(80, ' '))
                    if choice1 == '0':
                        break
                else:
                    show_cards()
                    choice1 = input("人员修改已完成,是否继续，'0'退出\n".center(80, ' '))
                    if choice1 == '0':
                        break
            else:
                print("输入有误".center(80, ' '))
                break

        else:
            print("你的输入有误, 请重新输入！".center(80, ' '))


def save_card():
    global card_list

    f = open("save_card.data", "w", encoding="utf-8")
    f.write(str(card_list))
    f.close()


def local_card_list():
    global card_list
    try:
        f = open("save_card.data", "r", encoding="utf-8")
        card_list = eval(f.read())
        f.close()
    except Exception:
        pass


def print_star():
    print("*" * 80)


def time_sleep():
    time.sleep(0.5)


if __name__ == '__main__':
    menu()