from socket import *
import struct
import json
import os
import sys
import time
from plan import process_bar

tcp_client = socket(AF_INET, SOCK_STREAM)
ip_port = (('127.0.0.1', 8080))
buffsize = 1024
tcp_client.connect_ex(ip_port)
print('等待链接服务端')
while True:
    head_struct = tcp_client.recv(4)  # 接收报头的长度,
    if head_struct:
        print('已连接服务端,等待接收数据')
    head_len = struct.unpack('i', head_struct)[0]  # 解析出报头的字符串大小
    data = tcp_client.recv(head_len)  # 接收长度为head_len的报头内容的信息 (包含文件大小,文件名的内容)

    head_dir = json.loads(data.decode('utf-8'))
    filesize_b = head_dir['filesize_bytes']
    filename = head_dir['filename']

    #   接受真的文件内容
    recv_len = 0
    recv_mesg = b''
    old = time.time()
    f = open(filename, 'wb')
    while recv_len < filesize_b:
        percent = recv_len / filesize_b

        process_bar(percent)
        if filesize_b - recv_len > buffsize:

            recv_mesg = tcp_client.recv(buffsize)
            f.write(recv_mesg)
            recv_len += len(recv_mesg)
        else:
            recv_mesg = tcp_client.recv(filesize_b - recv_len)
            recv_len += len(recv_mesg)
            f.write(recv_mesg)

    print(recv_len, filesize_b)
    now = time.time()
    stamp = int(now - old)
    print('总共用时%ds' % stamp)
    f.close()