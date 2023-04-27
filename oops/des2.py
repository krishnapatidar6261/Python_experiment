class employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id

  def getdata(self):
   print(self.name)
   print(self.id)

e=employee("kp",123)
e.getdata()
#e.name="naman"
#e.getdata()
#print(e.id)
