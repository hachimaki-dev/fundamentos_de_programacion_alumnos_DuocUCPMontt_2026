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
def buscar_libro(lista_libros , titulo_busqueda_usuario):
    for pocicion_libro in range(len(libros)):
        if libros[pocicion_libro]["titulo_libro"].lower() == titulo_busqueda_usuario.lower():
            return pocicion_libro
    print("no encontrado")     
    return -1

def eliminar_libro(titulo_busqueda_usuario):
    libro_encontrado = buscar_libro(libro_encontrado)
    libros.pop(libro_encontrado)
    return True

titulo_busqueda_usuario = input("ingresa el titulo que deseas buscar :\n")
posicion_libro = buscar_libro(libros,titulo_busqueda_usuario)
indice_libro_encontrado = buscar_libro(libros,posicion_libro)
if indice_libro_encontrado != -1:
    libro_encontrado = libros[posicion_libro]
    
    print(f"libro_encontrado en la posicion {indice_libro_encontrado}")

titulo_ingresado_para_eliminar = input("ingresa el titulo a eliminar : \n").strip()
if " " not in titulo_ingresado_para_eliminar or len(titulo_ingresado_para_eliminar) <=0: 
    buscar_libro_para_eliminar = buscar_libro(libros,titulo_ingresado_para_eliminar)
    if buscar_libro_para_eliminar != -1:
        libros.pop(buscar_libro_para_eliminar)
        print(libros)

    else:
        print(f"El libro {titulo_ingresado_para_eliminar} no se encuentra registrado")