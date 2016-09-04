# -*- coding:utf-8 -*-
import re

from send_email import send_email
from SinglePageSpider import SinglePageSpider
from SimpleDB import SimpleDB
from SendMailReliablly import SendMailReliablly


class UpdateMonitorBaseClass:
	"""抽象监测更新并发送邮件的逻辑，成为一个类，只需要简单传入参数即可塑造一个业务！"""
	def __init__(self, email_send_list, name, url, pattern, tips='章', columns=['link_address']):
		self.email_send_list = email_send_list
		self.name = name
		self.url = url
		self.db = SimpleDB()
		self.db.createTable(self.name, columns)
		self.reliableEmailSender = SendMailReliablly(self.name + "_failed")
		self.pattern = re.compile(pattern, re.I)
		self.tips = tips


	def getTargetContent(self):
		"""获取指定页面的目标内容：
		1）指定页面由SinglePageSpider获取；
		2）目标内容由正则表达式匹配得到。

		Returns: a list of update chapters' relative path and its title
		such as [('http://dazhuzai.net.cn/dazhuzai-1309.html', 'title 1'), ]
		"""
		page = SinglePageSpider().getPage(self.url)
		result = re.findall(self.pattern, page)
		if result:
			return result
		else:
			return None


	def checkUpdate(self):
		"""监测更新的主体逻辑：
		1）获取当前的页面内容；
		2）与数据库里保存的数据比对，找出更新的数据；
		3）生成通知的邮件内容，扔给“可靠邮件发送器”发送
		"""
		print('Checking {0}...'.format(self.name))
		currentTies = self.getTargetContent()
		print('Got {0}...'.format(self.name))
		if currentTies is None:
			return False

		updateTies = []
		for (tie, title) in currentTies:
			result = self.db.find([tie])
			if not result:
				updateTies.append((tie, title))
				print('update in {0}: {1}'.format(self.name, tie))
				self.db.insert([tie])

		to_whom_list, title, content = self.generate_noticification(updateTies)
		send_result = self.reliableEmailSender.send(to_whom_list, title, content)
		if send_result:
			print('发送邮件成功')
		else:
			print('发送邮件失败，待重发')	
		return len(updateTies) > 0



	def generate_noticification(self, new_contents):
		"""generate email to notify the users about the new contents"""
		if new_contents is not None and len(new_contents) > 0:
			mail_title = '{0}更新了{1}{2}'.format(self.name, len(new_contents), self.tips)
			content = mail_title + "：\n"
			for (url, title) in new_contents:
				content += '{0}\n{1}\n\n'.format(title, url)
			print('sending email...\n{0}'.format(content))
			return [self.email_send_list, mail_title, content]
		else:
			return [None] * 3

