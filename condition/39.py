input = input("Enter number: ")
if len(input) == 4:
    Num = ''
    for i in input:
        if i == '1':
            Num += i
else:
    print("wrong")

print(Num)
