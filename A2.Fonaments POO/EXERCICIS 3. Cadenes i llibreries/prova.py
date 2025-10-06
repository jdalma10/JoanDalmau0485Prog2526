# Classe Cotxe amb el seu mètode
class Cotxe:
    def __init__(self, marca, model, matricula):
        self.marca = marca
        self.model = model
        self.matricula = matricula
    
    def __str__(self):
        return f"Soc un {self.model}"

# Crida al mètode constructor per a

cotxe1 = Cotxe("Opel", "Corsa", "3333LLL") 

print(cotxe1.matricula)
print(cotxe1)


