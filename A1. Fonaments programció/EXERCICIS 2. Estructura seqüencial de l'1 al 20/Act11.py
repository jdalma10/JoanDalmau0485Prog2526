""" 11. Demana a l'usuari dos nombres i mostra la "distància" entre ells (el valor absolut de la seva diferència, 
de manera que el resultat sigui sempre positiu).
 """

nombre1 = float(input("Introdueix un nombre: "))
nombre2 = float(input("Introdueix un nombre: "))
distancia1= (nombre1-nombre2)
distancia2= (distancia1**2)**0.5

print ("la distancia entre ellos es: ",str(distancia2), "m")