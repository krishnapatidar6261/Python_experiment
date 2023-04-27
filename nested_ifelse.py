a=int(input("enter number to check even and divided by 4: "))

if(a%2==0):
    
        if(a%4==0):
            print("given number is even number and divided by 4")
        elif(a%2==0):
            print("number is even but does not divide by 4")
        else:
            print("number does not divided by 4")
    
else:
    print("number is does not even and divided by 4")