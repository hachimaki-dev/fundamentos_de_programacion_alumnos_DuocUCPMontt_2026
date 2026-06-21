lista_de_todos_los_animales = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1- Registrar animal")
    print("2- Buscar animal")
    print("3- Eliminar animal")
    print("4- Actualizar alertas")
    print("5- Mostrar animales")
    print("6- Salir")
    print("=====================================")

def leer_opcion_usuario_menu():
    while True:
        opcion_ingresada = input("Ingrese su opcion: ")
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6"]:
            return opcion_ingresada
        else:
            print("Opcion invalida. vuelva a intentar")

def validar_nombre_animal():
    nombre_animal = input("Ingrese el nombre del animal: ")
    if len(nombre_animal.strip()) <= 0:
        print("Error, el nombre no puede estar vacio")
        return None
    else:
        return nombre_animal

def validar_especie_animal():
    especie_animal = input("Ingrese la especie del animal: ")
    if len(especie_animal.strip()) <= 0:
        print("Error, la especie del animal no puede estar vacio")
        return None
    else:
        return especie_animal 

def validar_peso_animal():
    try:
        peso_ingresado = float(input("Ingrese el peso del animal en kg: "))
        if peso_ingresado > 0:
            return peso_ingresado
        else:
            print("Error, el peso debe ser mayor a 0")
            return None
    except ValueError:
        print("Valor invalido")
        return None

def registrar_animal():
    nombre_validado = validar_nombre_animal()
    if nombre_validado is None:
        return
    
    especie_validada = validar_especie_animal()
    if especie_validada is None:
        return
    
    peso_validado = validar_peso_animal()
    if peso_validado is None:
        return
    
    datos_animal = {
        "nombre" : nombre_validado,
        "especie" : especie_validada,
        "peso" : peso_validado,
        "alerta" : False
    }
    lista_de_todos_los_animales.append(datos_animal)
    print("Animal registrado exitosamente")

def buscar_animal():
    nombre_a_buscar = input("Ingrese el nombre del animal a buscar: ")
    posicion = 0

    for cada_animal in lista_de_todos_los_animales:
        if cada_animal["nombre"].lower() == nombre_a_buscar.lower():
            return posicion
        posicion = posicion + 1
    return -1

def eliminar_animal():
    nombre_a_eliminar = input("Ingrese el nombre del animal a eliminar: ")
    posicion_encontrada = -1
    posicion_actual = 0

    for cada_animal in lista_de_todos_los_animales:
        if cada_animal["nombre"].lower() == nombre_a_eliminar.lower():
            posicion_encontrada = posicion_actual
        posicion_actual = posicion_actual + 1
    
    if posicion_actual != -1:
        lista_de_todos_los_animales.pop(posicion_encontrada)
        print(f"El animal {nombre_a_eliminar} fue eliminado")
    else:
        print(f"El animal {nombre_a_eliminar} no se encuentra en nuestro sistema")

def actualizar_alertas():
    for cada_animal in lista_de_todos_los_animales:
        if cada_animal["peso"] < 3.0:
            cada_animal["alerta"] = True
        else:
            cada_animal["alerta"] = False

def mostrar_todos_los_animales():
    actualizar_alertas()
    print("LISTA DE ANIMALES")

    for cada_animal in lista_de_todos_los_animales:
        print(f"Nombre: {cada_animal['nombre']}")
        print(f"Especie: {cada_animal['especie']}")
        print(f"Peso: {cada_animal['peso']} kg")

        if cada_animal["alerta"] == True:
            print("Estado: Alerta")
        else:
            print("Estado: Normal")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_usuario_validada = leer_opcion_usuario_menu()

        if opcion_menu_usuario_validada == "1":
            registrar_animal()
        elif opcion_menu_usuario_validada == "2":
            print("Buscar animal")
            posicion_recibida = buscar_animal()

            if posicion_recibida != -1:
                print(f"Animal encontrado en la posicion {posicion_recibida}")
            else:
                print("El animal no se encuentra registrado")
        elif opcion_menu_usuario_validada == "3":
            eliminar_animal()
        elif opcion_menu_usuario_validada == "4":
            actualizar_alertas()
            print("Alertas de peso actualizadas correctamente")
        elif opcion_menu_usuario_validada == "5":
            mostrar_todos_los_animales()
        elif opcion_menu_usuario_validada == "6":
            print("Gracias por usar el sistema. Hasta pronto")
            break

iniciar_programa()

#Listo