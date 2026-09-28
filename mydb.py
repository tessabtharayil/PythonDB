import mysql.connector
# #    OR
# # from mysql import connector
#
# con=mysql.connector.connect(user="root",password="rootroot",host="localhost")
#     # establish connection between python code and mysql server
#     # it returns a connection object
# print(con)
#
# c=con.cursor() # cursor object used to execute sql queries/commands
#
# # c.execute(command)
# # create database file
# c.execute("create database school_db")
# print("Database file created")

con=mysql.connector.connect(user="root",password="rootroot",host="localhost",database="school_db")
c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
#                      name varchar(20),
#                      age int,
#                      place varchar(20),
#                      phone varchar(20),
#                      total_mark int)''')
# print("Table created successfully")

# c.execute('''insert into student(roll_no,name,age,place,phone,total_mark)
#                          values(101,"Arun",11,"ekm","8643695326",145),
#                                (102,"Amal",12,"ekm","6337858427",140),
#                                (103,"Anu",11,"tvm","9754146428",147),
#                                (104,"Hari",12,"tcr","9754245890",144),
#                                (105,"Manu",11,"ekm","7120945278",141)
# ''');
# con.commit() # to save data permanently inside db
# print("Data inserted")

# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(106,"Kiran",12,"ekm","9623490735",140)
# c.execute(query,data)
# con.commit()

# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")


# Read all attributes of a student with roll number=roll number entered by user
# ----------------------------------------------------------------------------
# number=int(input("Enter roll number:"))
# query="select * from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print("No records found")

# Update mark of a student with roll number=roll number entered by user
# ---------------------------------------------------------------------
# number=int(input("Enter roll number:"))
# mark=int(input("Enter mark to be updated:"))
# query="update student set total_mark=%s where roll_no=%s"
# data=(mark,number)
# c.execute(query,data)
# con.commit()
# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")

# Delete a record with roll number=roll number entered by user
# ------------------------------------------------------------
# number=int(input("Enter roll number:"))
# query="delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")

# Create a new record using values entered by user
# -------------------------------------------------
rollno=int(input("Enter roll number:"))
name=input("Enter name:")
age=int(input("Enter age:"))
place=input("Enter place:")
phone=input("Enter phone number:")
mark=int(input("Enter mark:"))
query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
data=(rollno,name,age,place,phone,mark)
c.execute(query,data)
query="select * from student"
c.execute(query)
records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("No records found")