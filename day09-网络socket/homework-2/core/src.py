import os
import json
import socket
import subprocess
import struct
import socketserver
import hashlib

def login():
    print('欢迎来到ftp系统！')
    count = 1
    while count < 4:
        print('请先登录')
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        with open('user', encoding='utf8')as f_registry:
            for i in f_registry:
                login_line = i.strip().split('|')
            if username == login_line[0] and password == login_line[1]:
                print('%s登录成功！' % (username))
            else:
                print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                count += 1




def run():
    pass
