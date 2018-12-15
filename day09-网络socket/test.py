import os,json,re

msg = 'E:\python24\office.ISO'
msg_size = os.path.getsize(msg)  # 获得文件大小
msg_name = re.findall('\w*[.]\w*', msg)  # 取出文件名
msg_name = 'new' + msg_name[0]
file_dict = {'file_name': msg_name, 'file_size': msg_size}
print(file_dict)