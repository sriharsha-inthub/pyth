# numbers = [2,5,4,6,2,4,8,10]
# uniques = []
# for number in numbers :
#   if number not in uniques:
#      uniques.append(number)
# print(uniques)
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="pertable")
def updateData(conn):
    print("Update")
    Id=input("Enter Id:")
    Name=input("Enter Name:")
    Location = input("Enter Location")
    sql ='update per set Name = %s, Location = %s where EmpId = %s'
    val = (Name, Location, Id,)
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()

#insertData()

#def update():

 #   id = input("Enter employe id:")
  #  Name = input("Enter Name:")
   # sql = "update per set Name=%s where EmpId=%s"
    #val = [Name, id,]
    #cursor = conn.cursor()
    #cursor.execute(sql, val)
    #conn.commit()
updateData(conn)

print("Success")
