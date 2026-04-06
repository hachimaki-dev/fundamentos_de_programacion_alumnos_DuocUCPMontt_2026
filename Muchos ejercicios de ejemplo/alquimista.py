print("bienvenido")
hierba = 0
frasco = 0
monedas = 500
buyhierba = 50
buyfrasco = 100
pocion = 0
while True :
    print("elija su opcion")
    print("1 - comprar hierba 50c/u")
    print("2 - comprar frasco 100c/u")
    print("3 - fabricar pocion, se necesita 2 hiebas y un frasco")
    print("4 - salir")
    respuesta = int(input("elija su opcion"))
    if respuesta == 1 :
        print("has elejido comprar hiebas")
        if monedas < buyhierba :
            print("no tienes suficientes monedas")
        elif monedas > buyhierba :
            print("has comprado 1 hierba")
            monedas = monedas - buyhierba
            hierba = hierba + 1
            print(f"tienes {hierba} hierba")
            print(f"tienes {monedas} monedas")
    elif respuesta == 2 :
        print("has elegido comprar frasco")
        if monedas < buyfrasco :
            print("no tienes suficientes monedas")
        elif monedas > buyfrasco :
            print("has comprado un frasco")
            monedas = monedas - buyfrasco
            frasco = frasco = 1
            print(f"tienes {frasco} frascos")
            frasco = frasco + 1
            print(f"tienes {monedas} monedas")
    elif respuesta == 3 :
        if hierba >= 2 and frasco >= 1 :
            print("has fabricado una pocion")
            pocion = pocion + 1
            hierba = hierba - 2
            frasco = frasco - 1
            print(f"te quedan {frasco} frascos")
            print(f"te quedan {hierba} hierbas")
            print(f"tienes {pocion} pociones ")
        else :
            print("no puedes hacer pocion te faltan productos")
    elif respuesta == 4 :
        print("has elejido salir")
        print("fin")
        break