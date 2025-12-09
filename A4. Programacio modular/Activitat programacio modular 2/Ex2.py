temperatures = [22.5, 19.0, -100, 25.3, 18.7, -100, 21.0]
temperatures2 = []

def isError(temp):
    if temp == -100:
        return True
    else:
        return False
    
def convert(temp):
    return round(temp * 1.8 + 32, 2)

def filtra(llista):
    novaLlista = []
    for l in llista:
        if isError(l):
            novaLlista.append("Error")
        else:
            far = convert(l)
            novaLlista.append(far)
       
    return novaLlista

temperatures2 = filtra(temperatures)
print(temperatures2) 
