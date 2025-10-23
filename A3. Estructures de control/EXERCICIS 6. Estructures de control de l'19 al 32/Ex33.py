hiHaNegatiu = False

n = int (input ("Posa 0 si vols acabar: "))

while n != 0:
    if n < 0:
        hiHaNegatiu = True
    n = int (input ("Posa 0 si vols acabar: "))

if hiHaNegatiu:
    print ("Hi ha un nombre negatiu")
else:
    print ("Tots positius")

