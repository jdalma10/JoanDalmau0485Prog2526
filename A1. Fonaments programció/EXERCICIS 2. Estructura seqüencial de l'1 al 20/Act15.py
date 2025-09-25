""" 15. Donades dues variables numèriques A i B, que l'usuari ha de teclejar, es demana realitzar un algoritme que intercanviï els valors de les dues variables 
i mostri que fa valen a al final les dues variables. """


a = int(input("Introdueix un nombre: "))
b = int(input("Introdueix un nombre: "))

# a,b = b,a


aux = a
a = b
b = aux

print(a,b)