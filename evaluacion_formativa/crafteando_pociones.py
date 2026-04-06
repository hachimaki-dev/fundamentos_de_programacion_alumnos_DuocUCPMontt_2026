#El jugador debe fabricar 'Pociones de Fuego'. Tienes un inventario inicial con 0 Hierbas y 0 Frascos, y cuentas con $500 monedas de oro.
#
#Menú:
#1) Comprar Hierba ($50 c/u)
#2) Comprar Frasco ($100 c/u)
#3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)
#4) Salir
#
#Lógica:
#- Para comprar, debes validar si tienes dinero suficiente. Si compras, suma al inventario y resta al oro.
#- Para fabricar, debes validar si tienes materiales suficientes. Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.
#- Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó.
salir = False
oro_total = 500
hierbas = 0
frascos = 0
pociones_totales = 0


while salir == False:
    eleccion = int(input("Menu: \n1)Comprar hierba ($50 c/u) \n2)Comprar Frasco ($100 c/u) \n3)Fabricar Pocion (Requiere: 2 Hierbas y 1 Frasco) \n4)Salir \nEscoja su opcion: "))
    if eleccion == 1 and oro_total >= 50:
        oro_total = oro_total - 50
        hierbas += 1
        print("compraste una hierba")
    elif eleccion == 2 and oro_total >= 100:
        oro_total = oro_total - 100
        frascos = frascos + 1
        print("compraste un frasco")
    elif eleccion == 3 and hierbas >= 2 and frascos >= 1:
        pociones_totales = pociones_totales + 1
        hierbas = hierbas - 2
        frascos = frascos - 1
        print("creaste una pocion")
    elif eleccion == 4:
        print("Saliste")
        salir = True
    else:
        print("opcion no valida")
    print(f"inventario: \nHierbas: {hierbas}\nFrascos: {frascos} \nPociones: {pociones_totales} \nOro: {oro_total}")

print(f"creaste un total de {pociones_totales} pociones y te quedo {oro_total} monedas de oro")