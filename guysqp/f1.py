from tkinter import *
import mysql.connector as m

def g():
    username=ent.get()
    pwd=ent2.get()
    #print(username,pwd)

    c=m.connect(
        host="localhost",
        user="root",
        password="1234",
        database="users"
    cur=c.cursor()
    )

win=Tk()
win.geometry("600x600")

l1=Label(win, text="Username")
l1.place(x=25,y=20)
l2=Label(win,text="Password")
l2.place(x=25,y=50)

ent=Entry(win)
ent.place(x=80,y=20)

ent2=Entry(win)
ent2.place(x=80,y=50)

btn=Button(win,text="Login")
btn.place(x=70,y=80)


get()
win.mainloop()