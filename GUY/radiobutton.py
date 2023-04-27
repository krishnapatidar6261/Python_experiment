from tkinter import *
from tkinter.messagebox import *

win=Tk()
win.geometry("500x500")

def SelectSize():
    t=size.get()
    showinfo("size",f"your size is: {t}",)

lbl1=Label(win, text="select your size")
lbl1.grid(row=0, column=0, columnspan=2)

size=StringVar(win,"0")


r1=Radiobutton(win,text="small",variable=size,value="Small")
r2=Radiobutton(win,text="medium",variable=size,value="Medium")
r3=Radiobutton(win,text="large",variable=size,value="Large")

r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

select=Button(win,text="select", command=SelectSize)
select.grid(row=4,column=0)




win.mainloop()
