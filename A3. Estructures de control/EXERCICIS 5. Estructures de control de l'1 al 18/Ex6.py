# 

import string 

lletra = input ("Introdueix una lletra: ")

""" codiAsci = int(lletra)
if codiAsci > 180  and codiAsci > 212: """

maj = string.ascii_uppercase
min = string.ascii_lowercase

if lletra in maj:
    print (f"{lletra} és majúscula")
elif lletra in min:
    print (f"{lletra} és minúscula")


if lletra.isupper():
    print (f"{lletra} és majúscula")
else: 
    print (f"{lletra} és minúscula")

