
libros = []


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def opcion_usuario():
    while True:
        opcion_elegida = input("ingresa una opcion : (1-6): ").strip()
        if opcion_elegida in ["1","2","3","4","5","6"]:
            return opcion_elegida
        else:
            print("opcion invalida , intenta nuevamente")
   


def agregar_libro():
    titulo_libro_validado = validar_titulo_libro()
    nombre_autor_validado = validar_nombre_libro()
    cantidad_ejemplares_validado = validar_cantidad_ejemplares()
    

    datos_libro = {
        "titulo" : titulo_libro_validado,
        "autor" : nombre_autor_validado,
        "ejemplares" : cantidad_ejemplares_validado,
        "disponible" : False
    }
    libros.append(datos_libro)
    print(libros)
    

def validar_titulo_libro():
    while True:
        titulo_libro_usuario = input("ingresa el titulo del libro : ").strip()

        if len(titulo_libro_usuario) <=0:
            print("vuelve a intentar. no se guardo registro ")
        else:
            return titulo_libro_usuario
        

def validar_nombre_libro():
    while True:
        nombre_autor_usuario = input("ingresa el nombre del autor del titulo : ").strip()
        if len(nombre_autor_usuario) <=0:
            print("intenta nuevamente. no se guardo registro")
        else:
            return nombre_autor_usuario
        

def validar_cantidad_ejemplares():
    while True:
        try:
            cantidad_ejemplares_usuario = int(input("ingresa la cantidad de ejemplares : "))
            if cantidad_ejemplares_usuario >=0:
                return cantidad_ejemplares_usuario
            else:
                print("la cantidad de ejemplares deber ser mayor que 0. no se guardo registro")
        except ValueError:
            print("valor no valido")


def buscar_libro():
    while True:
        titulo_busqueda_usuario = input("ingresa el titulo que buscas \n").strip()
        if len(titulo_busqueda_usuario) <=0:
            print("intenta nuevamente")
        else:
            return titulo_busqueda_usuario


def buscar_libro_en_lista(lista_libros ,nombre_libro_a_buscar):
    for pocicion_cada_libro in range(len(lista_libros)):
        if libros[pocicion_cada_libro]["nombre_libro"].lower() == nombre_libro_a_buscar.lower():
            return pocicion_cada_libro
    print("no encontrado")    
    return -1

        
def actualizar_disponibilidad_libros(lista_libros):
    for libro in libros:
        if libro["ejemplares"] >0:
            libro["disponible"] = True
        elif libro["ejemplares"] == 0:
            libro["disponible"] = False


def mostrar_libros(lista_libros):
    actualizar_disponibilidad_libros(lista_libros)
    print("=== LISTA DE LIBROS ===")
    for libro in lista_libros:
        if libro["disponible"] == True:
            libro["disponible"] = "DISPONIBLE"
        else:
            libro["estado"] = "SIN EJEMPLARES"
        print(f"Titulo: {libro["titulo"]} ")
        print(f"Autor: {libro["autor"]} ")
        print(f"Ejemplares: {libro["ejemplares"]} ")
        print(f"Estado: {libro["disponible"]} ")
        print("*******************************************")

        
def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_del_menu_seleccionada = opcion_usuario()

        if opcion_del_menu_seleccionada == "1":
            agregar_libro()

        elif opcion_del_menu_seleccionada == "2":
            nombre_libro_a_buscar = buscar_libro()
            indice_libro_encontrado = buscar_libro_en_lista(libros ,nombre_libro_a_buscar)
            if indice_libro_encontrado != -1:
                libro_encontrado = libros[indice_libro_encontrado]
                print(f"el libro fue encontrado en la posicion : {indice_libro_encontrado}")
                

        elif opcion_del_menu_seleccionada == "3":
            titulo_ingresado_para_eliminar = input("ingresa el titulo que deseas eliminar\n").strip()
            if " " not in titulo_ingresado_para_eliminar or len(titulo_ingresado_para_eliminar) <=0:
                buscar_libro_para_eliminar = buscar_libro_en_lista(libros,titulo_ingresado_para_eliminar)
                if buscar_libro_para_eliminar != -1:
                    libros.pop(buscar_libro_para_eliminar)
                else:
                    print(f"El libro {titulo_ingresado_para_eliminar} no se encuentra registrado")
            else:
                print(f"el dato que buscas no puede contener espacios")

        elif opcion_del_menu_seleccionada == "4":
            actualizar_disponibilidad_libros(libros)

        elif opcion_del_menu_seleccionada == "5":
            mostrar_libros(libros)

        elif opcion_del_menu_seleccionada == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
            
iniciar_programa()