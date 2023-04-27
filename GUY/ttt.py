import mysql.connector as m

c=m.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ak"
    )
cur=c.cursor()
ins="insert into f1 values(%s,%s);"
ask=int(input("How many input:"))

for i in range(ask):
        userInput=(input("Enter name: "),
                   input("Enter Enroll: "))
        cur.execute(ins,userInput)

c.commit()
