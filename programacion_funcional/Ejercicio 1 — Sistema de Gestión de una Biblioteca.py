#menu:
libros = []
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def opcion_usuario():
    while True:
        try:
            opcion_elegida = input("ingresa una opcion : (1-6): ")
            if opcion_elegida in ["1","2","3","4","5","6"]:
                return opcion_elegida
            else:
                print("opcion invalida , intenta nuevamente")
        except: 
            print("ingresa una opcion valida")


#lista de libros: 

#opcion 1 agregar libro:
def agregar_libro():
    titulo_libro_validado = validar_titulo_libro()
    nombre_autor_validado = validar_nombre_libro()
    cantidad_ejemplares_validado = validar_cantidad_ejemplares()
    

    datos_libro = {
        "nombre_libro" : titulo_libro_validado,
        "autor_libro" : nombre_autor_validado,
        "ejemplares" : cantidad_ejemplares_validado,
        "estado" : False
    }
    libros.append(datos_libro)
    print(libros)
    

#"titulo" Título del libro No vacío ni solo espacios en blanco
def validar_titulo_libro():
    while True:
        titulo_libro_usuario = input("ingresa el titulo del libro : ").strip()

        if " " in titulo_libro_usuario or len(titulo_libro_usuario) <=0:
            print("vuelve a intentar. no se guardo registro ")
        else:
            return titulo_libro_usuario
        

#autor" Nombre del autor No vacío ni solo espacios en blanco
def validar_nombre_libro():
    while True:
        nombre_autor_usuario = input("ingresa el nombre del autor del titulo : ").strip()
        if " " in nombre_autor_usuario or len(nombre_autor_usuario) <=0:
            print("intenta nuevamente. no se guardo registro")
        else:
            return nombre_autor_usuario
        
    
#"ejemplares"Cantidad de copias disponibles Entero mayor o igual a cero
def validar_cantidad_ejemplares():
    while True:
        try:
            cantidad_ejemplares_usuario = int(input("ingresa la cantidad de ejemplares : "))
            if cantidad_ejemplares_usuario >=0:
                return cantidad_ejemplares_usuario
            else:
                print("la cantidad de ejemplares deber ser mayor que 0. no se guardo registro")
        except ValueError:
            print("valor no valido")
# "disponible"¿Hay al menos un ejemplar? False al registrar lo asigna el sistema automáticamente


# Opción 2 – Buscar libro:Solicita un título al usuario. 
def solicitar_titulo_busqueda():
    while True:
        titulo_busqueda_usuario = input("ingresa el titulo que buscas \n")
        if  " " in titulo_busqueda_usuario or len(titulo_busqueda_usuario) >=6:
            print("intenta nuevamente")
        else:
            return titulo_busqueda_usuario

def buscar_libro(nombre_libro_a_buscar):
    for cada_libro in libros:
        if cada_libro["nombre_libro"] == nombre_libro_a_buscar:
            print("encontrado")
            indice_del_libro_encontrado = libros.index(cada_libro)
            return indice_del_libro_encontrado
        
        return -1
# Debes definir una función que
# reciba la lista y el título, recorra la lista y retorne la posición del libro si lo encuentra, 
# o -1 si no existe. El programa principal decide qué mostrar según ese valor.

 

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_del_menu_seleccionada = opcion_usuario()

        if opcion_del_menu_seleccionada == "1":
            agregar_libro()

        elif opcion_del_menu_seleccionada == "2":
            nombre_libro_a_buscar = solicitar_titulo_busqueda()
            indice_libro_encontrado = buscar_libro(nombre_libro_a_buscar)
            if indice_libro_encontrado is not None:
                for indice, cada_libro_exitente in enumerate(libros):
                    print(cada_libro_exitente[0])
            else:
                print("no encontrado")

iniciar_programa()