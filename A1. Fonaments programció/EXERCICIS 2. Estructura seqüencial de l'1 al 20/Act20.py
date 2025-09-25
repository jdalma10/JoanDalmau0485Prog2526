dos = int(input("Posa euros: "))
un = int(input("Posa euros: "))
mig = int(input("Posa centims: "))
vint = int(input("Posa centims: "))
deu = int(input("Posa centims: "))
cinc = int(input("Posa centims: "))

diners=200*(dos)+100*(un)+50*(mig)+20*(vint)+10*(deu)+5*(5)
eurostotal= diners // 100
centimstotal= diners % 100

print ("tenim", str(eurostotal), "€","i", str(centimstotal), "centims")