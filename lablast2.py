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
surname = input()
phone = int(input())


 
cur.execute("CALL insert_to_table(%s, %s, %s);", (name, surname, phone))
conn.commit();
cur.close()
conn.close()