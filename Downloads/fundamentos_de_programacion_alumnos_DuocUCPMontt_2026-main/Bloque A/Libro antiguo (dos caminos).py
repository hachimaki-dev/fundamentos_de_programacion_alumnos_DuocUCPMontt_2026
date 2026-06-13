def es_libro_antiguo(anio):
    return anio < 1990

libro = int(input("ingrese el año del libro: "))
respuesta = es_libro_antiguo(libro)
print(respuesta)