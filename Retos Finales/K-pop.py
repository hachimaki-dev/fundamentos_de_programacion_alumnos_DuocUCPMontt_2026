bandera = True

while bandera:
    print("Escoja una banda de K-POP")
    print("1. BTS")
    print("2. BLACKPINK")
    print("3. STRAYKIDS")
    
    opcion_a_elegir = input("Ingrese el nombre de su Banda").lower()
    
    if opcion_a_elegir == "bts" or opcion_a_elegir == "blackpink" or opcion_a_elegir == "straykids":
        print(f"Bienvenido al Fandom de {opcion_a_elegir}")
        break
    else:
        print("Ingrese un grupo valido")