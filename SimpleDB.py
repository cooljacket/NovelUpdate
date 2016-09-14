# -*- coding:utf-8 -*-
import os


class Singleton(type):
	"""用来辅助SimpleDB实现单例模式的"""
	def __init__(cls, name, bases, dict):
		super(Singleton, cls).__init__(name, bases, dict)
		cls._instance = None

	def __call__(cls, *args, **kw):
		if cls._instance is None:
			cls._instance = super(Singleton, cls).__call__(*args, **kw)
		return cls._instance


class Cursor:
	"""游标类，其实相当于数据库的迭代器"""
	def __init__(self, tableName):
		self.cursor = open(tableName)

	def getCursor(self):
		return self.cursor

	def close(self):
		self.cursor.close()


class SimpleDB:
	"""简易数据库类，支持建表、插入、查询、获取整张表、删除整张表的操作"""
	__metaclass__ = Singleton

	def __init__(self):
		self.cell_delimiter = '$_$'
		self.row_delimiter = '\n'
		self.filePrefix = '/home/NovelUpdate/'	# 绝对路径


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


	def insert(self, row, row_to_str=None):
		"""插入一行
		row: 一个列表，长度要和建表时指定的一样；
		row_to_str：可选，可以自己指定把插入的行转成字符串的函数
		"""
		with open(self.tableName, 'a') as db:
			if row_to_str is None or not callable(row_to_str):
				row_to_str = self.row_to_str
			db.write(row_to_str(row))


	# 线性查找过去
	def find(self, values):
		"""在数据库中查找
		values：只支持完全匹配，比如['name', 'age', '']表示查找名字刚好为'name'年轻刚好为'age'性别不限的人
		注意空字符串表示'*'，即任意值都可以

		返回值：True表示查找到了，False表示找不到
		"""
		cursorObj = Cursor(self.tableName)
		cursor = cursorObj.getCursor()
		result = False
		for row in cursor:
			row = row.strip().split(self.cell_delimiter)
			if len(values) == len(row):
				match = True
				for i in range(0, len(values)):
					if len(values[i]) > 0:
						if values[i] != row[i]:
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
		cursorObj = Cursor(self.tableName)
		cursor = cursorObj.getCursor()
		all = []
		for row in cursor:
			all.append(row.split(self.cell_delimiter))
			all[-1][-1] = all[-1][-1].strip()
		cursor.close()
		return all

