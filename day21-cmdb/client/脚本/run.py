import requests
import json
import subprocess


def agent():
    """
    执行命令，获取到资产信息，上报给api
    :return:
    """
    
    # 1. 在本机执行命令采集资产  硬盘、网卡、内存 。。。
    
    disk = subprocess.getoutput('dir')
    
    # 2. 错误的处理 （traceback.format_exc()）
    
    # 3. 自动发现
    
    """
    唯一标识：
        1. 物理机  s/n号
        2. 物理机 + 虚拟机
            1. 物理机 和 虚拟机 分开管理   s/n号 + 其他管理
            2. 主机名
                规则 + 流程：
                    1. 新增主机 空的文件  响应之后  把主机名保存到文件中
                    2. 老的主机  改主机名 读取文件中的主机名  和当前采集的主机名对比
                                原主机名和新的主机名都提交到api
                                api返回新的主机名  agent修改文件中主机名为当前主机名
                    
    """
    
    info = {'hostname': 'c1.com', 'disk': disk}
    
    r1 = requests.post(
        url='http://127.0.0.1:8000/api/asset/',
        # data=info,
        # json=info,
        data=json.dumps(info).encode('gbk'),
    
    )
    
    print(r1)
    print(r1.text)


# agent()
from concurrent.futures import ThreadPoolExecutor


def task(host):
    info = {'hostname': host, 'disk': 'xxxx'}
    
    r1 = requests.post(
        url='http://127.0.0.1:8000/api/asset/',
        # data=info,
        # json=info,
        data=json.dumps(info).encode('gbk'),
    
    )
    print(r1)


def ssh():
    # 1. 从api中获取到未采集的主机列表
    r1 = requests.get(
        url='http://127.0.0.1:8000/api/asset/',
    )
    
    # print(r1.content,type(r1.content))
    # print(r1.text,type(r1.text))
    # print(r1.json(),type(r1.json()))
    
    host_list = r1.json()
    
    # 2. 连接每一台主机 执行命令 得到资产信息 上报给api
    
    pool = ThreadPoolExecutor(20)
    
    for host in host_list:
        pool.submit(task, host)


agent()
