with open("file.txt","r") as f:
    #print(f.read())
   # print(f.readlines(3))
    lines=len(f.readlines())
    print(lines)
    a=1
    while a<=lines:
       print(f.readline())
       #print(f.readline())
       a=a+1
   # print(lines)