# 45. Si tenim una cadena amb un nom i cognoms, 
# realitzar un programa que mostri les inicials en majúscules.
name = input("enter your name: ")

posicio = 0
inicialCognom=""

intialName = name[0]

for i in range(len(name)):
    if name[i] == ' ':
        inicialCognom = name[i+1]
        break  


print(intialName.upper(), inicialCognom.upper())

