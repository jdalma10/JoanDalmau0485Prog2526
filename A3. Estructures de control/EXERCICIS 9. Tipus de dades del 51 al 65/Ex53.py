llista = []
aprovats = 0
total = 0
nota = int(input("Nota: "))
while True:
    if nota == "":
        break
    else:
        # llista.append(nota)
        total +=1
        if nota >= 5:
            aprovats += 1

""" for i in llista:
    total +=1
    if i >= 5:
        aprovats += 1 """

print(f"Percentatge: {aprovats*100/total}")


    
    

