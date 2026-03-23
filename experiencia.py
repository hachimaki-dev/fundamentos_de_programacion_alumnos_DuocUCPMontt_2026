print("  LLAMADA EJECUTIVO VTR ")

print("¿Que operacion desea realizar?")
while True: 
    print("INICIO DE PROGRMA *********")
    print("1.Recarga")
    print("2.Contratar plan")
    print("3.Salir")

    opcion = int(input("Elija su opcion "))


    if opcion == 1:
        print("¿Cuanto desea recargar? ")
        print ("1. 1000")
        print ("2. 2000")
        print ("3. 3000")
        recargar_elegida = int(input("Ingrese la cantidad a recargar "))
    
    if opcion == 2:
        print("¿Que plan desea contratar? ")
        print("1. Plan de 25GB")
        print ("2. Plan de 50GB")
        plan_elegido = int(input("Elija tipo plan ")) 
        if plan_elegido == 1:
            print("Plan de 25GB")
            print("Volviendo al menu incial")
        else:
            print("Eligio plan de 50GB")
            print("Volviendo al menu incial")
    if opcion == 3:
        break
    

print("   FIN DE LA LLAMADA   ")