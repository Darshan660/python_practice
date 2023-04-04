import sqlite3
connection = sqlite3.connect("myTable.db")
crsr = connection.cursor()
crsr.execute("SELECT * FROM emp")
ans = crsr.fetchall()
print(ans)