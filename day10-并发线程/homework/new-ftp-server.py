import sys, os
import time
import socket
import hashlib
import pickle
import subprocess
import socketserver
import json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import settings


# class FTP_server(socketserver.BaseRequestHandler):
#
#     def login(self,username,pwd):
#         user_file=pickle.load(open('user','rb'))
#         if  username in user_file:
#             if user_file[user_file] == self
#
#     def before(self,username,pwd,ret):
#         if ret = '1':
#             r=self.login()
#
#
#
#     def handle(self):
#         self.request.sendall(bytes('欢迎登陆FTP系统',encoding='utf-8'))
#         by=self.request.recv(1024)
#         ret=str(by,encoding='utf-8')
#         print(ret)
#         self.request.sendall(bytes('ojbk',encoding='utf-8'))
#         c=self.request.recv(1024)
#         r=str(c,encoding='utf-8')
#         username,pwd=r.split('|')
#         self.before(username, pwd, ret)

