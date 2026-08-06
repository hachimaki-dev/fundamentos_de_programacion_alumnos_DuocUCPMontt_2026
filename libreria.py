biblioteca = {
    'LIB001' : ['Maze runner', 'James Dashner', '2009'],
    'LIB002' : ['Hunger Games', 'Suzanne Collins', '2008'],
    'LIB003' : ['Un secreto en mi colegio', 'Angelica Dossetti', '2009']
}

def mostrar_menu():
    print("=== MENÚ ===")
    print("1.- AGREGAR LIBROS")
    print("2.- MOSTRAR TODOS LOS LIBROS")
    print("3.- BUSCAR LIBROS X AUTOR")
    print("4.- ELIMINAR LIBROS")
    print("5.- SALIR")

def seleccionar_opcion():
    while True:
        try:
            opcion_seleccionada = int(input("Ingrese una opcion del menú 1/2/3/4/5"))

            if opcion_seleccionada not in [1, 2, 3, 4, 5]:
                print("ERROR, Ingrese una opción valida!")
        except ValueError:
            print("ERROR, Ingrese un tipo de dato valido (numeros enteros positivos)")

def agregar_libro(id_libro, nombre, autor, año):
    id_libro = input("Ingrese el id del libro: ").strip()
    nombre = input("Ingrese el nombre del libro: ").strip()
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año del libro: ")).strip()

    libro = {
        "id_libro" : id_libro,
        "nombre" : nombre,
        "autor" : autor,
        "año" : año
    }

    biblioteca.append(libro)
    print("Libro agregado correctamente!")

def mostrar_libros():
    for i, libro in biblioteca:
        print(f"{i + 1}.- {libro["nombre"]} - {libro["autor"]} - {libro["año"]}")

def main():
    print("BIENVENIDO A LA LIBRERIA LIBRERO!")
    while True:

        mostrar_menu()
        eleccion_usuario = seleccionar_opcion()

        if eleccion_usuario == 1:
            agregar_libro()
        
        elif eleccion_usuario == 2:



main()