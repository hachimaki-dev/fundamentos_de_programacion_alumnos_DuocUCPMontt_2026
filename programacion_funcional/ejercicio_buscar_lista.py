#Opción 2 – Buscar libro: Solicita un título al usuario. Debes definir una función que
#reciba la lista y el título, recorra la lista y retorne la posición del libro si lo encuentra, o
#-1 si no existe. El programa principal decide qué mostrar según ese valor.

libros = [
    {'titulo_libro': 'jose', 
     'autor': 'ajaj', 
     'ejemplares': 20},

    {'titulo_libro': 'haha', 
     'autor': 'lemuak', 
     'ejemplares': 21},

   {'titulo_libro': "jeje", 
    'autor': 'niidea', 
    'ejemplares': 31}
]

"""def buscar_libro(lista_libros , titulo_busqueda):
    for libro in range(len(libros)):
        if libros[libro]["titulo_libro"].lower() == titulo_busqueda_usuario.lower():
            return libro

    return -1

titulo_busqueda_usuario = input("ingresa el libro a buscar : \n").strip()
posicion_libro = buscar_libro(libros,titulo_busqueda_usuario)
if posicion_libro != -1:
    libro_encontrado = libros[posicion_libro]
    print(f"\n¡Libro encontrado en la posición {posicion_libro}!")
    print(f"📌 Título: {libro_encontrado['titulo_libro']}")
    print(f"✍️ Autor: {libro_encontrado['autor']}")
    print(f"📚 Ejemplares: {libro_encontrado['ejemplares']}")"""

def buscar_libro(lista_libros , titulo_busqueda_usuario):
    for pocicion_libro in range(len(libros)):
        if libros[pocicion_libro]["titulo_libro"].lower() == titulo_busqueda_usuario.lower():
            return pocicion_libro
    print("no encontrado")     
    return -1

titulo_busqueda_usuario = input("ingresa el titulo que deseas buscar :\n")
posicion_libro = buscar_libro(libros,titulo_busqueda_usuario)
if posicion_libro != -1:
    libro_encontrado = libros[posicion_libro]
    print(libro_encontrado)