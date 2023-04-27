#Instance method    class method        static method


class student:
    university="meu"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def getinfo(self):
        print(self.name)
        print(self.roll)
        print(self.university)


s=student("krishna",123)
s.getinfo()
s1=student("hemnt",345)
s1.getinfo()
#a=s1.university="LNCT"
#print(a)

