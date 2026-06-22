lista_de_libros = []

def mostrar_menu():
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("7. Agregar elementos lista")

def opciones_usuario():
    while True:
            opcion_ingresada = input("Ingrese su opcion: ")
            if opcion_ingresada in ["1","2","3","4","5","6","7"]:
                return opcion_ingresada
            else:
                print("Ingrese una opcion valida")
  
def validar_titulo(titulo): 
    titulo_validado = titulo.strip()
    if titulo_validado != " ":
        return True
    else:
        return False
    
def validar_autor(autor):
    autor_validado = autor.strip()
    if autor_validado != " ":
        return True
    else:
        return False

def validar_ejemplares(ejemplar):
    while True:
        try:
            ejemplar_validado = int(ejemplar)
            if ejemplar_validado >= 0:
                return True
            else:
                return False
        except ValueError:
            return False

def validar_disponibilidad(disponibles):
    try:
        disponibles = int(disponibles)
        if disponibles == True:
            print("Disponible")
        else:
            print("Sin ejemplares")
    except ValueError:
        print("Valor invalido")
        
def agregar_libro(lista_de_libros):
    titulo = input("Ingrese titulo del libro: ")
    if not validar_titulo(titulo):
        print("El titulo no puede estar vacia")
    
    autor = input("Ingrese autor del libro: ")
    if not validar_autor(autor):
        print("El autor no puede estar vacio")
    
    ejemplar = input("Ingrese cantidad de ejemplares: ")
    if not validar_ejemplares(ejemplar):
        print("El ejemplar no puede estar vacio")

    libros = {
        "titulo": titulo,
        "autor": autor,
        "ejemplar": ejemplar,
        "disponible": False
    }
    lista_de_libros.append(libros)
    print("Se ha registrado exitosamente")

def buscar_libro_por_nombre(nombre_libro_a_buscar):
    for cada_libro in lista_de_libros:
        if cada_libro["titulo"] == nombre_libro_a_buscar:
            print("Existe")
            indice_libro = lista_de_libros.index(cada_libro)
            return indice_libro

def eliminar_libro_por_nombre(nombre_libro_a_buscar):
    indice_libro_encontrado = buscar_libro_por_nombre(nombre_libro_a_buscar)
    if indice_libro_encontrado is not None:
        lista_de_libros.pop(indice_libro_encontrado)
        return True

def insertar_datos_libros():
    lista_de_libros.append({
        "titulo": "hola",
        "autor": "pedro",
        "ejemplar": 3,
        "disponible": False
    })
    lista_de_libros.append({
        "titulo": "chao",
        "autor": "pacquito",
        "ejemplar": 5,
        "disponible": False
    })
    lista_de_libros.append({
        "titulo": "que tal",
        "autor": "maria",
        "ejemplar": 0,
        "disponible": False
    })

def actualizar_campo_disponibles():
    for cada_libro in lista_de_libros:
        if cada_libro["ejemplar"] > 0:
            cada_libro["disponible"] = True

def mostrar_todos_los_libros():
    print(lista_de_libros)

def main():
    while True:
        mostrar_menu()
        opciones_usuario_valida = opciones_usuario()
        if opciones_usuario_valida == "1":
            agregar_libro()

        elif opciones_usuario_valida == "2":
            nombre_libro_a_buscar = input("Ingrese nombre del libro a buscar: ")
            indice_encontrado = buscar_libro_por_nombre(nombre_libro_a_buscar)
            if indice_encontrado is not None:
                print("Lo encontramos")
                print(f"Titulo del libro: {lista_de_libros[indice_encontrado]["titulo"]}")
                print(f"Autor del libro: {lista_de_libros[indice_encontrado]["autor"]}")
                print(f"Ejemplares del libro: {lista_de_libros[indice_encontrado]["ejemplar"]}")
                print(f"Disponibilidad del libro: {lista_de_libros[indice_encontrado]["disponible"]}")
            else:
                print("No hay datos de este libro")
        
        elif opciones_usuario_valida == "3":
            nombre_libro_a_eliminar = input("Ingrese nombre del libro a eliminar: ")
            indice_encontrado = buscar_libro_por_nombre(nombre_libro_a_eliminar)
            if indice_encontrado is not None:
                print("Ha sido eliminado")
            else:
                print("No hay datos de este libro")
            
        elif opciones_usuario_valida == "4":
            actualizar_campo_disponibles()
        
        elif opciones_usuario_valida == "5":
            mostrar_todos_los_libros()

        elif opciones_usuario_valida == "6":
            print("Salir..")
            break
        elif opciones_usuario_valida == "7":
            insertar_datos_libros()
        else:
            print("Opcion invalida")
main()
