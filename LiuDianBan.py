# -*- coding:utf-8 -*-
import re

from SinglePageSpider import SinglePageSpider
from UpdateMonitorBaseClass import UpdateMonitorBaseClass


class LiuDianBan(UpdateMonitorBaseClass):
	def getTargetContent(self):
		"""爬取大主宰中文网的帖子，不过由于它的页面太过丰富，所以需要重写基类的这个获取目标内容的函数

		Returns: a list of update chapters' relative path and its title
		such as [('http://dazhuzai.net.cn/dazhuzai-1309.html', 'title 1'), ]
		"""
		page = SinglePageSpider().getPage(self.url, self.coding)
		result = re.findall(self.pattern, page)
		if result:
			for i in range(len(result)):
				result[i] = ('https://www.meipai.com' + result[i][0], result[i][1])
			return result
		else:
			return None
