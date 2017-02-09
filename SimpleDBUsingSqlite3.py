# -*- coding:utf-8 -*-
# 使用文件系统自制的简单文件系统
import os
import sqlite3

# DB的虚基类
from SimpleDB import SimpleDB



class SimpleDBUsingSqlite3(SimpleDB):
	"""使用sqlite3实现简易数据库类，支持建表、插入、查询、获取整张表、删除整张表的操作"""	
	def __init__(self, dbName, tableName, columns):
		self.db_name = dbName.replace(' ', '_')
		print('PATH lala: ', self.db_name)
		self.conn = sqlite3.connect(self.db_name)
		self.createTable(tableName, columns)


	def createTable(self, tableName, columns):
		self.tableName = tableName.replace(os.sep, '_').replace(' ', '_')
		self.columns = columns
		self.createSQL = 'CREATE TABLE IF NOT EXISTS {0} ({1} TEXT);'.format(
				self.tableName, ' TEXT, '.join(columns));
		print(self.createSQL)
		res = self.conn.execute(self.createSQL);
		self.conn.commit()	# 有修改的话，记得及时commit，否则不会对数据库真正做修改。


	def insert(self, row):
		"""插入一行
		row: 一个列表，长度要和建表时指定的一样；
		row_to_str：可选，可以自己指定把插入的行转成字符串的函数
		"""
		# print(row)
		values = []
		for r in row:
			if type(r) is str:
				values.append("'" + r + "'")
			else:
				values.append(r)
				print('??? ', r)
		sql = 'INSERT INTO {0} VALUES({1});'.format(self.tableName, ', '.join(values))
		self.conn.execute(sql)
		self.conn.commit()


	# 线性查找过去
	def find(self, values):
		"""在数据库中查找
		values：只支持完全匹配，比如['name', 'age', '']表示查找名字刚好为'name'年轻刚好为'age'性别不限的人
		注意空字符串表示'*'，即任意值都可以。

		返回值：True表示查找到了，False表示找不到
		"""
		sql = 'SELECT * FROM {0} WHERE '.format(self.tableName)
		size = len(values)
		for i in range(0, size):
			if i != size - 1:
				sql += "{0} = '{1}' and ".format(self.columns[i], values[i])
			else:
				sql += "{0} = '{1}';".format(self.columns[i], values[i]);
		x = self.conn.execute(sql)
		for r in x:
			return True
		return False


	def delete_all(self):
		"""删除所有的行"""
		sql = 'DELETE FROM {0};'.format(self.tableName)
		self.conn.execute(sql)
		self.conn.commit()


	def get_all(self):
		"""获取表里所有的行"""
		sql = 'SELECT * FROM {0};'.format(self.tableName)
		cursor = self.conn.execute(sql)
		all = []
		for row in cursor:
			all.append(row)
		return all