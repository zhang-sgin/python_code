from conf import settings
from src.engine.agent import AgentHandler
from src.engine.ssh import SSHHandler
from src.engine.salt import SaltHandler
from src.engine.aliyun import AliyunHandler
from lib.import_class import import_string


def run():
    """
    
    资产采集的程序的入口
    :return:
    """
    print('资产采集')
    if settings.ENGINE == 'agent':
        obj = AgentHandler()
        obj.handler()
    elif settings.ENGINE == 'ssh':
        obj = SSHHandler()
        obj.handler()
    elif settings.ENGINE == 'salt':
        obj = SaltHandler()
        obj.handler()
    elif settings.ENGINE == 'aliyun':
        obj = AliyunHandler()
        obj.handler()
    else:
        print('不支持该模式 {}'.format(settings.ENGINE))
    

    engine_path = settings.ENGINE_DICT.get(settings.ENGINE)
    engine_class = import_string(engine_path)

    obj = engine_class()
    obj.handler()
