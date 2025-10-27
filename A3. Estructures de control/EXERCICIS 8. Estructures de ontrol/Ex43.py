#43. Demana una cadena i un caràcter per teclat (valida que sigui un caràcter) i mostra totes les vegades que apareix el caràcter en la cadena.
from string import printable
cadena = input ("Cadena: ")
caracter = input ("Carácter: ")
comptadorCaracter = 0


while len(caracter) != 1 and caracter.lower() not in (printable):
    print ("ERROR, hi ha més d'un carácter o no és un carácter")
    caracter = input ("Carácter: ")

for i in cadena: 
    if i.lower() == caracter.lower():
        comptadorCaracter +=1

print (f"Hi han {comptadorCaracter} '{caracter}' en {cadena}.")