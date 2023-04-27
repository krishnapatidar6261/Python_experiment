class person:
    def getData(self,name,phone):
        print("your name is : ",name)
        print("your number is: ",phone)



name=input("enter your name : ")
phone=int(input("Enter you phone: "))
p1=person()
p1.getData(name,phone)