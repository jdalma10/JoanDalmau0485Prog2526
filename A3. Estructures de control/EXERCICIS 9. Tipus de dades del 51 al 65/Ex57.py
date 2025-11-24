from datetime import date
llista = []
for i in range(5):
    dia = input("Dia: ").zfill(2)
    mes = input("Mes: ").zfill(2)
    any = input("Any: ").zfill(4)

    data =  dia + "/" + mes + "/" + any
    datatime = date(2025, mes, dia)

    llista.append(data)
    