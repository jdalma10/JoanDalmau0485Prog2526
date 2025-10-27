#44. Suposant que hem introduït una cadena per teclat que representa una frase (paraules separades per espais), realitza un programa que compti quantes paraules té.
comptadorParaules = 1

cadena = input ("Cadena: ")
while len(cadena)== 0:
    cadena = input ("Cadena: ")

# M'asseguro que no hi hagi espais en blanc al principi i final
cadena = cadena.strip()

for lletra in cadena:
    if lletra == " ":
        comptadorParaules +=1

print(comptadorParaules)

