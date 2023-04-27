#method or function overloading
#same function name with diffrent parameter or work

def add(a,b):
    c=a+b
    print(c)

def add(a,b,c=1):
    d=a+b+c
    print(d)

add(10,20)
add(10,20,30)
