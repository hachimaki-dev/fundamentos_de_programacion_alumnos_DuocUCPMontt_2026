def saludar(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")

saludar("Juan")              # usa "español" por defecto
saludar("John", "inglés")    # sobreescribe el default
#Los parámetros con default van siempre después de los que no poseen un default