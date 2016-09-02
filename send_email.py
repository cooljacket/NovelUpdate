# -*- coding: utf-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text


EMAIL_HOST = 'zuoyela_jacket@sina.com'  # your email address
EMAIL_PASS = 'caibudao233666'   # your email account password
# EMAIL_PASS = '*'   # your email account password
SMTP_SERVER = 'smtp.sina.com'   # your email smtp server domain name
SMTP_PORT = '25'                # smtp protocol use port 25 to send email


# 如果返回值为空{}，则表示全部发送成功，否则……
def send_email(to_whom_list, title, content):
	msg = email.mime.multipart.MIMEMultipart()
	msg['from'] = EMAIL_HOST
	msg['to'] = ";".join(to_whom_list)
	msg['subject'] = title
	txt = email.mime.text.MIMEText(content)
	msg.attach(txt)

	have_exception = False
	try:
		smtp = smtplib.SMTP()
		smtp.connect(SMTP_SERVER, SMTP_PORT)
		smtp.login(EMAIL_HOST, EMAIL_PASS)
		result = smtp.sendmail(EMAIL_HOST, to_whom_list, str(msg))
	except Exception as e:
		print('exception when send_email...')
		have_exception = True
	finally:
		smtp.quit()
		if have_exception:
			print('finally raise e: {0}'.format(str(e)))
			raise e
		else:
			print('finally no exception raise')
	return result

# Example tl use the function:
# send_email(['happyjacket@qq.com', 'insysujacket@gmail.com'], 'Testing title', 'I am a test and I am testing the send_email function')
