import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

conn.execute('''
delete from participants
where g_id = 4''')

conn.commit()
conn.close()