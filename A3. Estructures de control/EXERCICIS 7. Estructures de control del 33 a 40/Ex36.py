# 36. Algorisme que determini quina és la primera vocal 
# que trobem en una frase.

frase = input("Frase: ")
vocals = ['a','e','i','o','u']
trobat = False

for lletra in frase:
    if lletra in vocals:
        trobat = True
        print(lletra)
        primera = lletra
        break  #Nomes volem una, no cal fer més iteracions

if not trobat:  
    print("No hi ha vocals")


""" if primera in locals:
    print(primera)
else:
    print("No hi ha vocals") """