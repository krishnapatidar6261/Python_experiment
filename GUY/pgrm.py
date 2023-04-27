from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("800x800")


def showtext():
    p=text1.get()
    lbl1.configure(text=p)
text1=Entry(win)
text1.pack()
lbl1=Label(win,text="click ")
lbl1.pack()
btn=Button(win,text="click",command=showtext)
btn.pack()





win.mainloop()