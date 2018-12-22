import re
import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib


FTP_CLIENT = socket.socket()
FTP_CLIENT.connect(('127.0.0.1',8080))

while 1:
    msg = 'D:\\baidu.exe'
    if  msg.upper() == 'Q': break

    msg_size = os.path.getsize(msg)     # 获得文件大小
    msg_name = re.findall('\w*[.]\w*', msg)     # 取出文件名
    msg_name = 'new' + msg_name[0]
    file_dict={'file_name':msg_name,'file_size':msg_size}   # 文件信息封装为字典

    head_info = json.dumps(file_dict)  # 转换为json字符串
    head_info_len = struct.pack('h',len(head_info),) # 字符串长度打包

    FTP_CLIENT.send(head_info_len)   # 发送head_info长度
    FTP_CLIENT.send(head_info.encode('utf-8'))   # 发送文件信息

    with open(msg,'rb')as f_msg:
        data = f_msg.read()
        FTP_CLIENT.send(data)
    print('%s文件发送完成' % msg)
    break
FTP_CLIENT.close()

