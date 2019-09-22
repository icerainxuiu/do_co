card_list = list()
list1 = list()


class Card:
    def __init__(self, name, gender, age, qq, email):
        self.name = name
        self.gender = gender
        self.age = age
        self.qq = qq
        self.email = email
        self.card_dict = dict()

    def card_create(self):
        global card_list
        self.card_dict["name"] = self.name
        self.card_dict["gender"] = self.gender
        self.card_dict["age"] = self.age
        self.card_dict["qq"] = self.qq
        self.card_dict["email"] = self.email
        card_list.append(self.card_dict)

    def card_update(self):
        self.card_dict["name"] = input("输入姓名")
        self.card_dict["gender"] = input("输入性别")
        self.card_dict["age"] = input("输入年龄")
        self.card_dict["qq"] = input("输入qq")
        self.card_dict["email"] = input("输入邮箱")

    def card_del(self):
        global card_list
        self.card_dict.clear()

    def card_search(self):
        pass


def save_card():
    global card_list
    global list1

    f = open("save_card.data", "w", encoding="utf-8")
    f.write(str(card_list))
    f.close()
    f = open("save_list.data", "w", encoding="utf-8")
    f.write(str(list1))
    f.close()


def local_card_list():
    global card_list
    global list1
    try:
        f = open("save_card.data", "r", encoding="utf-8")
        card_list = eval(f.read())
        f.close()
        f = open("save_card.list", "r", encoding="utf-8")
        list1 = eval(f.read())
        f.close()
    except Exception:
        pass


def menu():
    print("欢迎使用【名片管理系统】".center(80, ' '))
    print("1.新建名片".center(80, ' '))
    print("2.显示全部".center(80, ' '))
    print("3.删除名片".center(80, ' '))
    print("4.修改名片".center(80, ' '))
    print()
    print("0.保存退出".center(80, ' '))


def card_show():
    if len(card_list) < 1:
        print("列表中无人员".center(80, ' '))
    else:
        print("名片列表".center(80, "*"))
        print("%-14s%-14s%-14s%-14s%-20s%-20s" % ("ID", "姓名", "年龄", "性别", "QQ号", "qq邮箱\n"))
        for i_index in range(len(card_list)):
            print("%-14s%-14s%-16s%-15s%-18s%-20s" % (str(i_index + 1), card_list[i_index]["name"],
                                                      card_list[i_index]["age"], card_list[i_index]["gender"],
                                                      card_list[i_index]["qq"], card_list[i_index]["email"]))
    # print("%-14s%-14s%-14s%-14s%-20s" % ("姓名", "年龄", "性别", "QQ号","邮箱"))
    # print("%-14s%-14s%-14s%-14s%-20s" % (self.name, self.gender, self.age, self.qq, self.email))


def main():
    global card_list
    global list1
    local_card_list()
    while True:
        menu()
        choice = input("请输入你要执行的操作\n".center(80, ' '))
        if choice == '0':
            save_card()
            print("欢迎您下次使用\n".center(80, ' '))
            break
        if choice == "1":
            name = input("输入姓名")
            gender = input("输入性别")
            age = input("输入年龄")
            qq = input("输入qq")
            email = input("输入邮箱")
            name = Card(name, gender, age, qq, email)
            list1.append(name)
            print(list1)
            name.card_create()

        if choice == "2":
            card_show()
        if choice == "3":
            card_show()
        if choice == "4":
            card_show()
            id_update = int(input("输入你要修改的id"))
            card_list[id_update-1].card_update()


if __name__ == '__main__':
    main()
