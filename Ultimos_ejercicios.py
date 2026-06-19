registro_de_libros = []


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro") 
    print("2. Buscar libro") 
    print("3. Eliminar libro") 
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros") 
    print("6. Salir") 
    print("=====================================")


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_de_usuario = leer_opcion()

        if opcion_de_usuario == "1":
            agregar_libros()
        elif opcion_de_usuario == "2":
            buscar_libro()
        elif opcion_de_usuario == "3":
            eliminar_libro()
        elif opcion_de_usuario == "4":
            actualizar_disponibilidad()
        elif opcion_de_usuario == "5":
            mostrar_libros()
        elif opcion_de_usuario == "6":


def leer_opcion():
    while True:
        opcion_ingresada = input("")
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6"]:
            return opcion_ingresada
        else:
            print("La opcion ingresada no es una opcion valida. Vuelva a inentar")


def validar_cantidad_de_ejemplares():
    while True:
        try:        
            cantidad_de_ejemplares_validado = int(input("Ingrese la cantidad de ejemplares del libro: \n"))
            if cantidad_de_ejemplares_validado >= 0:
                return cantidad_de_ejemplares_validado
            else:
                print("")
        except ValueError:
            print("")



def validar_autor_del_libro():
    autor_del_libro_validado = input("Ingrese el nombre del autor del libro: \n").strip()
    if len(autor_del_libro_validado) > 0:
        return autor_del_libro_validado
    else:
        print("El nombre del autor no es válido, ingrese uno válido")



def validar_titulo_del_libro():
    titulo_del_libro_validado = input("Ingrese el Titulo del libro: \n").strip()
    if len(titulo_del_libro_validado) > 0:
        return titulo_del_libro_validado
    else:
        print("El nombre del libro no es válido, ingrese uno válido")


def registrar_libro(diccionario_del_libro):
    registro_de_libros.append(diccionario_del_libro)
    return True


def agregar_libros():
    titulo_del_libro_validado = validar_titulo_del_libro()
    autor_del_libro_validado = validar_autor_del_libro()
    cantidad_de_ejemplares_validado = validar_cantidad_de_ejemplares()

    datos_del_libro = {
        "Titulo" : titulo_del_libro_validado,
        "Autor_del_libro" : autor_del_libro_validado,
        "Cantidad_de_ejemplares" : cantidad_de_ejemplares_validado,
        "Disponibilidad" : False
    }

    se_registro = registrar_libro(datos_del_libro)


def insertar_datos_de_prueba():
    registro_de_libros.append({
        "Título": "Don Quijote",
        "Autor": "Miguel de Cervantes",
        "Ejemplares": 3,
        "Estado": DISPONIBLE
    })
    registro_de_libros.append({
        "Título": "El principito"
        "Autor": "Antoine de Saint-Exupéry" 
        "Ejemplares": 0 
        "Estado": SIN EJEMPLARES
    })

iniciar_programa()