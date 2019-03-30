from src.engine.base import SSHandSaltHandler
from conf import settings


class SSHHandler(SSHandSaltHandler):
    """

    ssh模式下资产采集

    """
    
    def cmd(self, command, hostname=None):
        """
        调用paramiko远程连接主机并执行命令，依赖rsa
        :param hostname:主机名
        :param command: 要执行的命令
        :return:
        """
        import paramiko
        
        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        ssh.close()
        return result
