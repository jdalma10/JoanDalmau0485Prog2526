# Torna la suma total
llista = [1,2,3,4,5]

# Declaració i inicalitzaió del acumulador
resultat = 0

for num in llista:
    resultat += num
print (resultat)


resultat = 0
for i in range(len(llista)):
   resultat += llista[i]
        
print (resultat)
