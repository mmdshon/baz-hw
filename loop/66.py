Input_number = []
for i in range(100):
    Input_number.append(int(input("Enter number " + str(i+1) + " ")))

fib1 = 0
fib2 = 1
sum = 0

for i in Input_number:
    if i % 2 == 1:
        while fib2 < i:
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        if fib2 == i:
            sum += 1

print(sum)