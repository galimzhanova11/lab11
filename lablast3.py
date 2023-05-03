import psycopg2
conn = psycopg2.connect(
	database="example",
	user='ex_user',
	password='l;fcnby',
	host='localhost',
	port= '5432'
)
cur = conn.cursor()
arr = [('name7', 'lastname7', 777555), ('name77', 'lastname77', 777965), ('name75', 'lastname75', 777833), ('name37', 'lastname37', 777), ('name17', 'lastname17', 77)]

many_users = "name7,lastname7,777555;name77,lastname77,777965"
cur.execute("CALL insert_many_users(%s);", (many_users,))

for i in cur.fetchall():
    print(i)
#conn.commit();
conn.commit()
cur.close()
conn.close()