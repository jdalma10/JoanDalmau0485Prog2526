llistaAsssig= []
llistaNotes = []

for i in range(5):
    llistaAsssig.append(input("Assig: "))
    llistaNotes.append(input("Nota: "))

for i in range(len(llistaNotes)):
    print(f"{llistaAsssig[i]}: {llistaNotes[i]}")
