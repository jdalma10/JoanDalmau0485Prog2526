for i in range(4):
    for j in range(4):
        if i == 0 or i == 3:
            print("*", end = "")
        elif i == 1 or i == 2: # else
            if j == 0 or j== 3:
                print("*", end = "")
            else:
                print(" ", end = "")
    print()
