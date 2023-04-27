class EST:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2

    def mstmarks(self):
        self.totalm=self.sub1+self.sub2
        print("Total marks of est is: ",self.totalm)

    def resultest(self):
        self.resultper=self.totalm/2
        print("total % of est marks: ",self.resultper)

e=EST(
    sub1=int(input("Enter marks of sub1: ")),
    sub2=int(input("Enter marks of sub2: "))
)
 while(True):
     print("Enter number for diffrent task on EST:")
     print("1. EST Total Marks    2. Result of EST marks in %")
     a=int(input("Enter number: "))
     if a==1:
        e.mstmarks()
     elif a==2
        e.resultest()
