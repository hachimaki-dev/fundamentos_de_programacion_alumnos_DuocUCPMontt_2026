# Ejercicio 15 — Sistema de control de inventario de una tienda

stock = 80
capacidad_maxima = 200

while True:

    print("=== INVENTARIO TIENDA DIGITAL ===")
    print("1. Ver stock actual")
    print("2. Registrar entrada de mercancía")
    print("3. Registrar venta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Stock actual: {stock} unidades")

    elif opcion == "2":

        try:
            entrada = int(input("Ingrese cantidad recibida: "))

            if entrada <= 0:
                print("Debe ingresar un valor positivo.")

            elif stock + entrada > capacidad_maxima:
                print("Se supera la capacidad máxima de la bodega.")

            else:
                stock += entrada

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "3":

        try:
            venta = int(input("Ingrese cantidad vendida: "))

            if venta <= 0:
                print("Debe ingresar un valor positivo.")

            elif venta > stock:
                print("No hay suficiente stock.")

            else:
                stock -= venta

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "4":
        print(f"Stock final: {stock} unidades. Sesión cerrada.")
        break

    else:
        print("Opción inválida.")