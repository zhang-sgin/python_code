import os,json,re
msg = 'E:\python24\office.ISO'

msg_size = os.path.getsize(msg)
msg_size = msg_size/1048576
msg_name = re.findall('\w*[.]\w*', msg)
file_dict = {'file_name': msg_name, 'file_size': msg_size}
file_info = 'send|%s|%smb' % (msg_name, msg_size)
file_dict_json = json.dumps(file_info)
print(file_dict_json)