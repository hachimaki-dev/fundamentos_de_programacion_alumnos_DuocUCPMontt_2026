while True:
    try:
        edad_conductor = int(input("Ingrese su edad:"))
            
        if edad_conductor < 18:
            print("Menor de edad. Ingresa una edad valida para conducir.")
            continue
        else:
            print(f"Edad registrada: {edad_conductor} .")
            break
    except ValueError:
        print("ingresa un valor valido, en numero ")  
              


        
