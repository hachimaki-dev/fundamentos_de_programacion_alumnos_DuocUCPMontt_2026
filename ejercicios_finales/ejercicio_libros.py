
lista_libros = []

def ver_menu():
    print("\n--- Menu Principal!!! ---")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")

def comenzar_programa():
    while True:
        ver_menu()
        opcion_elegida = opcion()
        
        if opcion_elegida == 1:
            agregar_libro() 
        elif opcion_elegida == 2:
            nombre_a_buscar = input("ingresa el nombre del titulo: ")
            dato_libro = buscar_libro(nombre_a_buscar)
            if dato_libro is not None:
                print(f"Libro encontrado en el índice: {dato_libro}")
            else:
                print("este libro no existe")
        elif opcion_elegida == 3:
            nombre_del_libro_eliminado = input("ingrese el nombre del libro que desea eliminar: ")
            eliminado = eliminar_libro(nombre_del_libro_eliminado)
            if eliminado == True:
                print("libro eliminado con éxito")
            else:
                print("hubo un error, no se pudo eliminar")
        elif opcion_elegida == 4:
            actualizar_disponibilidad()
            print("se actualizo la disponibilidad")
        elif opcion_elegida == 5:
            mostrar_libros()        
        elif opcion_elegida == 6:
            print("¡Gracias por usar la biblioteca!")
            break 

def mostrar_libros():
    if not lista_libros:
        print("La biblioteca está vacía.")
    else:
        print(lista_libros)

def registrar_libro(diccionario_libro):
    lista_libros.append(diccionario_libro)
    print("se registro de forma exitosa en la lista global")
    return True

def agregar_libro():
    titulo_valido = vlidar_titulo()
    autor_validado = validar_autor()
    ejemplares_validados = vlidar_ejemplares()
    
    print(f"los datos son: Nombre: {titulo_valido}, "
          f"su autor es: {autor_validado}, "
          f"y tiene ejemplares de un total de: {ejemplares_validados}")
    datos_del_libro = {
        'nombre' : titulo_valido,
        'autor'  : autor_validado,
        'ejemplares' : ejemplares_validados,
        'disponibilidad': False
    }
    exito = registrar_libro(datos_del_libro)
    return exito
    
def vlidar_titulo():
    while True:
        titulo = input("ingrese el titulo del libro: ").strip()
        if len(titulo) <= 0:
            print("ingrese un titulo de libro valido")
        else:
            return titulo
        
def validar_autor():
    while True:
        autor = input("ingrese el autor del libro: ").strip()
        if len(autor) <= 0:
            print("ingrese un nombre de autor valido")
        else:
            return autor
        
def vlidar_ejemplares():
    while True:
        try:
            ejemplares = int(input("ingrese la cantidad de ejemplares: "))
            if ejemplares <= 0:
                print("numero de ejemplares incorrecto")
            else:
                return ejemplares
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    
def buscar_libro(libro):
    for cada_libro in lista_libros:
        if cada_libro['nombre'] == libro:
            print("¡El libro sí existe!")
            indice_libro = lista_libros.index(cada_libro)
            return indice_libro
    return None 

def eliminar_libro(libro):
    indice_del_libro = buscar_libro(libro)
    if indice_del_libro is not None:
        lista_libros.pop(indice_del_libro)
        return True
    return False
    
def actualizar_disponibilidad():
    for cada_libro in lista_libros:
        if cada_libro['ejemplares'] > 0:
            print(f"Actualizando disponibilidad para: {cada_libro['nombre']}")
            cada_libro['disponibilidad'] = True

def opcion():
    while True:
        try:
            opcion_ingresada = int(input("ingresa una de las opciones del menu: "))
            if opcion_ingresada in [1, 2, 3, 4, 5, 6]:
                return opcion_ingresada
            else:
                print("opcion invalida, intentalo nuevamente")
        except ValueError:
            print("Por favor, introduce un número del 1 al 6.")
comenzar_programa()