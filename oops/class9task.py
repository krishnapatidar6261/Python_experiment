class vip:
    university="Mandsaur University"

    def vip2(self,name,roll):
        self.name=name
        self.roll=roll
    def vipget(self):
        print(self.name)
        print(self.roll)
        print(self.university)

s=vip()
s.vip2(
    name=input("name: "),
    roll=input("roll: ")
)
s.vipget()