# -*- coding:utf-8 -*-
import sys
from BDTieBa import BDTieBa
import urllib.request


def main(args):
	todo = [('大主宰', '/f?kw=%E5%A4%A7%E4%B8%BB%E5%AE%B0'), ('太古神王', '/f?kw=%E5%A4%AA%E5%8F%A4%E7%A5%9E%E7%8E%8B')]
	email_send_list = ['happyjacket@qq.com']
	for (name, main_page) in todo:
		tieba = BDTieBa(name, main_page, email_send_list)
		tieba.checkTopTie()
	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))