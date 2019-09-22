import card_tools


def main():
    card_tools.local_card_list()
    while True:
        card_tools.menu()
        choice = input("请输入你要执行的操作\n".center(80, ' '))
        if choice == '0':
            card_tools.save_card()
            print("欢迎您下次使用\n".center(80, ' '))
            break
        if choice == "1":
            card_tools.create()
        if choice == "2":
            card_tools.show_cards()
        if choice == "3":
            card_tools.del_card()
        if choice == "4":
            card_tools.update_card()


if __name__ == '__main__':
    main()
