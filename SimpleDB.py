# -*- coding:utf-8 -*-
import os


class Singleton(type):
	def __init__(cls, name, bases, dict):
		super(Singleton, cls).__init__(name, bases, dict)
		cls._instance = None

	def __call__(cls, *args, **kw):
		if cls._instance is None:
			cls._instance = super(Singleton, cls).__call__(*args, **kw)
		return cls._instance


class Cursor:
	def __init__(self, tableName):
		self.cursor = open(tableName)

	def getCursor(self):
		return self.cursor

	def close(self):
		self.cursor.close()


class SimpleDB:
	__metaclass__ = Singleton

	def __init__(self):
		self.cell_delimiter = '$_$'
		self.row_delimiter = '\n'


	def createTable(self, tableName, columns):
		self.tableName = tableName.replace('/', '_') + '.db_jacket'
		# 如果数据库文件已经存在，则保留原有数据，不要覆盖
		if not os.path.exists(self.tableName):
			self.size = len(columns)
			self.columnToIndex = {}
			for i in range(0, self.size):
				self.columnToIndex[columns[i]] = i
			# 清空数据库，保证所用的文件是存在的
			self.delete_all()


	def insert(self, row, row_to_str=None):
		with open(self.tableName, 'a') as db:
			if row_to_str is None or not callable(row_to_str):
				row_to_str = self.row_to_str
			db.write(row_to_str(row))


	# 线性查找过去
	def find(self, values):
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
		if os.path.exists(self.tableName):
			os.remove(self.tableName)
		with open(self.tableName, 'w') as f:
			pass


	def get_all(self):
		cursorObj = Cursor(self.tableName)
		cursor = cursorObj.getCursor()
		all = []
		for row in cursor:
			all.append(row.split(self.cell_delimiter))
			all[-1][-1] = all[-1][-1].strip()
		cursor.close()
		return all

