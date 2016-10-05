# -*- coding:utf-8 -*-
import sys
from DaZhuZai import DaZhuZai
from UpdateMonitorBaseClass import UpdateMonitorBaseClass
from LiuDianBan import LiuDianBan


def main(args):
	email_send_list = ['happyjacket@qq.com']

	ldb = LiuDianBan(email_send_list,
		'陈翔六点半',
		'https://www.meipai.com/user/32821588?p=1',
		'<a class="[^"]*" href="(/media/\d*)" itemprop="description">[^<]*<[^>]*>([^<]*)',
		tips='个视频'
		)
	ldb.checkUpdate()

	sdcs = UpdateMonitorBaseClass(email_send_list,
		'学院官网',
		'http://sdcs.sysu.edu.cn/',
		'<a href="(http://sdcs.sysu.edu.cn/\?p=\d*)" title="([^"]*)"[^<]*</a>',
		tips='条通知'
		)
	sdcs.checkUpdate()

	# 太古神王-百度贴吧
	# 已经不看了
	# taiGuShenWang = UpdateMonitorBaseClass(email_send_list,
	# 	'太古神王',
	# 	'http://tieba.baidu.com/f?kw=%CC%AB%B9%C5%C9%F1%CD%F5',
	# 	'<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"[^>]*>\s*(.*?)\s*</a>\s*</div>'
	# 	)
	# taiGuShenWang.checkUpdate()

	
	# 这个网站在国内好像被墙了。
	dazhuzai = UpdateMonitorBaseClass(email_send_list, 
		'大主宰', 
		'http://www.piaotian.net/bookinfo/4/4317.html',
		'<a href="(http://www.piaotian.net/html/4/4317/\d*.html)"[^>]*>([^<]*)</a>',
		coding='gbk'
		)
	dazhuzai.checkUpdate()


	# 王垠的博客
	wyblog = UpdateMonitorBaseClass(email_send_list,
		'王垠的博客',
		'http://www.yinwang.org',
		'<a href="(http://yinwang.org/blog-cn/[^"]*)">([^<]*)</a>',
		tips='篇博客'
		)
	wyblog.checkUpdate()


	# 大主宰网
#	daz = DaZhuZai(email_send_list, 
#		'大主宰', 
#		'http://dazhuzai.net.cn/category/dazhuzailianzai',
#		'<a href="http://dazhuzai.net.cn/dazhuzai-(\d{4}).html"[^>]*>([^<]*)</a>'
#		)
#	daz.checkUpdate()
	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
