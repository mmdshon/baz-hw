Input = int(input("Enter a number: "))

if Input >= 1 and Input <= 7:
    print("first week")
elif Input >= 8 and Input <= 14:
    print("second week")
elif Input >= 15 and Input <= 21:
    print("third week") 
elif Input >= 22 and Input <= 28:
    print("fourth week")
elif Input >= 29 and Input <= 30:
    print("fifth week")
else:
    print("wrong")
