import datetime

d1 = 12
m1 = 3
y1 = 2025

d2 = 10
m2 = 3
y2 = 2025

data1 = datetime.datetime(y1,m1,d1)
data2 = datetime.datetime(y2,m2,d2)
diferencia = data1- data2
print (diferencia.days)
