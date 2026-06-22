def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def opcion_menu_seleccionada():
    while True:
        opcion_elegida = input("Seleccione su opcion (1-6): ")
        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida
        else:
            print("Opcion no valida, vuelva a intentar.")

def validar_libro():
    while True:
        titulo_del_libro = input("Ingrese el titulo del libro: ").strip()

        if len(titulo_del_libro) <= 0:
            print("Error: el titulo no puede quedar vacio ni con espacios en blanco.")
        else:
            return titulo_del_libro

def validar_autor():
    while True:
        autor_del_libro = input("Ingrese el autor del libro: ").strip()

        if len(autor_del_libro) <= 0:
            print("Error: el autor no puede quedar vacio ni con espacios en blanco.")
        else:
            return autor_del_libro

def validar_ejemplares():
    while True:
        try:
            ejemplares_del_libro = int(input("Ingrese la cantidad de copias disponibles: "))

            if ejemplares_del_libro < 0:
                print("Error: debe de ingresar un numero entero mayor o igual a 0.")
            else:
                return ejemplares_del_libro
        except ValueError:
            print("Valor no valido.")


def agregar_libro(lista_de_libros):
    titulo_del_libro_validado = validar_libro()
    autor_del_libro_validado = validar_autor()
    ejemplares_del_libro_validado = validar_ejemplares()

    libro_registrado = {
        "nombre_del_libro": titulo_del_libro_validado,
        "autor_del_libro": autor_del_libro_validado,
        "ejemplares_del_libro": ejemplares_del_libro_validado,
        "disponibilidad_del_libro": False 
    }

    lista_de_libros.append(libro_registrado)
    print("Libro agregado exitosamente.")


def buscar_libro(lista_de_libros, buscar_libro_por_nombre):
    for cada_libro in lista_de_libros:
        if cada_libro["nombre_del_libro"].lower() == buscar_libro_por_nombre.lower():
            return lista_de_libros.index(cada_libro)
    return -1


def eliminar_libro(lista_de_libros):
    nombre_del_libro_a_eliminar = input("Ingrese el nombre del libro que desea eliminar: ").strip()
    
    indice_del_libro_encontrado = buscar_libro(lista_de_libros, nombre_del_libro_a_eliminar)
    
    if indice_del_libro_encontrado != -1:
        lista_de_libros.pop(indice_del_libro_encontrado)
        print(f"El libro '{nombre_del_libro_a_eliminar}' ha sido eliminado exitosamente.")
        return indice_del_libro_encontrado
    else:

        print(f"El libro '{nombre_del_libro_a_eliminar}' no se encuentra registrado.")
        return -1


def actualizar_disponiblidad_libro(lista_de_libros):
    for cada_libro in lista_de_libros:
        if cada_libro["ejemplares_del_libro"] > 0:
            cada_libro["disponibilidad_del_libro"] = True
        else: 
            cada_libro["disponibilidad_del_libro"] = False


def mostrar_libros(lista_de_libros):
    actualizar_disponiblidad_libro(lista_de_libros)
    
    print("\n=== LISTA DE LIBROS ===")
    if len(lista_de_libros) == 0:
        print("(No hay libros registrados en el sistema)")
        print("********************************************")
        return

    for libro in lista_de_libros:
        print(f"Título: {libro['nombre_del_libro']}")
        print(f"Autor: {libro['autor_del_libro']}")
        print(f"Ejemplares: {libro['ejemplares_del_libro']}")
        
        if libro["disponibilidad_del_libro"]:
            estado_del_texto = "DISPONIBLE"
        else:
            estado_del_texto = "SIN EJEMPLARES"

        print(f"Estado: {estado_del_texto}")
        print("********************************************")
        
lista_de_libros = []

def iniciar_programa():
    while True:
        menu_principal()
        opcion_elegida_usuario = opcion_menu_seleccionada()

        if opcion_elegida_usuario == "1":
            agregar_libro(lista_de_libros)

        elif opcion_elegida_usuario == "2":
            print("\n--- Buscar Libro ---")
            nombre_del_libro_a_buscar = input("Ingrese el nombre del libro a buscar: ").strip()
            indice_del_libro_encontrado = buscar_libro(lista_de_libros, nombre_del_libro_a_buscar)

            if indice_del_libro_encontrado != -1:
                libro = lista_de_libros[indice_del_libro_encontrado]
                print(f"\n¡Libro encontrado en la posicion {indice_del_libro_encontrado}!")
                print(f"Nombre: {libro['nombre_del_libro']} | Autor: {libro['autor_del_libro']} | Ejemplares: {libro['ejemplares_del_libro']}")
            else:
                print(f"\nEl libro '{nombre_del_libro_a_buscar}' no se encuentra en el sistema.")

        elif opcion_elegida_usuario == "3":
            print("\n--- Eliminar Libro ---")
            eliminar_libro(lista_de_libros)

        elif opcion_elegida_usuario == "4":
            actualizar_disponiblidad_libro(lista_de_libros)
            print("\nEstados de disponibilidad actualizados correctamente.")

        elif opcion_elegida_usuario == "5":
            mostrar_libros(lista_de_libros)

        elif opcion_elegida_usuario == "6":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break


iniciar_programa()