usuaris = ["a","b","c"]
passwords = ["a","b","c"]
notas = []


logged = False
intents = 0

while intents < 3 and not logged:
    user = input("Nom")
    passw = input("PAss")

    for i in range (len(usuaris)):
        if user == usuaris[i]  and passw == passwords[i]:
            logged = True
            break
       
    intents+=1

if logged == True:
    while True:
        opcio  = int(input("Tria opcio:"))
        if opcio == 1:
            notas.append(int(input("Posa nota:")))
        elif opcio == 2:
            if len(notas)==0:
                print("Error: lista vacia")
                continue
            cercar = int(input("Posa nota a cerar:"))
            for i in range(len(notas)):
                if cercar == notas[i]:
                    print(f"Nota trobada a la posició: {i}")
                else:
                    print("Nota no trobada")
        elif opcio == 3:
            if len(notas)==0:
                print("Error: lista vacia")
                continue
            min = notas[0]
            max = notas[0]
            suma = 0
            for nota in notas:
                if nota > max:
                    max = nota
                if nota < min:
                    min = nota
                suma += nota
            print(f"Max ={max}, Min = {min} i Mig = {suma/len(notas)}")
        elif opcio == 4:
            break
        else:
            print("Opcio invalida")


    
        

