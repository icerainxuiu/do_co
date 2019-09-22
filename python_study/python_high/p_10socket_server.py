import socket


def send_file_2_client(new_client_socket, client_addr):
    # new_client_socket, client_adrr = tcp_server_socket.accept()
    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端(%s)需要下载的文件是：%s" % (str(client_addr), file_name))
    # 接收客户端发送来的请求
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件%s" % file_name)
    if file_content:
        new_client_socket.send(file_content)
        # 回送一部分数据给客户端



def main():
    # 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("", 7718))
    # 设为响铃模式 套接字由主动变为被动
    tcp_server_socket.listen(128)
    while True:
        new_client_socket, client_adrr = tcp_server_socket.accept()

        # 等待客户端的连接
       # new_client_sockeet.send("hahhahah".encode("utf-8"))
        # 关闭套接字
        send_file_2_client(new_client_socket, client_adrr)
        new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()