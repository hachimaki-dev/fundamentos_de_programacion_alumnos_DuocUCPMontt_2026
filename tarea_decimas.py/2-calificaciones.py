lista_de_calificaciones = []

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1- Agregar registro")
    print("2- Buscar registro")
    print("3- Eliminar registro")
    print("4- Actualizar estados")
    print("5- Mostrar registros")
    print("6- Salir")
    print("==========================")

def leer_opcion_usuario_menu():
    while True:
        opcion_ingresada = input("Ingrese su opcion (1 al 6): ")
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6"]:
            return opcion_ingresada
        else:
            print("Opcion invalida. vuelva a intentar")

def validar_nombre_estudiante():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    if len(nombre_estudiante.strip()) < 0:
        print("Error, el nombre no puede estar vacio")
        return None
    else:
        return nombre_estudiante 

def validar_asignatura_estudiante():
    asignatura_estudiante = input("Ingrese la asignatura del estudiante: ")
    if len(asignatura_estudiante.strip()) < 0:
        print("Error, la asignatura del estudiante no puede estar vacia")
        return None
    else:
        return asignatura_estudiante

def validar_nota_estudiante():
    try:
        nota_ingresada = float(input("Ingrese la nota del estudiante: "))
        if nota_ingresada >= 1.0 and nota_ingresada <= 7.0:
            return nota_ingresada
        else:
            print("Error, la nota debe ser del 1.0 al 7.0")
            return None
    except ValueError:
        print("valor invalido")
        return None

def agregar_registro():
    nombre_validado = validar_nombre_estudiante()
    if nombre_validado is None:
        return
    
    asignatura_validada = validar_asignatura_estudiante()
    if asignatura_validada is None:
        return
    
    nota_validada = validar_nota_estudiante()
    if nota_validada is None:
        return
    
    datos_del_estudiante = {
        "nombre" : nombre_validado,
        "asignatura" : asignatura_validada,
        "nota" : nota_validada,
        "aprobado" : False
    }
    lista_de_calificaciones_global = lista_de_calificaciones
    lista_de_calificaciones_global.append(datos_del_estudiante)
    print("Registro agregado exitosamente")

def buscar_registro():
    nombre_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    posicion = 0

    for cada_registro in lista_de_calificaciones:
        if cada_registro["nombre"].lower() == nombre_a_buscar.lower():
            return posicion
        posicion = posicion + 1
    return -1

def eliminar_registro():
    nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    posicion_encontrada = -1
    posicion_actual = 0

    for cada_registro in lista_de_calificaciones:
        if cada_registro["nombre"].lower() == nombre_a_eliminar.lower():
            posicion_encontrada = posicion_actual
        posicion_actual = posicion_actual + 1

    if posicion_encontrada != -1:
        lista_de_calificaciones.pop(posicion_encontrada)
        print(f"El registro de {nombre_a_eliminar} fue eliminado")
    else:
        print(f"El registro de {nombre_a_eliminar} no se encuentra en el sistema")

def actualizar_estados():
    for cada_registro in lista_de_calificaciones:
        if cada_registro["nota"] >= 4.0:
            cada_registro["aprobado"] = True
        else:
            cada_registro["aprobado"] = False

def mostrar_todos_los_registro():
    actualizar_estados()
    print("Lista de registros")
    
    for cada_registro in lista_de_calificaciones:
        print(f"Nombre: {cada_registro['nombre']}")
        print(f"Asignatura: {cada_registro['asignatura']}")
        print(f"Nota: {cada_registro['nota']}")

        if cada_registro["aprobado"] == True:
            print("Estado: Aprobado")
        else:
            print("Reprobado")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_usuario_validada = leer_opcion_usuario_menu()

        if opcion_menu_usuario_validada == "1":
            agregar_registro()
        elif opcion_menu_usuario_validada == "2":
            print("Buscar registro....")
            posicion_recibida = buscar_registro()

            if posicion_recibida != -1:
                print(f"Registro encontrado en la posicion: {posicion_recibida}")
            else:
                print("El estudiante no se encuentra registrado")
        elif opcion_menu_usuario_validada == "3":
            eliminar_registro()
        elif opcion_menu_usuario_validada == "4":
            actualizar_estados()
            print("Estados actualizados correctamente")
        elif opcion_menu_usuario_validada == "5":
            mostrar_todos_los_registro()
        elif opcion_menu_usuario_validada == "6":
            print("Gracias por usar el sistema. Hasta pronto")
            break
iniciar_programa()
#LISTO  
