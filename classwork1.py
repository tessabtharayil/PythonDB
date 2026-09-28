import mysql.connector
con=mysql.connector.connect(user="root",password="rootroot",host="localhost",database="shop")
c=con.cursor()


# Create a database named shop
# ----------------------------
# c.execute("create database shop")
# print("Database file created")


# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
# ----------------------------------------------------
# c.execute('''
# create table product(product_id int not null primary key,
#                      name varchar(20),
#                      brand varchar(20),
#                      category varchar(20),
#                      price int,
#                      stock int)''')
# print("Table created successfully")


# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit
# --------------------------------------------------------------------------
def insert():
    n1 = int(input("Enter product id:"))
    n2 = input("Enter name:")
    n3 = input("Enter brand:")
    n4 = input("Enter category:")
    n5 = int(input("Enter price:"))
    n6 = int(input("Enter stock:"))
    query = "insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
    data = (n1,n2,n3,n4,n5,n6)
    c.execute(query, data)
    con.commit()

def read():
    query="select * from product"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

def search():
    id=int(input("Enter product id:"))
    query="select * from product where product_id=%s"
    data=(id,)
    c.execute(query,data)
    record=c.fetchone()
    if record:
        print(record)
    else:
        print("No records found")

def update():
    id=int(input("Enter product id:"))
    stock=int(input("Enter stock to be updated:"))
    query="update product set stock=%s where product_id=%s"
    data=(stock,id)
    c.execute(query,data)
    con.commit()

def delete():
    id=int(input("Enter product id:"))
    query="delete from product where product_id=%s"
    data=(id,)
    c.execute(query,data)
    con.commit()

while(True):
    print("1.Insert Product details")
    print("2.Read all Product details")
    print("3.Search a Product by product_id")
    print("4.Update the stock of a Product")
    print("5.Delete a Product record")
    print("6.Exit")
    ch=int(input("Enter a option:"))

    if ch==1:
        insert()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    else:
        exit()
