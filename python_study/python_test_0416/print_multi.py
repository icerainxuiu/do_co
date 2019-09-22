def print_one(char, times):
    print(char * times)


def print_multi(row, char, col):
    while row > 0:
        print_one(char, col)
        row -= 1


if __name__ == '__main__':
    print_multi(10, "^^", 10)
