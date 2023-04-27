class student:

    def get(self,name,branch):

         self.name=name
         self.branch=branch
        
    def set(self):
         print("student name is: ",self.name)
         print("student branch is: ",self.branch)


p1=student()
p1.get(
     input("Enter name of the student: "),
     input("Enter name of the student branch: ")
)

p1.set()