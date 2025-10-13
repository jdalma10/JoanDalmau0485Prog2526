numAlumnes = int(input("Num alumnes:"))

if (numAlumnes >= 100): 
    preu = 65 * numAlumnes
elif (numAlumnes < 100 and numAlumnes >= 50):
    preu = 70 * numAlumnes
elif (numAlumnes < 50 and numAlumnes >= 30):
    preu = 95 * numAlumnes
else:
    preu = 4000

print ("L'autobus costa " + str(preu) + "€")
print(f" Cada alumne ha de pagar {preu/numAlumnes:.2f}")