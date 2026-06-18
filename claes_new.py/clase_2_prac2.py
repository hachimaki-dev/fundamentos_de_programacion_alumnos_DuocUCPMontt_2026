lista_de_todos_los_bichos = []

def mostrar_menu():

    print("============================ Menú ============================")
    print("1. Ingresar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estado de todos los bichos (si es peligroso o no)")
    print("5. Mostrar todos los bichos")
    print("6. Salir")
    print("==============================================================")

def opcion_menu_usuario():
    while True:
        opcion_elegida = input("Ingrese su opción (1 al 6): ")
        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida
        else:
            print("Opción inválida, vuelva a intentarlo")

def validar_nombre_bicho():
    while True:
        nombre_bicho = input("Ingrese nombre del bicho: ")
        if " " in nombre_bicho or len(nombre_bicho) <= 0:
            print("Nombre inválido, vuelva a intentar")
        else:
            return nombre_bicho

def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del bicho: "))
            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("La longitud debe ser mayor que cero")
        except ValueError:
            print("Valor no válido")

def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese el nivel de peligrosidad del bicho (1 a 10): "))
            if 1.0 <= peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("La peligrosidad debe estar entre 1 y 10")
        except ValueError:
            print("Valor no válido")

def agregar_bicho():

    nombre_bicho = validar_nombre_bicho()
    longitud_bicho = validar_longitud_bicho()
    peligrosidad_bicho = validar_peligrosidad_bicho()

    datos_de_bicho = {
        "nombre_bicho": nombre_bicho,
        "longitud_bicho": longitud_bicho,
        "peligrosidad_bicho": peligrosidad_bicho,
        "es_peligroso": False
    }
    lista_de_todos_los_bichos.append(datos_de_bicho)
    print("Bicho agregado correctamente")

def mostrar_todos_los_bichos():

    if len(lista_de_todos_los_bichos) == 0:
        print("No hay bichos registrados")
    else:
        for bicho in lista_de_todos_los_bichos:
            print("--------------------")
            print("Nombre:", bicho["nombre_bicho"])
            print("Longitud:", bicho["longitud_bicho"])
            print("Peligrosidad:", bicho["peligrosidad_bicho"])
            print("¿Es peligroso?:", bicho["es_peligroso"])

#def buscar_bicho():
#    nombre_buscado = input("Ingrese el nombre del bicho a buscar: ")
#    for cada_bicho in lista_de_todos_los_bichos:
#        if cada_bicho["nombre_bicho"] == nombre_buscado:
#            print("Existe!!!!")
#            print(f"Bicho encontrado")
#            print(f"Su nombre {cada_bicho["nombre_bicho"]}")
#            print(f"Su longitud_bicho {cada_bicho["longitud_bicho"]}")
#            print(f"Su peligrosidad_bicho {cada_bicho["peligrosidad_bicho"]}")
#        else:
#            print("Bicho no encontrado lastimosamente :´()")

def buscar_bichos_por_nombre(nombre_del_bicho_a_buscar):
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["nombre_bicho"] == nombre_del_bicho_a_buscar:
            print("Encontrado")
            indice_encontrado = lista_de_todos_los_bichos
            return indice_encontrado

def iniciar_programa():

    while True:
        mostrar_menu()
        opcion_menu_seleccionada = opcion_menu_usuario()
        if opcion_menu_seleccionada == "1":
            agregar_bicho()
        elif opcion_menu_seleccionada == "2":
            nombre_bicho_buscar = print("Se manda a llamar la función que busca: ")
            indice_bicho_encontrado = buscar_bicho(nombre_bicho_buscar)
            buscar_bichos_por_nombre()
        elif opcion_menu_seleccionada == "3":
            print("Se manda a llamar la función que elimina")
        elif opcion_menu_seleccionada == "4":
            print("Se manda a llamar la función que actualiza el estado")
        elif opcion_menu_seleccionada == "5":
            mostrar_todos_los_bichos()
        elif opcion_menu_seleccionada == "6":
            print("Adiós")
            break

iniciar_programa()