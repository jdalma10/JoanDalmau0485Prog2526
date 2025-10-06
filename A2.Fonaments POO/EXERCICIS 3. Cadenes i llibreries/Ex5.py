# Escriu un programa que mesuri quant temps triga
#  en executar-se una operació,# com per exemple 
# calcular l'arrel quadrada de 3 # números 
# diferents.Utilitza datetime.now() 
# per obtenir el temps abans i 
# després de l'operació, i resta’ls per 
# calcular el temps total d'execució.

# o importem la llibreria
import datetime, time
ara = datetime.datetime.now()

# o dins de la llibreria, la classe
from datetime import datetime

ara2 =datetime.now()
time.sleep(3)
despres =datetime.now()
print(ara2,despres)

diferencia = despres-ara2

print(diferencia.seconds)

print("Temps passat: " + str(despres-ara2))