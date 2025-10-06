# 8. Escriu un programa que generi cinc números decimals aleatoris entre 0 i 1, 
# i els  mostri en la mateixa linia, 
# separats per guions, no es poden utilitzar llistes.

import random

float1 = format(random.random(), ".2f")
float2 = format(random.random(), ".2f")
float3 = format(random.random(), ".2f")
float4 = format(random.random(), ".2f")
float5 = format(random.random(), ".2f")

cadena = str(float1) +"-"+ str(float2) + "..."

print(cadena)