import socket

phone = socket.socket()
phone.connect(('127.0.0.1', 8080))

while 1:
    msg = input('>>>')
    if msg.upper() == 'Q': break
    
    phone.send(msg.encode('utf-8'))
    
    server_data = phone.recv(1024)
    print(server_data.decode('utf-8'))

phone.close()
