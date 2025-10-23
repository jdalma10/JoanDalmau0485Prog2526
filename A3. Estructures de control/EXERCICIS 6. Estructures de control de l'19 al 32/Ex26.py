# 26. Calcular les qualificacions d'un grup d'alumnes.
#  La nota final de cada alumne es calcula seguint el criteri:
#  la part pràctica val el 10%; la part de problemes val un 50% 
# i la part teòrica el 40%. Llegirà tres notes de cada alumne fins 
# trobar les tres notes com a 0. Les notes han d'estar entre 1 i 10, 
# si no ho estan, no imprimirà les notes, donarà error i llegirà les 
# d'un altre alumne.ç


while True:
    pract = int(input("prac"))
    # while pract < 1 or pract > 10:
        # pract = int(input("prac"))
    probl = int(input("probl"))
    teoria = int(input("teoria"))

    if pract == 0 and probl ==0 and teoria ==0: 
        break
    
    if (pract < 1 or pract > 10) or (probl < 1 or probl > 10) or (teoria < 1 or teoria > 10):
        print("Error.")
        continue
    else:
        print(f"Nota: {0.1*pract + 0.5*probl + 0.4*teoria}")




