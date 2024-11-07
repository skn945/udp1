import socket
import sys
#运行环境ubuntu的cmd，Vscode    配置，虚拟机IPv4地址，网络联通端口号80
#https://github.com/skn945/udp1
def udp_server(file_path, ip, port):
    # 创建一个UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 定义服务器地址和端口，使用传入的参数代码能在udp的socket中指定server IP而不是把serverIP写死在代码中
    server_address = (ip, port)
    
    # 将套接字绑定到服务器地址和端口
    server_socket.bind(server_address)
    
    # 打印服务器监听信息
    print(f'服务器正在运行，等待接收文件... 监听IP: {ip}, 端口: {port}')
    
    # 打开一个文件用于写入接收到的数据
    with open(file_path, 'wb') as file:#wb二进制文件写入命令
        while True:
            # 接收客户端发送的数据，最多接收1024字节
            data, address = server_socket.recvfrom(1024)

            # 检查是否接收到结束信号
            if data == b'END':
                break  # 跳出循环，结束文件接收

            # 将接收到的数据写入文件
            file.write(data)
            print(f'接收了来自{address}的数据')

            # 如果没有数据，表示文件传输完成
            if not data:
                break
            
            # 将接收到的数据写入文件
            file.write(data)
            # 打印接收数据的信息
            print(f'接收了来自{address}的数据')

    # 关闭套接字
    server_socket.close()
    # 打印文件接收完成信息
    print('文件接收完成。')

# 确保脚本是被直接运行的，而不是被导入的
if __name__ == '__main__':
    # 检查命令行参数的数量是否正确
    if len(sys.argv) != 4:
        # 如果参数数量不正确，打印使用方法并退出
        print("Usage: python script.py <Server IP> <Server Port> <File Path>")
        sys.exit(1)

    # 从命令行参数中获取服务器IP地址
    server_ip = sys.argv[1]
    # 从命令行参数中获取服务器端口，并转换为整数
    server_port = int(sys.argv[2])
    # 从命令行参数中获取文件保存路径
    file_path = sys.argv[3]

    # 调用udp_server函数，并传入获取的参数
    udp_server(file_path, server_ip, server_port)

