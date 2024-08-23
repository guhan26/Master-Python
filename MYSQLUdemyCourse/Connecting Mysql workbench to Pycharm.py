
# This line imports the mysql.connector module, which is a Python library used to connect to and interact with MySQL databases

import mysql.connector

# This block of code creates a connection object mydb to the MySQL database using the mysql.connector.connect method

mydb = mysql.connector.connect(

    host="localhost",  # Specifies that the MySQL server is running on the local machine
    user="YYYY",  # The username used to authenticate with the MySQL server
    password="XxxxxX@0987",  # The password associated with the specified user
    database="testdata"  # The name of the database you want to connect to
)

# This line creates a cursor object using the cursor method of the connection object mydb
mycursor = mydb.cursor()

# The execute method sends the query to the MySQL server
mycursor.execute("CREATE DATABASES")
for db in mycursor:
    print(db)

# CREATE DATABASE
mycursor.execute("CREATE DATABASE testdata")


# SHOW DATABASES
mycursor.execute("SHOW DATABASES")
for row in mycursor:
    print(row)

# CREATE TABLE 
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


# SHOW TABLES
mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)

# INSERT
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("XXXX", 23),
            ("YYYY", 24),
            ("ZZZZ", 25),
            ("MMMM", 29),]
mycursor.executemany(sqlFormula, students)
mydb.commit()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

# SELECT
sql = "SELECT * FROM students WHERE age = 23"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

# UPDATE
sql = "UPDATE students  SET age = 30 WHERE name = 'arun'"
mycursor.execute(sql)
mydb.commit()

# LIMIT
mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 2")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

# ORDER BY
sql = "SELECT * FROM students ORDER BY name"
mycursor.execute(sql)
myresult =  mycursor.fetchall()
for r in myresult:
    print(r)

# DELETE
sql = "DELETE FROM students WHERE  name = 'guhan'"
mycursor.execute(sql)
mydb.commit()

# DROP
sql = "DROP TABLE students"
mycursor.execute(sql)
mydb.commit()
