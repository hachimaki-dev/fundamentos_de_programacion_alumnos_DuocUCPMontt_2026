hierbas = 0
frascos = 0
pociones_totales = 0
oro = 500

while True:

    print("------- MENU -------")
    print(f"Inventario: {hierbas} Hierba(s) | {frascos} Frasco(s) | ${oro} Moneda(s) de oro")
    print("1) Comprar Hierba ($50 c/u)")
    print("2) Comprar Frasco ($100 c/u)")
    print("3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)")
    print("4) Salir\n")

    opcion_elegida = int(input("Que accion vas a realizar?: "))

    if opcion_elegida == 1:
        cantidad_hierba = int(input("¿Cuanta Hierba desea comprar?: "))
        costo_total = 50 * cantidad_hierba

        if oro >= costo_total:
            hierbas += cantidad_hierba
            oro -= costo_total
            print(f"Has adquirido {cantidad_hierba} hierba(s) al inventario.\n") 

        else:
            print("¡Dinero insuficiente!\n")

    elif opcion_elegida == 2:
        cantidad_frascos = int(input("¿Cuantos Frascos desea comprar?: "))
        costo_total = 100 * cantidad_frascos

        if oro >= costo_total:
            frascos += cantidad_frascos
            oro -= costo_total
            print(f"Has adquirido {cantidad_frascos} frasco(s) al inventario.\n")

        else:
            print("¡Dinero insuficiente!\n")

    elif opcion_elegida == 3:
        if hierbas >= 2 and frascos >= 1:
            hierbas -= 2
            frascos -= 1
            pociones_totales += 1
            print(f"Has fabricado {pociones_totales} pocion(es) de fuego.\n")

        else:
            print("¡Materiales insuficientes!\n")

    elif opcion_elegida == 4:
        break

print("~~~~~~~~~~~ RECUENTO DE INVENTARIO ~~~~~~~~~~\n")
print(f"Fabricaste un total de {pociones_totales} pocion(es) de fuego.")
print(f"Tu oro restante es de ${oro} moneda(s).")