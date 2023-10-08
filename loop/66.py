nums = []
for i in range(5):
    nums.append(int(input("enter number " + str(i + 1) + ": ")))
fib1 = 0
fib2 = 1
final = []
for i in nums:
    if i % 2 != 0:
        while fib2 < i:
            fib3 = fib2 + fib1
            fib1 = fib2
            fib2 = fib3
            if i == fib2:
                final.append(fib2)

print(final) 
