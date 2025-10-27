
cadena = input ("Cadena: ")
cadenaNova = ""


# Modificacio d'una cadena no permesa, necessitem crear nova cadena
for lletra in cadena:
    if lletra.isupper():
        cadenaNova += lletra.lower()
    else:
        cadenaNova += lletra.upper()


print(cadenaNova)

# Modificacio d'una llista mutable

lista = ['H','o','l','a']
cadena2 = "Hola"

for i in range(len(lista)):
    if lista[i].isupper():
        lista[i] = lista[i].lower()
        # cadena2[i] = cadena2[i].lower()   NO ES POT FER, CADENES SON NO MUTABLES
    else:
        lista[i] = lista[i].upper()