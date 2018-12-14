import os
import json
import socket
import struct
import re

FTP_CLIENT = socket.socket()
FTP_CLIENT.connect(('127.0.0.1',8080))

while 1:
    # msg = input('>>>')
    msg = 'E:\python24\office.ISO'
    if  msg.upper() == 'Q': break

    msg_size = os.path.getsize(msg)
    msg_name = re.findall('\w*[.]\w*', msg)
    file_dict={'file_name':msg_name,'file_size':msg_size}
    file_info = 'send|%s|%smb' % (msg_name, msg_size)
    file_dict_json = json.dumps(file_info)
    FTP_CLIENT.send(file_dict_json.encode('utf-8'))

    head_bytes = FTP_CLIENT.recv(4)
    total_size = struct.unpack('i',head_bytes)[0]

    data_size = 0
    res = b''
    with open(msg,'rb')as f_msg:
        msg_data = f_msg.read(1024)
        FTP_CLIENT.sendall(msg_data)

        while data_size < total_size:
            data = FTP_CLIENT.recv(1024)
            res = res + data
            data_size = data_size + len(data)



        print(res.decode('gbk'))

FTP_CLIENT.close()