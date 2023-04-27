with open("file.txt","r") as f:
     while(True):
        line=f.readline()
        if(line==""):
           break
        else:
           print(line)

