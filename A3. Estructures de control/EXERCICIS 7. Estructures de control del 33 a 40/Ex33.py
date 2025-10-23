# 33. Dissenya un algorisme corresponent a un programa que donada una frase, compti el nombre de caràcters que hi apareixen.

frase = input("Frase: ")

# print(len(frase))

lletres = 0
# Amb iterador de tipus index, enter
for i in range(len(frase)):
    lletres += 1

# Amb iterador de tipus element
for lletra in frase:
    lletres +=1

# Amb while
j = 0
while j < len(frase):
    j +=1

