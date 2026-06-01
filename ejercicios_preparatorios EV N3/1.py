while True:
    try:
        numero_usuario = int(input("ingrese un numero entero: "))
        
    except ValueError:
        print("ingrese un numero entero")
        
    else: 
        print(f"Numero recibido {numero_usuario}")
        break
        
        
        
        
    