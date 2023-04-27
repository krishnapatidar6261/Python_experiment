p=int(input("enter principal: "))
r=int(input("enter rate: "))
t=int(input("enter time in month: "))

if(p>5000):
    si=(p*r*t)/100
    print(si)
else:
    print("your principal ammount is less than 5000")