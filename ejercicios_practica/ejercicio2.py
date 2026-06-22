total_estudiantes = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
    print("=====================================")

def opciones_menu():
    while True:
        opcion_elegida = input("Seleccione su opcion (1-6): ")
        if opcion_elegida in ["1","2","3","4","5","6"]:
            return opcion_elegida
        else:
            print("Opcion no valida, vuelva a intentar.")

def validar_nombre_estudiante():
    while True:
        try:
            nombre_estudiante = input("Ingrese el nombre del estudiante a registar: ")
            if " " in nombre_estudiante or len(nombre_estudiante) <= 0:
                print("Dato invalido: no puede quedar vacio ni solo espacios en blanco.")
            else:
                return nombre_estudiante
        except ValueError:
            print("Dato invalido, vuelve a intentar.")

def validar_asignatura():
    while True:
        try:
            nombre_asignatura = input("Ingrese el nombre de la asignatura a registar: ")
            if " " in nombre_asignatura or len(nombre_asignatura) <= 0:
                print("Dato invalido: no puede quedar vacio ni solo espacios en blanco.")
            else:
                return nombre_asignatura
        except ValueError:
            print("Dato invalido, vuelve a intentar.")

def validar_nota():
    while True:
        try:
            nota_del_estudiante = float(input("Ingrese la nota del estudiante: "))
            if 1.0 <= nota_del_estudiante <= 7.0:
                return nota_del_estudiante
            else:
                print("Ingrese un numero entre 1 y 7.")
        except ValueError:
            print("Dato invalido, vuelva a intentar.")

def agregar_registro():
    nombre_estudiante_validado = validar_nombre_estudiante()
    nombre_asignatura_validado = validar_asignatura()
    nota_del_estudiante_validado = validar_nota()

    registro_estudiante = {"nombre_estudiante": nombre_estudiante_validado,
                        "asignatura": nombre_asignatura_validado,
                        "nota": nota_del_estudiante_validado,
                        "alumno_aprobado": False}

    total_estudiantes.append(registro_estudiante)
    print("Alumno registrado exitosamente.")

def buscar_estudiante(nombre_estudiante_a_buscar):
    for cada_alumno in total_estudiantes:
        if cada_alumno["nombre_estudiante"].lower() == nombre_estudiante_a_buscar.lower():
            return total_estudiantes.index(cada_alumno)
    return -1

def eliminar_estudiante(nombre_estudiante_a_buscar):
    indice_del_estudiante_encontrado = buscar_estudiante(nombre_estudiante_a_buscar)

    if indice_del_estudiante_encontrado == -1:
        return None

    total_estudiantes.pop(indice_del_estudiante_encontrado)
    return indice_del_estudiante_encontrado

def actualizar_estado_alumno():
    for cada_alumno in total_estudiantes:
        if cada_alumno["nota"] >= 4.0:
            cada_alumno["alumno_aprobado"] = True

    print("Se han actualizado todo los estados de los alumnos.")

def mostrar_registros_alumnos():
    actualizar_estado_alumno()

    print("==== LISTA DE REGISTROS ===")
    if len(total_estudiantes) == 0:
        print("No hay registros de alumnos en el sistema.")
        return
    
    for cada_alumno in total_estudiantes:
        print(f"Nombre: {cada_alumno["nombre_estudiante"]}")
        print(f"Asignatura: {cada_alumno["asignatura"]}")
        print(f"Nota: {cada_alumno["nota"]}")

        if cada_alumno["alumno_aprobado"] == True:
            estado_alumno = "APROBADO"
        else:
            estado_alumno = "REPROBADO"
                
        print(f"Estado: {estado_alumno}")
        print("*********************************************")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_elegida_usuario = opciones_menu()

        if opcion_elegida_usuario == "1":
            agregar_registro()

        elif opcion_elegida_usuario == "2":
            while True:
                try:
                    print("=== BUSCANDO REGISTRO ===")
                    nombre_estudiante_a_buscar = input("Ingresa el nombre del estudiante a buscar: ")
                    if " " in nombre_estudiante_a_buscar or len(nombre_estudiante_a_buscar) <= 0:
                        print("Dato invalido: no puede ingresar nombres vacios ni solo con espacios.")
                    else:
                        indice_del_estudiante_encontrado = buscar_estudiante(nombre_estudiante_a_buscar)

                        if indice_del_estudiante_encontrado != -1:
                            alumno = total_estudiantes[indice_del_estudiante_encontrado]
                            print(f"Alumno encontrado en la posicion {indice_del_estudiante_encontrado}!")
                            print(f"Nombre: {alumno["nombre_estudiante"]} | Asignatura: {alumno["asignatura"]} | Nota: {alumno["nota"]}")
                            break
                        else:
                            print(f"El alumno {nombre_estudiante_a_buscar} no se ha encontrado en el sistema.")
                            break

                except ValueError:
                    print("Dato invalido, vuelva a intentarlo.")
        
        elif opcion_elegida_usuario == "3":
            while True:
                try:
                    print("==== ELIMINANDO REGISTRO ====")
                    nombre_estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
                    if " " in nombre_estudiante_a_eliminar or len(nombre_estudiante_a_eliminar) <= 0:
                        print("Dato invalido: no puede ingresar nombres vacios ni solo con espacios.")
                    else:
                        fue_eliminado = eliminar_estudiante(nombre_estudiante_a_eliminar)
                        if fue_eliminado is not None:
                            print("Alumno eliminado exitosamente.")
                            break
                        else:
                            print(f"El registro de {nombre_estudiante_a_eliminar} no se encuentra en el sistema")
                            break

                except ValueError:
                    print("Dato invalido, vuelva a intentarlo.")
        
        elif opcion_elegida_usuario == "4":
            actualizar_estado_alumno()

        elif opcion_elegida_usuario == "5":
            mostrar_registros_alumnos()
        
        elif opcion_elegida_usuario == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Ingresa una opcion valida.")

iniciar_programa()