def validar_titulo(titulo):
    """Valida que el título no esté vacío ni solo tenga espacios."""
    return len(titulo.strip()) > 0

def validar_autor(autor):
    """Valida que el autor no esté vacío ni solo tenga espacios."""
    return len(autor.strip()) > 0

def validar_ejemplares(ejemplares_str):
    """Valida que los ejemplares sean un entero mayor o igual a cero."""
    if ejemplares_str.isdigit():
        return int(ejemplares_str) >= 0
    return False

def agregar_libro(biblioteca):
    """Solicita, valida y agrega un nuevo libro a la lista."""
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    ejemplares_raw = input("Ingrese la cantidad de ejemplares: ")

    
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío.")
        return
    
    if not validar_autor(autor):
        print("Error: El autor no puede estar vacío.")
        return
    
    if not validar_ejemplares(ejemplares_raw):
        print("Error: Los ejemplares deben ser un número entero mayor o igual a 0.")
        return

    
    ejemplares = int(ejemplares_raw)

    
    nuevo_libro = {
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "ejemplares": ejemplares,
        "disponible": False
    }

    biblioteca.append(nuevo_libro)
    print(f"¡Libro '{titulo}' registrado con éxito! (Estado inicial: No disponible hasta actualizar)")

 
def buscar_libro(biblioteca, titulo_buscar):
    """Recorre la lista y retorna el índice del libro, o -1 si no existe."""
    for i in range(len(biblioteca)):
        # Buscamos ignorando mayúsculas/minúsculas y espacios extra para mayor precisión
        if biblioteca[i]["titulo"].lower().strip() == titulo_buscar.lower().strip():
            return i
    return -1


def eliminar_libro(biblioteca):
    """Elimina un libro utilizando la función de búsqueda."""
    print("--- ELIMINAR LIBRO ---")
    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")
    
    posicion = buscar_libro(biblioteca, titulo_eliminar)
    
    if posicion != -1:
        libro_eliminado = biblioteca.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' ha sido eliminado exitosamente.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")



def actualizar_disponibilidad(biblioteca):
    """Actualiza el campo 'disponible' según la cantidad de ejemplares."""
    for libro in biblioteca:
        if libro["ejemplares"] > 0:
            libro["disponible"] = True
        else:
            libro["disponible"] = False



def mostrar_libros(biblioteca):
    """Actualiza disponibilidades y muestra los libros con el formato requerido."""
    actualizar_disponibilidad(biblioteca)
    
    print("\n=== LISTA DE LIBROS ===")
    if not biblioteca:
        print("No hay libros registrados en el sistema.")
        print("*******************************************")
        return
    
    for libro in biblioteca:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN EJEMPLARES"
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Ejemplares: {libro['ejemplares']}")
        print(f"Estado: {estado}")
        print("*******************************************")




def menu_principal():
    
    biblioteca = []

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Eliminar libro")
        print("4. Actualizar disponibilidad")
        print("5. Mostrar libros")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_libro(biblioteca)
            
        elif opcion == "2":
            print("\n--- BUSCAR LIBRO ---")
            titulo_buscar = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(biblioteca, titulo_buscar)
            
        
            if posicion != -1:
                libro = biblioteca[posicion]
                print(f"\n¡Libro encontrado en la posición {posicion}!")
                print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Ejemplares: {libro['ejemplares']}")
            else:
                print(f"El libro '{titulo_buscar}' no se encuentra registrado.")
                
        elif opcion == "3":
            eliminar_libro(biblioteca)
            
        elif opcion == "4":
            actualizar_disponibilidad(biblioteca)
            print("\nDisponibilidad de todos los libros actualizada correctamente.")
            
        elif opcion == "5":
            mostrar_libros(biblioteca)
            
        elif opcion == "6":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()