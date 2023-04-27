from tkinter import *
from tkinter import ttk
import mysql.connector

win=Tk()



win.geometry("600x600")

lbl=Label(win,text="Name",bg="white",fg="Black",font=("arial",16))
#lbl.grid(row=1,column=10)
lbl.place(x=200,y=50)

e1=Entry(win,font=("arial",16))
e1.place(x=290,y=50)


lbl2=Label(win,text="Fname",bg="white",fg="Black",font=("arial",16))
#lbl2.grid(row=3,column=10)
lbl2.place(x=200,y=90)

e2=Entry(win,font=("arial",16))
e2.place(x=290,y=90)

lbl3=Label(win,text="Enroll",bg="white",fg="RED",font=("arial",16))
#lbl3.grid(row=5,column=10)
lbl3.place(x=200,y=130)

e3=Entry(win,font=("arial",16))
e3.place(x=290,y=130)

lbl4=Label(win,text="Branch",bg="white",fg="Black",font=("arial",16))
lbl4.place(x=200,y=170)

#e4=Entry(win,font=("arial",16),fg="red")
#e4.place(x=290,y=170)

#c=StringVar()
ck=ttk.Combobox(win,font=("arial,16"),background="white")
ck["state"]="readonly"
ck["values"]=(
               "BCA",
               "BCA(SACS)",
               "BCA(CC)",
               "BTECH(CSE)",
               "BTECH(ENG)",
               "BTECH(CIVIL)",
               "BTECH(ELE)"
)
ck.place(x=290,y=173)

btn=Button(win, text="Submit",bg="white",fg="pink",font=("arial",16),
           relief="ridge",borderwidth=2,background="darkblue")
btn.place(x=270,y=210)










win.mainloop()