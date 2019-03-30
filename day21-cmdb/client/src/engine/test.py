from src.engine.base import BaseHandler
from src.plugins import get_server_info

import requests, json
import paramiko

class DISK:
    def __init__(self,ip,port,user,password):
        self.ip=ip
        self.port=port
        self.user=user
        self.password=password


    def connect(self,*args,**kwargs):
        ssh = paramiko.SSHClient()
        key = paramiko.AutoAddPolicy()
        ssh.set_missing_host_key_policy(key)
        ssh.connect(self.ip, self.port, self.user, self.password ,timeout=5)
        stdin, stdout, stderr = ssh.exec_command("df -h |awk 'NR == 2'")

        abc = stdout.read().decode('gbk').split()

        df = {
            'name':abc[0],
            'total':abc[1],
            'use':abc[2],
            'free':abc[3],
            'percent':abc[4],
            'location':abc[5]
        }
        disk = {'disk':df}
        return disk


    def handler(self):
        print('agent')

        # 1. 资产采集
        # info = get_server_info(self)
        info = DISK.connect()
        # 2. 上报资产信息

        r1 = requests.post(
            url='http://127.0.0.1:8000/api/asset/',
            # data=info,
            # json=info,
            data=json.dumps(info).encode('gbk'),
            headers={
                'content-type': 'application/json'
            }

        )

        print(r1)
        print(r1.text)



