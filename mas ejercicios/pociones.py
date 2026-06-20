""" El jugador debe fabricar 'Pociones de Fuego'. 
Tienes un inventario inicial con 0 Hierbas y 0 Frascos, 
y cuentas con $500 monedas de oro.

Menú:
1) Comprar Hierba ($50 c/u)
2) Comprar Frasco ($100 c/u)
3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
4) Salir

Lógica:
- Para comprar, debes validar si tienes dinero suficiente. 
Si compras, suma al inventario y resta al oro.

- Para fabricar, debes validar si tienes materiales suficientes.
 Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.

- Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó."""

hiervas = 0
frascos = 0
monedas = 500
posiones = 0
menu = 0
while True:
    print(f"tienes {hiervas} hiervas , {frascos} frascos, {monedas} monedas, pociones {posiones}")
    menu = int(input("1.comprar hierba $50 c/u  2.comprar frasco 100$ c/u   3.fabricar pocion: requiere 2 hierbas y un frasco.  4.salir"))

    if monedas > 0 and monedas <= monedas:
        if menu == 1:
            monedas = monedas - 50
            hiervas = hiervas + 1
            print(f"has comprado {hiervas} hiervas")

        elif menu == 2:
            monedas = monedas - 100
            frascos = frascos + 1
            print(f"has comprado {frascos} frasco")
        
        elif menu == 3:
            if hiervas >= 2 and frascos >= 1:
                hiervas = hiervas - 2 
                frascos = frascos - 1
                posiones = posiones + 1
                print(f"has creado {posiones} posiones")
        
        elif menu == 4:
            break
        
        else:
            print("no valido")
            
print(f" pociones = {posiones} , monedas = {monedas}")

