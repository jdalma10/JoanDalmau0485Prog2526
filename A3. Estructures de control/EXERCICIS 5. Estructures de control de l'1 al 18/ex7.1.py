base = int(input("Introdueix la base: "))
exponent = int(input("Introdueix l'exponent"))

if exponent == 0 :
    print(f"El resultat és ", 1)
          
else:
    print(f"El resultat és {base**exponent:.2f}")