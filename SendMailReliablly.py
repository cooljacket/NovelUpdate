# -*- coding:utf-8 -*-
from send_email import send_email
from SimpleDB import SimpleDB


class SendMailReliablly:
	def __init__(self, tableName):
		self.db = SimpleDB()
		self.db.createTable(tableName, ['to_whom_list', 'title', 'content'])
		self.newlineReplacer = '$^&'


	def send(self, to_whom_list, title, content):
		emails_to_send = self.db.get_all()
		if to_whom_list:
			emails_to_send.append(self.row2str([to_whom_list, title, content]))
		now_fail_emails = []

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