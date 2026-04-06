while True:

    print ("Bienvenido a la tienda de suplementos deportivos ¿Desea ver el catalogo?")

    Continuar = True

    valor_carrito = 0

    proteina = 35000
    creatina = 25000
    vitaminas = 17000

    cantidad_productos = 0

    while Continuar:
        print ("¿Que producto desea comprar?")
        print ("1. Proteina ($35000)")
        print ("2. Creatina ($25000)")
        print ("3. Vitaminas ($17000)")
        print ("4. Salir") 
        
        opcion = int(input("Ingrese el numero del producto para añadir al carrito o si desea salir "))
        if opcion == 1:
            valor_carrito = (valor_carrito + proteina)
            print ("Proteina añadida al carrito")   
            print (f"valor del carrito: {valor_carrito}")
            print ("¿Desea seguir comprando?")
            seguir = input("si/no ")
            if seguir == "no":
                print (f"El valor total del carrito es de: {valor_carrito}")
        elif opcion == 2:
            print ("Creatina añadida al carrito")
            print ("valor del carrito: $25000")
            print ("¿Desea seguir comprando?")
            seguir = input("si/no ")
        elif opcion == 3:
            print ("Vitaminas añadidas al carrito ($17000)")
            print ("valor del carrito: $17000")
            print ("¿Desea seguir comprando?")
            seguir = input("si / no ")
        elif opcion == 4:
            print ("Gracias por su visita")
            break