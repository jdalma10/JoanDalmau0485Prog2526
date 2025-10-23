# 38. Tenint en compte que la clau és "eureka", 
# escriure un algorisme que ens demani una clau.
# Únicament tenim 3 intents per encertar, 
# si fallem els 3 intents ens mostrarà un missatge 
# indicant-nos que hem esgotat els intents.
# Si encertem la clau, sortirem directament.

MAX_INTENTS = 3
intents = 0

while intents < MAX_INTENTS:
    codi = input("Contrasenya: ")
    if codi != 'Eureka':
        intents += 1
    else:
        break

if intents == 3:
    print("intents esgotats")
