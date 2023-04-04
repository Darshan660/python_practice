import sqlite3
connection = sqlite3.connect("myTable.db")

crsr = connection.cursor() #We will write code here but it will be uploaded in database

sql_command = """CREATE TABLE emp(
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
Lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""
crsr.execute(sql_command)
#crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (1,"selena","gomez","F","2020-03-01");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (2,"taylor","swift","F","2020-10-02");"""
crsr.execute(sql_command)

connection.commit()
connection.close()
