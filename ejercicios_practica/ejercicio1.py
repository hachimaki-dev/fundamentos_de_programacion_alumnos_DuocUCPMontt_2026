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
        if opcion_elegida in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion_elegida
        else:
            print("Opcion no valida, vuelva a intentar.")


def validar_libro():
    while True:
        titulo_del_libro = input("Ingrese el titulo del libro: ")
        if " " in titulo_del_libro or len(titulo_del_libro) <= 0:
            print("Error: el titulo no puede quedar vacio ni con espacios en blanco.")
        else:
            return titulo_del_libro

def validar_autor():
    while True:
        autor_del_libro = input("Ingrese el autor del libro: ")
        if " " in autor_del_libro or len(autor_del_libro) <= 0:
            print("Error: el titulo no puede quedar vacio ni con espacios en blanco.")
        else:
            return autor_del_libro

def validar_ejemplares():
    while True:
        try:
            ejemplares_del_libro = int(input("Ingrese la cantidad de copias disponibles: "))
            if ejemplares_del_libro <= 0:
                print("Error: debe de ingresar un numero entero mayor a 0.")
            else:
                return ejemplares_del_libro
        except ValueError:
            print("Valor no valido.")

def agregar_libro():
    titulo_del_libro_validado = validar_libro()
    autor_del_libro_validado = validar_autor()
    ejemplares_del_libro_validado = validar_ejemplares()

    libro_registrado = {"nombre_del_libro": titulo_del_libro_validado,
        "autor_del_libro": autor_del_libro_validado,
        "ejemplares_del_libro": ejemplares_del_libro_validado,
        "disponibilidad_del_libro": False }

    lista_de_libros.append(libro_registrado)
    print("Libro agregado exitosamente.")

def buscar_libro():
    buscar_libro_por_nombre = input("Ingrese el nombre del libro a buscar:  ")
    for cada_libro in lista_de_libros:
        if cada_libro["nombre_del_libro"] == buscar_libro_por_nombre:
            print("Libro encontrado.")
            print(f"Nombre: {nombre_del_libro} | Autor: {autor_del_libro} | Ejemplares: {ejemplares_del_libro} | Disponibilidad: {disponibilidad_del_libro}")
            indice_del_libro_encontrado = lista_de_libros.index(cada_libro)
            return indice_del_libro_encontrado
        else:
            return indice_del_bicho_encontrado - 1

lista_de_libros = []


def iniciar_programa():
    while True:
        menu_principal()
        opcion_elegida_usuario = opcion_menu_seleccionada()

    if opcion_elegida_usuario == "1":
        agregar_libro()

    if opcion_elegida_usuario == "2":
        buscar_libro()

iniciar_programa()