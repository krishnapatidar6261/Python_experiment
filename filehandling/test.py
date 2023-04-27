with open("one.txt","r") as f:

    a=f.read()
    #print(a)

with open("two.txt","w") as w:
       w.write(a)