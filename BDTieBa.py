# -*- coding:utf-8 -*-
import urllib.request
import re
from send_email import send_email

class BDTieBa:
	def __init__(self, name, main_page):
		self.fileName = '{0}.data'.format(name)
		self.tmpFileName = '{0}.tmpdata'.format(name)
		self.name = name
		self.host = 'http://tieba.baidu.com'
		self.main_page = main_page
		self.headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}


	def getPage(self, url, args=None):
		if args:
			data = urllib.parse.urlencode(args).encode('utf-8') 
			req = urllib.request.Request(url, headers = self.headers, data=data)
		else:
			req = urllib.request.Request(url, headers = self.headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		return respData.decode('utf-8')


	def getMainPage(self):
		return self.getPage(self.host + self.main_page)


	def getTopTie(self):
		# pattern = '<div class="threadlist_title[^>]*>[^<]*<i class="icon-top"[^>]*></i><i[^>]*></i>\s*<a href="([^"]*)".*</div>'
		# pattern = '<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"\s*title="([^"]*).*</div>'
		pattern = '<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"[^>]*>\s*(.*?)\s*</a>\s*</div>'
		pattern = re.compile(pattern, re.S)
		page = self.getMainPage()
		result = re.findall(pattern, page)
		if result:
			return result
		else:
			return None


	def getAllChapters(self, fileName):
		try:
			with open(fileName, 'r') as f:
				data = f.readlines()
		except FileNotFoundError as e:
			data = []
		finally:
			return data


	def saveChapters(self, fileName, data):
		with open(fileName, 'w') as f:
			for line in data:
				f.write(line)


	def checkNewChapters(self, tops):
		old_paths = self.getAllChapters(self.fileName)
		new_paths = []
		new_contents = []
		for (path, title) in tops:
			path += '\n'
			if old_paths.count(path) == 0:
				new_contents.append((self.host + path.strip(), title))
				new_paths.append(path)

		if new_paths:
			self.saveChapters(self.fileName, new_paths + old_paths)
		return new_contents


	def checkTopTie(self):
		print('Checking {0}...'.format(self.name))
		tops = self.getTopTie()
		new_contents = self.checkNewChapters(tops)
		if new_contents:
			send_result = self.send_noticification(new_contents)
			for (host, error) in send_result:
				print('Error happend when send email to {0}, {1}'.format(host, error))
				self.saveChapters(self.tmpFileName, new_contents)
		else:
			send_failed_contents = self.check_send_failed_contents()
			if not send_failed_contents:
				print('No update for {0}'.format(self.name))


	def send_noticification(self, new_contents):
		mail_title = '{0}更新了{1}章'.format(self.name, len(new_contents))
		content = mail_title + "：\n"
		for (url, title) in new_contents:
			content += '{0}\n{1}\n\n'.format(title, url)
		print('sending email...\n{0}'.format(content))
		return send_email(['1101925754@qq.com'], mail_title, content)


	def check_send_failed_contents(self):
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
			return send_failed_contents