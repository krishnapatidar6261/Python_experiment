class account:
    
       def __init__(self,name,acno,Phone):
              self.name=name
              self.acno=acno
              self.phone=Phone
              self.balance=1000
            
       def getinfo(self):
              print("Name of the Account holder: ",self.name)
              print("acount number of the Account holder: ",self.acno)
              print("Phone number of the Account holder: ",self.phone)

class savingsccount(account):
       itr_rate=4.0
       min_balace=1000

       def __init__(self,name,acno,Phone):
              super().__init__(name,acno,Phone)
       
       def dipo(self,dipammount):
              self.balance+=dipammount

       def withdr(self,withdra):
              self.balance-=withdra
              
       def checkbal(self):
              super().getinfo()
              print(self.balance)
      

s1=savingsccount(
       name=input("Enter your name: "), 
       acno=int(input("Enter you account")),
       Phone=int(input("Enter your phone number"))
)
s1.dipo(
       dipammount=int(input("Enter ammount for Diposite: ")
       )
)

#s1.getinfo()
s1.checkbal()