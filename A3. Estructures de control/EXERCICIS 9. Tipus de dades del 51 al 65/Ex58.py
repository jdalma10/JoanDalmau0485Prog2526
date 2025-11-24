llistaMesos = ["Gener", "Febrer", "Març"]
llistaIngressos = []
trobat = False
posicio = 0

for i in range(12):
    llistaIngressos.append(float(input("Posa el sou: ")))

buscar = float(input("Quantitat a buscar: "))

for i in range(12):
    if llistaIngressos[i] == buscar:
        trobat = True
        print(f"El Joan ha cobrat {buscar} € el mes de {llistaMesos[i]}")
        

if trobat:
    pass
else:
    print("no trobat")
