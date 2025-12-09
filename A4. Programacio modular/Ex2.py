import random
TIPUS = ["Aigua", "Foc"]


def pokemon():
    global nom, tipus, vida
    nom = input("Nom: ")
    tipusEleccio = int(input("0.Aigua, 1.Foc"))
    tipus = TIPUS[tipusEleccio]
    vida = random.randint(1,101)

def rival():
    global nomRival, tipusRival, vidaRival
    nomRival = "Pokembo"
    tipusRival = random.choice(TIPUS)
    vidaRival = random.randint(1,101)

def combat():
    global nom, tipus, vida, nomRival, tipusRival, vidaRival
    if tipus == "Aigua" and tipusRival == "Foc":
        vida *= 1.5
    elif tipus == "Foc" and tipusRival == "Aigua":
        vidaRival *= 1.5
    else:
        pass
    
    if vida > vidaRival:
        print("Guanyes")
    elif vidaRival > vida:
        print("Perds")
    else:
        print("Empat")

pokemon()
rival()
combat()