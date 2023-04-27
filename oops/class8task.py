class circle:
    

    def setradius(self,radius):
        self.r=radius

    def getarea(self):
         self.area=3.14*self.r*self.r
    

    def perimeter(self):
         self.perimete=2*3.14*self.r

    def total(self):
        print("Radius is: ",self.r)
        print("Area is: ",self.area)
        print("perimeter is: ",self.perimete)

ar=circle()
ar.setradius(
    radius=int(input("Enter Radius: "))
)
ar.getarea()
ar.perimeter()
ar.total()