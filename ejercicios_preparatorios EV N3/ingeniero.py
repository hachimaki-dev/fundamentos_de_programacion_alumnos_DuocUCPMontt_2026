mesas_disponibles = 20
capacidad = 20
historial = 0

while True:
    try:
        print("Sistema de mesas \n1)ver mesas disponible \n2)asignar mesas \n3)liberar mesas \n4)mesas ocupadas actualmente \n5)salir")
        
        eleccion = int(input("eliga su opción: "))
        if eleccion <= 0 or eleccion > 5:
            print("no puedes elegir un numero menor que 0 ni mayor que 6")
        
    except ValueError:
        print("solo puedes ingresar numeros enteros")
        
    if eleccion == 1:
        print(f"cantidad de mesas es igual a {mesas_disponibles}")
        
    elif eleccion == 2:
        while True:
            try:
                asignar_mesas = int(input("cuantas mesas quiere ingresar: "))
                if asignar_mesas > 0:
                    if asignar_mesas > mesas_disponibles:
                        print("no puedes hacer eso XD")   
                    else:
                        break
                else:
                    print("no puedes asignar un numero negativo")
            except ValueError:
                print("Solo puede ingresar numeros enteros")
                          
        mesas_disponibles -= asignar_mesas
        historial += asignar_mesas
        
    elif eleccion == 3:
        while True:
            try:
                liberar_mesas = int(input("cuantas mesas quiere liberar: "))
                if liberar_mesas > 0:
                    if liberar_mesas > capacidad - mesas_disponibles:
                        print("no puedes hacer eso XD HAY MESAS 0")
                    else:
                        break
                else:
                    print("no puedes asignar un numero negativo")
                    
            except ValueError:
                print("solo puedes ingresar numeros enteros")
                
        mesas_disponibles += liberar_mesas
        historial -= liberar_mesas
        
    elif eleccion == 4:
        print(f"mesas ocupadas actualmente son {historial}")
        
    elif eleccion == 5:
        print("buenas noches XD")
        break
        
        
                   
        


