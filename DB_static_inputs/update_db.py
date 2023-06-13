import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

conn.execute('''
update participants
set name = "Arjun Gaikwad"
where g_id = 1
''')

conn.commit()
conn.close()