resultat = 0
while True:
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))

    if n1 == 0 and n2 == 0:
        break
    else:
        resultat += (n1+n2)

print(resultat)