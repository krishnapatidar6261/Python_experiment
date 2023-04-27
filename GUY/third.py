from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("800x800")
lbl1=Label(win,text="BCCCCCCCCCCCCCC  VVVVVVVVVVVV ",borderwidth="2",relief="solid",bg="pink",width="30",height="2")
lbl1.pack(ipadx=10,ipady=20)
lbl2=Label(win,text="BCCCCCCCCCCCCCC  VVVVVVVVVVVV ",borderwidth="2",relief="solid",bg="pink",width="30",height="2")
lbl2.pack(pady="20")

text1=Entry(win)
text1.pack()


win.mainloop()