encert = int(input("Posa encert: "))
fallo = int(input("Posa fallo: "))
blanc = int(input("Posa blanc: "))

print(''' 
        Encerts: ''' + str(encert) + 
        ''' Fallos: ''' +  str(fallo)+ 
        ''' Blanc: ''' + str(blanc) + 
      
      ''' Nota: ''' + str(encert*5 + fallo *(-1)))