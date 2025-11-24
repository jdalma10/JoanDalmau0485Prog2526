cadena = input("Nums separats per comes")
max = 0
min = 1000
posicioMax = 0
posicioMin = 0
suma = 0
total = 0 

for i in range(len(cadena)):
    if cadena[i] != ",":
        suma += int(cadena[i])
        total += 1

        if int(cadena[i]) > max:
            max = int(cadena[i])
            posicioMax = i

        if int(cadena[i]) < min:
            min = int(cadena[i])
            posicioMin = i

print (f"{max} a la {posicioMax} posicio" )
print (f"{min} a la {posicioMin} posicio" )
print(f"Mitjana : {suma/total}")