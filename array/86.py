Input = int(input("enter n number: "))
Input_Numbers = []
for i in range(Input):
    Input_Numbers.append(int(input("Enter number " + str(i) + " : ")))

Max_num = Input_Numbers[0]

for i in Input_Numbers:
    if i > Max_num:
        Max_num = i

print(Max_num)