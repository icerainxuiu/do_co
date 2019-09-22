import socket


def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))
    send_data = input("请输入要发送的消息：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s : %s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("", 7878))
    # 循环循环来进行处理事情
    while True:
        # 发送
        print("....xxx聊天器....")
        print("1:send message:")
        print("2:receive message")
        print("0:exit")
        op = input("input the choose")
        # 获取要发送的内容
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("input the right values")


        # 接收并显示
if __name__ == '__main__':
    main()