from src.engine.base import BaseHandler
from ..plugins import get_server_info
import requests
import json


class AgentHandler(BaseHandler):
    """
    
    agent模式下资产采集  硬盘 网卡 内存。。。
    
    """
    
    def cmd(self, command, hostname=None):
        import subprocess
        return subprocess.getoutput(command)
    
    def handler(self):
        print('agent')
        
        # 1. 资产采集
        info = get_server_info(self)
        print(self)
        
        # 2. 上报资产信息
        
        r1 = requests.post(
            url='http://127.0.0.1:8000/api/asset/',
            # data=info,
            # json=info,
            data=json.dumps(info).encode('gbk'),
            headers={
                'content-type':'application/json'
            }
        
        )
        
        print(r1)
        print(r1.text)
