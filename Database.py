import sqlite3
pin=1234
conn=sqlite3.connect("employe.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS worker(id TEXT PRIMARY KEY,
               name TEXT ,
               salary INTERGER,
               job TEXT
               ) """)
def add_records ():
    id=input("enter the worker id:")
    name=input("enter the worker name: ")
    salary=input("enter the worker salary: ")
    job=input("enter the worker job: ")
    cursor.execute("INSERT INTO worker (id,name,salary,job)VALUES(?,?,?,?)",(id,name,int(salary),job))
    conn.commit()
    print("record added sucessfuly")

main_acess=input("press R to see records in database or press A to configure the database: ")
if main_acess=='R':
    cursor.execute("SELECT *FROM worker")
    rows=cursor.fetchall()
    for row in rows:
        print(rows)

elif main_acess=='A':
    db_acess=int(input("enter pin to access the database: "))
    while db_acess != pin:
        print("acess denied you enter the wrong pin")
        db_acess=int(input("enter pin to access the database: "))
    permission=input("press R to add records ")
    if permission=='R':
        num_records=int(input("enter number of records to enter: "))
        for _ in range(num_records):
            add_records()
        ques=input("press W to see records or press E to exit: ")
        if ques=='W':
            cursor.execute("SELECT *FROM worker")
            rows=cursor.fetchall()
            for row in rows:
                print(rows)
        elif ques=='E':
            exit()
        else:
            print("enter the correct option")
conn.close()
