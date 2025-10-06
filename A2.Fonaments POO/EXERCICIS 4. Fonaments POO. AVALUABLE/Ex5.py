import math
class Cercle:
    def __init__(self, radi):
        self.radi = radi
    
    def __str__ (self):
        return f"Soc un cercle de radi {self.radi} i {self.area():.2f} d'area"
    
    def area(self):
        return math.pi * (self.radi * self.radi)
    
cercle1 = Cercle(12)

print(cercle1)