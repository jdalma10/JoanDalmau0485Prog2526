PREU_INICIAL = 0.75

preu = 0
categoria = input("Posa la categoria (A/B): ")
calibre = int(input("Posa el calibre (1/2): "))
kilos = float(input("Posa la quantitat en kilos: "))


if categoria == 'A' or categoria == 'a':
    if calibre == 1:
        preu = PREU_INICIAL + 0.3
    elif calibre == 2:
        preu = PREU_INICIAL + 0.2
    else:
        print("Calibre erroni.") 
elif categoria == 'B' or categoria == 'b':
    if calibre == 1:
        preu = PREU_INICIAL - 0.3
    elif calibre == 2:
        preu = PREU_INICIAL - 0.5
    else:
        print("Calibre erroni.") 
else:
    print("Categoria errònia.")

if preu != 0:
    print("ha de pagar "+ preu*kilos+".")
