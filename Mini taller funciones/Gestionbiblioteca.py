libros_registrados = []
#########################################################
#VALIDACIONES
def validacion_titulo():
    while True:
        titulo = input("Ingrese el titulo del libro: ").strip()
        if len(titulo) > 0:
            return titulo
        else:
            print("Error, el titulo no puede contener espacios ni estar vacio.")
def validacion_autor():
    while True:
        autor = input("Ingrese el autor del libro: ").strip()
        if len(autor) > 0:
            return autor
        else:
            print("Error, el nombre autor no puede contener espacios ni estar vacio.")
def validacion_copias():
    while True:
        try:
            copias_libro = int(input("Ingrese la cantidad de ejemplares de este libro: "))
        except ValueError:
            print("Error, debe ser un numero entero positivo.")
        if copias_libro >= 0:
            return copias_libro
        else:
            print("Error, no puedes ingresar un número negativo.")
##########################################################
##########################################################
#OPCION 1
def agregar_libro():
    titulo_libro = validacion_titulo()
    print(f"== Libro registrado con exito ==")
    autor_libro = validacion_autor()
    print(f"== Autor registrado con exito ==")
    copias_libro = validacion_copias()
    nuevo_libro_agregado = {"Titulo" : titulo_libro.lower(), "Autor" : autor_libro.lower(), "Ejemplares": copias_libro, "Disponibilidad" : False}
    return libros_registrados.append(nuevo_libro_agregado)
##########################################################
##########################################################
#OPCION 2
def buscar_libro():
    titulo_libro = validacion_titulo()
    for i in libros_registrados:
        if i["Titulo"] == titulo_libro:
            return i
        else:
            return -1
##########################################################
##########################################################
#OPCION 3
def eliminar_libro():
    titulo_del = buscar_libro()
    if titulo_del >= 0:
        libros_registrados.pop[titulo_del]
    else:
        print("El libro no se encuentra registrado.")
#########################################################
#########################################################
#OPCION 4
def Actualizar_disponibilidad():
    for libro in libros_registrados:
        if libro["Ejemplares"] > 0:
            libro["Disponibilidad"] = True
#########################################################
#########################################################
#OPCION 5
def Mostrar_libros():
    Actualizar_disponibilidad()
    for libro in libros_registrados:
        print(f"Titulo: {libro["Titulo"]} | Autor: {libro["Autor"]}\nEjemplares: {libro["Ejemplares"]} | Disponibilidad: {libro["Disponibilidad"]}")
#########################################################
#MENÚ E INICIO DEL PROGRAMA
def Menu_principal():
    print("==== MENÚ PRINCIPAL ====")
    print("1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar libros\n6. Salir")

def opcion_elegida_del_menu():
    while True:
        eleccion_usuario = input("Ingrese su opción: ").strip()
        if eleccion_usuario in ["1", "2", "3", "4", "5", "6"]:
            return eleccion_usuario
        else:
            print("Ingresa una opción válida.")

def inicio_del_programa():
    while True:
        Menu_principal()
        eleccion_user = opcion_elegida_del_menu()
        if eleccion_user == "1":
            agregar_libro()
        elif eleccion_user == "2":
            buscar_libro()
            print("Libro encontrado")
        elif eleccion_user == "3":
            eliminar_libro()
            print("Libro eliminado.")
        elif eleccion_user == "4":
            Actualizar_disponibilidad()
            print("Disponibilidad actualizada.")
        elif eleccion_user == "5":
            Mostrar_libros()
        elif eleccion_user == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Error, debe ingresar una opcion valida.")
inicio_del_programa()