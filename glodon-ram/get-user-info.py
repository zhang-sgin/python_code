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

# 获取用户和权限
user_temp = []

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
                       database='aliyun-ram-control', port=3306, charset='utf8')
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

client = AcsClient('', '', 'cn-beijing')

# 获取用户名，显示名
get_uset_request = ListUsersRequest()
get_uset_request.set_accept_format('json')
# 获取用户详细信息
get_user_allinfo__request = GetUserRequest()
get_user_allinfo__request.set_accept_format('json')
# 获取用户权限信息
get_uset_policy_request = ListPoliciesForUserRequest()
get_uset_policy_request.set_accept_format('json')

# 获取用户ak
get_uset_ak_request = ListAccessKeysRequest()
get_uset_ak_request.set_accept_format('json')



# 获取用户key
get_user_key_request = ListAccessKeysRequest()
get_user_key_request.set_accept_format('json')
# 列出用户所在组
list_user_group_request = ListGroupsForUserRequest()
list_user_group_request.set_accept_format('json')




# 查找数据库中用户信息
user = "SELECT ram_user_name FROM ram_control_aliyun_ram_user"
r = cur.execute(user)
rows = cur.fetchall()

# 数据库插入用户名信息
get_user = client.do_action_with_exception(get_uset_request)
get_user = (json.loads(get_user))
name = get_user['Users']['User']

for i in rows:
    user_temp.append(i['ram_user_name'])

for online_user in name:
    ram_user_name = online_user['UserName']
    # ram_display_name = online_user['DisplayName']
    if ram_user_name not in user_temp:
        sql = "INSERT INTO ram_control_aliyun_ram_user(`ram_user_name`, `ram_display_name`) VALUES ('%s','%s')" % (
            ram_user_name)
        r = cur.execute(sql)


# 根据用户名插入用户权限信息
for i in rows:
    name = i['ram_user_name']
    get_uset_policy_request.set_UserName(name)
    get_uset_policy = client.do_action_with_exception(get_uset_policy_request)
    get_uset_policy = (json.loads(get_uset_policy))
    # print(get_uset_policy['Policies']['Policy'][0]['Description'])

    get_user_allinfo__request.set_UserName(name)
    get_userinfo = client.do_action_with_exception(get_user_allinfo__request)
    get_userinfo = (json.loads(get_userinfo))



    try:
        policy = get_uset_policy['Policies']['Policy'][0]['Description']
        DisplayName = get_userinfo['User']['DisplayName']
        Email = get_userinfo['User']['Email']
        Phone = get_userinfo['User']['MobilePhone']
        Comments = get_userinfo['User']['Comments']

        sql = "UPDATE ram_control_aliyun_ram_user set ram_display_name='%s',ram_auth='%s',ram_phone='%s',ram_mail='%s', ram_comment='%s'where ram_user_name='%s' " % (DisplayName, policy, Phone, Email, Comments, name)
        r = cur.execute(sql)
    except IndexError:
        DisplayName = get_userinfo['User']['DisplayName']
        sql = "UPDATE ram_control_aliyun_ram_user set ram_display_name='%s',ram_auth='%s',ram_phone='%s',ram_mail='%s', ram_comment='%s'where ram_user_name='%s' " % (DisplayName, ' ', ' ', ' ', ' ', name)
        r = cur.execute(sql)

conn.commit()
cur.close()
conn.close()
