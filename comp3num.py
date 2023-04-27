a=input("enter first number a:")
b=input("enter second number b:")
c=input("enter third number c:")
if(a>b and a>c):
    print("a is greater than b and c")
elif(c>b and c>a):
    print("c is greater than a and b")
else:
    print("b is greater than a and c")