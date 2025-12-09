""" 
1. En el mateix fitxer on vas crear la calculadora, crea una altra funció que calculi la potència d’un valor introduït per paràmetre, anomenada “eleva”. 
2. El mòdul s’ha d’anomenar “calculadora”. 
3. La funció que vam desenvolupar l'última sessió (suma, resta, etc.), s’ha d’anomenar “calcul_basic” . 
4. Des d’un segon fitxer, importa el mòdul i utilitza les dues funcions passant-hi paràmetres. 
5. Des d’un tercer fitxer, importa les dues funcions específiques i utilitza-les passant-hi paràmetres. """

#Crear una funció de calculadora bàsica que pugui realitzar operacions aritmètiques segons els arguments que rep. Aquesta funció ha de ser capaç de sumar, 
#restar, multiplicar o dividir dos nombres en funció de l'operació especificada per l'usuari.
import string

def calcul_basic(num1,num2,operacio):
    if operacio == "+":
        return num1 + num2
    elif operacio == "-":
        return num1 - num2
    elif operacio == "*":
        return num1 * num2
    elif operacio == "/":
        if num2 == 0:
            print("Error no es pot dividir entre zero!")
            return None
        else:
            return num1 / num2     
       
    else:
        return "Error Operacio no valida!"
    

def eleva(base, exponent):
    return base**exponent
        
        
"""     
numA = int(input("Introdueix el primer nombre:")) 
numB = int(input("Introdueix el segon nombre: "))   

while True:
    operacio = input("Introdueix la operació que vols ('+', '-', '*', '/'): ")
    if operacio in ('+', '-', '*', '/'):
        break
    print("Error: Operació no vàlida! Torna-ho a intentar.")
    
def eleva(valor, exponent):
    return valor ** exponent


resultat = calcul_basic(numA,numB,operacio) 
print(f"Resultat {numA} {operacio} {numB} = {resultat}") """