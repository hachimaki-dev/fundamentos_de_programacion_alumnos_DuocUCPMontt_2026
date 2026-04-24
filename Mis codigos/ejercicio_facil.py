libros = {
    "titulo:": "Harry potter", 
    "autor:": "J.K Rowlin",
    "anio:": 1997
 }

for clave, valor in libros.items():
    print(clave, valor)

libros["anio:"] = 2007
libros["editorial:"] = "Editorial Salamandra"

for clave, valor in libros.items():
    print(clave, valor)