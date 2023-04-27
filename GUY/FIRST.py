from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("My application")
root.iconbitmap('GUY\kpp.ico')
lbl=Label(root,text="Name:",font=("arial",16),bg="blue",fg="pink",borderwidth="2",relief="ridge",width="20")
#lbl.place(x=10,y=30)
lbl.place(x=2,y=2)
lbl2=Label(root,text="Branch:",bg="blue",fg="pink")
lbl2.place(x=2,y=35)


photo1=PhotoImage(file="GUY\jpg.png")
lbl3=Label(root, image=photo1)
lbl3.place(x=5,y=70)



root.resizable(False,False)
#root.attributes("-alpha",0.3)



root.mainloop()
