
while True: #ciclo infinito
    print("----Abriendo Mesa de crafteo----")
    print("\n ¿Que desea hacer?")
    print("1. Craftear Espada de Diamante")
    print("2. Craftear Pico")
    print("3. Salir de la Mesa de Crafteo")

    opcion = int(input("Eliga una opcion: "))
    if opcion == 1:
        print("¡Espada crafteada!")
    elif opcion == 2:
        print("¡Pico listo!")
    if opcion != 1 and opcion != 2 and opcion != 3: #si ninguna opcion es valida
        print("Receta desconocida. Intenta nuevamente.")
    elif opcion == 3:
        print("\n----Saliendo de la mesa de crafteo----")
        break
        
    





        


