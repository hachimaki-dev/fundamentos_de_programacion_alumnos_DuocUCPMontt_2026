condicion = True

while condicion == True: 
    print("Bienvenidos")
    print("1. Contar chiste" )
    print("2. Contar adivinanza")
    print("3. Salir")
    
    opcion_elejida = int(input( "Elija su opción"))
    
    if opcion_elejida == 1:
     print ("Contamos los chiste")
    if opcion_elejida == 2:
     print ("Contamos las adivinanzas")
    if opcion_elejida == 3:
     condicion = False