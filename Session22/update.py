import sqlite3
connection = sqlite3.connect("myTable.db")
connection.execute("UPDATE emp SET fname = 'tom' where fname='selena' ")
connection.commit()
print("Total number of rows updated:",connection.total_changes)

connection.execute("DELETE from emp where lname='swift' ")
connection.commit()
print("Total number of rows deleted:",connection.total_changes)


cursor = connection.execute("SELECT*FROM emp")
for row in cursor:
    print(row)

connection.close()