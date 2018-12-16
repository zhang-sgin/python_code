import re
import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib




# class client:
#     gg = {"查看家目录" : "list_home",
#           "创建目录" : "create_dir",
#           "删除目录" : 'del_dir',
#           "上传文件" : 'post_file',
#           "下载文件" : 'get_file',}
#     def __init__(self, name):
#         self.name = name
#
#     def list_home(self):
#         client = socket.socket()
#         client.connect(('127.0.0.1', 8080))
#         while 1:
#             msg = input('>>>')
#             if msg.upper() == 'Q': break
#             client.send(msg.encode('utf-8'))
#             head_bytes = client.recv(4)
#
#             total_size = struct.unpack('h', head_bytes)[0]
#
#             data_size = 0
#             res = b''
#             while data_size < total_size:
#                 data = client.recv(1024)
#                 res = res + data
#                 data_size = data_size + len(data)
#
#             print(res.decode('gbk'))
#
#         client.close()
#
#     def create_dir(self):
#         print('create_dir')
#
#     def del_dir(self):
#         print('del_dir')
#
#     def post_file(self):
#         FTP_CLIENT = socket.socket()
#         FTP_CLIENT.connect(('127.0.0.1', 8080))
#         while 1:
#             msg = 'E:\python24\office.ISO'
#             if  msg.upper() == 'Q': break
#
#             msg_size = os.path.getsize(msg)     # 获得文件大小
#             msg_name = re.findall('\w*[.]\w*', msg)     # 取出文件名
#             msg_name = 'new' + msg_name[0]
#             file_dict={'file_name':msg_name,'file_size':msg_size}   # 文件信息封装为字典
#
#             head_info = json.dumps(file_dict)  # 转换为json字符串
#             head_info_len = struct.pack('h',len(head_info),) # 字符串长度打包
#
#             FTP_CLIENT.send(head_info_len)   # 发送head_info长度
#             FTP_CLIENT.send(head_info.encode('utf-8'))   # 发送文件信息
#
#             with open(msg,'rb')as f_msg:
#                 data = f_msg.read()
#                 FTP_CLIENT.send(data)
#             print('发送%s文件完成' % msg)
#             break
#         FTP_CLIENT.close()
#
#     def get_file(self):
#         print('get_file')
#
#
#
#
# def login():
#     print('欢迎来到选课系统！')
#     count = 1
#     while count < 4:
#         print('请先登录')
#         username = input('请输入用户名：').strip()
#         password = input('请输入密码：').strip()
#         with open('user', encoding='utf8')as f_registry:
#             for i in f_registry:
#                 login_line = i.strip().split('|')
#                 if username == login_line[0] and password == login_line[1]:  # zz 123
#                     print('用户%s登录成功！' % (username))
#                     client_user = client(username)
#                     while 1:
#                         tmp = {}
#                         for index, i in enumerate(client_user.gg, 1):
#                             print(index, i)
#                             tmp[str(index)] = client_user.gg[i]
#                         C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
#                         func = getattr(client_user, tmp[C])
#                         func()
# login()



FTP_CLIENT = socket.socket()
FTP_CLIENT.connect(('127.0.0.1', 8080))
while 1:
    msg = 'E:\python24\office.ISO'
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
    print('发送%s文件完成' % msg)
    break
FTP_CLIENT.close()