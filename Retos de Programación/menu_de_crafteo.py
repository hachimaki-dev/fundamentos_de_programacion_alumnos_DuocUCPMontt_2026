print("==========Mesa de Crafteo========")

while True:
    print("1. Craftear Espada de Diamante")
    print("2 .Craftear Pico")
    print("3 .Salir de la Mesa de Crafteo")
    opcion_del_jugador = int(input("Ingrese la accion que desea realizar(1/2/3):   "))
    if opcion_del_jugador == 3:
        print("saliste de la mesa de crafteo")
        break
    elif opcion_del_jugador == 1:
        print("¡Espada crafteada!")
    elif opcion_del_jugador == 2:
        print("¡Pico listo!")
    else:
        print("Receta desconocida")
        continue
