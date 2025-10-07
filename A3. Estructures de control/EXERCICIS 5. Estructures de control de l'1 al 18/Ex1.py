# 1. Algorisme que demani dos nombres i indiqui si el primer és més gran que el segon o no.

num1 = int(input("Primer nombre: "))
num2 = int(input("Segon nombre: "))

if num1 > num2:
    print("El primer nombre és més gran que el segon")

elif num2 > num1:
    print("El segon nombre és més gran")

else:
    print("Són el mateix nombre")