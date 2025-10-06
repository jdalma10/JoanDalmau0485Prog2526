class Calculadora:
    @staticmethod
    def sumar(n1,n2):
        return n1 + n2
    
    def resta(n1,n2):
        return n1 - n2
    
    def divideix(n1,n2):
        return n1 / n2    

int1 = int(input("Posa el primer nombre: ")) 
int2 = int(input("Posa el segon nombre: ")) 
print (Calculadora.sumar(int1,int2))
print (Calculadora.resta(int1,int2))
print (Calculadora.divideix(int1,int2))