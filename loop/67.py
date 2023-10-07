# Input_Number = int(input("Enter Number: "))

# Nums = []
# fib1 = 0
# fib2 = 1
# count = 0

# while fib2 <= 100000:   
#     if fib2 % Input_Number == 0:
#         Nums.append(fib2)
#     fib3 = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib3
# print(Nums)

number = int(input("Enter a Number :"))
fb1 = 0
fb2 = 1
Nums = []
while fb2 < 99999:
    if fb2 % number == 0:
        Nums.append(fb2)
    fb3 = fb1 + fb2
    fb1 = fb2
    fb2 = fb3
print(Nums)