import pymysql

def testdb():
	conn = pymysql.connect(host='100.99.164.19',port=3306,user='yq365',passwd='AccessLogValve991',db='fdd_portal_2',charset='UTF8')
	cursor = conn.cursor()
	sql = 'select * from t_yq_platform_push'
	cursor.execute(sql)
	
	for i in cursor:
		print(i)

	cursor.close()
	conn.close()


if __name__=='__main__':
    testdb()