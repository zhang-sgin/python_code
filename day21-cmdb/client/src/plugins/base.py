from conf import settings

class BasePlugin:
    
    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASE_DIR
    
    def get_os(self, handler, hostname=None):
        # os = handler.cmd('dir', hostname)
        
        return 'linux'
    
    def process(self, handler, hostname=None):
        
        os = self.get_os(handler, hostname)
        
        if os == 'win':
            ret = self.win(handler, hostname)
        else:
            ret = self.linux(handler, hostname)
        
        return ret
