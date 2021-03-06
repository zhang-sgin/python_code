import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)

while 1:
    con, addr = phone.accept()
    print(addr)
    
    while 1:
        try:
            client_data = con.recv(1024)
            ret = subprocess.Popen(client_data.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()
            con.send(correct_msg + error_msg)
        except Exception:
            break
    
    con.close()

phone.close()
