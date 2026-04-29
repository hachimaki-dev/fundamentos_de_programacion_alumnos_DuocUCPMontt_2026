ahorro = 0
opcion = 0
while opcion != 3:
    print("--alcancia--")
    print("1 . Ahorrar dinero")
    print("2 . Ver mis ahorros")
    print("3 . Romper la alcancia")
    opcion = int(input("Ingrese una opcion valida (1 al 3)"))
    if opcion == 1:
        dinero = int(input("Cuanto dinero quiere ingresar?"))
        ahorro = dinero + ahorro
    elif opcion == 2:
        print(f"Su ahorro es de {ahorro}")
        if ahorro >= 100:
            print("¡Excelente , tiene buenos ahorros!")
        else :
            print("Siga ahorrando , vas por buen camino")
    elif opcion == 3:
        print("Ha roto la alcancia!")
        break
    else :
        print("Ingrese opcion valida!")