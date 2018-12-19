import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  #配置文件的上层目录
NEW_FILENAME=os.path.join(BASE_DIR,'view')             #新文件目录
NAME_PWD=os.path.join(BASE_DIR,'db','user')        #用户名和密码目录
USER_FILE=os.path.join(BASE_DIR,'db')

