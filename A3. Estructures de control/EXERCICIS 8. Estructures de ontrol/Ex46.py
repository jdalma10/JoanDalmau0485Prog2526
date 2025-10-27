paraula = input("enter your name: ")
paraulaReves = ""


for i in range(len(paraula)-1, -1, -1):
    paraulaReves += paraula[i]


for ll in paraula:
    paraulaReves = ll + paraulaReves

print(paraulaReves)