import string

frase = input("Text a analitzar")

def contaCaracters (text):
    cont = 0
    for i in text:
        if i!=" ":
            cont += 1
    return cont

def contaParaules(text):
    contParaula = 1
    for i in text:
        if i==" ":
            contParaula += 1
    return contParaula 

def contaLletresiDigits(text):
    lletres= 0
    digits = 0 
    for i in text:
        if i in string.ascii_letters:
            lletres += 1
        elif i in string.digits:
            digits +=1
        else:
            continue
    return lletres, digits 

caracters = contaCaracters(frase)
paraules = contaParaules(frase)
lletres, digits = contaLletresiDigits(frase)
print(f"Hi ha {caracters} caràcters, {paraules} paraules")
print(f"Hi ha {lletres} lletres i {digits} digits")