""" 14. Donat un nombre de dues xifres, 
dissenyi un algoritme que permeti obtenir el nombre invertit. 
Exemple, si s'introdueix 23 que mostri 32. """

num = int(input("Posa un num: "))

desenes = num // 10
unitats = num % 10

""" resultat = unitats *10 + desenes
print (type(resultat))

print (resultat) """

print(f"{unitats}{desenes}")
print (type(f"{unitats}{desenes}"))