import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@23"
)
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)