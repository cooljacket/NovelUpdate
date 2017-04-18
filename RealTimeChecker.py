# -*- coding:utf-8 -*-
import sys
from UpdateMonitorBaseClass import UpdateMonitorBaseClass
from SimpleDBUsingFS import SimpleDBUsingFS
from SimpleDBUsingSqlite3 import SimpleDBUsingSqlite3


def main(args):
	email_send_list = ['happyjacket@qq.com']

	bigBang = UpdateMonitorBaseClass(
		email_send_list,
		'生活大爆炸',
		'http://www.meijuworld.com/11838.html',
		'<a href="https://pan.baidu.com/s/([^"]+)" target="_blank">([^<]+)</a>',
		tips = '集',
		url_prefix = 'https://pan.baidu.com/s/',
		dbClass = SimpleDBUsingFS
		)

	sdcs = UpdateMonitorBaseClass(
		email_send_list,
		'《学院官网》',
		'http://sdcs.sysu.edu.cn/',
		'<a href="/(node/\d+)">([^"]*)</a>',
		tips = '条通知',
		url_prefix = 'http://sdcs.sysu.edu.cn/',
		)


	wanGuShenDi = UpdateMonitorBaseClass(
		email_send_list,
		'万古神帝',
		'http://www.heiyange.com/book/4113/',
		'<a href="/(book/4113/\d+.html)">([^<]*)</a>',
		dbClass=SimpleDBUsingSqlite3,
		tips = '章小说',
		url_prefix = 'http://www.heiyange.com/',
		coding = 'gbk'
		)


	# 这个网站在国内好像被墙了，换成IP地址就好了……
	#email_send_list + ['853242365@qq.com'],
	dzz_url = '107.151.164.90'
	dazhuzai = UpdateMonitorBaseClass(
		email_send_list + ['853242365@qq.com'],
		'《大主宰》', 
		'http://{0}/html/4/4317/index.html'.format(dzz_url),
		'<a href="(\d+.html)">([^<]*)</a>',
		url_prefix = 'http://{0}/html/4/4317/'.format(dzz_url),
		coding = 'gbk'
		)


	# 漫画：给我来个小和尚
	xiaoHeShang = UpdateMonitorBaseClass(
		email_send_list,
		'《给我来个小和尚》',
		'http://www.kuaikanmanhua.com/web/topic/588/',
		'<a href="/(web/comic/\d*/)" title="([^"]*)">[^<]*</a>',
		tips = '话漫画',
		url_prefix = 'http://www.kuaikanmanhua.com/'
		)

	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
