a = float(input("Costat A: "))
b = float(input("Costat B: "))
c = float(input("Costat C: "))

if a == b == c:
    print("Triangle equilàter")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("Triangle rectangle")
elif a == b or b == c or a == c:
    print("Triangle isòsceles")
else:
    print("Triangle escalè")