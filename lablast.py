import psycopg2
conn = psycopg2.connect(
	database="people",
	user='postgres',
	password='rootroot',
	host='localhost',
	port= '5432'
)
cur = conn.cursor()
name_part = input()

cur.callproc('get_users_by_namepart7', (name_part,))

for i in cur.fetchall():
    print(i)
cur.close()
conn.close()