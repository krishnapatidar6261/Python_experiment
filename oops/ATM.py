class HDFC:
       
    def information(self,name,acno):
        self.name=name
        self.acno=acno
        self.bal=5000
    def withdr(self,withd):
        self.bal-=withd

    def diposite(self,dipos):
        self.bal+=dipos             

class SBI:
       
    def information(self,name,acno):
        self.name=name
        self.acno=acno
        self.bal=5000
    def withdr(self,withd):
        self.bal-=withd

    def diposite(self,dipos):
        self.bal+=dipos             

a=input("Which the name of the bank:: SBI or HDFC ")

if a=="HDFC" or "hdfc":
       hd=HDFC()
       hd.information("kp",123456)
       hd.withdr(200)
       hd.diposite(800)

elif a=="SBI"or "sbi":
       sb=SBI()
       sb.information("chandrakala",143)
       sb.withdr(400)
       sb.diposite(4000)
else:
       print("invlid choice")


