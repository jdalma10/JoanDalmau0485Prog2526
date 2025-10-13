# 8. Algorisme que demani dos nombres 'nota' i 'edat' i un caràcter 'sexe' i mostri el missatge 'ACCEPTADA'
#  si la nota és major o igual a cinc, l'edat és més gran o igual a divuit i el sexe és 'F'. 
# En cas que es compleixi el mateix, però el sexe sigui 'M', ha imprimir 'POSSIBLE'.
#  Si no es compleixen aquestes condicions s'ha de mostrar 'NO ACCEPTADA'.

nota = float(input("Introdueix nota: "))
edat = int(input("Introdueix edat: "))
sexe = input("Introdueix sexe: ")

if nota >= 5 and edat >= 18 and sexe == "F":
    print("ACCPTADA")
elif nota >= 5 and edat >= 18 and sexe == "M":
    print("POSSIBLE")
else:
    print("NO ACCEPTADA")

""" if sexe == 'F':
    if nota >=5 and edat >=18:
        print("ACCPTADA")
    else:
        print("NO ACCEPTADA")
else:
    if nota >=5 and edat >=18:
        print("POSSIBLE")
    else:
        print("NO ACCEPTADA")  """

