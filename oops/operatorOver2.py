class mul:
    def __init__(self,x):
        self.x=x

    def __mul__(self,tamp):
        return self.x*tamp.x
    
o1=mul(3)
o2=mul(4)
print(o1*o2)