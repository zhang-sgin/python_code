import socket
import struct

phone = socket.socket()
phone.connect(('127.0.0.1', 8080))

while 1:
    msg = input('>>>')
    if msg.upper() == 'Q': break
    
    phone.send(msg.encode('utf-8'))
    
    head_bytes = phone.recv(4)
    
    total_size = struct.unpack('i',head_bytes)[0]
    
    data_size = 0
    res = b''
    while data_size < total_size:
        data = phone.recv(1024)
        res = res + data
        data_size = data_size + len(data)
    
    print(res.decode('utf-8'))

phone.close()
