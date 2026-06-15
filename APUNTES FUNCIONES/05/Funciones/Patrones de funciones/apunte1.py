def saludar(nombre, idioma="español"):      #el parametro idioma="español" 
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")

saludar("Juan")              # usa "español" por defecto
saludar("John", "inglés")    # sobreescribe el default