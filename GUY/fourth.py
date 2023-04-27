from tkinter import*
win=Tk()
win.geometry("500x500")
frm=Frame(win,height=100,width=300,relief="groove",borderwidth=2,bg="green")
frm.pack()
lbl=Label(frm,text="Enter your name")
lbl.pack(side="left")

e=Entry(frm)
e.pack(side="right")
win.mainloop()