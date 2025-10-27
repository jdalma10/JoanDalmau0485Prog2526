# 47. Demana una cadena i dos caràcters per teclat (valida que sigui un caràcter), 
# substitueix l'aparició del primer caràcter en la cadena pel segon caràcter.

from string import printable
cadena = input ("Cadena: ")
caracterARemplazar = input ("Carácter: ")
caracterNou =  input ("Carácter: ")
paraulaNova =""

while len(caracterARemplazar) != 1 and caracterARemplazar.lower() not in (printable):
    print ("ERROR, hi ha més d'un carácter o no és un carácter")
    caracterARemplazar = input ("Carácter: ")

while len(caracterNou) != 1 and caracterNou.lower() not in (printable):
    print ("ERROR, hi ha més d'un carácter o no és un carácter")
    caracterNou = input ("Carácter: ")

for lletra in cadena:
    if caracterARemplazar == lletra:
        paraulaNova += caracterNou 
    else:
        paraulaNova += lletra


    