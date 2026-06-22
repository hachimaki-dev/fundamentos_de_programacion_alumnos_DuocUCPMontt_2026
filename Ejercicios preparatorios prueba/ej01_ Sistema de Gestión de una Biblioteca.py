#Establecemos variables que vamos a utilizar
lista_de_libros = []
menu = ['1', '2', '3', '4', '5', '6']

#Funciones del menú
def mostrarMenu():
    print("""\n========== MENÚ PRINCIPAL ==========
 1. Agregar libro
 2. Buscar libro
 3. Eliminar libro
 4. Actualizar disponibilidad
 5. Mostrar libros
 6. Salir
 =====================================""")

def elegirOpcion():
    while True:
        opcion = input("Ingresa la acción a realizar: ")
        if opcion in menu:
            return opcion
        else:
            print("Ingrese una opción válida")

#Feunciones necesarias para registrar los libros x.x
def validarTitulo():
    while True:
        titulo_libro = input("Ingrese el título del libro: ").strip().title()
        if len(titulo_libro) == 0:
            print("Ingrese un título válido")
        else:
            return titulo_libro
        
def validarAutor():
    while True:
        autor_libro = input("Ingrese el autor del libro: ").strip().title()
        if len(autor_libro) == 0:
            print("Ingrese un autor válido")
        else:
            return autor_libro

def validarEjemplares():
    while True:
        try:
            ejemplares = int(input("Ingrese la cantidad de ejemplares disponibles: "))
            if ejemplares < 0:
                print("Error: la cantidad de ejemplares debe ser mayor a 0.")
            else:
                return ejemplares
        except ValueError:
            print("Ingrese una cantidad válida")

#registro de libros
def registrarLibro(diccionario):
    lista_de_libros.append(diccionario)
    return True

def agregarLibro():
    titulo = validarTitulo()
    autor = validarAutor()
    ejemplares = validarEjemplares()

    ficha_libro = {
        'Título': titulo,
        'Autor': autor,
        'Ejemplares': ejemplares,
        'Disponibilidad': False
    }

    registro = registrarLibro(ficha_libro)
    if registro == True:
        print("El libro ha sido registrado de forma existosa.")
        return True
    else:
        print("Ocurrió un error inesperado.")
        return False
    
#Función encargada de Buscar un libro
def BuscarlibroXnombre(lista, titulo_libro):
    libro_a_buscar = titulo_libro.strip().lower()
    if len(lista) == 0:
        print("No hay libros registrados.")
        return -1
    
    for libro in range(len(lista)):
        if lista[libro]['Título'].lower() == libro_a_buscar:
            return libro
        
    return -1

#Ahora vamos a eliminar un libro
def eliminarLibroXtitulo(titulo_libro):
    indice_libro = BuscarlibroXnombre(lista_de_libros, titulo_libro)
    if indice_libro != -1:
        eliminado = lista_de_libros.pop(indice_libro)
        print(f"Se eliminó '{eliminado['Título']}' correctamente. ")
        return True
    else:
        print("No se ha encontrado el título.")
        return False
    
#Ahora actualizaremos el registro de libros
def actualizarLibros(lista):
    for libro in lista:
        if libro['Ejemplares'] > 0:
            libro['Disponibilidad'] = True
        else:
            libro['Disponibilidad'] = False
    print("El registro de libros ha sido actualizado.")

#Mostraremos las lista de libros
def mostrarLibros(lista):
    print("\n========= LISTA DE LIBROS ============")
    if len(lista) == 0:
        print("No hay libros registrados.")
        return
    
    for libro in lista:
        if libro['Disponibilidad'] == True:
            estado = "DISPONIBLE"
        else:
            estado = "SIN EJEMPLARES"

        print(f"""Título: {libro['Título']}
Autor: {libro['Autor']}
Ejemplares: {libro['Ejemplares']}
Estado: {estado}
""")
        print("*" * 30)

#Función encargada de iniciar el programa de registro de libros :p
def main():
    while True:
        mostrarMenu()
        respuesta_usuario = elegirOpcion()
        if respuesta_usuario == '1':
            print("\n========= AGREGAR LIBRO =========")
            agregarLibro()
        
        elif respuesta_usuario == '2':
            print("\n========= BUSCAR LIBRO =========")
            libro_a_buscar = validarTitulo()
            indice = BuscarlibroXnombre(lista_de_libros, libro_a_buscar)
            if indice != -1:
                print("Libro encontrado.")
            else:
                print("El libro no se encuentra registrado.")

        elif respuesta_usuario == '3':
            print("\n========= ELIMINAR LIBRO =========")
            libro_a_eliminar = validarTitulo()
            eliminarLibroXtitulo(libro_a_eliminar)

        elif respuesta_usuario == '4':
            print("\n========= ACTUALIZAR REGISTRO DE LIBROS =========")
            actualizarLibros(lista_de_libros)

        elif respuesta_usuario == '5':
            actualizarLibros(lista_de_libros)
            mostrarLibros(lista_de_libros)

        elif respuesta_usuario == '6':
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida")

main()