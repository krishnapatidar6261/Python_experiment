class student:
    def __init__(self, name, branch, enroll):
        self.name = name
        self.branch = branch
        self.enroll = enroll


class MST:
    def __int__(self, name, branch, enroll):
        super().__init__(name, branch, enroll)

    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def mstmarks(self):
        self.totalm = self.sub1 + self.sub2
        print("Total marks of mst is: ", self.totalm)

    def resultmst(self):
        self.resultper = self.totalm / 2
        print("total % of mst marks: ", self.resultper)


class EST:
    def __int__(self, name, branch, enroll):
        super().__init__(name, branch, enroll)

    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def estmarks(self):
        self.totalm = self.sub1 + self.sub2
        print("Total marks of est is: ", self.totalm)

    def resultest(self):
        self.resultper = self.totalm / 2
        print("total % of est marks: ", self.resultper)


s = student(
    name=input("Enter the name of Student: "),
    branch=input("Enter the name of the Branch: "),
    enroll=input("Enter the Enrollment of the Student: ")
)


def Echoice():
    e = EST(
        sub1=int(input("Enter EST marks of Python: ")),
        sub2=int(input("Enter EST marks of java: "))
    )

    while (True):
        print("Enter number for diffrent task on EST:")
        print("1. EST Total Marks    2. Result of EST marks in %")
        print("3. both 1 and 2       4.exit")
        print("5. Enter for give the MST marks: ")
        a = input("Enter number: ")
        if a == "1":
            e.estmarks()
        elif a == "2":
            e.resultest()
        elif a == "3":
            e.estmarks()
            e.resultest()
            while(True):
               
               b=input("If you want to Enter MST marks Yes or NO: ")
               if b=="yes" or b=="YES":
                   Mchoice()
                   break
               elif b=="NO" or b=="no":
                   break
               else:
                   print("Invalid Choice")
        elif b == "4":
            break
        elif b=="5":
            Mchoice()
        else:
            print("Invalid Choice")

def Mchoice():
          m = MST(
              sub1=int(input("Enter MST exam marks of Python: ")),
              sub2=int(input("Enter MST exam marks of Java: "))
          )
      
          while (True):
              print("Enter number for diffrent task on MST:")
              print("1. MST Total Marks    2. Result of MST marks in % ")
              print("3. both 1 and 2       4.exit")
              print("5.Enter for EST marks")
              c = input("Enter number: ")
              if c =="1":
                  m.mstmarks()
              elif c =="2":
                  m.resultmst()
              elif c=="3":
                  
                  m.mstmarks()
                  m.resultmst()

                  while(True):
               
                      b=input("If you want to Enter EST marks Yes or NO: ")
                      if b=="yes" or b=="YES":
                          Echoice()
                          break
                      elif b=="NO" or b=="no":
                          break
                      else:
                          print("Invalid Choice")
              elif c =="4":
                  break
              elif c=="5":
                  Echoice()
              else:
                  print("Invalid Choice")
print("Enter you want to give the number of exam : ")
a = input("EST Exam or MST exam: ")
while(True): 
  if a == "EST" or a == "est":
  
      Echoice()
      break
        
  elif a == "MST" or a == "mst":
         Mchoice()
         break
  else:
      print("Invlid Choice")
  