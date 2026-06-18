libros = []
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")
    

menu()

def titulo_validado():
    titulo_libro = input("agrage el titulo del libro: ").strip()
    if titulo_libro not in " ":
        return titulo_libro
    else:
        print ("intenta nuevamente")

def autor_validado():
    autor_libro = input("agrage el titulo del libro: ").strip()
    if autor_libro not in " ":
        return autor_libro
    else:
        print ("intenta nuevamente")


def ejemplares_validado():
    cantidad_ejemplares = int(input("ingrese la cantidad de ejemplares: "))
    if cantidad_ejemplares >= 0: 
        return cantidad_ejemplares
    else:
        print("intenta nuevamente")


def agregar_libro():
    titulo_libro_validado = titulo_validado()
    autor_libro_validado = autor_validado()
    cantidad_ejemplares_validado = ejemplares_validado()
    disponible = False
    if cantidad_ejemplares_validado > 0: 
        disponible = True
    
    datos_libros = {
        "nombre_libro" : titulo_libro_validado(),
        "autor_libro" : autor_libro_validado(),
        "cantidad_ejemplares" : cantidad_ejemplares_validado(),
        "disponible" : disponible
    }
    libros.append(datos_libros)
