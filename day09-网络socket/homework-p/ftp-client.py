import re
import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib
from db import *


class client:
    gg = {"查看家目录 dir" : "cmd",
          "创建目录 md folder" : "cmd",
          "删除目录" : 'cmd',
          "上传文件rmdir /s/q folder " : 'post_file',
          "下载文件" : 'get_file',}
    def __init__(self, name):
        self.name = name

    def cmd(self):
        cmd_client = socket.socket()
        cmd_client.connect(('127.0.0.1', 8080))
        while 1:
            msg = input('>>>')
            if msg.upper() == 'Q': break

            file_dict = {'action': 'cmd'}
            head_info = json.dumps(file_dict)  # 转换为json字符串
            head_info_len = struct.pack('i', len(head_info), )  # 字符串长度打包

            cmd_client.send(head_info_len)  # 发送head_info长度
            cmd_client.send(head_info.encode('utf-8'))  # 发送文件信息

            head_info = json.dumps(msg)  # 转换为json字符串
            head_info_len = struct.pack('i', len(head_info), )

            cmd_client.send(msg.encode('utf-8'))
            head_bytes = cmd_client.recv(4)

            total_size = struct.unpack('i', head_bytes)[0]

            data_size = 0
            res = b''
            while data_size < total_size:
                data = cmd_client.recv(1024)
                res = res + data
                data_size = data_size + len(data)

            print(res.decode('gbk'))

        cmd_client.close()

    def post_file(self):
        FTP_CLIENT = socket.socket()
        FTP_CLIENT.connect(('127.0.0.1', 8080))
        while 1:
            msg = 'E:\python24\office.ISO'
            if msg.upper() == 'Q': break

            msg_size = os.path.getsize(msg)  # 获得文件大小
            msg_name = re.findall('\w*[.]\w*', msg)  # 取出文件名
            msg_name = 'new' + msg_name[0]
            file_dict = {'file_name': msg_name, 'file_size': msg_size, 'action': "post_file"}  # 文件信息封装为字典

            head_info = json.dumps(file_dict)  # 转换为json字符串
            head_info_len = struct.pack('i', len(head_info))  # 字符串长度打包

            FTP_CLIENT.send(head_info_len)  # 发送head_info长度
            FTP_CLIENT.send(head_info.encode('utf-8'))  # 发送文件信息
            FTP_CLIENT.send(head_info_len)  # 发送head_info长度
            FTP_CLIENT.send(head_info.encode('utf-8'))  # 发送文件信息

            # post_file_status = obj.recv(1024)
            # print(post_file_status)
            # status = json.loads(post_file_status.decode('utf-8'))
            # print(status)

            with open(msg, 'rb')as f_msg:
                data = f_msg.read()
                FTP_CLIENT.send(data)
                # post_file_status = obj.recv(1024)
                # print(post_file_status)
                # status = json.loads(post_file_status.decode('utf-8'))
                # print(status)
                print('发送%s文件完成' % msg)
            break
        FTP_CLIENT.close()

    def get_file(self):
        print('get_file')

def login(username,pwd):
    user_dict = {'name':username,'pwd':pwd}
    user_dict_json = json.dumps(user_dict)   # 转换为json字符串
    user_head = struct.pack('i', len(user_dict_json))    # 字符串长度打包
    obj.send(user_head)  # 发送user_info长度
    obj.send(user_dict_json.encode('utf-8'))  # 发送文件信息
    login_status=obj.recv(1024)
    head = json.loads(login_status.decode('utf-8'))
    if head == 'ok':
        print('用户%s登录成功' % username)
        client_user = client(username)
        while 1:
            tmp = {}
            for index, i in enumerate(client_user.gg, 1):
                print(index, i)
                tmp[str(index)] = client_user.gg[i]
            C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
            func = getattr(client_user, tmp[C])
            func()
    else:
        print('用户%s登录失败，请重试' % username)

    obj.close()


if __name__ == '__main__':
    obj=socket.socket() #创建客户端socket对象
    obj.connect(('127.0.0.1',8080))
    usrname=input('请输入用户名：')
    pwd=input('请输入密码：')
    login(usrname,pwd)



# def login():
#     print('欢迎来到FTP系统！')
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



# FTP_CLIENT = socket.socket()
# FTP_CLIENT.connect(('127.0.0.1', 8080))
# while 1:
#     msg = 'E:\python24\office.ISO'
#     if msg.upper() == 'Q': break
#
#     msg_size = os.path.getsize(msg)     # 获得文件大小
#     msg_name = re.findall('\w*[.]\w*', msg)     # 取出文件名
#     msg_name = 'new' + msg_name[0]
#     file_dict = {'file_name': msg_name, 'file_size': msg_size, 'action': "post_file"}  # 文件信息封装为字典
#
#     head_info = json.dumps(file_dict)  # 转换为json字符串
#     print(head_info)
#     print(len(head_info))
#     head_info_len = struct.pack('i', len(head_info))  # 字符串长度打包
#     print(head_info_len)
#
#     FTP_CLIENT.send(head_info_len)   # 发送head_info长度
#     FTP_CLIENT.send(head_info.encode('utf-8'))   # 发送文件信息
#     FTP_CLIENT.send(head_info_len)   # 发送head_info长度
#     FTP_CLIENT.send(head_info.encode('utf-8'))   # 发送文件信息
#
#     with open(msg, 'rb')as f_msg:
#         data = f_msg.read()
#         FTP_CLIENT.send(data)
#     print('发送%s文件完成' % msg)
#     break
# FTP_CLIENT.close()



# cmd_client = socket.socket()
# cmd_client.connect(('127.0.0.1', 8080))
# while 1:
#     msg = input('>>>')
#     if msg.upper() == 'Q': break
#
#     file_dict={'action':'cmd'}
#     head_info = json.dumps(file_dict)  # 转换为json字符串
#     head_info_len = struct.pack('i',len(head_info),) # 字符串长度打包
#
#     cmd_client.send(head_info_len)   # 发送head_info长度
#     cmd_client.send(head_info.encode('utf-8'))   # 发送文件信息
#
#
#
#     head_info = json.dumps(msg)  # 转换为json字符串
#     head_info_len = struct.pack('i',len(head_info),)
#
#     cmd_client.send(msg.encode('utf-8'))
#     head_bytes = cmd_client.recv(4)
#
#     total_size = struct.unpack('i', head_bytes)[0]
#
#     data_size = 0
#     res = b''
#     while data_size < total_size:
#         data = cmd_client.recv(1024)
#         res = res + data
#         data_size = data_size + len(data)
#
#     print(res.decode('gbk'))
#
# cmd_client.close()

