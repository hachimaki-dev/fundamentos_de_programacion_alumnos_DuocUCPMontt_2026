datos_de_la_biblioteca = []

def menu_bibloteca():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================\n")


def elegir_opcion():
    while True:
        try:
            opcion_a_elegir = int(input("Ingrese la Opcion a Realizar :      "))
            if opcion_a_elegir < 1 or opcion_a_elegir > 6 :
                print("\nDebe de eligir una opcion entre 1 y 6\n")
            else:
                return opcion_a_elegir
        except ValueError:
            print("\nIngrese una opcion valida\n")


def opcion1_agregar_libro():
    titulo_valido = validar_titulo()
    autor_valido = validar_autor()
    ejemplares_validos = validar_ejemplares()

    datos_de_la_biblioteca.append({"Titulo" :   titulo_valido , "Autor" : autor_valido , "Ejemplares" : ejemplares_validos , "Estado" : False})

def validar_titulo():
    while True:
        titulo_del_libro = input("Ingrese el titulo del libro a Registrar :     ")
        if len(titulo_del_libro) <= 0 or " " in titulo_del_libro:
            print("\nIngrese un titulo Valido (Minimo 1 caracter y sin espacios)\n")
        else:
            return titulo_del_libro

def validar_autor():
    while True:
        autor_del_libro = input("Ingrese el Autor del libro a Registrar :     ")
        if len(autor_del_libro) <= 0 or " " in autor_del_libro:
            print("\nIngrese un Autor Valido (Minimo 1 caracter y sin espacios)\n")
        else:
            return autor_del_libro

def validar_ejemplares():
    while True:
        try:
            ejemplares = int(input("Ingrese los Ejemplares Del libro :  "))
            if ejemplares < 0 :
                print("\nIngrese un Numero entero Positivo\n ")
            else:
                return ejemplares 
        except ValueError:
            print("\ningrese una opcion valida\n ")

def buscar_libro():
    while True:
        bandera_buscar = False
        buscar_el_libro = input("Ingrese El titulo del libro que esta Buscando :    ").lower()
        if len(buscar_el_libro) <= 0 or " " in buscar_el_libro :
            print("\nIngrese algo valido con el minimo de caracteres (1) y Sin espacios\n")
        else:
            for i in datos_de_la_biblioteca:
                if i["Titulo"].lower() == buscar_el_libro:
                    bandera_buscar = True
                    return print(f"Titulo : {i["Titulo"]} \nAutor : {i["Autor"]}\nEjemplares : {i["Ejemplares"]}\nEstado : {i["Estado"]}")

        if not bandera_buscar:
            print("\nNo se a Encontrado Ese libro , Vuelva a intentarlo\n")


def eliminar_libro():
    while True:
        bandera_eliminar = False
        eliminar_el_libro = input("Ingrese El titulo del libro que Quiera Eliminar :    ").lower()
        if len(eliminar_el_libro) <= 0 or " " in eliminar_el_libro :
            print("\nIngrese algo valido con el minimo de caracteres (1) y Sin espacios\n")
        else:
            for i in datos_de_la_biblioteca:
                if i["Titulo"].lower() == eliminar_el_libro:
                    bandera_eliminar = True
                    datos_de_la_biblioteca.remove(i)
                    return print(f"Acaba de eliminar el Libro llamado {i["Titulo"]}")

        if not bandera_eliminar:
            print(f"\nEl libro {i["Titulo"]} no se encuentra registrado.\n")


def actualizar_disponibilidad():
    for act in datos_de_la_biblioteca:
        if act["Ejemplares"] > 0:
            act["Estado"] = "Disponible"
        else:
            act["Estado"] = "Sin Ejemplares"
    print("\nProceso Terminado , Datos ya Actualizados\n")


def opcion_de_salir():
    print("\nGracias por usar el sistema. ¡Hasta pronto!\n")


def main():
    while True:
        menu_bibloteca()
        opcion_seleccionada = elegir_opcion()

        if opcion_seleccionada == 1:
                opcion1_agregar_libro()
        elif opcion_seleccionada == 2:
            if len(datos_de_la_biblioteca) <= 0:
                print("\nIntente mas tarde , Todavia no hay libros registrados\n")
            else:
                buscar_libro()
        elif opcion_seleccionada == 3:
            if len(datos_de_la_biblioteca) <= 0:
                print("\nIntente mas tarde , Todavia no hay libros registrados\n")
            else:
                eliminar_libro()
        elif opcion_seleccionada == 4:
            if len(datos_de_la_biblioteca) <= 0:
                print("\nIntente mas tarde , Todavia no hay libros registrados\n")
            else:
                actualizar_disponibilidad()
        elif opcion_seleccionada == 5:
            if len(datos_de_la_biblioteca) <= 0:
                print("\nIntente mas tarde , Todavia no hay libros registrados\n")
            else:
                print("\n=== LISTA DE LIBROS ===\n")
                for mtrs in datos_de_la_biblioteca:
                    print(f"Titulo : {mtrs["Titulo"]} \nAutor : {mtrs["Autor"]}\nEjemplares : {mtrs["Ejemplares"]}\nEstado : {mtrs["Estado"]}")
                    print("********************************************")
        elif opcion_seleccionada == 6:
            opcion_de_salir()
            break
        else:
            print("Ingrese una opcion valida")

main()