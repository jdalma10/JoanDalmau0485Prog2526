# 23. Algorisme que donades les hores setmanals i 
# el preu hora treballades, si aquestes passen de 40 hores les hores extraordinàries
#  es pagaran 1,5 vegades la hora ordinària.

horesTreballades = float(input("Hores: "))
preuHora = float(input("Preu: "))

if horesTreballades > 40:
    horesExtres = horesTreballades - 40
    total = 40 * preuHora + (1.5*preuHora*horesExtres)
else:
    total = horesTreballades * preuHora


print(f"Et pagaran {total} €.")
