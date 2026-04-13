hierbas =  0
frascos = 0
oro = 500
pociones_totales = 0
opcion = 0

while opcion != 4:
    print("\n ¿Que quieres hacer?") #\n para saltar una linea.
    print("1. Comprar hierbas ($50 c/u)")
    print("2. Comprar frascos ($100 c/u)")
    print("3. Fabricar poción de fuego (Requiere: 2 hierbas y 1 frasco)")
    print("4. Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        if oro >= 50:
            oro -= 50
            hierbas += 1
            print(f"Has comprado una hierba, ahora tienes {hierbas} hierbas, y te queda ${oro} de oro.")
        else:  
            print("Oro insuficiente para realizar esta compra.")
    
    elif opcion == 2:
        if oro >= 100:
            oro -= 100
            frascos += 1
            print(f"Has comprado un frasco, ahora tienes {frascos} frascos, y te queda ${oro} de oro.")
        else:
            print("Oro insuficiente para realizar esta compra.")

    elif opcion == 3:
        if hierbas >= 2 and frascos >= 1:
            hierbas -= 2
            frascos -= 1
            pociones_totales += 1
            print(f"Has creado una poción de fuego, tienes {pociones_totales} de pociones.")
        else:
            print("Materiales insuficientes")
    elif opcion == 4:
        print("\n ****RESUMEN*****")
        print(f"Has creado {pociones_totales} pociones.")
        print(f"Y te queda ${oro} de oro.")
    else:
        print("Opcion no valida")
       


        


        
            
        
               
    

        


    






