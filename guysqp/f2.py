from tkinter import *
import mysql.connector as m
from tkinter import messagebox


def g():

    
    
    c=m.connect(
        host="localhost",
        user="root",
        password="1234",
        database="users"
    )
    cur=c.cursor()
    q=f"select * from f1 where username='{uname.get()}' and password='{pwd.get()}'"
    
    cur.execute(q)
    result=cur.fetchall()
    print(result)
    if(result==""):
        infor="Please Check Username or Password"
    
        uname.set("")
        pwd.set("")
        var=messagebox.showinfo("Warring",infor) 
        if var=='ok':
            newwin() 
    

    else:
        inforr="login sucess"
        global name
        name=uname.get()
        uname.set("")
        pwd.set("")
        var=messagebox.showinfo("Status",inforr)
        if var=='ok':
            newwin()  
    
    c.close()

def newwin():
     s=Tk()
     s.geometry("300x300")
     global name
     lb=Label(s,text=f"your name is {name}")
     lb.pack()

     
     s.mainloop()

win=Tk()
win.geometry("600x600")
global uname
global pwd
uname=StringVar()
pwd=StringVar()

lbl=Label(win,text="Login",bg="red",font=("arial",16))
lbl.place(x=60,y=0)

lbl1=Label(win,text="Username",font=("arial",16))
lbl1.place(x=40,y=40)

lbl2=Label(win,text="Password",font=("arial",16))
lbl2.place(x=40,y=90)

ent1=Entry(win,font=("arial",16),textvariable=uname)
ent1.place(x=150,y=40)

ent2=Entry(win,font=("arial",16),show="*",textvariable=pwd)
ent2.place(x=150,y=90)

btn= Button(win,text="GET",font=("arial",16),command=g)
btn.place(x=100,y=140)

win.mainloop()
