# -*- coding:utf-8 -*-
import sys
from UpdateMonitorBaseClass import UpdateMonitorBaseClass


def main(args):
	email_send_list = ['happyjacket@qq.com']

	wanGuShenDi = UpdateMonitorBaseClass(
		email_send_list,
		'万古神帝',
		'http://www.heiyange.com/book/4113/',
		'<a href="(/book/4113/\d+.html)">([^<]*)</a>',
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

	ldb = UpdateMonitorBaseClass(
		email_send_list,
		'《陈翔六点半》',
		'https://www.meipai.com/user/32821588?p=1',
		'<a class="[^"]*" href="(/media/\d*)" itemprop="description">[^<]*<[^>]*>([^<]*)',
		tips = '个视频',
		url_prefix = 'https://www.meipai.com'
		)

	sdcs = UpdateMonitorBaseClass(
		email_send_list,
		'《学院官网》',
		'http://sdcs.sysu.edu.cn/',
		'<a href="(http://sdcs.sysu.edu.cn/\?p=\d*)" title="([^"]*)"[^<]*</a>',
		tips = '条通知'
		)

	# 太古神王-百度贴吧
	# 已经不看了
	# taiGuShenWang = UpdateMonitorBaseClass(email_send_list,
	# 	'《太古神王》',
	# 	'http://tieba.baidu.com/f?kw=%CC%AB%B9%C5%C9%F1%CD%F5',
	# 	'<div class="threadlist_title[^>]*>\s*<i[^>]*></i>\s*<i[^>]*></i>\s*<a href="([^"]*)"[^>]*>\s*(.*?)\s*</a>\s*</div>'
	# 	)
	
	# 这个网站在国内好像被墙了。
	dazhuzai = UpdateMonitorBaseClass(
		email_send_list, 
		'《大主宰》', 
		'http://198.211.60.226/bookinfo/4/4317.html',
		'<a href="(http://www.piaotian.net/html/4/4317/\d*.html)"[^>]*>([^<]*)</a>',
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
