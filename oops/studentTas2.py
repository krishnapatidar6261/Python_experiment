class student:
    def __init__(self,name,branch,enroll):
        self.name=name
        self.branch=branch
        self.enroll=enroll
class MST:
    def __int__(self,name,branch,enroll):
        super().__init__(name,branch,enroll)


    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2

    def mstmarks(self):
        self.totalm=self.sub1+self.sub2
        print("Total marks of mst is: ",self.totalm)

    def resultmst(self):
        self.resultper=self.totalm/2
        print("total % of mst marks: ",self.resultper)

class EST:
    def __int__(self,name,branch,enroll):
        super().__init__(name,branch,enroll)

        
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2

    def estmarks(self):
        self.totalm=self.sub1+self.sub2
        print("Total marks of est is: ",self.totalm)

    def resultest(self):
        self.resultper=self.totalm/2
        print("total % of est marks: ",self.resultper)

s=student(
    name=input("Enter the name of Student: "),
    branch=input("Enter the name of the Branch: "),
    enroll=input("Enter the Enrollment of the Student: ")
)


print("Enter you want to give the number of exam : ")
a=input("EST Exam or MST exam: ")

if a=="EST" or a=="est":
    e = EST(
        sub1=int(input("Enter marks of sub1: ")),
        sub2=int(input("Enter marks of sub2: "))
    )

    while (True):
        print("Enter number for diffrent task on EST:")
        print("1. EST Total Marks    2. Result of EST marks in %")
        print("3. both 1 and 2       4.exit")
        a = int(input("Enter number: "))
        if a == 1:
            e.estmarks()
        elif a == 2:
            e.resultest()
        elif a==3:
            e.estmarks()
            e.resultest()
            break
        elif a==4:
            break
        else:
            print("Invalid Choice")

elif a=="MST"or a=="mst":
    m= MST(
        sub1=int(input("Enter marks of Python: ")),
        sub2=int(input("Enter marks of Java: "))
    )

    while (True):
        print("Enter number for diffrent task on MST:")
        print("1. MST Total Marks    2. Result of MST marks in % ")
        print("3. both 1 and 2       4.exit")
        a = int(input("Enter number: "))
        if a == 1:
            m.mstmarks()
        elif a == 2:
            m.resultmst()
        elif a==3:
            m.mstmarks()
            m.resultmst()
            break
        elif a==4:
            break
        else:
            print("Invalid Choice")


else:
    print("Invlid Choice")
