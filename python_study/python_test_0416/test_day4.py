import is_even
import print_multi


def main():
    num3 = 5
    while num3 > 0:
        m = int(input("输入数"))
        print(is_even.is_even(m))
        num3 -= 1


def print_char():
    print_multi.print_multi(1, "love\t", 10)
    print_multi.print_one("me\t\t", 10)


if __name__ == '__main__':
    main()
