while True:
    try:
            nombre_de_bodega = input("nombre del codigo ")

            contador = 0
            for i in nombre_de_bodega:
             if i == " ":
                raise ValueError
             contador = contador + 1
        
            if contador < 6:
             raise ValueError
        
            print(f"producto registrado con codigo {nombre_de_bodega}")
            break
    
    except ValueError:
       print("minimo 6 catracters y sin espacio")



