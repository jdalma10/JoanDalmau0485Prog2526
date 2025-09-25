# Una botiga ofereix un descompte de l'15% sobre el total de la compra i un client vol saber quant haurà de pagar finalment per la seva compra.
porcentaje=15
compra=float(input("Introduce la cantidad de compra: "))
compra_descuento= (compra-(porcentaje/100)*compra)
#compra * 0.85
print ("El precio de compra tras el porcentaje es "+str(compra_descuento)+"€")
