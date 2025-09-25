minuts = float(input("Escolleixi els minuts que vulgui convertir a hores: "))

minutsh = (minuts//60)
minutsr = (minuts%60)

print("Els seus minuts a hores són: " + str(minutsh) +
       "hores i " + str(minutsr) + "minuts")