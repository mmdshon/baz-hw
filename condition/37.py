Input_Number = []

for i in range(3):
    Input_Number.append(int(input("Enter Number " + str(i) + " ")))

Input_Number.sort(reverse=True)

print(Input_Number)