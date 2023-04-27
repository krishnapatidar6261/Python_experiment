a=int(input("enter year to check leep year or not: "))

if a%4==0 or a%400==0:
    print("given year is leep year")
else:
    print("given year is not a leep year")