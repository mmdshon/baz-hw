Input_Number = []

for i in range(3):
    Input_Number.append(int(input("Enter Number " + str(i) + " ")))

Max = Input_Number[0]

for i in Input_Number:
    if i > Max:
        Max = i

print(Max)