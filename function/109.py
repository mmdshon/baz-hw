def Fact():
    Vorodi_n = int(input("Enter N number: "))
    final = []
    for i in range(Vorodi_n):
        Vorodi = int(input("Enter Number " + str(i) + " "))
        Fact = 1
        for i in range(1,Vorodi+1):
            Fact *= i
        final.append(f"{Vorodi} != {Fact}")
    return final
for i in Fact():
    print(i)