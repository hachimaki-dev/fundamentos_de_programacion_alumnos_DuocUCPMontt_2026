lista_libro =[]

def validar_titulo():
    while True:
        titulo = input("Ingresar titulo: ")
        if titulo.strip() == "":
            print("El titulo no es valido. Vuelva a intentarlo")
        else:
            return titulo
        
def buscar(titulo_buscar):
    for cada_libro in lista_libro:
        if cada_libro["titulo"].lower() == titulo_buscar.lower():
            print("existe")
            indice_libro_encontrado = lista_libro.index(cada_libro)
            return indice_libro_encontrado
        
def eliminar_libro(titulo_buscar):
    indice_libro_buscar = buscar(titulo_buscar)
    if indice_libro_buscar is not None: 
        if lista_libro.pop(indice_libro_buscar):
            return True
        else:
            print("no se pudo eliminar")
            return False

        
def agregar_libro():
    titulo_validar = validar_titulo()
    autor_validar = validar_autor()
    ejemplares_validar = validar_ejemplares()
    
    datos_libro ={
        "titulo": titulo_validar,
        "autor": autor_validar,
        "ejemplares": ejemplares_validar,
        "disponible": False
    }
    lista_libro.append(datos_libro)


def validar_autor():
    while True:
        autor = input("Ingrese el autor: ")
        if autor.strip() == "":
            print("El autor no es valido")
        else:
            return autor
        
def validar_ejemplares():
    while True:
        try:
            ejemplares =int(input("Ingrese cuantos ejemplares esta ingresando: "))
            
            if ejemplares < 0:
                print("No puede ser menor a cero")
            else:
                return ejemplares
        except ValueError:
            print("Ingrese un numero entero")
            
def mostrar_libros():
    print("======== LISTA DE LIBROS ========")
    if len(lista_libro) == 0:
        print("No hay libros disponibles")
    else:
        for libro in lista_libro:
            if libro["disponible"]:
                estado = "DISPONIBLE"
            else:
                estado = "SIN EJEMPLARES"
            print(f"libro: {libro['titulo']} | Autor: {libro['autor']} | ejemplares {libro['ejemplares']} | Estado: {estado}")
            print("====================================")
            
def actualizar_disponibilidad():
    for cada_libro in lista_libro:
        if cada_libro["ejemplares"] > 0:
            cada_libro["disponible"] = True
        else:
            cada_libro["disponible"] = False
           
    
def mostrarmenu():
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Mostrar libros")
    print("5. Actualizar libros")
    print("6. Salir")



def iniciar_programa():
    while True:
        mostrarmenu()
        opcion_usuario = input("Ingrese su opcion: ")
        
        if opcion_usuario == "1":
            agregar_libro()
            
        elif opcion_usuario == "2":
            nombre_a_buscar = input("Ingrese el titulo que desea buscar: ")
            indice_libro = buscar(nombre_a_buscar)
            if indice_libro is not None:
                print("Libro encontrado")
            else:
                print("El libro no se pudo encontrar")
                
        elif opcion_usuario == "3":
            nombre_libro_eliminar = input("Ingrese el libro que desea eliminar: ")
            fue_eliminado = eliminar_libro(nombre_libro_eliminar)
            if fue_eliminado == True:
                print("Fue eliminado con exito")
            else:
                print("No se pudo eliminar")
                
        elif opcion_usuario == "4":
            mostrar_libros()
           
        elif opcion_usuario == "5":
            actualizar_disponibilidad()  
                
        elif opcion_usuario == "6":
            print("Finalizando programa")
            break
            
            
iniciar_programa()
    
            