import time
import os
import os.path
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


'''
	8、加盐的密文登陆

'''

'''
	9、完成一个既可以向文件输出又可以向屏幕输出的日志设置
'''



