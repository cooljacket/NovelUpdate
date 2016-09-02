# -*- coding:utf-8 -*-
import re

from SinglePageSpider import SinglePageSpider
from UpdateMonitorBaseClass import UpdateMonitorBaseClass


class DaZhuZai(UpdateMonitorBaseClass):
	def getTargetContent(self):
		"""爬取大主宰中文网的帖子，不过由于它的页面太过丰富，所以需要重写基类的这个获取目标内容的函数

		Returns: a list of update chapters' relative path and its title
		such as [('http://dazhuzai.net.cn/dazhuzai-1309.html', 'title 1'), ]
		"""
		page = SinglePageSpider().getPage(self.url)
		result = re.findall(self.pattern, page)
		if result:
			newestResult = []
			for update in result:
				if int(update[0]) > 1300:
					url = 'http://dazhuzai.net.cn/dazhuzai-{0}.html'.format(update[0])
					newestResult.append([url, update[1]])
			return newestResult
		else:
			return None
