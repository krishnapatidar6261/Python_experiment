class EST:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def estmarks(self):
        self.totalm=self.sub1+self.sub2
        print("Total marks of est is: ",self.totalm)


class MST:
    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def mstmarks(self):
        self.totalm = self.sub1 + self.sub2
        print("Total marks of mst is: ", self.totalm)

print("Enter you want to give the number of exam : ")
a=input("EST Exam or MST exam: ")


if a=="MST"or "mst":
    m= MST(
        sub1=int(input("Enter marks of sub1: ")),
        sub2=int(input("Enter marks of sub2: "))
    )
    while (True):
        print("Enter number for diffrent task on MST:")
        print("1. MST Total Marks    2. Result of MST marks in %   3.exit")
        a = int(input("Enter number: "))
        if a == 1:
            m.mstmarks()

if a=="EST" or "est":
    e = EST(
        sub1=int(input("Enter marks of sub1: ")),
        sub2=int(input("Enter marks of sub2: "))
    )
    while (True):
        print("Enter number for diffrent task on EST:")
        print("1. EST Total Marks    2. Result of EST marks in %")
        a = int(input("Enter number: "))
        if a == 1:
            e.estmarks()
else:
    print("Invlid Choice")