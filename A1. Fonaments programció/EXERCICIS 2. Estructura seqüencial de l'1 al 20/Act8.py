soubase = float(input("Sou base:"))
venda1 = float(input("Venta1:"))
venda2 = float(input("Venta2:"))
venda3 = float(input("Venta3:"))

ventatotal = venda1 + venda2 + venda3
comissió = ventatotal * 0.10
soutotal = soubase + comissió

print (soutotal)
print (comissió)
