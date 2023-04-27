class EST:

    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def totalmarks(self):
        self.total=self.sub1+self.sub2
        print("Total EST marks is:",self.total)

    def outof(self,ESToutof):
        self.outof1=ESToutof


class MST:

    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def totalmarks(self):
        self.total= self.sub1 + self.sub2
        print("Total EST marks is:",self.total)

    def outof(self, ESToutof):
        self.outof1 = ESToutof

print("Enter you want to give the number of exam : ")
a=input("EST Exam or MST exam: ")

if a=="EST" or "est":
    e1=EST(
        sub1=int(input("sub1 marks: ")),
        sub2=int(input("sub1 marks: "))

    )
elif a=="MST"or "mst":

    m1=MST(
        sub1=int(input("sub1 marks: ")),
        sub2=int(input("sub1 marks: "))
    )
    m1.totalmarks()

