#13. Realitza un programa que demani per teclat el resultat (dada sencer) obtingut a llançar un dau de sis 
# cares i mostri per pantalla el nombre en lletres (dada cadena) de la cara oposada a el resultat obtingut.

num = int(input("Introduïu el nombre del dau (1-6): "))

if num < 1 or num > 6:
    print("ERROR: nombre incorrecte.")
else:
    oposat = 7 - num  
    print(f"A la cara oposada hi ha el \"{oposat}\".")
