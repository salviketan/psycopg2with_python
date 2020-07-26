import psycopg2


def insert(name,lastname,age,salary):
    try:
        conn=psycopg2.connect(host='localhost',database='testdb',user='postgres',password='linux')
        cur=conn.cursor()
        query="insert into pri_key_example (name,lastname,age,salary) values(%s,%s,%s,%s)"
        cur.execute(query,(name,lastname,age,salary))
        conn.commit()
        print("Row is created successfully.")
        print()

    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            print("There is a problem: ",e)
    finally:
        cur.close()
        conn.close()


def view(tname):
    try:
        conn=psycopg2.connect(host='localhost',database='testdb',user='postgres',password='linux')
        cur=conn.cursor()
        query="select * from {};".format(tname)
        # print(query)
        cur.execute(query)
        data=cur.fetchall()
        print(data)
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            print("There is a problem: ",e)
    finally:
        cur.close()
        conn.close()


def search(name,lastname,age,salary):
    try:
        conn=psycopg2.connect(host='localhost',database='testdb',user='postgres',password='linux')
        cur=conn.cursor()
        query="select * from my_table where name =%s or lastname =%s or age::text like %s or salary::text like %s;"
        cur.execute(query,(name,lastname,age,salary))
        row=cur.fetchall()
        print(row)
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            print("There is a problem: ",e)
    finally:
        cur.close()
        conn.close()


def update(name,lastname,age,salary):
    try:
        conn=psycopg2.connect(host='localhost',database='testdb',user='postgres',password='linux')
        cur=conn.cursor()
        query="select * from my_table where name =%s or lastname =%s or age::text like %s or salary::text like %s;"
        cur.execute(query,(name,lastname,age,salary))
        row=cur.fetchall()
        index=row[0][0]

        w=input("Enter the name to be Updated:")
        x=input("Enter the lastname to be Updated: ")
        y=input("Enter the age to be Updated: ")
        z=input("Enter the salary to be Updated: ")
        cur.execute("update my_table set name=%s ,lastname=%s,age=%s,salary=%s where name=%s;",(w,x,y,z,index))
        conn.commit()
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            print("There is a problem: ",e)
    finally:
        cur.close()
        conn.close()


def delete(name,lastname,age,salary):
    try:
        conn=psycopg2.connect(host='localhost',database='testdb',user='postgres',password='linux')
        cur=conn.cursor()
        query="select * from my_table where name =%s or lastname =%s or age::text like %s or salary::text like %s;"
        cur.execute(query,(name,lastname,age,salary))
        row=cur.fetchall()
        index=row[0][0]
        print()
        print("Selected row for delete operation: ",row)
#        print(index)
        del_=input("Are you sure you want to delete this row? ").lower()
        if del_:
            if del_[0]=='y':
                cur.execute("delete from my_table where name=%s;",(index,))
                print("Row is deleted.")
                conn.commit()
            elif del_[0]=='n':
                print("Abort")
            else:
                print("Please enter [Yes|No].")
        else:
            print("Please enter [Yes|No].")
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            print("There is a problem: ",e)
    finally:
        cur.close()
        conn.close()



option=int(input('''Choose your option:
             1) Insert
             2) View all:can search any table in db
             3) Search
             4) Update/Edit
             5) Delete \n'''))
if option == 1:
    records_range=int(input("Enter the number of row's you want to insert: "))
    if records_range >0:
        for i in range(records_range):
            print("{} entry:".format(i+1))
            a=input("Enter the name: ")
            b=input("Enter the lastname: ")
            c=int(input("Enter the age: "))
            d=float(input("Enter the salary: "))
            insert(a,b,c,d)
    else:
        print("Enter the valid input \nWarning:input should be a number and it should be greater than '0'")
elif option ==2:
    t=input("Enter the table name: ")
    view(t)
elif option ==3:
    a=input("Enter the name: ")
    b=input("Enter the lastname: ")
    c=input("Enter the age: ")
    d=input("Enter the salary: ")
    search(a,b,c,d)
elif option ==4:
    a=input("Enter the name: ")
    b=input("Enter the lastname: ")
    c=input("Enter the age: ")
    d=input("Enter the salary: ")
    update(a,b,c,d)
elif option ==5:
    print("Please provide name/lastname parameters for exact selection.")
    a=input("Enter the name: ")
    b=input("Enter the lastname: ")
    c=input("Enter the age: ")
    d=input("Enter the salary: ")
    delete(a,b,c,d)
else:
    print("Select the valid option form the list [type number and hit enter].")
