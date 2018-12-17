import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib


# def process_bar(precent, width=50):
#     use_num = int(precent*width)
#     space_num = int(width-use_num)
#     precent = precent*100
#     print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')
#
#
# # FTP_SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# # FTP_SERVER.bind(('127.0.0.1',8080))
# # FTP_SERVER.listen(5)
#
# class FTP_SERVER(socketserver.BaseRequestHandler):
#     def handle(self):
#         # while 1:
#         #     conn,addr = FTP_SERVER.accept()
#         #     print(conn)
#         try:
#             # clinet_head = conn.recv(1024)
#             clinet_head = self.request.recv(1024)
#             print(clinet_head)
#             if clinet_head:print('已连接')
#             clinet_head_len = struct.unpack('i',clinet_head)[0]
#             print(clinet_head_len)
#             # clinet_data = conn.recv(clinet_head_len)
#             clinet_data =  self.request.recv(clinet_head_len)
#             print(clinet_data)
#             head = json.loads(clinet_data.decode('utf-8'))
#             print(head)
#
#             data_size = 0
#             res = b''
#             old = time.time()
#             with open(head['file_name'], 'wb')as f_file:
#                 while data_size < head['file_size']:
#                     percent = data_size / head['file_size']
#                     process_bar(percent)
#                     # process_bar(data_size,head['file_size'])
#                     if head['file_size'] - data_size >= 1024:
#                         # res = conn.recv(1024)
#                         res =  self.request.recv(1024)
#                         f_file.write(res)
#                         data_size += len(res)
#                     else:
#                         # res = conn.recv(head['file_size']-data_size)
#                         res =  self.request.recv(head['file_size']-data_size)
#                         data_size += len(res)
#                         f_file.write(res)
#                         break
#             print(data_size, head['file_size'])
#             now = time.time()
#             stamp = int(now - old)
#             print('总共用时%ds' % stamp)
#         except Exception as e:
#             pass
# server=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FTP_SERVER)
# server.serve_forever()







# buffer =  1024
# def process_bar(precent, width=50):
#     use_num = int(precent*width)
#     space_num = int(width-use_num)
#     precent = precent*100
#     print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')
#
#
# class FTP_SERVER(socketserver.BaseRequestHandler):
#     def handle(self):
#         clinet_head = self.request.recv(1024)
#         print(clinet_head)
#         if clinet_head: print('已连接')
#         clinet_head_len = struct.unpack('h', clinet_head)[0]
#         clinet_data = self.request.recv(clinet_head_len)
#         head = json.loads(clinet_data.decode('utf-8'))
#
#     def get_file(self,*args,**kwargs):
#         file_size = args[0].get('file_size')
#         file_name = args[0].get('file_name')
#         data_size = 0
#         res = b''
#         old = time.time()
#         with open(file_name, 'wb')as f_file:
#             while data_size < file_size:
#                 percent = data_size / file_size
#                 process_bar(percent)
#                 # process_bar(data_size,head['file_size'])
#                 if file_size - data_size >= 1024:
#                     # res = conn.recv(1024)
#                     res =  self.request.recv(1024)
#                     f_file.write(res)
#                     data_size += len(res)
#                 else:
#                     res =  self.request.recv(file_size-data_size)
#                     data_size += len(res)
#                     f_file.write(res)
#                     break
#         print(data_size, file_size)
#         now = time.time()
#         stamp = int(now - old)
#         print('总共用时%ds' % stamp)
#
# server=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FTP_SERVER)
# server.serve_forever()



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

    def post_file(self,*args,**kwargs):
        # clinet_head = self.request.recv(2)  # 上传文件
        # print(clinet_head, type(clinet_head))
        # if clinet_head: print('已连接')
        #
        # clinet_head_len = struct.unpack('h', clinet_head)[0]
        # print(clinet_head_len)
        # clinet_data = self.request.recv(clinet_head_len)
        # print(clinet_data)
        # head = json.loads(clinet_data.decode('utf-8'))

        clinet_head = self.request.recv(4)  # 上传文件
        print(clinet_head, type(clinet_head))
        if clinet_head: print('post_file已连接')

        clinet_head_len = struct.unpack('i', clinet_head)[0]
        print(clinet_head_len,type(clinet_head_len))
        clinet_data = self.request.recv(clinet_head_len)
        print(clinet_data)
        head = json.loads(clinet_data.decode('utf-8'))
        print(head)

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
                else:
                    res = self.request.recv(head['file_size'] - data_size)
                    data_size += len(res)
                    f_file.write(res)
                    break
        print(data_size, head['file_size'])
        now = time.time()
        stamp = int(now - old)
        print('总共用时%ds' % stamp)

    def handle(self):
        clinet_head = self.request.recv(4)  # 上传文件
        print(clinet_head, type(clinet_head))
        if clinet_head: print('handle已连接')

        clinet_head_len = struct.unpack('i', clinet_head)[0]
        print(clinet_head_len,type(clinet_head_len))
        clinet_data = self.request.recv(clinet_head_len)
        # print(clinet_data)
        head = json.loads(clinet_data.decode('utf-8'))
        value=head.get('action')
        # print(head,type(head))
        if hasattr(self, value):
            getattr(self, value)(value)

    # def handle(self):
    #     while 1:
    #         data_msg = self.recv_msg()
    #         print('handle')
    #         print(data_msg)
    #         if hasattr(self, '%s' % data_msg['action']):
    #             getattr(self, '%s' % data_msg['action'])(data_msg)



server=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FTP_SERVER)
server.serve_forever()