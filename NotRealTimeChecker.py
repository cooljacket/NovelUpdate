# -*- coding:utf-8 -*-
import sys
from UpdateMonitorBaseClass import UpdateMonitorBaseClass
from SimpleDBUsingFS import SimpleDBUsingFS
from SimpleDBUsingSqlite3 import SimpleDBUsingSqlite3


def main(args):
	email_send_list = ['happyjacket@qq.com']

	googleBlog = UpdateMonitorBaseClass(
		email_send_list,
		'Google blog',
		'http://developers.googleblog.cn/',
		"<a href='(http://developers.googleblog.cn/[^']*)' itemprop='url' title='([^']*)'>[^<]*</a>",
		tips = '篇博客'
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

	libfeihu_blog = UpdateMonitorBaseClass(
		email_send_list,
		'libfeihu blog',
		'http://feihu.me/blog/',
		'<a href="(/blog/\d+/[^/]*/)">([^<]*)</a>',
		tips = '篇博客',
		url_prefix = 'http://feihu.me'
		)


	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
