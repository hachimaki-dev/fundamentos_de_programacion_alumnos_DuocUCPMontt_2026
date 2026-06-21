lista_de_todos_los_libros =[]
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1.- Agregar libros")
    print("2.- Buscar libro")
    print("3.- Eliminar libro")
    print("4.- Actualizar disponibilidad")
    print("5.- Mostrar libros")
    print("6.- Salir")

def leer_opcion_usaurio_menu():
    while True:
        opcion_ingresada = input("Selecciona una opcion (1 al 6): ".strip())
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6"]:
            return opcion_ingresada
        else:
            print("Opcion invalida, vuelve a intentar")

def validar_titulo_libro():
    titulo = input("Ingrese el titulo del libro: ")
    if titulo.strip() == "":
        print("Error, El titulo no puede estar vacio ni contener solo espacios")
    else:
        return titulo.strip()

def validara_autor_libro():
    autor = input("Ingrese el autor del libro: ")
    if autor.strip() == "":
        print("Error, El autor no puede estar vacio ni contener solo espacios")
    else:
        return autor.strip()

def validar_ejemplares_libros():
    try:
        ejemplares_str = input("Ingrese la cantidad de ejemplares: ")
        if not ejemplares_str.isdigit():
            print("Error, la cantidad de ejemplares debe ser un numero entero valido")
        else:
            cantidad = int(ejemplares_str)
            if cantidad < 0:
                print("Error, la cantidad debe ser mayor o igual a 0")
            else:
                return cantidad
    except ValueError:
        print("Valor invalido, inserte un numero entero")

def agregar_libro():
    titulo_validado = validar_titulo_libro()
    autor_validado = validara_autor_libro()
    ejemplares_validado = validar_ejemplares_libros()

    if titulo_validado is None or autor_validado is None or ejemplares_validado is None:
        print("No se pudo guardar el registro debido a errores en los datos")
    else:
        datos_del_libro = {
            "titulo" : titulo_validado,
            "autor" : autor_validado,
            "ejemplares" : ejemplares_validado,
            "disponible" : False
        }
        lista_de_todos_los_libros.append(datos_del_libro)
        print(f"Libro {titulo_validado} registrado con exito")

def buscar_libro_por_titulo(titulo_a_buscar):
    busqueda = titulo_a_buscar.strip().lower()
    for cada_libro in lista_de_todos_los_libros:
        if cada_libro["titulo"].lower() == busqueda:
            indice_libro = lista_de_todos_los_libros.index(cada_libro)
            return indice_libro
    return -1

def eliminaar_libro_por_titulo(titulo_a_eliminar):
    indice_del_libro_encontrado = buscar_libro_por_titulo(titulo_a_eliminar)
    if indice_del_libro_encontrado != -1:
        lista_de_todos_los_libros.pop(indice_del_libro_encontrado)
        return True
    
def actualizar_disponibilidad():
    for cada_libro in lista_de_todos_los_libros:
        if cada_libro["ejemplares"] > 0:
            cada_libro["disponible"] = True
        else:
            cada_libro["disponible"] = False

def mostrar_todos_los_libros():
    actualizar_disponibilidad()
    print("LISTA DE LIBROS")

    if len(lista_de_todos_los_libros) == 0:
        print("No hay libros registrados")
        return
    
    for cada_libro in lista_de_todos_los_libros:
        estado = "DISPONIBLE" if cada_libro["disponible"] else "SIN EJEMPLARES"
        print(f"Titulo: {cada_libro['titulo']}")
        print(f"Autor: {cada_libro['autor']}")
        print(f"Ejemplares: {cada_libro['ejemplares']}")
        print(f"Estado: {estado}")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_validada = leer_opcion_usaurio_menu()

        if opcion_menu_validada == "1":
            agregar_libro()
        elif opcion_menu_validada == "2":
            titulo_a_buscar = input("Ingrese el titulo a buscar: ")
            indice_encontrado = buscar_libro_por_titulo(titulo_a_buscar)

            if indice_encontrado != -1:
                print(f"El libro se encuentra en la posicion {indice_encontrado} del sistema")
            else:
                print("El libro no esta registrado")
        elif opcion_menu_validada == "3":
            titulo_a_eliminar = input("Ingrese el titulo a eliminar: ")
            se_elimino = eliminaar_libro_por_titulo(titulo_a_eliminar)
            if se_elimino is True:
                print("Se elimino con exito el libro")
            else:
                print(f"El libro '{titulo_a_eliminar.strip()}' no se encuentra registrado")
        elif opcion_menu_validada == "4":
            actualizar_disponibilidad()
            print("Disponibilidad actualizada para todos los libros")
        elif opcion_menu_validada == "5":
            mostrar_todos_los_libros()
        elif opcion_menu_validada == "6":
            print("Gracias por usar el sistema. Hasta pronto")
            break
iniciar_programa()

#Este esta perfecto