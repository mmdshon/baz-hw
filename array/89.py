Numbers = []
Not_Aval = []
for i in range(10):
    Numbers.append(int(input("Enter number " + str(i + 1) + ": ")))

for i in Numbers:
    for a in range(2,i-1):
        if i % a == 0:
            Not_Aval.append(i)
            break

print(Not_Aval)