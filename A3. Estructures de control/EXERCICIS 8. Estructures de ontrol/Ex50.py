# 50. Introduir una cadena de caràcters i indicar si és un palíndrom. 
# Una paraula palíndrom és aquella que es llegeix igual endavant que 
# enrere.


cadena = input ("Cadena: ")
palidrom = True


for i in range(len(cadena)//2):
    if cadena[i] != cadena [len(cadena)-1 -i]:
        palidrom = False
        break

print(palidrom)