libros = []

#funciones de validacion con reintentos
def validar_titulo():
    while True:
        titulo = input("Ingrese el titulo que busca: ")
        if titulo.strip() == "":
            print("El titulo no puede estar vacio ")
        else:
            return titulo
        
def validar_autor():
    while True:
        autor = input("Ingrese el autor: ")
        if autor.strip() == "":
            print("No puede estar vacio")
        else:
            return autor
        
def validar_ejemplares():
    while True:
        try:
            ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
            if ejemplares > 0:
                print("La cantidad de ejemplares debe ser mayor a cero")
            else:
                return ejemplares
        except ValueError:
            print("Erorr. Ingrese un numero entero valido")

#agregar libros
def agregar_libros(libros):
    titulo_valido = validar_titulo
    autor_valido = validar_autor
    ejemplares_validos = validar_ejemplares
    
    libro = {
        "titulo": titulo_valido,
        "autor": autor_valido,
        "ejemplares": ejemplares_validos,
        "disponible": False
    }
    libros.append(libro)
    print(f"libro '{titulo_valido}'agregado correctamente")
    
#buscar libro

def buscar_libro(libros, titulo):
    for indice, libro in enumerate

        
        
    
    

def menu():
    print("======== Menu Principal ========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    opcion =input("Ingrese su opcion: ")
    
    if opcion == "1":
        
        