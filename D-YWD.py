days=int(input("Enter days to calculate year,week,day: "))

year=days//365
month=(days%365)//30
week=(days%365)//7
day=(days%365)%7
#ghanta =(days%365)%24

print("year,week,day of the given days is: ",year,month,week,day)