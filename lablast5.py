import psycopg2
conn = psycopg2.connect(
	database="example",
	user='ex_user',
	password='l;fcnby',
	host='localhost',
	port= '5432'
)
cur = conn.cursor()
name = input()


 
cur.execute("CALL delete_by_name(%s);", [name])
conn.commit();
cur.close()
conn.close()