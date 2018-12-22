import os
import json
import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',8090))
buffer = 1024 #读取文件的时候，每次读取的大小
head = {
            'filepath':r'C:\Users\Administrator\Desktop\python_code\day09-网络socket\homework', #需要下载的文件路径，也就是文件所在的文件夹
            'filename':'QQ.exe',  #改成上面filepath下的一个文件
            'filesize':None,
        }

file_path = os.path.join(head['filepath'],head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
# json_head = json.dumps(head,ensure_ascii=False)  #字典转换成字符串
json_head = json.dumps(head)  #字典转换成字符串
bytes_head = json_head.encode('utf-8') #字符串转换成bytes类型
print(json_head)
print(bytes_head)

#计算head的长度，因为接收端先接收我们自己定制的报头，对吧
head_len = len(bytes_head) #报头长度
pack_len = struct.pack('i',head_len)
print(head_len)
print(pack_len)
sk.send(pack_len)  #先发送报头长度
sk.send(bytes_head) #再发送bytes类型的报头

#即便是视频文件，也是可以按行来读取的，也可以readline，也可以for循环，但是读取出来的数据大小就不固定了，影响效率，有可能读的比较小，也可能很大，像视频文件一般都是一行的二进制字节流。
#所有我们可以用read，设定一个一次读取内容的大小，一边读一边发，一边收一边写
with open(file_path,'rb') as f:
    while filesize:
        if filesize >= buffer: #>=是因为如果刚好等于的情况出现也是可以的。
            content = f.read(buffer) #每次读取出来的内容
            sk.send(content)
            filesize -= buffer #每次减去读取的大小
        else: #那么说明剩余的不够一次读取的大小了，那么只要把剩下的读取出来发送过去就行了
            content = f.read(filesize)
            sk.send(content)
            break

sk.close()
# test