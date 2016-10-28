import os

os_name = os.name
print(os_name)

try:
	os_uname = os.uname()
	print(os_uname)
except Exception as e:
	pass

os_environ = os.environ
# print(os_environ)
print('type_env:',type(os_environ))
# print(os_environ.get('path'))

print('os.path.abspath:',os.path.abspath(__file__))

testjoin = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testjoin')
print('testjoin:',testjoin)

split = os.path.split(os.path.abspath(__file__))
print('type_split:',type(split))

# os.rename('','')
# os.rmmove('')

# os.listdir(path)
# '.' 表示当前目录
# '..' 表示当前目录的父目录
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print('dirs:',dirs)

splittext = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print('splittext:',splittext)

print('获取当前目录:',os.getcwd())

print('>>>>>>>>>>>>>>>>>>>end<<<<<<<<<<<<<<<<')