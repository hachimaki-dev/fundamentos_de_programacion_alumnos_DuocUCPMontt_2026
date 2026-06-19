#Establecemos variables que vamos a utilizar
lista_de_libros = []
menu = ['1', '2', '3', '4', '5', '6', '7']

#Funciones del menú
def mostrarMenu():
    print(""" ========== MENÚ PRINCIPAL ==========
 1. Agregar libro
 2. Buscar libro
 3. Eliminar libro
 4. Actualizar disponibilidad
 5. Mostrar libros
 6. Salir
 7. Pruebas del programa
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
        if len(titulo_libro) < 0:
            print("Ingrese un título válido")
        else:
            return titulo_libro
        
def validarAutor():
    while True:
        autor_libro = input("Ingrese el título del libro: ").strip().title()
        if len(autor_libro) < 0:
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
    print("El libro ha sido registrado")
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
    
#Función encargada de iniciar el programa de registro de libros :p
def main():
    while True:
        mostrarMenu()
        respuesta_usuario = elegirOpcion()
        if respuesta_usuario == '1':
            agregarLibro()
        elif respuesta_usuario == '2':
            pass
        elif respuesta_usuario == '3':
            pass
        elif respuesta_usuario == '4':
            pass
        elif respuesta_usuario == '5':
            pass
        elif respuesta_usuario == '6':
            pass
        elif respuesta_usuario == '7':
            pass
        else:
            print("Opción inválida")

main()