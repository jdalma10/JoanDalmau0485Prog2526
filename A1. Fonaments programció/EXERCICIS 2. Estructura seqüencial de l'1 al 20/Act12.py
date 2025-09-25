""" 12. Demana a l'usuari dos parells de nombres x1, y1 i x2, y2,
 que representin dos punts en el pla. Calcula i mostra la distància entre ells.
 """

x1 = int(input("Quin es el num de 1?:"))
y1 = int(input("Quin es el num de 1.2?:"))
x2 = int(input("Quin es el num de 2?:"))
y2 = int(input("Quin es el num de 2.1?:"))

catet1 = x2-x1
catet2 = y2-y1
h = (catet1**2+catet2**2)**0.5

print ("La distancia es:",h)

