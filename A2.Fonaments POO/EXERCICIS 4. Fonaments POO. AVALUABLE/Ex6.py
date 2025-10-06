class Producte:
    def __init__(self, nom, preu, descompte):
        self.nom=nom
        self.preu= preu
        self.descompte= descompte

    def __str__(self):
        preuDescompote = self.preu * self.descompte
        return f"{self.nom}: {preuDescompote}€"
    

    
producte1 =Producte("Pantalla", 150, 0.8)


print (producte1)

