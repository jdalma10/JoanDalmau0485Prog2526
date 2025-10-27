iguals = True

while True:
    cadena =input ("Introdueix una frase: ")
    subcadena = input("Introdueix subcadena:")
    if len(cadena) >= len(subcadena):
        break

for i in len(subcadena):
    if cadena[i] != subcadena[i]:
        iguals = False
        break

