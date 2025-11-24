llista = []
posicio = 100

for i in range(3):
    llista.append(input("Valor: "))


valor = input("Valor a buscar: ")


for i in range(3):
    if llista[i] == valor:
        posicio = i
        break

if posicio != 100:
    print(f"Element trobat  la posicio: {i}")
else:
    print(f"Element no trobat ")