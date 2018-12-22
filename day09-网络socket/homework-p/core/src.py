import os,sys,re,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from lib import common
from conf import setting
from db import *

# def login():
#     print('欢迎来到ftp系统！')
#     count = 1
#     while count < 4:
#         print('请先登录')
#         username = input('请输入用户名：').strip()
#         password = input('请输入密码：').strip()
#         with open('user', encoding='utf8')as f_registry:
#             for i in f_registry:
#                 login_line = i.strip().split('|')
#             if username == login_line[0] and password == login_line[1]:
#                 print('%s登录成功！' % (username))
#             else:
#                 print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
#                 count += 1
login_status={'username':None,'status':False}
def login(x):
    def inner(*args,**kwargs):
        if login_status['status']:
            ret = x(*args,**kwargs)
            return ret
        else:
            count = 1
            while count <4:
                print('请先登录')
                username=input('请输入用户名：').strip()
                password=input('请输入密码：').strip()
                user=db.user
                for i in user:print(i)
                with open(user,encoding='utf8')as f_registry:
                    for i in f_registry:
                        login_line=i.strip().split(' ')
                        # print(login_line)
                        if username == login_line[0] and password ==login_line[1]:
                            login_status['username'] = username
                            login_status['status'] = password
                            ret=x(*args,**kwargs)
                            return ret
                    else:
                        print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                        count += 1
    return inner

def run():
    print(123)
