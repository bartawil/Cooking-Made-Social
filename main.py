import pymysql


def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password="1234",
		db='database_workshop',
	)

	cur = conn.cursor()

	# Select query
	cur.execute("select * from users")
	output = cur.fetchall()
	print(output)

	# flg = 0
	# g = ''
	# for i in output:
	# 	id = str(i[0])
	# 	name = str(i[1])
	# 	q = "select * from users"
	#
	# 	cur.execute(q)
	conn.commit()


	# To close the connection
	conn.close()


# Driver Code
if __name__ == "__main__":
	mysqlconnect()

