#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkram.request.v20150501.CreateUserRequest import CreateUserRequest
from aliyunsdkram.request.v20150501.CreateLoginProfileRequest import CreateLoginProfileRequest
from aliyunsdkram.request.v20150501.AddUserToGroupRequest import AddUserToGroupRequest
from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
from aliyunsdkram.request.v20150501.GetUserRequest import GetUserRequest
from aliyunsdkram.request.v20150501.ListGroupsForUserRequest import ListGroupsForUserRequest
from aliyunsdkram.request.v20150501.DeleteLoginProfileRequest import DeleteLoginProfileRequest



client = AcsClient('', '', 'cn-beijing')

# 创建用户
request = CreateUserRequest()
request.set_accept_format('json')

request.set_Email("782108321@qq.com")
request.set_MobilePhone("15651592276")
request.set_DisplayName("张政测试1")
request.set_UserName("zhangz-test1")
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))


# 创建密码开启控制台登陆
request = CreateLoginProfileRequest()
request.set_accept_format('json')

request.set_PasswordResetRequired(False)
request.set_Password("123456")
request.set_UserName("zhangz-test1")

response = client.do_action_with_exception(request)

response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))


# 添加到组
request = AddUserToGroupRequest()
request.set_accept_format('json')

request.set_GroupName("group-yw")
request.set_UserName("zhangz-test1")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))


# 获取用户key
request = ListAccessKeysRequest()
request.set_accept_format('json')

request.set_UserName("zhangz-l")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))


# 获取用户详细信息
request = GetUserRequest()
request.set_accept_format('json')

request.set_UserName("zhangz-test1")
response = client.do_action_with_exception(request)



print(str(response, encoding='utf-8'))



# 列出用户所在组
request = ListGroupsForUserRequest()
request.set_accept_format('json')

request.set_UserName("zhangz-test1")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))



# 关闭用户控制台登陆
request = DeleteLoginProfileRequest()
request.set_accept_format('json')

request.set_UserName("zhangz-test1")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
