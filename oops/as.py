class employee:
  def __init__(self,name,id):
    self.__name=name
    self.__id=id

  def getdata(self):
   print(self.__name)
   print(self.__id)

e=employee("kp",123)
e.getdata()
e.__name="naman"
e.__id=1233446789
e.getdata()
print(e.__name)
print(dir(e))
#print(_employee__name)