from tkinter import*

win=Tk()

win.iconbitmap("kpp.ico")
win.geometry("500x500")

name=Label(win,text="Name: ",bg="pink", borderwidth=5)
name.place(x=2,y=4)
nameEnt=Entry(win,bg="white",borderwidth=5,fg="red",width=40)
nameEnt.place(x=70,y=4)

branch=Label(win,text="Branch: ",bg="pink",border=5)
branch.place(x=2,y=40)
branchEnt=Entry(win,bg="white",borderwidth=5,fg="red",width=40)
branchEnt.place(x=70,y=40)
enroll=Label(win,text="Enroll: ",bg="pink",border=5)
enroll.place(x=2,y=76)
enrollEnt=Entry(win,bg="white",borderwidth=5,fg="red",width=40)
enrollEnt.place(x=70,y=76)


win.mainloop()