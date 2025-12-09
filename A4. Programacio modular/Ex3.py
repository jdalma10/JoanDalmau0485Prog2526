empresa = []
validat = False

def login(user, pas):
    if user == "admin" and pas == "1234":
        empresa.append(user)
        return True
    else:
        return False
    
def fichar():
    usuari = input ("Usuari: ")
    if usuari in empresa:
        empresa.remove(usuari)
    else:
        empresa.append(usuari)


while not validat:
    usuari = input ("user: ")
    contra = input ("pass: ")
    validat = login(usuari,contra)

while len(empresa) != 0:
    fichar()
    


