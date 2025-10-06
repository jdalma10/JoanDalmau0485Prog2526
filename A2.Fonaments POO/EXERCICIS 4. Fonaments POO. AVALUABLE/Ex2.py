# Afegeix a la classe anterior un mètode per a que mostri el nom i l'edat de la persona en aquest format " Nom: Manel, Edat: 19".
class Persona:
    def __init__(self, nom, edat):
        self.nom=nom
        self.edat= edat
    def __str__(self):
        return f"{self.nom},{self.edat}"
    
persona =Persona("Manel", 19)
print (persona)