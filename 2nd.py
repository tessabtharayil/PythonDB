# Define a class to perform database operations on Book Table
# Create a class named BookListCreateRetrieveUpdateDelete
# Define methods
    # list() --> for reading all records
    # create() --> for creating a new record
    # retrieve() --> for reading a specific record
    # update(id,data) --> for updating a specific record
    # delete(id) --> for deleting a specific record
# -------------------------------------------------------------
import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root", password="rootroot", host="localhost", database="library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("Sucessfully connected")

    def list(self):
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")

    def create(self,title,author,price,pages,language):
        query = "insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
        data = (title,author,price,pages,language)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("Data Inserted Sucessfully")

    def retrieve(self,id):
        query = "select * from book where id=%s"
        data=(id,)
        # if there is only one element in tuple to read it in sequence just use a comma after element
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No records found")

    def update(self,id,title,author,price,pages,language):
        query = "update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data = (title,author,price,pages,language,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Updated Sucessfully")
        else:
            print("No Record Found")

    def delete(self,id):
        query = "delete from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        #self.connection.commit()
        if self.cursor.rowcount>0: # if no updations rowcount returns 0
            print("Data is Deleted")
        else:
            print("No Record Found")
book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create("STU","Sam",400,500,"English")
# book_instance.retrieve(2)
# book_instance.update(2,"PQR","Mike",300,400,"English")
# book_instance.delete(1)