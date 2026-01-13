
alumne = {
    "idAlumne":3,
    "nom":"Joan",
    "edat":39,
    "colors": ["red", "white", "blue"]
}

print(alumne["nom"])

alumne["curs"] = "DAM"

print(alumne.get("curs"))

x = alumne.keys()

print(x)


for a in alumne:
    print (f"{a}: {alumne[a]}")

for x in alumne.values():
  print(x)