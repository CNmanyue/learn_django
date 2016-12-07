#!/usr/bin/env python
'''
解析excel中的简历信息
保存到数据库中
create_time:2016/12/07
'''
import sqlite3
# 1.得到文件夹下面所有的excel
import os
# //os模块，调用操作系统提供的接口函数
ABS_PATH = r'C:\Users\Mokushle\Desktop\temp\11\1121\张大叔'
file_list = [os.path.join(ABS_PATH,x) for x in os.listdir(ABS_PATH) if os.path.splitext(x)[1]=='.xls' or os.path.splitext(x)[1]=='xlsx']

print('检索到的文件:\n',file_list)

# 2.解析excel
import xlrd

for x in file_list:
	# 打开
	data = xlrd.open_workbook(x)
	# 获取一个工作列表
	# sheet = data.sheets()[0]
	# sheet = data.sheet_by_index(0) # 通过索引获取


	# 2.1按照文件名，按照是否包含"智联"、"51"、"cjol"分成三类，调用不同的处理函数
	if '智联' in x:
		print('调用智联的处理函数')
		do_by_zl(data)
	elif '51' in x:
		print('调用51job的处理函数')
	elif 'cjol' in x:
		print('调用人才热线的处理函数')
	else:
		print('未知的格式:',x)

print('end of run.')


def do_by_zl(data):
	pass
