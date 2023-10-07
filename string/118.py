Input_Numebr = input("Enter Input_Number String: ")

for i in Input_Numebr:
    n = ord(i)
    if 48 <= n <= 57:
        print(n - 48)
