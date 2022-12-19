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
	cur.execute("select post_id, recipe_name from post")
	output = cur.fetchall()

	flg = 0
	g = ''
	for i in output:
		id = str(i[0])
		name = str(i[1])
		q = "UPDATE recipe SET recipe.post_id=" + id + " WHERE recipe.name_id=" + "'"+ name+"'"
		# print(q)
		cur.execute(q)
		conn.commit()


	# To close the connection
	conn.close()


# Driver Code
if __name__ == "__main__":
	mysqlconnect()

