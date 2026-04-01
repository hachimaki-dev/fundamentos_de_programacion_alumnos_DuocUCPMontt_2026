vida_jefe = 1000
while vida_jefe > 0:
 daño = int (input ( "ingrese el daño del ataque"))
 vida_jefe -= (daño)
 if daño <= 0:
    print ("el ataque fallo")
 else:
      print ("el jefe tiene", vida_jefe, "de vida" )
print ("jefe derrotado")
      
      
  