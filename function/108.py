def Is_aval(numbers):
    count = 0
    is_aval = True
    for i in numbers :
        for a in range(2,i):
            if i % a == 0:
                is_aval = False
                break
        if is_aval == True and i != 1:
            count += 1
    return count

Input_Numbers = []
for i in range(5):
    Input_Numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
print(Is_aval(Input_Numbers))