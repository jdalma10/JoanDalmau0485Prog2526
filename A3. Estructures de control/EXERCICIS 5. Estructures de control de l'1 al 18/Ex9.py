#9. Algorisme que demani tres nombres i els mostri ordenats (de més a menys);

a = int(input("N1: "))
b = int(input("N2: "))
c = int(input("N3: "))

if a < b :
    a , b = b ,a 

if b < c:
    b,c = c,b

if a < b :
    a , b = b ,a 

print(a,b,c)