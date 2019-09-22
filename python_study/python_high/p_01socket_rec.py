import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    localaddr = ("", 7788)
    udp_socket.bind(localaddr)
    while True:
        # 绑定一个本地信息

        # 接收数据
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))

    # 2. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()