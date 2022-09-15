import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="admin", database="pertable")
#pip install mysql
#print(conn)
cursor = conn.cursor()
def insert():
    EmpId = input("Enter Employee Id:")
    Name=input("Enter Name:")
    Location=input("Enter Location")
    sql= "insert into per(EmpId,Name,Location) values(%s,%s,%s)"
    val=(EmpId,Name,Location)
    try:
        cursor.execute(sql,val)
        conn.commit()
        print("successfull")
        menu()
    except Exception as e:
        print(e)
        menu()
def Read():
    sql= "select * from per"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for x in data:
            print(f'{x}')
        print("Successfull")
        menu()
    except Exception as e:
        print(e)
        menu()
def Delete():
    Name=input("Enter employe Name:")
    sql="delete from per where Name=%s"
    val=(Name,)
    try:
        cursor.execute(sql,(val))
        conn.commit()
        print("successfull")
        menu()
    except Exception as e:
        print(e)
        menu()
def Update():
    id = input("Enter employe id:")
    sql = "select * from per where EmpId=%s"
    val = (id,)
    try:
        cursor.execute(sql,val)
        data=cursor.fetchall()
        for x in data:
           Name=x[1]
           Location=x[2]

       # print("1.update Name\n 2.Update Location ")
        #ch=int(input("Enter Choice:"))
        #if(ch==1):
        Name=input("Enter Name")
        #elif(ch==2):
        Location=input("Enter Location")
        #else:
         #   print("Wrong input")
            #menu()

        sql= "update per set Name=%s,Location=%s"
        val=(Name,Location,)
        try:
            cursor.execute(sql,val)
            conn.commit()
            print("successfull")
            menu()
        except Exception as e:
            print(e)
            menu()
    except Exception as e:
        print(e)
        menu()


def menu():
    print("Select any option\n 1.Insert\n 2.Read\n 3.Update\n 4.Delete")
    ch=int(input("Enter your choice"))
    if(ch==1):
        insert()
    elif(ch==2):
        Read()
    elif(ch==3):
        Update()
    elif(ch==4):
        Delete()
    else:
        print("Wrong input")
        menu()
menu()