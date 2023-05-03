import psycopg2
conn = psycopg2.connect(
	database="example",
	user='ex_user',
	password='l;fcnby',
	host='localhost',
	port= '5432'
)
cur = conn.cursor()
limit = int(input())
offset = int(input())

cur.callproc('pag', (limit, offset,))

for i in cur.fetchall():
    print(i)
#conn.commit();
cur.close()
conn.close()