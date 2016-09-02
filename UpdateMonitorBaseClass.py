# -*- coding:utf-8 -*-
import os
import re

from send_email import send_email
from SinglePageSpider import SinglePageSpider
from SimpleDB import SimpleDB
from SendMailReliablly import SendMailReliablly


class UpdateMonitorBaseClass:
	def __init__(self, email_send_list, name, url, pattern, columns=['link_address']):
		self.email_send_list = email_send_list
		self.name = name
		self.url = url
		self.db = SimpleDB()
		self.db.createTable(self.name, columns)
		self.reliableEmailSender = SendMailReliablly(self.name + "_failed")
		self.pattern = re.compile(pattern, re.I)


	def getTargetContent(self):
		"""爬取贴吧的置顶帖子

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
		self.reliableEmailSender.send(to_whom_list, title, content)
		return len(updateTies) > 0



	def generate_noticification(self, new_contents):
		"""generate email to notify the users about the new contents"""
		if new_contents is not None and len(new_contents) > 0:
			mail_title = '{0}更新了{1}章'.format(self.name, len(new_contents))
			content = mail_title + "：\n"
			for (url, title) in new_contents:
				content += '{0}\n{1}\n\n'.format(title, url)
			print('sending email...\n{0}'.format(content))
			return [self.email_send_list, mail_title, content]
		else:
			return [None] * 3

