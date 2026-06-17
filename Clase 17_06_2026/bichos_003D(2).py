lista_de_todos_los_bichos = []

def mostrar_menu():
    print("1. Ingresar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados (nivel de peligrosidad)")
    print("5. Mostar todos los bichos")
    print("6. Salir")
    print("7. Insertar datos de prueba")

def leer_opcion_usuario_menu():
    while True:
        opcion_ingresada = input("Ingrese su opción: ")
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion_ingresada
        else:
            print("Opcion invalida, vuelva a intentar")

def validar_nombre_bicho():
    especie_bicho = input("Ingrese la especie del bicho: ")
    if len(especie_bicho) <= 0 or " " in especie_bicho:
        print("El nombre de la especie no es valido")
    else:
        return especie_bicho

def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del bicho: "))
            if longitud_bicho <= 0:
                print("Ingrese una longitud superior a 0")
            else:
                return longitud_bicho
        except ValueError:
            print("Valor invalido, inserte un número entero")

def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese la peligrosidad del bicho: "))
            if peligrosidad_bicho >= 1.0 and peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("Por favor ingrese un rango valido (entre 1.0 y 10.0)")
        except ValueError:
            print("Valor invalido, inserte un número decimal o entero")

def agregar_bicho():
    especie_bicho_validado = validar_nombre_bicho()
    longitud_bicho_validada = validar_longitud_bicho()
    peligrosidad_bicho_validada = validar_peligrosidad_bicho()
    
    print(f"El nombre del bicho es {especie_bicho_validado} su tamaño es {longitud_bicho_validada} y su nivel de peligrosidad es: {peligrosidad_bicho_validada}")

    datos_del_bicho = {
        "especie_bicho": especie_bicho_validado,
        "longitud_bicho": longitud_bicho_validada,
        "peligrosidad_bicho": peligrosidad_bicho_validada,
        "es_peligroso": False
    }

    lista_de_todos_los_bichos.append(datos_del_bicho)


def buscar_bicho_por_nombre(nombre_de_la_especie_a_buscar):
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["especie_bicho"] == nombre_de_la_especie_a_buscar:
            print("Existe")
            indice_bicho = lista_de_todos_los_bichos.index(cada_bicho)
            return indice_bicho

def eliminar_bicho_por_nombre(nombre_de_la_especie_a_buscar):
    indice_del_bicho_encontrado = buscar_bicho_por_nombre(nombre_de_la_especie_a_buscar)
    if indice_del_bicho_encontrado is not None:
        lista_de_todos_los_bichos.pop(indice_del_bicho_encontrado)
        return True


def insertar_datos_de_prueba():
    lista_de_todos_los_bichos.append({
        "especie_bicho": "mariposa",
        "longitud_bicho": 5,
        "peligrosidad_bicho": 9.2,
        "es_peligroso": False
    })

    lista_de_todos_los_bichos.append({
        "especie_bicho": "gusano",
        "longitud_bicho": 8,
        "peligrosidad_bicho": 8.2,
        "es_peligroso": False
    })

    lista_de_todos_los_bichos.append({
        "especie_bicho": "garrapata",
        "longitud_bicho": 9,
        "peligrosidad_bicho": 9.2,
        "es_peligroso": False
    })

def actualizar_estado_de_peligrosidad():
    for cada_bicho in lista_de_todos_los_bichos :
        if cada_bicho["peligrosidad_bicho"] >= 7.0:
            cada_bicho["es_peligroso"] = True

def mostrar_todos_los_bichos():
    print(lista_de_todos_los_bichos)

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_usuario_validada = leer_opcion_usuario_menu()

        if opcion_menu_usuario_validada == "1":
            agregar_bicho()
        elif opcion_menu_usuario_validada == "2":
            nombre_especie_a_buscar = input("Ingrese nombre de la especie a buscar: \n")
            indice_encontrado = buscar_bicho_por_nombre(nombre_especie_a_buscar)

            if indice_encontrado is not None:
                print("Lo encontramos!")
                print(f"Nombre especie: {lista_de_todos_los_bichos[indice_encontrado]["especie_bicho"]}")
                print(f"Longitud especie: {lista_de_todos_los_bichos[indice_encontrado]["longitud_bicho"]}")
                print(f"Peligrosidad especie: {lista_de_todos_los_bichos[indice_encontrado]["peligrosidad_bicho"]}")
                print(f"Si es peligrosa o no : {lista_de_todos_los_bichos[indice_encontrado]["es_peligroso"]}")
            else:
                print("No hay datos de esta especie")

        elif opcion_menu_usuario_validada == "3":
            nombre_del_bicho_a_eliminar = input("Ingrese nombre del bicho que desea eliminar")
            se_elimino = eliminar_bicho_por_nombre(nombre_del_bicho_a_eliminar)
            if se_elimino is not None:
                print("Se elimino con exito")
            else:
                print("No se puede elimiar algo que no existe")
        elif opcion_menu_usuario_validada == "4":
            actualizar_estado_de_peligrosidad()
        elif opcion_menu_usuario_validada == "5":
            mostrar_todos_los_bichos()
        elif opcion_menu_usuario_validada == "6":
            print("Salimos")
            break
        elif opcion_menu_usuario_validada == "7":
            insertar_datos_de_prueba()
        else:
            print("Opcion no permitida")

iniciar_programa()