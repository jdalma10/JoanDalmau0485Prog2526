""" 16. Dos vehicles viatgen a diferents velocitats (v1 i v2) 
i estan distanciats per una distància d.
El que està darrere viatja a una velocitat més gran.
Es demana fer un algoritme per ingressar la distància 
entre els dos vehicles (km) i les seves respectives velocitats 
(km / h) i amb això determinar i mostrar en què temps (minuts)
arribarà el vehicle més ràpid a l'altre. """

# t = d/ dif vel

dist = int(input("Dist. en km "))
v1 = int(input("v1 en km/h"))
v2 = int(input("v2 en km/h"))

t_en_hores = dist / (v1 - v2)  

# t = 100 km/ 10(km/h) = 100 / 10 (1/h) = 10 / (1/h) = 10h   ja que 1/ (1/2) = 1/0.5 = 2

t_minuts = t_en_hores * 60

