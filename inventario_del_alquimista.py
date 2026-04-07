'''
El jugador debe fabricar 'Pociones de Fuego'. Tienes un inventario inicial con 0 Hierbas y 0 Frascos, y cuentas con $500 monedas de oro.

Menú:
1) Comprar Hierba ($50 c/u)
2) Comprar Frasco ($100 c/u)
3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
4) Salir

Lógica:
- Para comprar, debes validar si tienes dinero suficiente. Si compras, suma al inventario y resta al oro.
- Para fabricar, debes validar si tienes materiales suficientes. Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.
- Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó.
'''

hierbas = 0
frascos = 0
precio_hierba = 50
precio_frasco = 100
pociones_totales = 0

oro = 500

while True :
    print(f"\nHierbas restantes: {hierbas}")
    print(f"Frascos restantes: {frascos}")
    print(f"Pociones fabricadas: {pociones_totales}\n")
    print(f"1) Comprar Hierba (${precio_hierba} c/u)")
    print(f"2) Comprar Frasco (${precio_frasco} c/u)")
    print("3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)")
    print("4) Salir")

    opcion = int (input("Seleccione una opción: "))

    match opcion :
        case 1 :
            if oro < precio_hierba :
                print("No tiene oro suficiente para una hierba.")
            else :
                oro -= precio_hierba
                hierbas += 1

                print("Ha comprado 1 hierba.")
        case 2 :
            if oro < precio_frasco :
                print("No tiene oro suficiente para un frasco.")
            else :
                oro -= precio_frasco
                frascos += 1

                print("Ha comprado 1 frasco.")
        case 3 :
            if hierbas >= 2 and frascos >= 1 :
                hierbas -= 2
                frascos -= 1
                pociones_totales += 1

                print("Ha fabricado 1 poción.")
            else :
                print("No tiene materiales suficientes para fabricar.")
        case 4 :
            break
