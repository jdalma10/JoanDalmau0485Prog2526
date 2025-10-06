#4. Escriu un programa que generi un color 
# aleatori en format RGB. 
# Cada component (R, G, B) 
# ha de ser un valor entre 0 i 255.

import random
# rang = range(256)  ==>> 0 i 255

numero1 = random.randint(0,255)
numero2 = random.randint(0,255) 
numero3 = random.randint(0,255) 

print(f"El seu numero és RGB({numero1}, {numero2}, {numero3}).")