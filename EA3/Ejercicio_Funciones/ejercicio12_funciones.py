def tiene_contenido_v2(texto):
    if texto.strip() != "":
        return True
    else:
        return False
def solicitar_titulo_valido():
    while True:
        titulo = input("Ingrese el titulo:\n")
        if tiene_contenido_v2(titulo):
            return titulo
        else:
            print("Error: El titulo no puede estar vacio ni contener solamente espacios.")