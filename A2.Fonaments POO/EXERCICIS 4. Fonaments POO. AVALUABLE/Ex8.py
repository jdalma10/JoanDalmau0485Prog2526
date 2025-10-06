import random

class Dau:
    @staticmethod
    def tirada():
        return random.randint(1,6)
    

tirades = ""
tirades += str(Dau.tirada()) + " "
tirades += str(Dau.tirada()) + " "
tirades += str(Dau.tirada()) + " "
tirades += str(Dau.tirada()) 

print(tirades)