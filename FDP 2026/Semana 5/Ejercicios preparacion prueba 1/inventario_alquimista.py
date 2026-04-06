oro = 500
hierbas = 0
frascos = 0
pociones_totales = 0

while True:
    print("1) Comprar Hierba ($50 c/u)")
    print("2) Comprar Frasco ($100 c/u)")
    print("3) Fabricar poción (Requiere: 2 Hierbas y 1 Frasco)")
    print("4) Salir ($50 c/u)")

    opcion_escogida = int(input("Ingrese su opcion"))

    match opcion_escogida:
        case 1:
            if oro - 50 >= 0:
                print("Hierba comprada con éxito")

                oro -= 50
                hierbas += 1
                continue
            else:
                print("Oro insuficiente")
                continue
        case 2:
            if oro - 100 >= 0:
                print("Frasco comprado con éxito")

                oro -= 100
                frascos += 1
                continue
            else:
                print("Oro insuficiente")
                continue
        case 3:
            if hierbas >= 2 and frascos >= 1:
                print("Poción fabricada con éxito")
                
                hierbas -= 2
                frascos -= 1
                pociones_totales += 1
                continue
        case 4:
            print(f"Lograste hacer {pociones_totales} pociones")
            print(f"Te quedó {oro} de oro")
            break
        case _:
            print("Opción inválida")