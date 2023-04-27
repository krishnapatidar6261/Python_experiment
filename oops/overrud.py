class one:
    def show(self):
        print("one")

class two:
    def show(self):
        print("two")
class three(one,two):
    def disply(self):
        print("no use")

temp=three()
temp.show()