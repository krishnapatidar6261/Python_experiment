class req:
    def getdata(self,b,l):
        self.b=b
        self.l=l

    def calculate(self):
        self.area=self.b*self.l


    def show_area(self):
        print(self.area)

p1=req()
p1.getdata(
    b=int(input("enter req b: ")),
    l=int(input("enter req l: "))
)
p1.calculate()
p1.show_area()
