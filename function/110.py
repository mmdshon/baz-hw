def Sort_Number():
    N_Number = int(input("Enter N Number: "))
    Input_Number = []
    
    for i in range(N_Number):
        Input_Number.append(int(input("Enter numebr " + str(i) + " ")))

    final = sorted(Input_Number,reverse= True)
    return final

for i in Sort_Number():
    print(i)