print("\n**********BIENVENIDO**********")

precio_producto = 0
tipo_producto = ""

for intento in range(3):
    print("\nSELECCIONE EL PRODUCTO: ")
    print("1. AGUA ($1000)")
    print("2. JUGO ($1200)")
    print("3. BEBIDA ($1500)")

    seleccion = input("\nSeleccione 1, 2 o 3 (o 9 para salir): ")

    if seleccion == "9":
        print("\nSaliendo ... \n")
        print("¡Vuelva pronto!\n")
        break
    elif seleccion == "1":
        tipo_producto = "Agua"
        precio_producto = 1000
        break
    elif seleccion == "2":
        tipo_producto = "Jugo"
        precio_producto = 1200
        break
    elif seleccion == "3":
        tipo_producto = "Bebida"
        precio_producto = 1500
        break
    else:
        print("\nERROR: Seleccion no valida")
        restantes = 2 - intento
        print(f"Intentos restantes: {restantes}")
    
        if restantes == 0:
            print("Por favor comience de nuevo\n")


if precio_producto > 0:
    print("\n***********PAGO***************")
    print(f"Producto seleccionado: {tipo_producto}")
    print(f"Monto a pagar: ${precio_producto}")
    print("******************************\n")