import time
import os, sys
import os.path
import hashlib
import random, string
import logging
import logging.config

'''

	1、计算两个格式化时间之间差了多少年月日时分秒
'''
# def count_time():
#     print('提示：\n 世界地球日：1970-04-22 13:00:00 \n 当前时间：2018-11-26 21:30:00')
#     time_one=input('请输入地球日时间（精确时间）：'.strip())
#     time_two=input('请输入当前时间：'.strip())
#     old_time=time.mktime(time.strptime(time_one,'%Y-%m-%d %H:%M:%S'))
#     new_time=time.mktime(time.strptime(time_two,'%Y-%m-%d %H:%M:%S'))
#     is_time=new_time-old_time
#     struct_time=time.gmtime(is_time)
#     print('过去了%d年%d月%d天%d小时%d分钟%d秒'
#           % (struct_time.tm_year-1970,struct_time.tm_mon-1,
#             struct_time.tm_mday-1,struct_time.tm_hour,
#             struct_time.tm_min,struct_time.tm_sec))
# if __name__=='__main__':
#     count_time()
'''
	2、计算当前时间所在月1号的时间戳
'''
# def first_time():
#     in_time=time.strftime('%Y-%m-%d %H:%M:%S')
#     in_time2=in_time[0:7]+'-01'+' 00:00:00'
#     old_time = time.mktime(time.strptime(in_time2 , '%Y-%m-%d %H:%M:%S'))
#     print(old_time)
# if __name__=='__main__':
#     first_time()
'''
	3、分别列出给定目录下所有的文件和文件夹
	
'''
# def seesee():
#     in_dir=input('请输入查询目录：').strip()
#     in_dir2=os.listdir(in_dir)
#     for i in in_dir2:
#         print(i)
# if __name__=='__main__':
#     seesee()
'''
	4、获取当前文件所在目录

'''
# print(os.getcwd())

'''
	5、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件

'''
# def create_dir_file():
#     create_dir=input('请输入创建的目录：')
#     create_file=input('请输入创建的文件：')
#     print(os.mkdir(create_dir))
#     see_create_dir=os.path.isdir(create_dir)
#     if see_create_dir:
#         os.chdir(create_dir)
#         with open(create_file,encoding='utf-8',mode='w')as f_1:
#             f_1.write('seesee 就 seesee!')
#
# if __name__=='__main__':
#     create_dir_file()

'''
	6、计算某路径下所有文件和文件夹的总大小

'''
# size = []
# def count_dir_file(path):
#     in_dir2 = os.listdir(path)
#     for i in in_dir2:
#         a_path=os.path.join(path,i)
#         if os.path.isdir(a_path):
#             count_dir_file(a_path)
#         elif os.path.isfile(a_path):
#             z_file_size=os.path.getsize(a_path)
#             fil_size=z_file_size/1024
#             print('{} 大小为：{}KB'.format(a_path,round(fil_size,2)))
#             size.append(fil_size)
#
# ss_dir =input('请输入路径：')
# if __name__ == '__main__':
#     count_dir_file(ss_dir)
#     print('目录中的文件总大小：{}KB'.format(round(sum(size))))

'''
	7、校验两个文件的一致性
'''
# def count_md5(file):
#     md5 = hashlib.md5()
#     with open(file,encoding='utf-8')as f_1:
#         for i in f_1:
#             if i:
#                 md5.update(i.encode('utf-8'))
#     print(md5.hexdigest())
# if __name__ == '__main__':
#     file1 = input('请输入对比文件1：')
#     file2 = input('请输入对比文件2：')
#     count_md5(file1)
#     count_md5(file2)

'''
	8、加盐的密文登陆
'''
md5 = hashlib.md5('12323414'.encode('utf-8'))
pwd = '123'
md5.update(pwd.encode('utf-8'))
print(md5.hexdigest())


def login():
    count=1
    salt='haha'
    while count < 4:
        login_user_name=input('请输入您的用户名：')
        login_password=input('请输入用户名密码：')
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8)) # 生成8位随机字符串
        md5 = hashlib.md5(ran_str.encode('utf-8'))
        with open('user_info.txt',encoding='utf-8')as f_login:
            for i in f_login:
                login_line=i.strip().split(' ')
                if login_user_name == login_line[0] and login_password == login_line[1]:
                    print('登录成功')
                    md5.update(login_password.encode('utf-8'))
                    with open('md5_user',encoding='utf-8',mode='a')as f_md5:
                        f_md5.write(login_user_name + '|' + md5.hexdigest() + '|'+'\n')
                else:
                    print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                    count+=1
                break
login()
'''
	9、完成一个既可以向文件输出又可以向屏幕输出的日志设置
'''

# logger = logging.getLogger()
# fh = logging.FileHandler('test.log',encoding='utf-8')
# ch = logging.StreamHandler()

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setLevel(logging.DEBUG)

# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')


# 定义三种日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束
logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
logfile_name = 'zz-test.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('hahahahahahhsb')  # 记录该文件的运行状态


if __name__ == '__main__':
    load_my_logging_cfg()
