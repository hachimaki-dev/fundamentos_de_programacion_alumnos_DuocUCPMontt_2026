libros = []

def validar_titulo(titulo):
    if titulo.strip() == "":
        print("Error: El título no puede estar vacío.")
        return False
    return True
        
def validar_autor(autor):
    if autor.strip() == "":
        print("Error: El autor no puede estar vacío.")
        return False
    return True
        
def validar_ejemplares(ejemplares_str):
    try:
        ejemplares = int(ejemplares_str)
        if ejemplares < 0:
            print("Error: La cantidad de ejemplares debe ser mayor o igual a cero.")
            return False
        return True
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return False


def agregar_libros(libros):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor: ")
    ejemplares_str = input("Ingrese la cantidad de ejemplares: ")
    
    if validar_titulo(titulo) and validar_autor(autor) and validar_ejemplares(ejemplares_str):
        libro = {
            "titulo": titulo.strip(),
            "autor": autor.strip(),
            "ejemplares": int(ejemplares_str),
            "disponible": False  
        }
        libros.append(libro)
        print(f"Libro '{titulo.strip()}' agregado correctamente.")
    else:
        print("No se pudo guardar el registro debido a errores de validación.")
    
def buscar_libro(libros, titulo):
    titulo_buscar = titulo.strip().lower()
    for indice, libro in enumerate(libros):
        if libro["titulo"].lower() == titulo_buscar:
            return indice  
    return -1  

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["ejemplares"] > 0:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    
    print("\n=== LISTA DE LIBROS ===")
    for libro in libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN EJEMPLARES"
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Ejemplares: {libro['ejemplares']}")
        print(f"Estado: {estado}")
        print("*******************************************")


def menu():
    while True:
        print("\n======== Menú Principal ========")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Eliminar libro")
        print("4. Actualizar disponibilidad")
        print("5. Mostrar libros")
        print("6. Salir")
        print("================================")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            agregar_libros(libros)
            
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(libros, titulo)
            if posicion != -1:
                print(f"El libro fue encontrado en la posición {posicion} de la lista.")
            else:
                print(f"El libro '{titulo}' no se encuentra registrado.")
                
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a eliminar: ")
            posicion = buscar_libro(libros, titulo)
            if posicion != -1:
                libros.pop(posicion)
                print(f"El libro '{titulo}' ha sido eliminado correctamente.")
            else:
                print(f"El libro '{titulo}' no se encuentra registrado.")
                
        elif opcion == "4":
            actualizar_disponibilidad(libros)
            print("Disponibilidad de los libros actualizada con éxito.")
            
        elif opcion == "5":
            mostrar_libros(libros)
            
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()