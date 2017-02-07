# encoding: utf-8
import sqlite3

def test(db, table):
	conn = sqlite3.connect(db)
	cu = conn.execute('select * from {0}'.format(table))
	cnt = 0
	for r in cu:
		cnt += 1
		# print(r)
	cu.close()
	return cnt


print('data: ', test('NovelUpdate_data', '万古神帝'))
print('fail: ', test('NovelUpdate_fail', '万古神帝'))
