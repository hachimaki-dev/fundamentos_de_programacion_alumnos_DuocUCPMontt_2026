while True :
    total = 0
    contador = 0
    descuento = 10
   
    eleccion_usuario = int(input("Elija el precio del suplemento:")) 
    if eleccion_usuario == 0 :

        print("El usuario ha decidido salir")
        break
    total = total + 1
    contador = contador + 1
    
    if contador >= 3 :
        final = total/100*10
        total = total - final
        print(f"llevas {contador} productos")




     





    
    