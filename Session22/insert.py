import sqlite3
connection = sqlite3.connect("MyTable.db")

#cursor
crsr = connection.cursor()
sql_command = """INSERT INTO emp VALUES(3,"Ariana","Grande","F","2021-10-01") """
crsr.execute(sql_command)
connection.commit()