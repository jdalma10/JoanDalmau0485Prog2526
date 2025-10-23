#39. Algorisme que llegeixi nombres enters fins trobar 0,
#  i ens mostri el màxim, el mínim i la mitjana de tots ells.
#  Pensa com haurem d'inicialitzar les variables.

num = int(input("Posa un nombre: "))
suma = 0
quant = 0
max = num
min = num

while num != 0:
    suma += num
    quant += 1
    if num > max:
        max = num
    if num < min:
        min = num
        
    num = int(input("Posa un nombre: "))

print(f"Mitjana: {suma/quant}")
print(f"Max: {max}, Min: {min}")

