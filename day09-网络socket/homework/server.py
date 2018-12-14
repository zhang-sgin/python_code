import os
import json
import socket
import subprocess
import struct

FTP_SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
FTP_SERVER.bind(('127.0.0.1',8080))
FTP_SERVER.listen(5)

while 1:
    con,addr = FTP_SERVER.accept()
    print(addr)
    while 1:
        try:
            clinet_data = con.recv(1024)
            ret = subprocess.Popen(clinet_data.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()

            total_size = len(correct_msg + error_msg)
            print(total_size)

            head = struct.pack('i',total_size)
            con.send(head)

            con.send(correct_msg)
            con.send(error_msg)
        except Exception:
            break
    con.close()
FTP_SERVER.close()