m=[]
MIDA = 3

for i in range(MIDA):
    f = []
    for j in range(MIDA):
        f.append(1)
    m.append(f)

for i in range(MIDA):
    for j in range(MIDA):
        print(m[i][j], end="\t")
    print()