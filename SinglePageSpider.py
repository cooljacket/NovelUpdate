# -*- coding:utf-8 -*-
import urllib.request


class SinglePageSpider:
	def __init__(self):
		self.headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
		

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


	# def 