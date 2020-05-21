from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 设置要发送到服务端地址
HOST = '127.0.0.1'
PORT = 8888
ADDR = ((HOST, PORT))
# ADDR = (('127.0.0.1', 8888))

for data in[b'1',b'2',b'3']:
    sockfd.sendto(data,('127.0.0.1',8888))
    print(sockfd.recv(1024).decode('utf-8'))

    
# 关闭套接字
sockfd.close()