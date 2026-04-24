print("bienvenido")
while True :

    print("1. Craftear Espada de Diamante")
    print("2. Craftear Pico")
    print("3. Salir de la mesa de crafteo")

    opcion = int(input("selecciona una opcion: "))

    if opcion == 1:
        print("espada crafteada")
    elif opcion == 2:
        print("Pico crafteado")
    elif opcion == 3:
        break

    else:
        print("Receta desconocida(intentalo denuevo)")