    # 18. Escriu un programa que demani una data (dia, mes i any) 
    # i digui si és correcta.




dataOK = False

dia = int(input("Dia"))
mes = int(input("MEs"))
any = int(input("Any"))

if mes == 1 or  mes == 3 or  mes == 5 or  mes == 7 or  mes == 8  or mes == 10 or  mes == 12:
    if dia >= 1 and dia <=31:
        dataOK = True
    else:
        dataOK = False
elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
    if dia >= 1 and dia <=30:
        dataOK = True
    else:
        dataOK = False
elif mes == 2:
    if any % 4 == 0:
        if any % 100 == 0:
            if any % 400 == 0:
                diesFef = 29
            else:
                diesFef = 28
        else:
            diesFef = 29
    else:
        diesFef = 28

    if dia >=1 and dia <= diesFef:
        dataOK = True
    else:
        dataOK = False
else:
    dataOK = False

if dataOK:
    print("OK")
else:
    print("No OK")

