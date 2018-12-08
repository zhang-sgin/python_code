import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)

con,addr = phone.accept()

while 1:
    try:
        client_data = con.recv(1024)
        con.send(client_data + b'sb')
    except Exception:
        break

phone.close()

