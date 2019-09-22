import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取服务器的ip port
    dest_ip = input("输入ip")
    dest_port = int(input("输入端口"))
    # 连接服务器
    tcp_socket.connect((dest_ip, dest_port))
    # 获取下载的文件名字
    download_file_name = input("输入文件名")
    # 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("gbk"))
    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        # 保存接收到的数据到一个文件中
        with open("[new]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()