



while True :

    try :
        
        cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
        
        if cantidad_pasajeros < 1 :
            print("Ingrese un numero mayor que 0")
            continue
        
        else:
            print(f"Vuelo resgistado con {cantidad_pasajeros}")
            break
            
        
    except ValueError:

       print("Error: ingrese un numero entero positivo")
            
   
    

        
        