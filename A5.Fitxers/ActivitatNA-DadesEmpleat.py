import csv, os
wd = os.getcwd()

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1 - Afegir empleat")
    print("2 - Mostrar empleats")
    print("3 - Exportar a fitxer")
    print("4 - Importar de fitxer")
    print("5 - Exportar a fitxer CSV")
    print("6 - Importar de fitxer CSV")
    print("7 - Sortir")

def afegir_empleat(empleats, avancat=False):
    try:
        nom = input("Introdueix el nom: ")

        if avancat:
            dni = input("Introdueix el DNI: ")
            edat = int(input("Introdueix l'edat: "))
            empleats.append(f"{nom}/{dni}/{edat}")
        else:
            empleats.append(nom)

        print("Empleat afegit correctament.")
    except ValueError:
        print("Error: l'edat ha de ser un número enter.")

def mostrar_empleats(empleats):
    if not empleats:
        print("No hi ha empleats registrats.")
        return

    print("\n=== LLISTA D'EMPLEATS ===")
    for i, e in enumerate(empleats, 1):
        print(f"{i}. {e}")

def exportar_fitxer(empleats, nom_fitxer):
    try:
        with open(nom_fitxer, "w", encoding="utf-8") as f:
            for e in empleats:
                f.write(e + "\n")
        print(f"Empleats exportats correctament a {nom_fitxer}")
    except Exception as e:
        print(f"Error en exportar: {e}")

def importar_fitxer(nom_fitxer):
    empleats = []
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            for linia in f:
                empleats.append(linia.strip())
        print(f"Fitxer {nom_fitxer} importat correctament.")
    except FileNotFoundError:
        print("Error: el fitxer no existeix.")
    except Exception as e:
        print(f"Error desconegut: {e}")
    return empleats

def exportar_fitxerCSV(empleats, fitxer, avancat=False):
   if avancat:
       
       matriu = []
       for e in empleats:
           empleat = e.split("/")
           matriu.append(empleat)

       with open(wd+'\JoanDalmau0485Prog2526\A5.Fitxers\output.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(empleats)
   else:
        with open(wd+'\JoanDalmau0485Prog2526\A5.Fitxers\output.csv', 'w', newline='', encoding='utf-8') as f:
            for e in empleats:
                f.write(e+"\n")

        


    

def triarMode():
    print("Vols mode fàcil (només nom) o avançat (nom/dni/edat)?")
    mode = input("Introdueix F per fàcil o A per avançat: ").upper()
    while mode not in ['A', 'F']:
         mode = input("Introdueix F per fàcil o A per avançat: ").upper()
    if mode == 'A':
        return True
    else:
        return False

def main():

    import os
    wd = os.getcwd()
    nom_fitxer = wd+'\JoanDalmau0485Prog2526\A5.Fitxers\demofile.txt'
    empleats = []

    avancat = triarMode()

    while True:
        mostrar_menu()
        try:
            opcio = int(input("Escull una opció: "))
        except ValueError:
            print("Has d'introduir un número del 1 al 5.")
            continue

        if opcio == 1:
            afegir_empleat(empleats, avancat)

        elif opcio == 2:
            mostrar_empleats(empleats)

        elif opcio == 3:
            exportar_fitxer(empleats, nom_fitxer)

        elif opcio == 4:
            empleats = importar_fitxer(nom_fitxer)

        elif opcio == 5:
            exportar_fitxerCSV(empleats, nom_fitxer, avancat)
        

        elif opcio == 6:
          #  empleats = importar_fitxerCSV(nom_fitxer)
          pass

        elif opcio == 7:
            print("Sortint del programa...")
            break

        else:
            print("Opció no vàlida. Introdueix un número del 1 al 5.")

if __name__ == "__main__":
    main()
