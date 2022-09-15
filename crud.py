import mysql.connector


#pip install mysql-connector
conn=mysql.connector.connect(host="localhost", user="root", passwd="admin", database="pertable")
print(conn)
def getData(conn):
   print("Read")
   cursor = conn.cursor();
   cursor.execute("select * from per")
   for row in cursor:
      print(f'{row}')


getData(conn)
def insertData(conn):
    print("insert")
    cursor = conn.cursor()
    cursor.execute(
        "insert into per (EmpId,Name,Location) values('ID0007','Krish','Bangalore')",
        )
    conn.commit()

#insertData(conn)
#getData(conn)
def updateData(conn):
    print("Update")
    #Id=input("Enter Id:")
    #Name=input("Enter Name:")
    sql ='update per set Name = "xyz" , Location = "Bangalore" where EmpId = "0"'
    #val = (Name, Id,)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

#insertData()
updateData(conn)

getData(conn)

