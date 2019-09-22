import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("input the ip:")
    server_port = int(input("input the port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    send_data = input("send message:")
    tcp_socket.send(send_data.encode("utf-8"))
    tcp_socket.close()


if __name__ == '__main__':
    main()
