lista_de_bichos_encontrados = []

def validacion_de_la_especie(especie):
    especie_limpia = especie.strip()

    if especie_limpia != "":
        return True
    else:
        return False

def validar_tamano(tamano_str):
    try:
        tamano = int(tamano_str)
        if tamano > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_peligrosidad(peligrosidad_str):
    try:
        peligrosidad = float(peligrosidad_str)
        if 1.0 <= peligrosidad <= 10.0:
            return True
        else:
            return False
    except ValueError:
        return False

def agregar_bicho(lista):
    especie = input("Ingrese especie del bicho: ")
    if not validar_especie(especie):
        print("Error: La especie no puede estar vacía.")
        return
        
    tamano_str = input("Ingrese tamaño en cm: ")
    if not validar_tamano(tamano_str):
        print("Error: El tamaño debe ser un número entero mayor a 0.")
        return
        
    peligrosidad_str = input("Ingrese nivel de peligrosidad (1.0 - 10.0): ")
    if not validar_peligrosidad(peligrosidad_str):
        print("Error: Peligrosidad debe ser un número decimal entre 1.0 y 10.0.")
        return
    
    bicho = {
        "especie": especie.strip(),
        "tamaño": int(tamano_str),
        "peligrosidad": float(peligrosidad_str),
        "peligroso": False
    }
    lista.append(bicho)
    print("¡Bicho registrado exitosamente!")

def buscar_bicho(lista, especie_buscada):
    buscar = especie_buscada.lower().strip()
    for i in range(len(lista)):
        if lista[i]["especie"].lower() == buscar:
            return i 
    return -1

def menú_principal():

    menú_en_funcion = True

    while menú_en_funcion:

        print("=== Panel Ménu Principal ===")
        print("1. Agregar bicho")
        print("2. Buscar bicho")
        print("3. Eliminar bicho")
        print("4. Actualizar estados")
        print("5. Mostrar bichos")
        print("6. Salir")
        print("============================")
