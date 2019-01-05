import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib
import re

buffer =  1024
def process_bar(precent, width=50):
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')


class FTP_SERVER(socketserver.BaseRequestHandler):
    def recv_msg(self):
        head_size = self.request.recv(4)
        st_data = struct.unpack('i', head_size)[0]
        head_data = self.request.recv(st_data).decode('utf-8')
        return json.loads(head_data)

    def cmd(self,*args,**kwargs):
        client_data = self.request.recv(1024)
        ret = subprocess.Popen(client_data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        correct_msg = ret.stdout.read()
        error_msg = ret.stderr.read()
        total_size = len(correct_msg + error_msg)
        print(total_size)
        head = struct.pack('i', total_size)
        self.request.send(head)
        self.request.send(correct_msg)
        self.request.send(error_msg)

    def quota_count(self,file_size,quota):
        nums = []
        with open('quota', 'r') as f:
            for s in re.findall(r'\d+', f.read()):
                nums.append(float(s))
        z = (sum(nums))
        # print(sum(nums))
        return z

    def post_file(self,*args,**kwargs):
        quota = 1348576000
        clinet_head = self.request.recv(4)  # 上传文件
        print(clinet_head, type(clinet_head))
        if clinet_head: print('post_file已连接')

        clinet_head_len = struct.unpack('i', clinet_head)[0]
        print(clinet_head_len,type(clinet_head_len))
        clinet_data = self.request.recv(clinet_head_len)
        # print(clinet_data)
        head = json.loads(clinet_data.decode('utf-8'))
        print(head)
        post_file_size=head.get('file_size')
        print(post_file_size,type(post_file_size))

        quota_size =  int(self.quota_count(post_file_size,quota))
        print(quota_size,type(quota_size))
        if quota_size <= quota:
            with open('quota', encoding='utf-8', mode='a+')as f_quota:
                post_file_size = str(post_file_size)
                f_quota.write('a' + post_file_size)
            data_size = 0
            res = b''
            old = time.time()
            with open(head['file_name'], 'wb')as f_file:
                while data_size < head['file_size']:
                    percent = data_size / head['file_size']
                    process_bar(percent)
                    if head['file_size'] - data_size >= 1024:
                        res = self.request.recv(1024)
                        f_file.write(res)
                        data_size += len(res)
                        ok_reset = json.dumps('ok')
                        self.request.sendall(ok_reset.encode('utf-8'))
                    else:
                        res = self.request.recv(head['file_size'] - data_size)
                        data_size += len(res)
                        f_file.write(res)
                        break
            reset=(data_size, head['file_size'])
            print(reset)
            now = time.time()
            stamp = int(now - old)
            ok_reset = json.dumps('ok')
            self.request.sendall(ok_reset.encode('utf-8'))
            print('总共用时%ds' % stamp)
            with open('quota', encoding='utf-8',mode='r+')as f_quota:
                post_file_size=str(post_file_size)
                f_quota.write('a'+post_file_size)
        else:
            print('文件太大啦，限额不足')
            fail_reset = json.dumps('fail')
            self.request.sendall(fail_reset.encode('utf-8'))

    def md5(self, username, pwd):
        md5 = hashlib.md5('zhangz-l'.encode('utf-8'))
        md5.update(pwd.encode('utf-8'))
        return md5.hexdigest()

    def handle(self):
        clinet_head = self.request.recv(4)  # 上传文件
        print(clinet_head, type(clinet_head))
        if clinet_head: print('handle已连接')

        clinet_head_len = struct.unpack('i', clinet_head)[0]
        print(clinet_head_len, type(clinet_head_len))
        clinet_data = self.request.recv(clinet_head_len)
        head = json.loads(clinet_data.decode('utf-8'))
        print(head)
        if ('name') in head.keys():
            name = head.get('name')
            pwd = head.get('pwd')
            with open('user', encoding='utf8')as f_registry:
                for i in f_registry:
                    login_line = i.strip().split('|')
                    md5_pwd = self.md5(name, login_line[1])
                    if name == login_line[0] and pwd == md5_pwd:  # zz 123
                        ok_reset = json.dumps('ok')
                        self.request.sendall(ok_reset.encode('utf-8'))
                    else:
                        fail_reset = json.dumps('fail')
                        self.request.sendall(fail_reset.encode('utf-8'))
        elif ('action') in head.keys():
            value = head.get('action')
            # print(head,type(head))
            if hasattr(self, value):
                getattr(self, value)(value)

server=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FTP_SERVER)
server.serve_forever()