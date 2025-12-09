""" 5.  Registre d'usuari

Escriu una funció validar_contrasenya on pasast un paràmetre contrasenya, retorni True si compleix TOTES les condicions:

    mínim 8 caràcters
    conté almenys una majúscula
    conté almenys una minúscula
    conté almenys un dígit
    conté almenys un símbol (!@#$%^&*_-)

Després crea una funció registrar_usuari() que demani una contrasenya repetida 2 cops i només l accepti si aquestes coincidèixen i si passa la validació. """

def validar_contrasenya(contrasenya):
    simbols = "!@#$%^&*_-"

    if len(contrasenya) < 8:
        return False

    majuscula = False
    minuscula = False
    digit = False
    simbol = False

    for c in contrasenya:
        if 'A' <= c <= 'Z':
            majuscula = True

        elif 'a' <= c <= 'z':
            minuscula = True

        elif '0' <= c <= '9':
            digit = True

        if c in simbols:
            simbol = True

    return majuscula and minuscula and digit and simbol

   

def registrar_usuari():
    while True:
        contrasenya1 = input("Introdueix la contrasenya: ")
        contrasenya2 = input("Repetiu la contrasenya: ")

        if contrasenya1 != contrasenya2:
            print("Les contrasenyes no coincideixen. Torna-ho a intentar.")
            continue

        if not validar_contrasenya(contrasenya1):
            print("La contrasenya no compleix els requisits. Torna-ho a intentar.")
            continue

        print("Usuari registrat correctament!")
        break

registrar_usuari()



    
     
         