suma = 0
lista = []
contador = 0

while True:
    numero= input("introduce un numero: ")
    if numero == "0":
        break 
    if numero.isdigit():
        numero_entero= int(numero)
        contador += 1
        suma += numero_entero
        lista.append(numero_entero)
    else:
        print ("ERROR, caracter no valido")

print (f"la suma de todos ellos es {suma}")
print (f"los números son {lista}")
print (f"la cantidad de numeros introducidos es {contador}")