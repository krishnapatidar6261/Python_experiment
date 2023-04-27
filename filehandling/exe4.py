a=2
b=0
l=[1,2,3,4]
try:
    c=a/b
    print(l[6])
    with open("not.txt","r") as f:
        print("file found")
except ZeroDivisionError:
    print("divisijon by 0 not possible")
except listIndexOutOfRange:
    print("list index given by u not found")