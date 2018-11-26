import time,datetime
'''
	1、计算两个格式化时间之间差了多少年月日时分秒
'''
# def count_time():
#     print('提示：\n 建国时间：1949-10-01 15:00:00 \n 当前时间：2018-11-26 21:30:00')
#     time_one=input('请输入建国时间（精确时间）：')
#     time_two=input('请输入当前时间：')
#     # old_time=time.mktime(time.strptime('1949-10-01 15:00:00','%Y-%m-%d %H:%M:%S'))
#     old_time=time.mktime(time.strptime(time_one,'%Y-%m-%d %H:%M:%S'))
#     # new_time=time.mktime(time.strptime('2018-11-26 21:30:00','%Y-%m-%d %H:%M:%S'))
#     new_time=time.mktime(time.strptime(time_two,'%Y-%m-%d %H:%M:%S'))
#     is_time=new_time-old_time
#     struct_time=time.gmtime(is_time)
#     print('从中华人民共和国建国至今，过去了%d年%d月%d天%d小时%d分钟%d秒'
#           % (struct_time.tm_year-1970,struct_time.tm_mon-1,
#             struct_time.tm_mday-1,struct_time.tm_hour,
#             struct_time.tm_min,struct_time.tm_sec))
#
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


'''
	4、获取当前文件所在目录

'''

'''
	5、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件

'''

'''
	6、计算某路径下所有文件和文件夹的总大小

'''

'''
	7、校验两个文件的一致性

'''

'''
	8、加盐的密文登陆

'''

'''
	9、完成一个既可以向文件输出又可以向屏幕输出的日志设置
'''