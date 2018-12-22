import os,sys,re,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from homework.lib import commom
from homework.conf import settings

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



# buffer =  1024
def process_bar(precent, width=50):
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')


class FTP_SERVER(socketserver.BaseRequestHandler):
    def handle(self):
        clinet_head = self.request.recv(2)
        print(clinet_head,type(clinet_head))
        if clinet_head: print('已连接')
        clinet_head_len = struct.unpack('h', clinet_head)[0]
        clinet_data = self.request.recv(clinet_head_len)
        head = json.loads(clinet_data.decode('utf-8'))

        data_size = 0
        res = b''
        old = time.time()
        with open(head['file_name'], 'wb')as f_file:
            while data_size < head['file_size']:
                percent = data_size / head['file_size']
                process_bar(percent)
                if head['file_size'] - data_size >= 1024:
                    res =  self.request.recv(1024)
                    f_file.write(res)
                    data_size += len(res)
                else:
                    res =  self.request.recv(head['file_size']-data_size)
                    data_size += len(res)
                    f_file.write(res)
                    break
        print(data_size, head['file_size'])
        now = time.time()
        stamp = int(now - old)
        print('总共用时%ds' % stamp)
server=socketserver.ThreadingTCPServer(IP_PORT,FTP_SERVER)
server.serve_forever()

def run():
    pass
