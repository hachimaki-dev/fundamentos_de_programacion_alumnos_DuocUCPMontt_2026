libros_de_biblioteca = []
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ========== \n1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar librosn\n6. Salir\n=====================================")
def verificador_de_titulos(Título):
    while True:
        
        if len(Título.strip()) == 0:
            print("El título no puede estar vacío")
        else:
            print(f"Titulo {Título} guardado")
            return Título
def verificador_de_nombre_autor():
    while True:
        autor_del_libro = input("Ingrese el nombre del autor del libro: ")
        if len(autor_del_libro.strip()) == 0:
            print("El nombre del autor no puede estar vacío")
        else:
            print(f"Autor {autor_del_libro} guardado")
            return autor_del_libro
def verificador_de_cantidad_ejemplares():
    while True:
        try:
            cantidad_de_ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
            if cantidad_de_ejemplares < 0:
                print("Ingrese una cantidad mayor o igual a 0")
            else:
                return cantidad_de_ejemplares
        except ValueError:
            print("Ingrese un numero válido")
def actualizar_disponibilidad_libro():
    for cada_libro in libros_de_biblioteca:
        if cada_libro["Cantidad de ejemplares"] > 0:
            libros_de_biblioteca.index(cada_libro)["Disponibilidad"] = True
        else:
            libros_de_biblioteca.index(cada_libro)["Disponibilidad"] = False
def verificar_opcion_menu():
    while True:
        opcion_incertada = input("Ingrese una opción del menú: ").strip()
        if opcion_incertada in ["1","2","3","4","5","6"]:
            return opcion_incertada
        else:
            print("Inserte un número de opción válida (del 1 al 6)")
def agregar_libro():
    Título_de_libro = input("Ingrese un título: ") 
    Título_de_libro = verificador_de_titulos(Título_de_libro)
    Nombre_de_autor = verificador_de_nombre_autor()
    ejemplares_del_libro = verificador_de_cantidad_ejemplares()
    diccionario_libro = {"Título": Título_de_libro, "Nombre del autor": Nombre_de_autor, "Cantidad de ejemplares": ejemplares_del_libro, "Disponibilidad": False}
    libros_de_biblioteca.append(diccionario_libro)
def buscar_libro():
    titulo_a_buscar = input("Ingrese el titulo a buscar:")
    for libros in libros_de_biblioteca:
        if libros["Título"] == titulo_a_buscar:
            print(f"El libro {libros["Título"]} existe")
            indice_del_libro = libros_de_biblioteca.index(libros)
            return indice_del_libro
def eliminar_libro_por_nombre():
    índice_del_libro = buscar_libro()
    if índice_del_libro == -1:
        print("el libro que desea eliminar no existe")
    else:
        libros_de_biblioteca.pop(índice_del_libro)
        print(f"Libro {libros_de_biblioteca.index(1)["Título"]} ")
def mostrar_libros():
    actualizar_disponibilidad_libro()
    print("==Lista de Libros==")
    for cada_libro in libros_de_biblioteca:
        print(f"Título: {cada_libro["Título"]}")
        print(f"Autor: {cada_libro["Nombre del autor"]}")
        print(f"Ejemplares: {cada_libro["Cantidad de ejemplares"]}")
        if cada_libro["Disponibilidad"] == False:
            print(f"Estado: NO DISPONIBLE")
        else:
            print(f"Estado: DISPONIBLE")
        print("****************************************")

        
def inicio_programa():
    while True:
        mostrar_menu()
        opción_menu = verificar_opcion_menu()
        print(opción_menu)
        if opción_menu == "1":
            agregar_libro()
        elif opción_menu == "2":
            buscar_libro()
        elif opción_menu == "3":
            eliminar_libro_por_nombre()
        elif opción_menu == "4":
            actualizar_disponibilidad_libro()
        elif opción_menu == "5":
            mostrar_libros()
        elif opción_menu == "6":
            print("Cierre del programa, hasta luego")
            break
    return
inicio_programa()