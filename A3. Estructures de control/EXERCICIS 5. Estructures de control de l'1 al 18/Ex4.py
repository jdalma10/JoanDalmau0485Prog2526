# 4. Crea un programa que demani a l'usuari dos nombres i mostri la seva divisió si el segon no és zero,
#  o un missatge d'avís en cas contrari.

n1 = float(input("Numero1:"))
n2 = float(input("Numero2:"))

if n2 == 0:
    print("Error")
else:
    print(n1/n2)