import socket
import sys
#运行环境windows的cmd，Vscode    配置，本机IPv4地址，网络联通，端口号80
def udp_client(file_path, server_ip, server_port):
    # 创建一个UDP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 使用传入的参数定义服务器的地址和端口该代码能在udp的socket中指定server IP而不是把serverIP写死在代码中
    server_address = (server_ip, server_port)

    # 打开一个文件用于读取要发送的数据
    with open(file_path, 'rb') as file:
        while True:
            # 读取文件内容，每次最多读取1024字节
            data = file.read(1024)
            
            # 如果没有数据，表示文件读取完成
            if not data:
                # 发送一个结束信号到服务器，表示文件传输完成
                client_socket.sendto(b'END', server_address)
                break
            
            # 将数据发送到服务器
            client_socket.sendto(data, server_address)

    # 关闭套接字
    client_socket.close()
    print('文件发送完成。')

if __name__ == '__main__':
    # 检查命令行参数是否正确
    if len(sys.argv) != 4:
        print("Usage: python script.py <Server IP> <Server Port> <File Path>")
        sys.exit(1)

    # 从命令行参数中获取服务器IP、端口和文件路径
    server_ip =   sys.argv[1]
    server_port = int(sys.argv[2])
    file_path = sys.argv[3]

    # 调用udp_client函数，并传入获取的参数
    udp_client(file_path, server_ip, server_port)
