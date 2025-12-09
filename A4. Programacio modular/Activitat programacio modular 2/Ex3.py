credencials = ["anna-1234", "joan-abcd", "maria-qwerty"]

def valida (user, passw):

    validat = False
    for i in credencials:
        usuari = i.split("-")[0]
        contra = i.split("-")[1]

        if usuari == user and contra == passw:
            validat =  True
            breakpoint
        else:
            validat = False
    return valida
        
intents = 0

while intents < 3:
    user = input("nom")
    passw = input("contra")

    if valida(user, passw):
        print ("acces validat")
        break
    else:
        intents += 1

if intents == 3:
    print ("acces denegat")
            