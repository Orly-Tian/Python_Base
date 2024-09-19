import socket


def main():
    # 创建UDP socket套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 准备接收方信息
    dest_addr = input("Input address, please: ")
    dest_port = int(input("Input port, please: "))
    # 接收方信息用元组存储，IP为字符串，端口为整型
    dest_info = (dest_addr, dest_port)

    send_data = input("Input sent data, please: ")

    # 使用socket发送数据
    # 第一个参数为发送内容，encode方法设置编码格式
    # 第二个参数指定地址与端口
    udp_socket.sendto(send_data.encode('utf-8'), dest_info)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
