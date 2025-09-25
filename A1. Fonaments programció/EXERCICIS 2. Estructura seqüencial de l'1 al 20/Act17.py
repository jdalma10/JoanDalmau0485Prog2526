""" 17. Un ciclista parteix d'una ciutat A a les HH hores, 
MM minuts i SS segons. 
El temps de viatge fins arribar a una altra ciutat B és de T segons
. Escriure un algoritme que determini l'hora d'arribada a la 
ciutat B.
 """

temps_viatge = int(input("Posa temps entre ciutats(segons): "))
h_sortida = int(input("Posa hores: "))
m_sortida = int(input("Posa minuts: "))
s_sortida = int(input("Posa segons: "))


seg_h = h_sortida* 3600
seg_m = m_sortida * 60

horaSortidaEnSegons = seg_h + seg_m + s_sortida

horaArribada = horaSortidaEnSegons + temps_viatge

HHArribada = (horaArribada // 3600)  %24  
auxMinuts =  horaArribada % 3600
MMArribada = auxMinuts // 60
SSArribada = auxMinuts % 60


print(HHArribada,":",MMArribada,SSArribada)