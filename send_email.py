# -*- coding: utf-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text


EMAIL_HOST = 'zuoyela_jacket@sina.com'  # your email address
EMAIL_PASS = 'caibudao233666'   # your email account password
# EMAIL_PASS = '*'   # your email account password
SMTP_SERVER = 'smtp.sina.com'   # your email smtp server domain name
SMTP_PORT = '25'                # smtp protocol use port 25 to send email

def send_email(to_list, sub, content):
	msg = email.mime.multipart.MIMEMultipart()
	msg['from'] = EMAIL_HOST
	msg['to'] = ";".join(to_list)
	msg['subject'] = sub
	txt = email.mime.text.MIMEText(content)
	msg.attach(txt)

	smtp = smtplib.SMTP()
	smtp.connect(SMTP_SERVER, SMTP_PORT)
	smtp.login(EMAIL_HOST, EMAIL_PASS)
	result = smtp.sendmail(EMAIL_HOST, to_list, str(msg))
	smtp.quit()
	return result

# Example tl use the function:
# send_email(['1101925754@qq.com', 'insysujacket@gmail.com'], 'Testing title', 'I am a test and I am testing the send_email function')
