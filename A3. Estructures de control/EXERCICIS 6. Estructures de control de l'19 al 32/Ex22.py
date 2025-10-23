# 22. Algorisme que sumi tots els números parells compresos entre 2 i 100.

acumula = 0

for i in range(2,101):
    if i % 2 == 0:
        acumula += i

print(acumula)