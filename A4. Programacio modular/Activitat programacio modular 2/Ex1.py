temperatures = [22.5, 19.0, -100, 25.3, 18.7, -100, 21.0]
temperatures2 = []


def filtra(llista):
    novaLlista = []
    for l in llista:
        if l != -100:
            novaLlista.append(l)
    return novaLlista

temperatures2 = filtra(temperatures)

""" def isError(temp):
    if temp == -100:
        return True
    else:
        return False


for t in temperatures:
    if isError(t):
        pass
    else:
        temperatures2.append(t)

print(temperatures2) """
