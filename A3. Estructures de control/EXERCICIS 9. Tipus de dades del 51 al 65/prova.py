noms = []
tels = []

while True:
    opcio = int(input("Opcio:"))

    if opcio == 1:
        noms.append(input("Nom:"))
        tels.append(input("Tel:"))
    elif opcio == 2:
        for i in range (len(noms)):
            print(f"{noms[i]}: {tels[i]}")
    elif opcio == 3:
        for i in range (len(noms)):
            if noms[i] == input("Cerca"):
                print(tels[i])
                break
    else:
        break