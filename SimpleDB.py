# -*- coding:utf-8 -*-
import abc


class SimpleDB:
	"""简易数据库类，支持建表、插入、查询、获取整张表、删除整张表的操作"""

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __init__(self):
		pass	

	@abc.abstractmethod
	def createTable(self, tableName, columns):
		pass


	@abc.abstractmethod
	def insert(self, row):
		"""插入一行
		row: 一个列表，长度要和建表时指定的一样；
		row_to_str：可选，可以自己指定把插入的行转成字符串的函数
		"""
		pass


	@abc.abstractmethod
	def find(self, values):
		"""在数据库中查找
		values：只支持完全匹配，比如['name', 'age', '']表示查找名字刚好为'name'年轻刚好为'age'性别不限的人
		注意空字符串表示'*'，即任意值都可以

		返回值：True表示查找到了，False表示找不到
		"""
		pass


	@abc.abstractmethod
	def delete_all(self):
		"""删除所有的行"""
		pass


	@abc.abstractmethod
	def get_all(self):
		"""获取所有的行"""
		pass
