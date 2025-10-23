# 34. Dissenya un algorisme corresponent a un programa que donada una 
# frase acabada, compti el nombre de caràcters que hi apareixen a 
#   partir de la primera “a”.
""" primeraA = -1

frase = input("Frase: ")

for i in range(len(frase)):
    if frase[i] == 'a':
        primeraA = i
        break

if primeraA != -1:
    print(len(frase) - primeraA -1) """


frase = input("Frase: ")
trobat = False
comptador = 0
for i in range(len(frase)):
    if trobat:
        comptador += 1
    else:
        if frase[i] == 'a':
            trobat = True

print(comptador)