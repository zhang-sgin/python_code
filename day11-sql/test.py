import pymysql
import paramiko


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
    def connect_host(self):
        # ssh_host=input('请输入远程地址：')
        # ssh_port=input('请输入远程端口：')
        # ssh_user=input('请输入远程用户：')
        # ssh_paas=input('请输入远程密码：')
        ssh_host = '101.200.37.252'
        ssh_port = 22
        ssh_user = 'root'
        ssh_paas = '31)yz+$zutZ+e6EJ'
        while True:
            cmd_input = input('>>>:')
            ssh = parmikoclient(ssh_host,ssh_port,ssh_user,ssh_paas)
            ssh.run_ssh(cmd_input)
            if cmd_input == 'quit':
                ssh.close()

    def close(self):
        self.cur.close()
        self.conn.close()
        exit()
A=connect_mysql_product()
A.connect_host()