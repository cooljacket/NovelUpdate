# -*- coding:utf-8 -*-
import sys
from DaZhuZai import DaZhuZai
from UpdateMonitorBaseClass import UpdateMonitorBaseClass


def main(args):
	email_send_list = ['happyjacket@qq.com']

	# 太古神王-百度贴吧
	taiGuShenWang = UpdateMonitorBaseClass(email_send_list,
		'太古神王',
		'http://tieba.baidu.com/f?kw=%CC%AB%B9%C5%C9%F1%CD%F5',
		'<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"[^>]*>\s*(.*?)\s*</a>\s*</div>'
		)
	taiGuShenWang.checkUpdate()


	# 王垠的博客
	wyblog = UpdateMonitorBaseClass(email_send_list,
		'王垠的博客',
		'http://www.yinwang.org',
		'<a href="(http://yinwang.org/blog-cn/[^"]*)">([^<]*)</a>'
		)
	wyblog.checkUpdate()


	# 大主宰网
	daz = DaZhuZai(email_send_list, 
		'大主宰', 
		'http://dazhuzai.net.cn/category/dazhuzailianzai',
		'<a href="http://dazhuzai.net.cn/dazhuzai-(\d{4}).html"[^>]*>([^<]*)</a>'
		)
	daz.checkUpdate()
	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))