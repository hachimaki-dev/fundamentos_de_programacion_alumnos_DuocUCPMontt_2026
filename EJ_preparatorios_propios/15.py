stock = 80

print("####"*10)
print("Inventario Tienda Digital")
print("####"*10)

while True:
    print("1. Ver Stock Actual \n2. registrar Entrada de mercancia \n3. Registrar Venta\n4. Salir")

    try:
        opcion_elegida = int(input("Ingrese la opcion que desea realizar :   "))
        
        if opcion_elegida == 4:
            print(f"Stock Final: {stock} unidades")
            break
        elif opcion_elegida == 1:
            print(f"Stock :  {stock}")
        elif opcion_elegida == 2:
            while True:
                try:
                    registrar_mercancia = int(input("Ingrese cuanta mercancia  va a Entrar :  "))
                    if stock + registrar_mercancia > 200:
                        print("El limite de stock es 200 con la mercancia de entrada esta sobrepasando el limite ")
                        continue
                    else:
                        stock += registrar_mercancia
                        print(f"Stock :  {stock}")
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
                    continue
        elif opcion_elegida == 3:
            while True:
                try:
                    registrar_venta = int(input("Ingrese la cantidad de venta :   "))
                    if registrar_venta > stock:
                        print("Lo que se va a vender no puede superar los 200 (Limite del Stock)")
                    else:
                        stock -= registrar_venta
                        print(f"Stock actual :  {stock}")
                        break
                except ValueError:
                    print("ingrese una opcion valida ")
    except ValueError:
        print("ingrese una opcion valida ")
