class student:
    def __init__(self, name, branch, enroll):
        self.name = name
        self.branch = branch
        self.enroll = enroll
    def info(self):
        print("Student name is: ",self.name)
        print("Student branch is: ",self.branch)
        print("Student enroll is: ",self.enroll)

class MST(student):
    def __int__(self, name, branch, enroll):
        super().__init__(name, branch, enroll)

    def __init__(self, sub1_1, sub2_1):
        
        self.sub1_1 = sub1_1
        self.sub2_1 = sub2_1
    
    def mstmarks(self):
        self.totalm = self.sub1_1+ self.sub2_1
        print("Total marks of mst is: ", self.totalm)

    def resultmst(self):
        self.resultper = self.totalm / 2
        print("total % of mst marks: ", self.resultper)
    

class EST(student):
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
class final(MST,EST):
    def __init__(self, sub1_1, sub2_1,sub1,sub2):
        super(MST).__init__(sub1_1, sub2_1),
        super(EST).__init__(sub1,sub2)

    #super().info()
    def total(self):
        self.subject1ttl=self.sub1+ self.sub1_1
        self.subject2ttl=self.sub2+self.sub2_1
        self.bothsub=self.subject1ttl+self.subject2ttl
        print("Total Number of  sub1: ",self.subject1ttl)
        print("Total Number of sub2: ",self.subject2ttl)
        print("Total Number of sub1+sub2: ",self.bothsub)

    def fpersantage(self):
        self.finalper=self.bothsub/2
        print("Final persantage of the subject is: ",self.finalper)

s = student(
    name=input("Enter the name of Student: "),
    branch=input("Enter the name of the Branch: "),
    enroll=input("Enter the Enrollment of the Student: ")
)

#f=final()
def Echoice():
    e = EST(
        sub1=int(input("Enter EST marks of Python: ")),
        sub2=int(input("Enter EST marks of java: "))
    )

    while (True):
        print("Enter number for diffrent task on EST:")
        print("1. EST Total Marks    2. Result of EST marks in %")
        print("3. both 1 and 2       4.exit")
        print("5. Enter fozr give the MST marks: ")
        print("6. For Final result")
        a = input("Enter number: ")
        if a =="1":
            e.estmarks()
        elif a =="2":
            e.resultest()
        elif a =="3":
            e.estmarks()
            e.resultest()
            while(True):
               
               b=input("If you want to Enter MST marks Yes or NO: ")
               if b=="yes" or b=="YES":
                   Mchoice()
                   
               elif b=="NO" or b=="no":
                   break
               else:
                   print("Invalid Choice")
               break
        elif a =="4":
            break
        elif a=="5":
            Mchoice()
            while(True):
                      print("if you want to final result of the marks EST or MST: ")
                      fr=input("YES or NO: ")
                      if fr=="YES"or fr=="yes":
                          f=final()
                          f.info()
                          f.fpersantage()
                          f.total()
                          f.estmarks()
                          f.mstmarks()
                          f.resultest()
                          f.resultmst()
                          break
                      elif fr=="NO"or fr=="no":
                          break
                      else:
                          print("Invalid Choice")
        elif a=="6":
                   #f=final()
                   f.info()
                   f.fpersantage()
                   f.total()
                   f.estmarks()
                   f.mstmarks()
                   f.resultest()
                   f.resultmst()
                   break
        else:
            print("Invalid Choice")

def Mchoice():
          m = MST(
              sub1_1=int(input("Enter MST exam marks of Python: ")),
              sub2_1=int(input("Enter MST exam marks of Java: "))
          )
      
          while (True):
              print("Enter number for diffrent task on MST:")
              print("1. MST Total Marks    2. Result of MST marks in % ")
              print("3. both 1 and 2       4.exit")
              print("5.Enter for EST marks")
              print("")
              print("6. Final result")
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
                 
                  while(True):
                      print("if you want to final result of the marks EST or MST: ")
                      fr=input("YES or NO: ")
                      if fr=="YES"or fr=="yes":
                          f=final()
                          f.info()
                          f.fpersantage()
                          f.total()
                          #f.estmarks()
                          #f.mstmarks()
                          #f.resultest()
                          #f.resultmst()
                          
                      elif fr=="NO"or fr=="no":
                          break
                      else:
                          print("Invalid Choice")
              elif c=="6":
                   f=final()
                   f.info()
                   f.fpersantage()
                   f.total()
                   f.estmarks()
                   f.mstmarks()
                   f.resultest()
                   f.resultmst()
                          
              else:
                  print("Invalid Choice")
print("Enter you want to give the number of exam : ")
k = input("EST Exam or MST exam: ")
while(True): 
  if k == "EST" or k == "est":
  
      Echoice()
      break
        
  elif k == "MST" or k == "mst":
         Mchoice()
         break
  else:
      print("Invlid Choice")
  