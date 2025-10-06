#9.Escriu un programa que generi una hora específica a l'atzar (per exemple, les 10:30:00) 
# i mostri quanta estona ha passat fins ara, en hores, minuts i segons.
import random
import datetime
hores = random.randint(0, 23)
minuts = random.randint(0, 59)
segons = random.randint(0, 59)
hora_aleatoria = datetime.time(hores, minuts, segons)

print("Hora aleatòria generada:", hora_aleatoria)
ara = datetime.datetime.now().time()
print("Hora actual:", ara)

diferencia = datetime.timedelta(hours=ara.hour - hores, minutes=ara.minute - minuts, seconds=ara.second - segons)
print("Temps transcorregut:", diferencia)
