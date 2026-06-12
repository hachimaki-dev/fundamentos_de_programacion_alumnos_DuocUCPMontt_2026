def saludar(nombre, idioma = "español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")
        
saludar("Juan")            #Usa "español" por defecto
saludar("John", "inglés")  #Sobreescribe el default
        
