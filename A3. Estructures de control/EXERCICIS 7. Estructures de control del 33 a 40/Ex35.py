#35. Dissenya un algorisme corresponent a un 
# programa que donada una frase, determini si té més
#  caràcters “b” que “c”.

frase = input("Frase: ")
trobat = False
comptadorB = 0
comptadorC = 0
for lletra in frase:
    if lletra == 'B' or lletra == 'b':
        comptadorB += 1
    elif lletra == 'C' or lletra == 'c':
        comptadorC += 1
    else:
        pass

if comptadorB > comptadorC:
    print("Hi ha mes B")
elif comptadorB < comptadorC:
    print("Hi ha mes C")
