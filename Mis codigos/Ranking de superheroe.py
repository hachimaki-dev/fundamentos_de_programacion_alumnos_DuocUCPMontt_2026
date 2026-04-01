misiones_exitosas = 0
daño_civiles = 0

misiones_exitosas = int(input("ingrese las misiones exitosas")) 
daño_civiles = int(input("ingrese el daño a los civiles"))

if misiones_exitosas >= 10 and daño_civiles == 0:
    print("Heroe categoria S.Bono Maximo")
    
elif misiones_exitosas > 4:
    print ("Heroe Categoria A. Cumple promedio")
    
elif misiones_exitosas < 5 and daño_civiles > 10000000:
    print ("Despedido. Demasiado caos")
    
else:
    print("Heroe en observacion")

