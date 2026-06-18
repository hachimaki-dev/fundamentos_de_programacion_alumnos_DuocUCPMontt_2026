lista_de_todos_los_bichos = []


def mostrar_menu():
    print("1. Ingresar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estado de todos los bichos (si es peligroso o no)")
    print("5. Mostrar todos los bichos")
    print("6. Salir")


def opcion_menu_usuario():
    while True:
        opcion_elegida = input("Ingrese su opción (1 al 6): ")

        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida
        else:
            print("Opción inválida, vuelva a intentarlo")


def validar_nombre_bicho():
    while True:
        nombre_bicho = input("Ingrese nombre del bicho:\n")

        if " " in nombre_bicho or len(nombre_bicho) <= 0:
            print("Nombre inválido, vuelva a intentar")
        else:
            return nombre_bicho


def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del bicho:\n"))

            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("La longitud debe ser mayor que cero")

        except ValueError:
            print("Valor no válido")


def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(
                input("Ingrese el nivel de peligrosidad del bicho:\n")
            )

            if 1.0 <= peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("La peligrosidad del bicho debe estar entre 1.0 y 10.0")

        except ValueError:
            print("Valor no válido")


def agregar_bicho():
    nombre_bicho_validado = validar_nombre_bicho()
    longitud_bicho_validada = validar_longitud_bicho()
    peligrosidad_bicho_validada = validar_peligrosidad_bicho()

    datos_de_bicho = {
        "nombre_bicho": nombre_bicho_validado,
        "longitud_bicho": longitud_bicho_validada,
        "peligrosidad_bicho": peligrosidad_bicho_validada,
        "es_peligroso": False
    }

    lista_de_todos_los_bichos.append(datos_de_bicho)


def mostrar_todos_los_bichos():
    print(lista_de_todos_los_bichos)


def buscar_bicho():
    nombre_bicho_a_buscar = input("Ingrese el nombre del bicho: ")

    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["nombre_bicho"] == nombre_bicho_a_buscar:
            print("Bicho encontrado\n")
            print(f"Su nombre: {cada_bicho['nombre_bicho']}")
            print(f"Su longitud_bicho: {cada_bicho['longitud_bicho']}")
            print(f"Su peligrosidad_bicho: {cada_bicho['peligrosidad_bicho']}")
        else:
            print("Bicho no encontrado")


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_seleccionada = opcion_menu_usuario()

        if opcion_menu_seleccionada == "1":
            agregar_bicho()

        elif opcion_menu_seleccionada == "2":
            buscar_bicho()

        elif opcion_menu_seleccionada == "3":
            print("Se manda a llamar la función que elimina")

        elif opcion_menu_seleccionada == "4":
            print("Se manda a llamar la función que actualiza el estado")

        elif opcion_menu_seleccionada == "5":
            mostrar_todos_los_bichos()

        elif opcion_menu_seleccionada == "6":
            print("Adiós")
            break

        else:
            print("La opción ingresada no es una opción válida")


iniciar_programa()