import datetime
import time
import smtpd

with open('E:\python24\python_code\haha',mode='a+',encoding='utf-8') as f_test:
    f_test.write('\n'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#
#
# # 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()