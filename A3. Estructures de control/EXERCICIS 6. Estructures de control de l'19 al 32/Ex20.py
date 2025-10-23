# 20. Dissenya un algorisme corresponent a un programa que donada una successió
#  de 5 nombres, determini un per un si és parell o imparell. de la seguent manera: 

for i in range(5):
    num = int(input("Posa un nombre: "))
    if num % 2 == 0:
        print(f"{num}, parell")
    else:
        print(f"{num}, imparell")