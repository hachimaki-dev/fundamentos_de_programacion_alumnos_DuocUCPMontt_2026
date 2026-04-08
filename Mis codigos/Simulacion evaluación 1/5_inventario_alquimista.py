# 5. Inventario del Alquimista (Crafting)
# El jugador debe fabricar 'Pociones de Fuego'. Tienes un inventario inicial con 0 Hierbas y 0 Frascos, y cuentas con $500 monedas de oro.

# Menú:
# 1) Comprar Hierba ($50 c/u)
# 2) Comprar Frasco ($100 c/u)
# 3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
# 4) Salir

# Lógica:
# - Para comprar, debes validar si tienes dinero suficiente. Si compras, suma al inventario y resta al oro.
# - Para fabricar, debes validar si tienes materiales suficientes. Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.
# - Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó.

print(" INVENTARIO DEL ALQUIMISTA ".center(40, "-"))

contador_hierbas = 0
contador_frascos = 0
contador_pociones = 0
monedas_de_oro = 500
opcion_elegida = 0

while True:
    print("-----------------------------")
    print("             MENU")
    print("1) Comprar Hierba ($50 c/u)\n2) Comprar Frasco ($100 c/u)\n3) Fabricar Pocion\n4) Salir")
    print("-----------------------------")

    opcion_elegida = int(input("Ingrese una opcion: "))
    if opcion_elegida == 1:
        if monedas_de_oro >= 50:
            monedas_de_oro -= 50
            contador_hierbas += 1
            print(f"\n¡Has comprado una hierba! | Stock de hierbas: {contador_hierbas}")
        else:
            print(f"\nNo tienes monedas suficientes para comprar una hierba\nMonedas restantes: {monedas_de_oro}")
    elif opcion_elegida == 2:
        if monedas_de_oro >= 100:
            monedas_de_oro -= 100
            contador_frascos += 1
            print(f"\n¡Has comprado un frasco! | Stock de frascos: {contador_frascos}")
        else:
            print(f"\nNo tienes monedas suficientes para comprar un frasco\nMonedas restantes: {monedas_de_oro}")
    elif opcion_elegida == 3:
        if contador_hierbas >= 2 and contador_frascos >=1:
            contador_hierbas -= 2
            contador_frascos -= 1
            contador_pociones += 1
            print("\n¡Pocion fabricada!")
        else:
            print("\nMaterial insuficiente\nPara fabricar una pocion necesitas 2 hierbas y un frasco")
            print(f"Actualmente tienes: {contador_hierbas} hierbas y {contador_frascos} frascos")
    elif opcion_elegida == 4:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nIngrese una opcion valida")

print("\n----------------------------")
print("         INVENTARIO")
print(f"Hierbas: {contador_hierbas}\nFrascos: {contador_frascos}\nPociones: {contador_pociones}\nMonedas de Oro: {monedas_de_oro}")
print("----------------------------")
