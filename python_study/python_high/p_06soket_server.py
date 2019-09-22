import socket


def main():
    # 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("", 7718))
    # 设为响铃模式 套接字由主动变为被动
    tcp_server_socket.listen(128)
    # 等待客户端的连接
    new_client_sockeet,client_adrr = tcp_server_socket.accept()
    print("---- 2 ----")
    print(client_adrr)
    # 接收客户端发送来的请求
    recv_data = new_client_sockeet.recv(1024)
    print(recv_data)
    # 回送一部分数据给客户端
    new_client_sockeet.send("hahhahah".encode("utf-8"))
    # 关闭套接字
    new_client_sockeet.close()
    tcp_server_socket.close()
    

if __name__ == '__main__':
    main()