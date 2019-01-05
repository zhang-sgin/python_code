'''
表关系：
    管理员表：
        ID  用户名   密码    邮箱
    业务线：
        ID  名称
    主机表：
        ID  主机名  密码  业务线ID

需求：
    用户登录（密码基于md5且加盐）
    业务线管理：
        添加业务线
        删除业务线
        修改业务线
        查看业务线
    主机管理（含外键）：
        添加主机
        删除主机
        修改主机
        查看主机
    基于paramiko模块向指定服务器执行命令
'''

import paramiko
import pymysql

def connect_mysql(user,pwd):
    conn = pymysql.connect(host='127.0.0.1', user='root', password="123456", database='day11-homework', port=3306,charset='utf8')  # 创建连接
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select user_name,user_pass from admin_user  WHERE user_name='%s' AND user_pass='%s'" %(user,pwd)
    cur.execute(sql)
    rows = cur.fetchall()
    # print(rows, type(rows))
    conn.commit()
    cur.close()
    conn.close()
    return rows

class parmikoclient:
    def __init__(self,host,port,user,pwd):
        # self.host = '101.200.37.252'
        # self.port = 22
        # self.user = 'root'
        # self.pwd = '31)yz+$zutZ+e6EJ'
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.timeout = '600'
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host,port=self.port,username=self.user,password=self.pwd,timeout=float(self.timeout))

    def run_ssh(self,cmd_command):
        stdin,stdout,stderr = self.client.exec_command(cmd_command)     # 执行命令，输出结果在stdout中，如果是错误则放在stderr中
        result = stdout.read()      # read方法读取输出结果
        if len(result) == 0:    # 判断如果输出结果长度等于0表示为错误输出
            print(stderr.read().decode())
        else:
            print(str(result, 'utf-8'))

    def close(self):
        self.client.close()

class connect_mysql_product:
    gg = {"添加业务线": 'add_course', '删除业务线': 'del_course', "修改业务线": 'change_course', "查看业务线": 'list_course',
          "添加主机": 'add_host', '删除主机': 'del_host', "修改主机": 'change_host', "查看主机": 'list_host',"远程连接主机": 'connect_host',"退出":'close'}

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password="123456", database='day11-homework', port=3306,charset='utf8')  # 创建连接
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def add_course(self):
        a_course = input('请输入新增业务线：')
        sql = "insert into product(product_name) values('%s')" %(a_course)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('新增成功')
        else:
            print('新增失败')

    def add_host(self):
        a_host_ip = input('请输入新增主机地址：')
        a_host_paas = input('请输入新增主机密码：')
        print(self.list_course())
        a_host_course = input('请输入新增主机所属产品ID：')
        sql = "INSERT INTO host(host_name, host_pass, product_id) VALUES ('%s', '%s', %s)" %(a_host_ip,a_host_paas,a_host_course)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('新增成功')
        else:
            print('新增失败')

    def del_course(self):
        print(self.list_course())
        d_course = int(input('请输入删除业务线ID：'))
        sql = "DELETE FROM product WHERE id=%s" %(d_course)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('删除成功')
        else:
            print('删除失败')

    def del_host(self):
        print(self.list_host())
        d_host = int(input('请输入删除主机ID：'))
        sql = "DELETE FROM host WHERE id=%s" %(d_host)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('删除成功')
        else:
            print('删除失败')

    def change_course(self):
        print(self.list_course())
        new_id = int(input('请输入需要修改的业务线ID：'))
        new_name = input('请输入需要修改后的名称：')
        sql = "UPDATE product SET product_name = '%s' WHERE id = %s" %(new_name,new_id)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('修改成功')
        else:
            print('修改失败')

    def change_host(self):
        print(self.list_host())
        c_host_ID = int(input('请输入需要修改的主机ID：'))
        c_host_ip = input('请输入修改主机地址：')
        c_host_paas = input('请输入修改主机密码：')
        print(self.list_course())
        c_host_course = input('请输入修改主机所属产品ID：')
        sql = "UPDATE host SET host_name='%s',host_pass='%s',product_id=%s  WHERE id = %s" %(c_host_ip,c_host_paas,c_host_course,c_host_ID)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        if sql:
            print('修改成功')
        else:
            print('修改失败')


    def list_course(self):
        sql = "SELECT id,product_name FROM product"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        # print(result)
        return result

    def list_host(self):
        sql = "SELECT id,host_name,host_pass,product_id FROM host"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def connect_host(self):
        # ssh_host=input('请输入远程地址：')
        # ssh_port=input('请输入远程端口：')
        # ssh_user=input('请输入远程用户：')
        # ssh_paas=input('请输入远程密码：')
        ssh_host = '1.1.1.1'
        ssh_port = 22
        ssh_user = 'root'
        ssh_paas = '123'
        while True:
            cmd_input = input('>>>:')
            ssh = parmikoclient(ssh_host,ssh_port,ssh_user,ssh_paas)
            ssh.run_ssh(cmd_input)
            if cmd_input.upper() == 'Q':
                ssh.close()
                break

    def close(self):
        self.cur.close()
        self.conn.close()
        exit()






def login(username,password):
    print('欢迎来到数据远程操作系统！')
    count = 1
    while count < 4:
        mysql_user = connect_mysql(username,password)
        for i in mysql_user:
            name = i['user_name']
            pwd = i['user_pass']
            if username == name and password == pwd:
                print('管理员%s登录成功！' % (username))
                mysql = connect_mysql_product()
                while 1:
                    tmp = {}
                    for index, i in enumerate(mysql.gg, 1):
                        print(index, i)
                        tmp[str(index)] = mysql.gg[i]
                    C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
                    if C.upper() == 'Q': break
                    func = getattr(mysql, tmp[C])
                    func()

            else:
                print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                count += 1


if __name__ == '__main__':
    print('请先登录')
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    login(username,password)


