def Zoj():
    sum = 0
    for i in range(5):
        Input = int(input("Enter number" + str(i + 1) + ": "))
        if Input % 2 == 0:
            sum += 1

    return sum

print(Zoj())

