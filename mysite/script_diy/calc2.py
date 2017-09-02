# -*- coding: utf-8 -*-

#时间，最大值400天，一个农民干到死
days = range(401)
#农民，最大值400-1个，400个农民一天搞定
farmers = range(400)
#成功解次数
count = 0

#1.需要f个农民
f=0
#2.已有x个农民
x=1
#3.生产出n个农民需要d天
d=0
#4.已花费时间
dd=0
#每日剩余的粮食
overplusRice = 0
while f<401:
	dd+=1
	overplusRice = overplusRice+5*x
	z = (overplusRice)/50
	if z > 0:
		#可以再生产z个农民
		if (x+z)>f:
			#超出所需农民数，需要控制兑换农民的数量
			z = (f-x)
			f = f+1
		
		overplusRice = overplusRice-50*z
		x += z
		d = int((2000-overplusRice)/50)
		print(d)
		if isinstance(d,int):
			count+=1
			print('成功解：农民：%d \t时间：%s'%(f+1,(dd+d)))
			
if count<1:
	print('无解')
