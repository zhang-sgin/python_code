import time
import os, sys
import os.path
import hashlib
import random, string
import logging
import logging.config
from cryptography.fernet import Fernet
import re

# def md5(username,pwd):
#     salt='haha'
#     md5 = hashlib.md5('zhangz-l'.encode('utf-8'))
#     md5.update(username.encode('utf-8'))
#     return md5.hexdigest()
# zz = md5('zz',123)
# print(zz)



# with open('filesize',encoding='utf-8',mode='a+')as f_size:
#     f_size.write('a1234')
# nums = []
# with open('filesize',encoding='utf-8')as f_size_r:
#     # print(f_size_r.read().split('a'))
#     for s in re.findall(r'\d+', f_size_r.read()):
#         nums.append(float(s))
#     print(sum(nums))


md5 = hashlib.md5('zhangz-l'.encode('utf-8'))
md5.update("123".encode("utf-8"))
secret=md5.hexdigest()
print(secret)