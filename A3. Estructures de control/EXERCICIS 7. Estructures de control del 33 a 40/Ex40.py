#40 40. Llegir tres nombres que denoten una data (dia, mes, any). 
# Comprovar que és una data vàlida. Si no és vàlida dona un missatge d'error.
# Si és vàlida escriure la data canviant el número del mes pel seu nom.
esTraspas = False

# Ús de bucle amb una única iteració per estalviar instruccions en cas de error ràpid.
while True:
    dia = int(input("dia: "))
    mes = int(input("mes: "))
    any = int(input("any: "))

    if (any % 4 == 0 and any % 100 != 0 ) or any % 400 == 0:
        esTraspas = True

    if mes not in range(1,13):
        print("Error, data no valida")
        break

    if mes in [1,3,5,7,8,10,12]:
        diaMax = 31
    elif mes in [4,6,9,11]:
        diaMax = 30
    else:
        if esTraspas:
            diaMax = 29
        else:
            diaMax = 28

    if dia not in range(1, diaMax+1):
       print("Error, data no valida")
       break 

    print("Data correcta")
    break