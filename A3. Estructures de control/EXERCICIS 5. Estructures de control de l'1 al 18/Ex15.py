import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if dist > r1 + r2:
    print("Exteriors")
elif dist == r1 + r2:
    print("Tangents exteriors")
elif abs(r1 - r2) < dist < r1 + r2:
    print("Secants")
elif dist == abs(r1 - r2):
    print("Tangents interiors")
elif dist < abs(r1 - r2):
    print("Interiors")
else:
    print("Concèntriques")