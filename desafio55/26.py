
hojas_restantes = 5

for i in ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']:
   if hojas_restantes <= 0:
      print("no tiene mas hojas")
      break

        
   print ("imprimiendo",i)
   
   if i == 'TEXTO':
      hojas_restantes -= 1
   else:
        hojas_restantes -= 3