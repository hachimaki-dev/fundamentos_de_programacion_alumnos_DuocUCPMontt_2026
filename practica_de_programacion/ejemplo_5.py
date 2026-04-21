# El jugador debe fabricar 'Pociones de Fuego'. Tienes un inventario inicial con 0 Hierbas y 0 Frascos, y cuentas con $500 monedas de oro.

"""
1) Comprar Hierba ($50 c/u)
2) Comprar Frasco ($100 c/u)
3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
4) Salir

- Para comprar, debes validar si tienes dinero suficiente. Si compras, suma al inventario y resta al oro.
- Para fabricar, debes validar si tienes materiales suficientes. Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.
- Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó.
"""

sequencia_de_tienda = True
monedas_de_oro = 500
hierba = 0
frascos = 0
pociones_de_fuego = 0

print("Bienvenido hechizero")

while sequencia_de_tienda == True:
    print("Seleccione una opcion para continuar (1-4)")
    print("1. Comprar Hierba ($50 c/u)")
    print("2. Comprar Frasco ($100 c/u)")
    print("3. Fabricar Pocion (Requiere 2 Hierbas y un Frasco)")
    print("4. Salir")

    seleccion = int(input("[]: "))
    if seleccion == 1:
        if monedas_de_oro > 0:
            monedas_de_oro -= 50
            hierba += 1
            print("Hierba comprada exitosamente!")
        if monedas_de_oro <= 0:
            print("Oro insuficiente :(")
    if seleccion == 2:
        if monedas_de_oro > 0:
            monedas_de_oro -= 100
            frascos += 1
            print("Frasco comprado exitosamente!")
        if monedas_de_oro <= 0:
            print("Oro insuficiente :/")
    if seleccion == 3:
        if hierba >= 2 and frascos >= 1:
            hierba -= 2
            frascos -= 1
            pociones_de_fuego += 1
            print("Pocion de fuego creada!")
        elif hierba < 2 or frascos < 1:
            print("Ingredientes insuficientes")
    if seleccion == 4:
        break

print(f"Has elaborado {pociones_de_fuego} pociones de fuego y te has sobrado ${monedas_de_oro} monedas de oro!")
