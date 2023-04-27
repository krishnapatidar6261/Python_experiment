count=0
with open("file.txt","r") as f:
    while True:
        line=f.readline()
        if line=="":
            break
        else:
            t=line.split()
            count=count+len(t)
    print(count)