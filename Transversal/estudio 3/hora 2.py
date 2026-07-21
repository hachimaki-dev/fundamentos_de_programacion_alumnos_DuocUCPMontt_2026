def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ["G", "PG", "M"]

def validar_precio_texto(precio_texto):
    try:
        return int(precio_texto) > 0
    except ValueError:
        return False
    

while True:
    titulo = input("Ingrese el nombre del titulo: ")
    if validar_titulo(titulo):
        break
    print("Error: El titulo no puede estar vacio")

while True:
    clasificacion = input("Ingrese la clasificación (G, PG, M): ")
    if validar_clasificacion(clasificacion):
        break
    print("Error: La clasificacion no es valida")

while True:
    precio_texto = input("Ingrese el precio del anime: ")
    if validar_precio_texto(precio_texto):
        precio = int(precio_texto)
        break
    print("Error: Ingrese un número entero positivo Mayor a 0")

    