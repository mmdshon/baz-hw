import math
N_Number = int(input("Enter N number: "))
Input_Number = []
fact = []

for i in range(N_Number):
    Input_Number.append(int(input("Enter Number" + str(i + 1) + " :")))
for i in Input_Number:
    fact.append(math.factorial(i))
for i in range(len(Input_Number)):
    print(f"{Input_Number[i]} != {fact[i]}")
