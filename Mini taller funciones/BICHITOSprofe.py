lista_de_todos_los_bichos = []
def mostrar_menu_principal():
    print("1. Ingresar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estado de peligrosidad")
    print("5. Mostrar todos los bichos")
    print("6. Salir")
    print("7. Rellenar")
def opcion_menu_elegida():
    while True:
        opcion_elegida = input("Ingrese una opción: ")
        if opcion_elegida in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion_elegida
        else:
            print("Opción inválida, intente nuevamente")
def validar_nombre_bicho():
    while True:
        nombre_bicho = input("Ingrese nombre del bicho: ")
        if len(nombre_bicho) <= 0:
            print("Nombre inválido, intente nuevamente")
        else:
            return nombre_bicho
def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese la longitud del bicho: "))
            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("Longitud inválida, ingrese una longitud superior a cero")
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")
def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(
                input("Ingrese la peligrosidad del bicho: ")
            )
            if 1.0 <= peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print(
                    "Peligrosidad inválida, ingrese un valor entre 1.0 y 10.0"
                )
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")
def agregar_bicho():
    nombre_bicho_validado = validar_nombre_bicho()
    longitud_bicho_validada = validar_longitud_bicho()
    peligrosidad_bicho_validada = validar_peligrosidad_bicho()
    datos_bicho = {
        "nombre_bicho": nombre_bicho_validado,
        "longitud_bicho": longitud_bicho_validada,
        "peligrosidad_bicho": peligrosidad_bicho_validada,
        "es_peligroso": False,
    }
    lista_de_todos_los_bichos.append(datos_bicho)
def buscar_bicho_por_nombre(nombre_del_bicho_por_parametro):
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["nombre_bicho"] == nombre_del_bicho_por_parametro:
            indice_bicho = lista_de_todos_los_bichos.index(cada_bicho)
            return indice_bicho
def actualiza_peligrosidad():
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["peligrosidad_bicho"] >= 7.0:
            cada_bicho["es_peligroso"] = True
def eliminar_bicho_por_nombre(nombre_del_bicho_por_parametro):
    respuesta_indice = buscar_bicho_por_nombre(nombre_del_bicho_por_parametro)
    if lista_de_todos_los_bichos.pop(respuesta_indice) :
        return True
    else:
        False
def mostrar_todos_los_bichos():
    print(lista_de_todos_los_bichos)
def rellenarLista():
    lista_de_todos_los_bichos.append({
        "nombre_bicho": "mantis",
        "longitud_bicho": 10,
        "peligrosidad_bicho": 9.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_bicho": "mosquito",
        "longitud_bicho": 10,
        "peligrosidad_bicho": 9.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_bicho": "pulga",
        "longitud_bicho": 10,
        "peligrosidad_bicho": 1.9,
        "es_peligroso": False,
    })
def iniciar_programa():
    while True:
        mostrar_menu_principal()
        opcion_elegida_validada = opcion_menu_elegida()
        if opcion_elegida_validada == "1":
            agregar_bicho()
        elif opcion_elegida_validada == "2":
            nombre_del_bicho = input("Ingrese nombre del bicho")
            respuesta_buscando_bicho = buscar_bicho_por_nombre(nombre_del_bicho)
            if respuesta_buscando_bicho is not None:
                print(f"Nombre de la especie: {lista_de_todos_los_bichos[respuesta_buscando_bicho]["nombre_bicho"]}")
                print(f"Longitud de la especie: {lista_de_todos_los_bichos[respuesta_buscando_bicho]["longitud_bicho"]}")
                print(f"Peligrosidad de la especie: {lista_de_todos_los_bichos[respuesta_buscando_bicho]["peligrosidad_bicho"]}")
                print(f"Es peligroso?: {lista_de_todos_los_bichos[respuesta_buscando_bicho]["es_peligroso"]}")
            else:
                print("Ese nombre de bicho no existe")
        elif opcion_elegida_validada == "3":
            nombre_del_bicho = input("Ingrese nombre del bicho")
            respuesta_eliminando_bicho = eliminar_bicho_por_nombre(nombre_del_bicho)
            if respuesta_eliminando_bicho == True:
                print("Bicho eliminado")
            else:
                print("No se puede eliminar un bicho que no existe")
        elif opcion_elegida_validada == "4":
            actualiza_peligrosidad()

        elif opcion_elegida_validada == "5":
            mostrar_todos_los_bichos()

        elif opcion_elegida_validada == "6":
            print("Salimos")
            break
        elif opcion_elegida_validada == "7":
            print("Rellenando")
            rellenarLista()
        else:
            print("Opción inválida, vuelva a intentarlo")
iniciar_programa()