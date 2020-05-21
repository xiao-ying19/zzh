from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)
print('服务端已开启....')
while True:
    # 接收消息
    data, addr = sockfd.recvfrom(1024)
    # 发送消息
    if data.decode() == '##':
        print(addr, '已退出')
        continue
    print(addr, '说', data.decode())
    sockfd.sendto('接收到你的消息'.encode(), addr)