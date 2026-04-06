hierba=0
frascos=0
monedas=500
pociones_totales=0
print("Fuiste al mercado para comprar utiles para hacer pociones de fuego para tu tienda de alquimia, para hacer una pocion de fuego necesitas un frasco y dos hierbas")
while monedas >0:
    print("==========================")
    print("Para hacer la pocion necestias un frasco y dos hierbas")
    print(f"inventario monedas {monedas} frascos: {frascos} hierbas: {hierba} pociones: {pociones_totales}")
    print("1-Comprar frasco = 100$ ")
    print("2-Comprar hierba = 50$ ")
    print("3-Fabricar la pocion ")
    print("4-Salir ")
    print("===========================")
    decidir=int(input("Que desea hacer: "))
    if decidir==1:
        print("Has comprado un frasco")
        frascos+=1
        monedas-=100
        print(f"Te quedan {monedas} monedas")
    elif decidir==2:
        print("Has comprado una hierba")
        hierba+=1
        monedas-=50
        print(f"Te quedan {monedas} monedas")
    elif decidir==3:
        if frascos <1 and hierba<2:
            print("Te falta todo")
        elif frascos < 1:
            print("Te faltan frascos")
        elif hierba < 2:
            print("Te faltan hierbas")
        else:
            print("Has hecho una pocion ")
            pociones_totales +=1
    elif decidir >= 5:
        print("Elija una opcion valida")
    elif decidir<=0:
        print("Elija una opcion valida")
    else:
        print("Has salido de la tienda...")
        break
print(f"Te has quedado sin monedas y sales de la tienda has hecho {pociones_totales} pociones")
print(f"tu inventario ==hierbas: {hierba}== ==frascos: {frascos}== ==monedas: {monedas}== ==pociones: {pociones_totales}==")
print("====fin del juego====")
