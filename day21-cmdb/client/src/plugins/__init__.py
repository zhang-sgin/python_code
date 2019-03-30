from conf import settings
from lib.import_class import import_string


def get_server_info(handler, hostname=None):
    """
    通过配置 去采集信息
    :return:
    """
    
    info = {}
    
    for name, path in settings.PLUGINS_DICT.items():
        """
        disk src.plugins.disk.Disk
        memory src.plugins.memory.Memory
        nic src.plugins.nic.NIC
        """
        plugin_class = import_string(path)
        obj = plugin_class()
        ret = obj.process(handler, hostname)
        info[name] = ret
        print(info)
    
    return info