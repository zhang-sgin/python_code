from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest
from aliyunsdkram.request.v20150501.ListPoliciesForUserRequest import ListPoliciesForUserRequest
from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
from aliyunsdkram.request.v20150501.CreateUserRequest import CreateUserRequest
from aliyunsdkram.request.v20150501.CreateLoginProfileRequest import CreateLoginProfileRequest
from aliyunsdkram.request.v20150501.AddUserToGroupRequest import AddUserToGroupRequest
from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
from aliyunsdkram.request.v20150501.GetUserRequest import GetUserRequest
from aliyunsdkram.request.v20150501.ListGroupsForUserRequest import ListGroupsForUserRequest
from aliyunsdkram.request.v20150501.DeleteLoginProfileRequest import DeleteLoginProfileRequest
import json, pymysql

# 创建用户
create_user_request = CreateUserRequest()
create_user_request.set_accept_format('json')
# 创建用户密码开启控制台登陆
create_user_pwd_request = CreateLoginProfileRequest()
create_user_pwd_request.set_accept_format('json')
# 用户添加到组
user_to_group_request = AddUserToGroupRequest()
user_to_group_request.set_accept_format('json')
# 关闭用户控制台登陆
close_login_request = DeleteLoginProfileRequest()
close_login_request.set_accept_format('json')


# 获取用户和权限
user_temp = []

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
                       database='aliyun-ram-control', port=3306, charset='utf8')
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

client = AcsClient('', '', 'cn-beijing')

user ="SELECT ram_user_name FROM ram_control_aliyun_ram_user"
r = cur.execute(user)
rows=cur.fetchall()


conn.commit()
cur.close()
conn.close()