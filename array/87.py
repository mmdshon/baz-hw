N_Input = int(input("Enter n number: "))
Input_Numbers = []

for i in range(N_Input):
    Input_Numbers.append(int(input("Enter number " + str(i) + " ")))

Input_Numbers.sort(reverse=True)

print(Input_Numbers)