# 2. Escriu un programa que generi una cadena de 
# 3 caràcters que inclogui lletres 
# (majúscules i minúscules) i números aleatoris.

import random 
from string import ascii_letters, digits

conjunt = ascii_letters + digits

# 3 caràcters que inclogui lletres 

cad= random.choice (conjunt)
cad+= random.choice (conjunt)
cad+= random.choice (conjunt)

# cad = random.choices(conjunt, k = 3)

print (cad)


