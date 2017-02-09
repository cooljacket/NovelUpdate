# -*- coding:utf-8 -*-
import sys
from UpdateMonitorBaseClass import UpdateMonitorBaseClass
from SimpleDBUsingFS import SimpleDBUsingFS
from SimpleDBUsingSqlite3 import SimpleDBUsingSqlite3


def main(args):
	email_send_list = ['happyjacket@qq.com']

	sdcs = UpdateMonitorBaseClass(
		email_send_list,
		'《学院官网》',
		'http://sdcs.sysu.edu.cn/',
		'<a href="(/node/\d+)">([^"]*)</a>',
		tips = '条通知',
		url_prefix = 'http://sdcs.sysu.edu.cn',
		)


	wanGuShenDi = UpdateMonitorBaseClass(
		email_send_list,
		'万古神帝',
		'http://www.heiyange.com/book/4113/',
		'<a href="(/book/4113/\d+.html)">([^<]*)</a>',
		dbClass=SimpleDBUsingSqlite3,
		tips = '章小说',
		url_prefix = 'http://www.heiyange.com',
		coding = 'gbk'
		)


	# 这个网站在国内好像被墙了，换成IP地址就好了……
	dazhuzai = UpdateMonitorBaseClass(
		email_send_list + ['853242365@qq.com'],
		'《大主宰》', 
		'http://198.211.60.226/bookinfo/4/4317.html',
		'<a href="http://www.piaotian.net(/html/4/4317/\d*.html)"[^>]*>([^<]*)</a>',
		url_prefix = 'http://198.211.60.226',
		coding = 'gbk'
		)


	# 漫画：给我来个小和尚
	xiaoHeShang = UpdateMonitorBaseClass(
		email_send_list,
		'《给我来个小和尚》',
		'http://www.kuaikanmanhua.com/web/topic/588/',
		'<a href="(/web/comic/\d*/)" title="([^"]*)">[^<]*</a>',
		tips = '话漫画',
		url_prefix = 'http://www.kuaikanmanhua.com'
		)

	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
