from tkinter import*

win=Tk()
win.geometry("800x800")
#win.columnconfigure(0,weight=1)
#win.columnconfigure(1,weight=1)
lbl=Label(win,text="Name")
lbl.grid(row = 0, column = 0)
entuname=Entry(win)
entuname.grid(row = 0, column = 1)


lblpws=Label(win,text="Password")
lblpws.grid(row = 1, column = 0)

entpwd=Entry(win)
entpwd.grid(row = 1, column = 1,pady=20,sticky=SE)

btnlogin=Button(win,text="Login")
btnlogin.grid(row = 2, column = 1,columnspan = 2)



win.mainloop()
