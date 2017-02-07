# -*- coding:utf-8 -*-
from send_email import send_email
from SimpleDBUsingFS import SimpleDBUsingFS


class SendMailReliablly:
	"""可靠邮件发送器，发送失败会自动保存进数据库里，下次激活时自动重发"""
	def __init__(self, tableName):
		self.db = SimpleDBUsingFS()
		# 为发送失败的邮件建立数据库
		self.db.createTable(tableName + "_failed", ['to_whom_list', 'title', 'content'])
		self.newlineReplacer = '$^&'


	def send(self, to_whom_list, title, content):
		"""发送邮件的主体逻辑：
		1）待发送邮件=以前发送失败的+现在要发送的
		2）逐封邮件发送（可能需要调整一个发送间隔，因为太快连续发送，会导致邮件服务器拒绝服务；
		3）收集这一次发送失败的邮件；
		4）清空原来的“发送失败”数据库，把新的数据保存进去。
		"""
		emails_to_send = self.db.get_all()	# 以前发送失败的邮件

		# 现在要发送的邮件，由于标题和内容可能存在换行符（\n）而FSDB用的是换行符来分隔，所以需要先转码一番！
		if to_whom_list:
			emails_to_send.append(self.row2str([to_whom_list, title, content]))

		now_fail_emails = []	# 当前发送失败的邮件列表

		for email in emails_to_send:
			email = self.str2row(email)
			try:
				result = send_email(email[0], email[1], email[2])
			except Exception as e:
				result = {str(e)}
				print('smtplib error happend.......................')
			
			print('send_result....', result)
			if len(result) > 0:
				now_fail_emails.append(email)

		self.db.delete_all()
		for email in now_fail_emails:
			email = self.row2str(email)
			self.db.insert(email)
		return len(now_fail_emails) == 0


	def row2str(self, row):
		"""把发送列表（第0维）转为字符串，把换行符替换为自己的分隔符"""
		row[0] = ','.join(row[0])
		row[1] = row[1].replace('\n', self.newlineReplacer)
		row[2] = row[2].replace('\n', self.newlineReplacer)
		return row


	def str2row(self, row_str):
		"""把发送列表的字符串形式分割回来，把自己的分隔符恢复为原来的换行符"""
		row_str[0] = row_str[0].split(',')
		row_str[1] = row_str[1].replace(self.newlineReplacer, '\n')
		row_str[2] = row_str[2].replace(self.newlineReplacer, '\n')
		return row_str