contador = 0
acumulador = 0


while contador < 5:
    num = int(input("posa un num: "))
    if num % 2 == 1:
        contador = contador + 1
        acumulador += num

print(acumulador)