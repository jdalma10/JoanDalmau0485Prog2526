dia = int(input("Introdueix el número del dia (1-7): "))
dies = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]

if 1 <= dia <= 7:
   print(f"El dia és {dies[dia - 1]}.")
   """  if dia == 1:
       print("Dilluns")
    elif dia == 2:
       print("Dimarts")
    # elif ...
    else:
       print ("diumenge") """
else:
    print("Error: número de dia incorrecte.")