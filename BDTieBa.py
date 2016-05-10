# -*- coding:utf-8 -*-
import urllib.request
import os
import re
from send_email import send_email

class BDTieBa:
	def __init__(self, name, main_page, email_send_list):
		self.fileName = '{0}.data'.format(name)
		self.tmpFileName = '{0}.tmpdata'.format(name)
		self.email_send_list = email_send_list
		self.name = name
		self.host = 'http://tieba.baidu.com'
		self.main_page = main_page
		self.headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
		self.prefix = os.getcwd() + '/'


	def getPage(self, url, args=None):
		"""get the html content of the given url with args

		Returns: a string whose content is the html
		"""
		if args:
			data = urllib.parse.urlencode(args).encode('utf-8') 
			req = urllib.request.Request(url, headers = self.headers, data=data)
		else:
			req = urllib.request.Request(url, headers = self.headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		return respData.decode('utf-8')


	def getMainPage(self):
		"""get the main page content"""
		return self.getPage(self.host + self.main_page)


	def getTopTie(self):
		"""get the top ties of this website

		Returns: a list of update chapters' relative path
		such as ['/p/12345', '/p/233666']
		"""
		pattern = '<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"[^>]*>\s*(.*?)\s*</a>\s*</div>'
		pattern = re.compile(pattern, re.S)
		page = self.getMainPage()
		result = re.findall(pattern, page)
		if result:
			return result
		else:
			return None


	def getAllChapters(self, fileName):
		"""get all lines in the file

		Returns: a list of string
		"""
		fileName = self.prefix + fileName
		try:
			with open(fileName, 'r') as f:
				data = f.readlines()
		except FileNotFoundError as e:
			data = []
		finally:
			return data


	def saveChapters(self, fileName, data):
		"""append new data to the head of the file"""
		fileName = self.prefix + fileName
		old_data = self.getAllChapters(fileName)
		with open(fileName, 'w') as f:
			for line in data + old_data:
				f.write(line)


	def checkNewChapters(self, tops):
		"""check if there is any new chapters among tops
		if yes then save them into the achieve file

		Args:
			tops: a list of paths of the top ties in the main page

		Returns: a list of new contents, each content is consist of a title and an url
		such as [(title1, url1), (title2, url2)]
		"""
		old_paths = self.getAllChapters(self.fileName)
		new_paths = []
		new_contents = []
		for (path, title) in tops:
			path += '\n'
			if old_paths.count(path) == 0:
				new_contents.append((self.host + path.strip(), title))
				new_paths.append(path)

		if new_paths:
			self.saveChapters(self.fileName, new_paths)
		return new_contents


	def checkTopTie(self):
		"""check if there is any new chapters in main page
		if yes, save them and send email to nitify the user
		if errors occur when sending email, then save the contents to the tmpFile
		"""
		print('Checking {0}...'.format(self.name))
		tops = self.getTopTie()
		new_contents = self.checkNewChapters(tops)

		have_new_chaptes = False
		if new_contents:
			have_new_chaptes = True
			send_result = self.send_noticification(new_contents)
			for (host, error) in send_result:
				print('Error happend when send email to {0}, {1}'.format(host, error))
				self.saveChapters(self.tmpFileName, new_contents)

		send_failed_contents = self.check_send_failed_contents()

		# if no new chapters or again fail to send failed contents
		if not (have_new_chaptes or send_failed_contents):
			print('No update for {0}'.format(self.name))


	def send_noticification(self, new_contents):
		"""send email to notify the users about the new contents"""
		mail_title = '{0}更新了{1}章'.format(self.name, len(new_contents))
		content = mail_title + "：\n"
		for (url, title) in new_contents:
			content += '{0}\n{1}\n\n'.format(title, url)
		print('sending email...\n{0}'.format(content))
		return send_email(self.email_send_list, mail_title, content)


	def check_send_failed_contents(self):
		"""send the failed contents again"""
		try:
			with open(self.tmpFileName, 'r') as f:
				send_failed_contents = f.readlines();
		except FileNotFoundError as e:
			send_failed_contents = []
		finally:
			if send_failed_contents:
				send_result = self.send_noticification(send_failed_contents)
				# if send success, send_result is {}, so we should clear the file now
				if not send_result:
					with open(self.tmpFileName, 'w') as f:
						pass
			return send_failed_contents == {}