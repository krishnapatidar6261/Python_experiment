#check box 
#with the help of get method we can check the value of chekbox

from tkinter import*
root=Tk()
root.geometry("600x600")
check1=IntVar()
check2=IntVar()

def fun1():
    if check1.get() == 1 and check2.get() == 1:
        en.configure(text="You select python and java")
        #print("JAVA")
    elif check2.get()==1:
        en.configure(text="You selct python")
    elif check1.get()==1:
        en.configure(text="you selected java")
    
lbltitle=Label(root, text="Select programing")
lbltitle.grid(row=0,column=0,columnspan=2)

chkbtn1=Checkbutton(root,text="JAVA",onvalue=1,offvalue=0,command=fun1,variable=check1)
chkbtn1.grid(row=1, column=1)
chkbtn2=Checkbutton(root,text="Python",onvalue=1,offvalue=0,command=fun1,variable=check2)
chkbtn2.grid(row=2, column=1)

en=Label(root,text="")
en.grid(row=4,column=1)
root.mainloop()