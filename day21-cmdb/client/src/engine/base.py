from ..plugins import get_server_info
import requests
from concurrent.futures import ThreadPoolExecutor
import json


class BaseHandler():
    """
    定义一个基类  约束派生类的行为
    定义handler方法
    
    """
    
    def cmd(self, command, hostname=None):
        raise NotImplementedError('cmd() must be Implemented')
    
    def handler(self):
        raise NotImplementedError('handler() must be Implemented')


class SSHandSaltHandler(BaseHandler):
    def handler(self):
        
        print(self.__class__)
        # 1. 获取未采集的主机列表
        r1 = requests.get(
            url='http://127.0.0.1:8000/api/asset/',
        )
        host_list = r1.json()
        
        # 2. 创建线程池
        pool = ThreadPoolExecutor(20)
        
        # 3. 提交任务
        for hostname in host_list:
            pool.submit(self.task, hostname)
    
    def task(self, hostname):
        """
        获取资产信息 提交到API
        :param hostname:
        :return:
        """
        
        info = get_server_info(self, hostname)
        
        r1 = requests.post(
            url='http://127.0.0.1:8000/api/asset/',
            # data=info,
            # json=info,
            data=json.dumps(info).encode('gbk'),
        
        )
        
        print(r1)
        print(r1.text)
