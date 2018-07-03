# -*- coding: utf-8 -*-
import email.mime.multipart
import email.mime.text
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
import smtplib


from_addr = '1101925754@qq.com'
password = 'dicttmcpysgtidfc'
smtp_server = 'smtp.qq.com'
port = 25


# 如果返回值为空{}，则表示全部发送成功，否则……
def send_email(to_whom_list, title, content):
	msg = email.mime.multipart.MIMEMultipart()
	msg['from'] = from_addr
	msg['to'] = ";".join(to_whom_list)
	msg['subject'] = title
	txt = email.mime.text.MIMEText(content)
	msg.attach(txt)
	print('-------------------' + str(to_whom_list))
	result = {}
	have_exception = False

	try:
		server = smtplib.SMTP(smtp_server, port) # SMTP协议默认端口是25
		server.set_debuglevel(1)
		server.starttls()
		server.login(from_addr, password)
		result = server.sendmail(from_addr, to_whom_list, msg.as_string())
		server.quit()
		print(result)
	except Exception as e:
		print('exception when send_email...')
		print(e)
	return result


# send_email(['happyjacket.com'], '测试拉', 'hahahhaha')


