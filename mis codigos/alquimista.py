hierbas = 0
frascos = 0
oro = 500
costo_hierba = 50
costo_frasco = 100
pociones_de_fuego = 0
while True:
    menu = input("Elige tu acción: 1) Comprar hierba 2) Comprar frasco 3) Fabricar Pocion 4) Salir: ")
    if menu == "1":
        if oro >= costo_hierba:
            hierbas += 1
            oro -= costo_hierba
            print("Has comprado una hierba. Hierbas: ", hierbas, "Oro restante: ", oro)
        else:
            print("No tienes suficiente oro para comprar una hierba.")
    elif menu == "2":
        if oro >= costo_frasco:
            frascos += 1
            oro -= costo_frasco
            print("Has comprado un frasco. Frascos: ", frascos, "Oro restante: ", oro)
        else:
            print("No tienes suficiente oro para comprar un frasco.")
    elif menu == "3":
        if hierbas >= 2 and frascos >= 1:
            hierbas -= 2
            frascos -= 1
            pociones_de_fuego += 1
            print("Has fabricado una poción. Hierbas restantes: ", hierbas, "Frascos restantes: ", frascos)
        else:
            print("No tienes suficientes recursos para fabricar una poción.")
    elif menu == "4":
        print("Adiós, alquimista. Has fabricado ", pociones_de_fuego, " pociones de fuego. Te queda ", oro, " de oro.")
        break
    else:
        print("Opción no válida.")