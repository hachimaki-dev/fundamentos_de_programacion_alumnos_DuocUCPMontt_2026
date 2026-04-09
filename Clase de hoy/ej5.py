"""
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
"""
Hierba = 0
Frascos = 0
Pociones = 0
Monedas = 500

while True:
    print("""Menú:
1) Comprar Hierba ($50 c/u)
2) Comprar Frasco ($100 c/u)
3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
4) Salir
""")
    answer = int(input())
    if answer == 1:
        if Monedas >= 50:
            Monedas = Monedas - 50
            Hierba = Hierba + 1
            if Hierba == 1:
                print(f"Tienes {Hierba} hierba")
            else:
                print(f"Tienes {Hierba} hierbas")
            print(f"Te queda ${Monedas}")
        else:
            print("No tienes dinero suficiente")
    elif answer == 2:
        if Monedas >= 100:
            Monedas = Monedas - 100
            Frascos = Frascos + 1
            if Frascos == 1:
                print(f"Tienes {Frascos} frasco")
            else:
                print(f"Tienes {Frascos} frascos")
            print(f"Te queda ${Monedas}")
        else:
            print("No tienes dinero suficiente")
    elif answer == 3:
        if Hierba >= 2 and Frascos >= 1:
            Hierba = Hierba - 2
            Frascos = Frascos - 1
            Pociones = Pociones + 1
            if Pociones == 1:
                print(f"Tienes {Pociones} pocion")
            else:
                print(f"Tienes {Pociones} pociones")
        else:
            print("No tienes materiales suficientes")
    elif answer == 4:
        break
    else:
        print("Respuesta no valida")
if Pociones == 1:
    print(f"Lograste hacer {Pociones} pocion y te quedo ${Monedas}")
else:
    print(f"Lograste hacer {Pociones} pociones y te quedo ${Monedas}")