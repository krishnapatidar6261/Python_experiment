with open("w.txt","w") as f:
    a=int(input("How many friends"))
    for i in range(a):
        name=input("name: ")
        f.write(name)
        f.write("\n")