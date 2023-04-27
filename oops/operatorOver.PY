class add:
    def __init__(self,x):
        self.x=x

    def __add__(self,tamp):
        return self.x+tamp.x
    
o1=add(3)
o2=add(4)
print(o1+o2)