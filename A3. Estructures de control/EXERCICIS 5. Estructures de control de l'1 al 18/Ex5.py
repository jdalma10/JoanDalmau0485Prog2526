# 5. Escriu un programa que demani un nom d'usuari i una contrasenya i si s'ha introduït "anna" i "12345" s'indica "Has entrat a sistema", sinó es dona un error.

nom_usuari = input("Introdueix el nom d'usuari:")
contrasenya = int(input ("Introdueix la contrasenya:"))

if nom_usuari == "anna" and contrasenya == 12345:
    print("Acces al sistema")
else:
    print("Error")

""" 
if nom_usuari == "anna":
    if contrasenya == 12345: 
        print("Acces al sistema")
    else:
        print("Error")
else:
    print("Error") """