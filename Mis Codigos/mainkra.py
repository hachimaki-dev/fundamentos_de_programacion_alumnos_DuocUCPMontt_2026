while True:
    seleccion = int(input("Selecione lo que quiere crear\n1)Espeada \n2)Pico \n3)Salir de la mesa de crafteo"))
    if seleccion == 1:
        print("creando espeada de mainkra")
    elif seleccion == 2:
        print("Creando Pico de mankra")
    elif seleccion == 3:
        print("le saliendo")
        break
    else:
        print("Receta desconocida. Intenta nuevamente")
        continue