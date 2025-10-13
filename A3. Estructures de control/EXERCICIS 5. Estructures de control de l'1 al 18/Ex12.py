# 12. La política de cobrament d'una companyia telefònica és...

temps = int(input("Durada en minuts: "))
dia = input("És diumenge? (s/n): ").lower()
if dia != 's':
    torn = input("Torn (m per matí, t per tarda): ").lower()

# Calcul del cost base segons trams
if temps <= 5:
    cost_base = 1.0
elif temps <= 8:
    cost_base = 1.0 + (temps - 5) * 0.80
elif temps <= 10:
    cost_base = 1.0 + 3 * 0.80 + (temps - 8) * 0.70
else:
    cost_base = 1.0 + 3 * 0.80 + 2 * 0.70 + (temps - 10) * 0.50

# Impost segons el dia/torn
if dia == 's':
    impost = cost_base * 0.03
elif torn == 'm':
    impost = cost_base * 0.15
else:
    impost = cost_base * 0.10

total = cost_base + impost

print(f"Cost base: {cost_base:.2f} €")
print(f"Impost: {impost:.2f} €")
print(f"Total a pagar: {total:.2f} €")