# Determinar quantes ñ trobem

cadena = "El meu cosí és ñove."

# Declaració i inicalitzaió del comptador
numeroEñes = 0

for i in range(len(cadena)):
    if cadena[i] == 'ñ':
        # Incrementar comptador
        numeroEñes = numeroEñes + 1
        # numeroEñes += 1

print (f"Hi ha {numeroEñes} ñ ")
