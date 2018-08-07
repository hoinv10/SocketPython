import pymysql
db	=	pymysql.connect(host='localhost',user='root',passwd	='123456',db='SINHVIEN')

cursor	=	db.cursor()
sql	=	'SELECT	*	FROM	TEST'
cursor.execute(sql)
myusers	=	cursor.fetchall()
print (myusers)

cursor.close()
db.close()

