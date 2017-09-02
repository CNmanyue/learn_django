# -*- coding: utf-8 -*-

#时间，最大值400天，一个农民干到死
days = range(401)
#农民，最大值400-1个，400个农民一天搞定
farmers = range(400)
#成功解次数
count = 0
for f in farmers:
	for d in days:
		if d==20-20*(0.5**f)+400/(f+1):
			print('成功解：农民：%d \t时间：%s'%(f+1,d))
			count+=1
		else:
			pass
			#print('失败解：农民：%s \t时间：%s'%(f,d))
			
print('成功解次数：%d'%count)