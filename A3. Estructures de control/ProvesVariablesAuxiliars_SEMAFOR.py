# Determinar si es troba una ñ
cadena = "El meu cosí és ñove."

# Declaració de la variavble semàfor.
hiHaEñe = False

for i in range(len(cadena)):
    if cadena[i] == 'ñ':
        # Activar semafor
        hiHaEñe = True
        posicio = i 

if hiHaEñe:
    print (f"Si, hi ha una ñ a la posicio  {posicio}")
else:
    print("No hi ha ñ")