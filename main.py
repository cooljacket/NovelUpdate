# -*- coding:utf-8 -*-
import sys
from UpdateMonitorBaseClass import UpdateMonitorBaseClass
from SimpleDBUsingFS import SimpleDBUsingFS
from SimpleDBUsingSqlite3 import SimpleDBUsingSqlite3


def main(args):
	email_send_list = ['happyjacket@qq.com']

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

	googleBlog = UpdateMonitorBaseClass(
		email_send_list,
		'Google blog',
		'http://developers.googleblog.cn/',
		"<a href='(http://developers.googleblog.cn/[^']*)' itemprop='url' title='([^']*)'>[^<]*</a>",
		tips = '篇博客'
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


	# 不需要了，有公众号，更好的推送方式
	# ldb = UpdateMonitorBaseClass(
	# 	email_send_list,
	# 	'《陈翔六点半》',
	# 	'https://www.meipai.com/user/32821588?p=1',
	# 	'<a class="[^"]*" href="(/media/\d*)" itemprop="description">[^<]*<[^>]*>([^<]*)',
	# 	tips = '个视频',
	# 	url_prefix = 'https://www.meipai.com'
	# 	)

	# 使用了新网站，待更新正则表达式
	# sdcs = UpdateMonitorBaseClass(
	# 	email_send_list,
	# 	'《学院官网》',
	# 	'http://sdcs.sysu.edu.cn/',
	# 	'<a href="(http://sdcs.sysu.edu.cn/\?p=\d*)" title="([^"]*)"[^<]*</a>',
	# 	tips = '条通知'
	# 	)

	
	# 这个网站在国内好像被墙了，换成IP地址就好了……
	dazhuzai = UpdateMonitorBaseClass(
		email_send_list + ['853242365@qq.com'],
		'《大主宰》', 
		'http://198.211.60.226/bookinfo/4/4317.html',
		'<a href="http://www.piaotian.net(/html/4/4317/\d*.html)"[^>]*>([^<]*)</a>',
		url_prefix = 'http://198.211.60.226',
		coding = 'gbk'
		)

	# 王垠的博客
	wyblog = UpdateMonitorBaseClass(
		email_send_list,
		'《王垠的博客》',
		'http://www.yinwang.org',
		'<a href="(http://yinwang.org/blog-cn/[^"]*)">([^<]*)</a>',
		tips = '篇博客'
		)

	# 贺希荣老师的博客
	xrBlog = UpdateMonitorBaseClass(
		email_send_list,
		'《贺希荣老师的博客》',
		'http://hxrong7.blog.163.com/',
		'<a href="(http://hxrong7.blog.163.com/blog/static/\d*/)"[^>]*>([^<]*)</a>',
		tips = '篇博客',
		coding = 'gbk'
		)


	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
