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

	flg = 0
	for i in output:
		if flg == 0:
			print(i)
			# flg = 1

	# To close the connection
	conn.close()


# Driver Code
if __name__ == "__main__":
	mysqlconnect()

