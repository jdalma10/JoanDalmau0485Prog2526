# 37. Algorisme que compti el nombre de "LA" dins una seqüència de caràcters.
frase = input("Frase: ").upper()
la = 0

for i in range(len(frase)-1):
    if frase[i] == "L" and frase[i+1] == "A":
        la += 1

print(la)