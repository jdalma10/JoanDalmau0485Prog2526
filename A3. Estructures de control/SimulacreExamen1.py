# Simulacre d'exàmen 16/10. Login amb 3 intents. Si valida, menú amb 2 opcions. 1. Suma. 2. Núm primer.
intents = 3

while intents > 0:
    usuari = input("User: ")
    contra = input("Contra: ")

    if (usuari == "joan" and contra == "1234") or (usuari == "maria" and contra == "4567"):
        print("Login correcte")

        print("1. Suma")
        print("2. Primer")
        opcio = int(input("Opcio:"))
        # Ús del bucle per a controlar l'input correcte. Mentre posi opció diferent a 1 i 2, tornem a demanar.
        while opcio != 1 and opcio != 2:
            print ("Opcio incorrecta.")
            print("1. Suma")
            print("2. Primer")
            opcio = int(input("Opcio:"))

        if opcio == 1:
            num1 = int(input("Num1: "))
            num2 = int(input("Num1: "))
            print(f"Suma: {num1 + num2}")
        else:
            num = int(input("Num: "))
            primer = True
            # Com que tot número és divisible per ell mateix i per 1, mirarem el rang interior.
            # Només que trobem un numero divisor interior tal que el num sigui divisible per ell,
            # podrem assegurar que num no és primer.
            for i in range(num-1,1,-1):
                if(num%i==0):
                    primer = False
                    break
            if primer:
                print("Es primer")
            else:
                print("No es primer") 

        # Per a que no torni a entrar al bulcle. Podriem posar un break amb el mateix efecte.
        intents = 0   

    # si falla el login, restem un intent.            
    else:
        print("Login inccorrecte")
        intents -= 1
    