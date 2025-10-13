any_ = int(input("Introdueix l'any: "))

#  Un any és de traspàs si:
#   És divisible per 4
#   2PERÒ no és divisible per 100
#   EXCEPTE si també és divisible per 400 (en aquest cas SÍ que és de traspàs)

# Exemple:
#   2020 → divisible per 4 i no per 100 → traspàs
#   1900 → divisible per 100 però no per 400 → no traspàs
#   2000 → divisible per 400 → traspàs


if any_ % 4 == 0:
    # Si és divisible per 4, podria ser de traspàs, però cal mirar més condicions
    if any_ % 100 == 0:
        # Si també és divisible per 100, normalment NO és de traspàs
        if any_ % 400 == 0:
            # EXCEPTE si és divisible per 400, llavors SÍ que és de traspàs
            print(f"L'any {any_} és de traspàs (divisible per 400).")
        else:
            print(f"L'any {any_} NO és de traspàs (divisible per 100 però no per 400).")
    else:
        # Si és divisible per 4 però NO per 100, SÍ és de traspàs
        print(f"L'any {any_} és de traspàs (divisible per 4 i no per 100).")
else:
    # Si no és divisible per 4, mai no és de traspàs
    print(f"L'any {any_} NO és de traspàs (no divisible per 4).")

