# 49. Realitzar un programa que comprovi si una cadena conté una subcadena. Les dues cadenes s'introdueixen per teclat.

cadena = input ("Cadena: ")
subcadena = input ("subadena: ")

n = len(cadena)
m = len(subcadena)
conte = False

for i in range(n - m + 1):
    if conte:
        break
    for j in range(m):
        if cadena[j+i]== subcadena[j]:
            if j == len(subcadena)-1:
                conte = True
            continue
        else:
            break


print(conte)
