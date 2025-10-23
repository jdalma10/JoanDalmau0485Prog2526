#19. Dissenya un algorisme corresponent a un programa que donada una sèrie de 5 nombres enters, 
# determini si la seqüència està formada exclusivament per valors positius.

# Funciona, però diseny mes rebuscat
totsPositius = True
for num in range(5):
    numero = int(input("Posa un número, si us plau:"))
    if numero > 0 and totsPositius == True:
        totsPositius = True
    else:
        totsPositius = False

        
# Disseny més eficient
totsPositius = True
for num in range(5):
    numero = int(input("Posa un número, si us plau:"))
    if numero < 0:
        totsPositius = False

