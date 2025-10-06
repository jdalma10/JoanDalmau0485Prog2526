# Crea una classe Persona amb atributs nom i edat. Crea un objecte de tipus Persona amb nom = "Manel" i edat = 19 . Imprimex l'objecte, que veus?
class Persona:
    def __init__(self, nom, edat):
        self.nom=nom
        self.edat= edat
    
persona =Persona("Manel", 19)

print (persona)

""" Per defecte, quan imprimim un objecte se’ns mostrarà
la referència a memòria on
es troba allotjat. """
