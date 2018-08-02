import pymysql

conn = pymysql.connect("localhost","root","SQLac931014","test")
cur = conn.cursor()



def isExisted(username,password):
	conn = pymysql.connect("localhost","root","SQLac931014","test")
	cur = conn.cursor()
	sql="select * from user where username ='%s' and password ='%s'" %(username,password)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

def isExisted_name(username):
	conn = pymysql.connect("localhost","root","SQLac931014","test")#too long to connect to fail
	cur = conn.cursor()
	sql="select * from user where username ='%s'" %(username)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

def insert(username,password):
	conn = pymysql.connect("localhost","root","SQLac931014","test")#too long to connect to fail
	cur = conn.cursor()
	if isExisted_name(username):
		return False
	else:
		sql = "insert into user (username,password) values ('%s','%s')" %(username,password)
		cur.execute(sql)
		conn.commit()
		conn.close()
    	
		return True
    	
	    
	


