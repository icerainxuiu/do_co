import socket


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ("", 7789)
    udp_socket.bind(localaddr)
    while True:
        send_data = input("请输入您要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.13.141", 7788))


if __name__ == "__main__":
    main()