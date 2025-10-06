#3. Escriu un programa que demani a l'usuari
#  una cadena i la mostri al revés. 
#  "Hola, món!" -> "!nóm ,aloH"
cadena = "hola mon"
cadena_inversa = cadena[::-1]
print (cadena_inversa)

""" cadena_inversa = ""
for i in range(len(cadena)):
    aux = len(cadena)-1
    cadena_inversa += cadena[aux]
    aux -= 1 """