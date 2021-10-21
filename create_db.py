import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.68 ",
    user="root",
    password = "amanshah",
)
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE hms")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
