# Define a class to perform database operations on Vehicle Table
# Create a class named VehicleListCreateRetrieveUpdateDelete
# Define methods
    # list() --> for reading all records
    # create() --> for creating a new record
    # retrieve() --> for reading a specific record
    # update(id,data) --> for updating a specific record
    # delete(id) --> for deleting a specific record
# -------------------------------------------------------------
import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root", password="rootroot", host="localhost", database="vehicle_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("Sucessfully connected")

    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No record found")

    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)"
        data = (brand,model,type,price,year)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("Data Inserted Sucessfully")

    def retrieve(self,id):
        query = "select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No records found")

    def update(self,id,brand,model,type,price,year):
        query = "update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data = (brand,model,type,price,year,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Updated Sucessfully")
        else:
            print("No Record Found")

    def delete(self,id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        # self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Data is Deleted")
        else:
            print("No Record Found")

vehicle_instance=VehicleListCreateRetrieveUpdateDelete()
# vehicle_instance.list()
#vehicle_instance.create("Tesla","Model Y","Electric",5000000,2020)
#vehicle_instance.retrieve(1)
#vehicle_instance.update(1,"Mahindra","Thar","Petrol",2500000,2025)
#vehicle_instance.delete(1)