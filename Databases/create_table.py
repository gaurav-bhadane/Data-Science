import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@23"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS SAMPLE1")
mycursor.execute("USE SAMPLE1")
mycursor.execute("CREATE TABLE IF NOT EXISTS sample_data (id INT PRIMARY KEY,name VARCHAR(30))")
mycursor.execute("INSERT INTO sample_data VALUES(1,'Gaurav'),(2,'Raj')")
mydb.commit()
mycursor.execute("SELECT * FROM sample_data ")
for x in mycursor.fetchall:
    print(x)
mydb.close()