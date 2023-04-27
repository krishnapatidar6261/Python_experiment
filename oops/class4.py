class product:
    def setdata(self,pname,qty,price):
        self.pname=pname
        self.qty=qty
        self.price=price
    def totalprice(self):
        self.total=self.qty*self.price

    def getdata(self):
        print(self.pname)
        print(self.qty)
        print(self.total)
p1=product()
p1.setdata("shampho",2,30)
p1.totalprice()
p1.getdata()
p2=product()
p2.setdata("sugar",2,40)
p2.totalprice()
p2.getdata()