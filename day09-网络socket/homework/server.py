import os,sys,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib


def process_bar(precent, width=50):
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')


FTP_SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
FTP_SERVER.bind(('127.0.0.1',8080))
FTP_SERVER.listen(5)

while 1:
    conn,addr = FTP_SERVER.accept()
    print(conn)
    try:
        clinet_head = conn.recv(1024)
        if clinet_head:print('已连接')
        clinet_head_len = struct.unpack('i',clinet_head)[0]
        clinet_data = conn.recv(clinet_head_len)
        head = json.loads(clinet_data.decode('utf-8'))

        data_size = 0
        res = b''
        old = time.time()
        with open(head['file_name'], 'wb')as f_file:
            while data_size < head['file_size']:
                percent = data_size / head['file_size']
                process_bar(percent)
                # process_bar(data_size,head['file_size'])
                if head['file_size'] - data_size >= 1024:
                    res = conn.recv(1024)
                    f_file.write(res)
                    data_size += len(res)
                else:
                    res = conn.recv(head['file_size']-data_size)
                    data_size += len(res)
                    f_file.write(res)
                    break
        print(data_size, head['file_size'])
        now = time.time()
        stamp = int(now - old)
        print('总共用时%ds' % stamp)
    except Exception as e:
        pass