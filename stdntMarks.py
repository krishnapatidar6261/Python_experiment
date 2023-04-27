m=int(input("enter marks of Maths subject: "))
p=int(input("enter marks of Physics subject:"))
c=int(input("enter marks of Chemistry subject: "))
h=int(input("enter marks of Hindi subject: "))
e=int(input("enter marks of English subject: "))
out_of=int(input("enter out of marks of all subject:"))

total=m+p+c+h+e

avg=total/5
print("average of the given marks is: ",avg)
out_of=out_of*5
per=(total/out_of)*100
print("percentage of given marks is: ",per)