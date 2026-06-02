#Variables necesarias para resolver el ejercicio
opcion = 0
stock = 80
stock_max = 200

#Menu que se repite en loop, por eso va dentro del while
while True:

    print("\n=== INVENTARIO TIENDA DIGITAL ===")
    print("1. Ver stock actual")
    print("2. Registrar entrada de mercancía")
    print("3. Registrar venta")
    print("4. Salir")

    #acción  a realizar
    while True:
        try:
            opcion = int(input("Ingresa número de la opción: "))
            if 1 <= opcion <= 4:
                break
            else:
                print("Error: Ingrese una opción válida")
        except ValueError:
            print("Error: Ingrese una opción válida")

    #El primer if es la opción salir :)
    if opcion == 4:
        print(f"Stock final: {stock} unidades. Sesión cerrada.")
        break

    elif opcion == 1:
        print(f"Tu stock actual es {stock} productos.")

    #entrada de mercancia, la entrada de mercancia no puede superar 200
    elif opcion == 2:
        while True:
            try:
                entrada = int(input("Cantidad de productos entrando: "))
                if entrada <= 0:
                    print("Error: La cantidad de mercancia entrante debe ser mayor a 0.")
                elif (entrada + stock) > stock_max:
                    print("Error: La suma de la entrada y el stock, no puede superar el stock máximo")
                else:
                    stock += entrada
                    if stock == stock_max:
                        print("Capacidad máxima alcanzada.")

                    print(f"Ingresaste {entrada} productos.")
                    print(f"Tu stock actual es {stock} productos.")
                    break
            except ValueError:
                print("Error: Ingresa la cantidad en formato numérico.")

    #Salida de mercancia
    elif opcion == 3:
        while True:
            try:
                salida = int(input("Cantidad de productos vendidos: "))
                if salida <= 0:
                    print("Error: La venta debe ser mayor a 0.")
                elif salida > stock:
                    print("Error: La venta debe ser menor o igual al stock disponible.")
                else:
                    stock -= salida
                    print(f"Se vendieron {salida} productos.")
                    print(f"Tu stock actual es {stock} productos.")
                    break
            except ValueError:
                print("Error: Ingresa la cantidad en formato numérico.")