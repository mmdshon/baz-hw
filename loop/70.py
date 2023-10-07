for i in range(56,1985):
    for a in range(1,i + 1):
        if i % a == 0:
            print(f"{i} = {a}")