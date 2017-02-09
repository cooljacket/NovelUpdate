# -*- coding:utf-8 -*-
# 使用文件系统自制的简单文件系统
import os

# DB的虚基类
from SimpleDB import SimpleDB


class Cursor:
	"""
	游标类，其实相当于数据库的迭代器。
	使其支持迭代器，方便写代码。
	"""
	def __init__(self, tableName, row_delimiter, cell_delimiter):
		self.data = open(tableName)
		self.row_delimiter = row_delimiter
		self.cell_delimiter = cell_delimiter
		self.blockSize = 1024
		self.last = self.data.read(self.blockSize)
		# self.last = ''

	def __iter__(self):
		return self

	def __next__(self):
		while True:
			pos = self.last.find(self.row_delimiter)
			if pos == -1:
				now = self.data.read(self.blockSize)
				if len(now) == 0:
					break
				self.last += now
			else:
				break

		result = self.last[0:pos]
		self.last = self.last[pos + len(self.row_delimiter):]
		if len(result) == 0:
			raise StopIteration
		return result.split(self.cell_delimiter)


	def close(self):
		self.data.close()


class SimpleDBUsingFS(SimpleDB):
	"""使用fileSystem实现简易数据库类，支持建表、插入、查询、获取整张表、删除整张表的操作"""
	def __init__(self, dbLocation, tableName, columns):
		self.cell_delimiter = '$_$'		# 列之间的分隔符
		self.row_delimiter = '^_^'		# 行之间的分隔符
		self.filePrefix = dbLocation	# 绝对路径
		if not os.path.exists(self.filePrefix):
			os.mkdir(self.filePrefix)
		self.createTable(tableName, columns)


	def createTable(self, tableName, columns):
		# 要用绝对路径，因为使用crontab运行时，若按照相对目录输出的话，你不知道在哪
		self.tableName = self.filePrefix + tableName.replace(os.sep, '_') + '.db_jacket'
		print('creating', self.tableName)
		# 如果数据库文件不存在，则新建一个
		if not os.path.exists(self.tableName):
			self.size = len(columns)
			self.columnToIndex = {}
			for i in range(0, self.size):
				self.columnToIndex[columns[i]] = i
			# 清空数据库，保证所用的文件是存在的
			self.delete_all()


	def insert(self, row):
		"""插入一行
		row: 一个列表，长度要和建表时指定的一样；
		row_to_str：可选，可以自己指定把插入的行转成字符串的函数
		"""
		with open(self.tableName, 'a') as db:
			db.write(self.row_to_str(row))


	# 线性查找过去
	def find(self, values):
		"""在数据库中查找
		values：只支持完全匹配，比如['name', 'age', '']表示查找名字刚好为'name'年轻刚好为'age'性别不限的人
		注意空字符串表示'*'，即任意值都可以。

		返回值：True表示查找到了，False表示找不到
		"""
		result = False
		cursor = Cursor(self.tableName, self.row_delimiter, self.cell_delimiter)
		for row in cursor:
			if len(values) == len(row):
				match = True
				for i in range(0, len(values)):
					# 需要全部都匹配才算可以！空字符串可以匹配任意内容！
					if len(values[i]) > 0 and values[i] != row[i]:
							match = False
							break
				if match:
					result = True
					break
		cursor.close()
		return result


	def row_to_str(self, row):
		if row is None or len(row) == 0:
			return ''
		row_str = row[0]
		for i in range(1, len(row)):
			row_str += '{0}{1}'.format(self.cell_delimiter, row[i])
		row_str += self.row_delimiter
		return row_str


	def delete_all(self):
		"""删除所有的行"""
		if os.path.exists(self.tableName):
			os.remove(self.tableName)
		with open(self.tableName, 'w') as f:
			pass


	def get_all(self):
		"""获取表里所有的行"""
		cursor = Cursor(self.tableName, self.row_delimiter, self.cell_delimiter)
		all = []
		for row in cursor:
			all.append(row)
		cursor.close()
		return all
