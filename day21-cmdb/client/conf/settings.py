import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE = 'agent'

ENGINE_DICT = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
    'aliyun': 'src.engine.aliyun.AliyunHandler',
    
}

PLUGINS_DICT = {
    
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.NIC',
}

# ################  SSH配置 ################
SSH_PRIVATE_KEY = '私钥的路径'
SSH_PORT = '22'  # 端口
SSH_USER = 'cmdb'  # 用户名

DEBUG = True
