nota1 = float(input("Introdueix la primera nota parcial: "))
nota2 = float(input("Introdueix la segona nota parcial: "))
nota3 = float(input("Introdueix la tercera nota parcial: "))

examenfinal = float(input("Introdueix la nota de l'examen final: "))
treballfinal = float(input("Introdueix la nota del treball final: "))

mitjanaparcials = (nota1 + nota2 + nota3) /3

notafinal = (mitjanaparcials * 0.55) + (examenfinal * 0.30) + (treballfinal * 0.15)

print(f"La nota final dels Algorismes és: {notafinal}")