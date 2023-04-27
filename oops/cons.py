class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal 
    
    def getdata(self):
        print(self.name)
        print(self.sal)


e=employee("aachal",50000)
e.getdata()