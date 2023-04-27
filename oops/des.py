class student:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("object destory")

    def showname(self,name):
        print(name)

s=student()
s.showname("ram")
r=s
r.showname("naman")

del s
del r