lista_de_todos_los_bichos = []


def mostrar_menu():
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("7. Insertar datos de prueba")


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_de_usuario = leer_opcion()

        if opcion_de_usuario == "1":
            agregar_bicho()
        elif opcion_de_usuario == "2":
            nombre_a_buscar = input("Ingres el nombre del bicho que desea buscar: \n")
            indice_del_bicho = buscar_bicho_por_nombre(nombre_a_buscar)
            if indice_del_bicho is not None:
                print("Bicho encontrado")
            else:
                print("Este no existe")

        elif opcion_de_usuario == "3":
            nombre_del_bicho_a_eliminar = input("Ingrese el nombre del bicho que desea eliminar: \n")
            fue_eliminado = eliminar_bicho_por_nombre(nombre_del_bicho_a_eliminar)
            if fue_eliminado == True:
                print("Se elimino")
            else:
                print("no se pudo eliminar")
        elif opcion_de_usuario == "4":
            actualizar_si_es_peligroso()
            print("Se han actualiado todos los bichos peligrosos")
        elif opcion_de_usuario == "5":
            mostrar_todos_los_bichos()
        elif opcion_de_usuario == "6":
            print("LLAMAR A LA FUNCION QUE FINALIZA EL PROGRAMA")
            break
        elif opcion_de_usuario == "7":
            insertar_datos_de_prueba()
        else:
            print("Opcion invalida, vuelva a intentarlo")


def mostrar_todos_los_bichos():
    print(lista_de_todos_los_bichos)


def leer_opcion():
    while True:
        opcion_ingresada = input("Seleccione una opción: ")

        if opcion_ingresada in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion_ingresada
        else:
            print("La opción ingresada no es válida. Vuelva a intentar.")


def validar_nombre_especie():
    while True:
        nombre_especie = input("Ingrese la especie del bicho:\n")

        if " " in nombre_especie or len(nombre_especie) <= 0:
            print("El nombre de la especie no es válido, ingrese uno válido")
        else:
            return nombre_especie


def validar_longitud_especie():
    while True:
        try:
            longitud_especie = int(input("Ingrese el tamaño de la especie:\n"))

            if longitud_especie <= 0:
                print("La longitud debe ser mayor que 0")
            else:
                return longitud_especie

        except ValueError:
            print("Ingrese un número válido")


def validar_peligrosidad_especie():
    while True:
        try:
            peligrosidad_especie = float(
                input("Ingrese la peligrosidad de la especie:\n")
            )

            if peligrosidad_especie <= 0:
                print("La peligrosidad debe ser mayor que 0")
            else:
                return peligrosidad_especie

        except ValueError:
            print("Ingrese un número válido")


def registrar_especie(diccionario_de_la_especie):
    lista_de_todos_los_bichos.append(diccionario_de_la_especie)
    print("El bicho se registró de forma exitosa")
    return True


def agregar_bicho():
    # Nombre o especie del bicho
    # Tamaño del bicho int
    # Peligrosidad 1 a 10 float
    # El programa determina si es o no peligroso.
    # Mayores a 7.0 lo son.

    nombre_especie_validado = validar_nombre_especie()
    longitud_especie_validada = validar_longitud_especie()
    peligrosidad_especie_validada = validar_peligrosidad_especie()

    print(
        f"Los datos son: Nombre {nombre_especie_validado}, "
        f"su longitud es {longitud_especie_validada} "
        f"y su peligrosidad es {peligrosidad_especie_validada}"
    )

    datos_de_la_especie = {
        "nombre_especie": nombre_especie_validado,
        "longitud_especie": longitud_especie_validada,
        "peligrosidad_especie": peligrosidad_especie_validada,
        "es_peligroso": False,
    }

    se_registro = registrar_especie(datos_de_la_especie)

    if se_registro:
        print("Se registró de forma correcta")
        return True
    else:
        print("Algo inesperado sucedió")
        return False

def buscar_bicho_por_nombre(nombre_del_bicho_a_buscar_por_parametro):
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["nombre_especie"] == nombre_del_bicho_a_buscar_por_parametro:
            print("existe")
            indice_bicho_encontrado = lista_de_todos_los_bichos.index(cada_bicho)
            return indice_bicho_encontrado

def eliminar_bicho_por_nombre(nombre_del_bicho_a_buscar_por_parametro):
    indice_del_bicho_a_buscar = buscar_bicho_por_nombre(nombre_del_bicho_a_buscar_por_parametro)
    if indice_del_bicho_a_buscar is not None:
        if lista_de_todos_los_bichos.pop(indice_del_bicho_a_buscar):
            print("Eliminado")
            return True
        else:
            print("no se pudo eliminar")
            return False


def actualizar_si_es_peligroso():
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["peligrosidad_especie"] >= 7.0:
            print("Es peligroso, entonces actualicemos su estado")
            cada_bicho["es_peligroso"] = True

def insertar_datos_de_prueba():
    lista_de_todos_los_bichos.append({
        "nombre_especie": "mariposa",
        "longitud_especie": 5,
        "peligrosidad_especie": 9.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_especie": "gusano",
        "longitud_especie": 8,
        "peligrosidad_especie": 2.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_especie": "pulga",
        "longitud_especie": 1,
        "peligrosidad_especie": 8.9,
        "es_peligroso": False,
    })

iniciar_programa()