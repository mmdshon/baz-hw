Number1 = int(input("Enter Number: "))
sum_Zero = 0
num_str = str(Number1)
for zero in num_str:
    if zero == '0':
        sum_Zero += 1

print (sum_Zero)
