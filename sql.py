#https://www.youtube.com/watch?v=g60QghtJmjY&t=957s
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd= "root", database="sb")
print(mydb) 

if(mydb):
	print("done")

else:
	print("failed")

mycursor=mydb.cursor()
mycursor.execute("show databases")

print(" ")
print("databases are")
for db in mycursor:
	print(db)


#create table
#mycursor.execute("create table emp(name varchar(20), salary int(20))")
mycursor.execute("Show tables")

print(" ")
print("Tables are")
for tb in mycursor:
	print(tb)

sqlform= "Insert into emp(name, salary) values(%s, %s)"
empl=[("urvi", 2000000), ("q", 112312)]
mycursor.executemany(sqlform, empl)
mydb.commit()

print(" ")
print("rows are")
mycursor.execute("select * from emp")
for d in mycursor:
	print(d)

