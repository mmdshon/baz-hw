Input_Number = []
N_number = int(input("Enter N number: "))
count = 0
for i in range(N_number):
    Input_Number.append(int(input("Enter number " + str(i + 1) + " ")))

Input_Number_sorted = sorted(Input_Number)

for i in range(len(Input_Number)):
    if Input_Number_sorted[i] == Input_Number[i]:
        count += 1

if count == N_number:
    print("Yes")
else:
    print("No")