""" #7. Realitza un algoritme que calculi la potència, per això demana per teclat la base i l'exponent. Poden ocórrer tres coses:
L'exponent sigui positiu, només has d'imprimir la potència.
L'exponent sigui 0, el resultat es 1.
L'exponent sigui negatiu, el resultat es 1 / potència amb l'exponent positiu. """

base = int(input("Introdueix la base: "))
exponent = int(input("Introdueix l'exponent"))

if exponent > 0:
    print("El resultat és: ", base ** exponent)
elif exponent == 0:
    print("El resultat és: 1")
else:
    print("El resultat és: ", 1/((base ** ((exponent ** 2)**0.5))))    # 1 / base ** abs(exponent)

if exponent == 0 :
    print(f"El resultat és ", 1)
          
else:
    print(f"El resultat és {base**exponent:.2f}")