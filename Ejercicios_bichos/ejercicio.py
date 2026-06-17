def validar_especie():
    while True:
        nombre_bicho = input("Ingrese el nombre del bicho: ")
        if " " in nombre_bicho or len(nombre_bicho) <= 0:
            print("Error: el nombre no puede quedar vacio ni con espacios.")
        else:
            return nombre_bicho

def validar_longitud():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del bicho: "))
            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("Error: la longitud del bicho debe de ser un numero entero mayor a 0.")
        except ValueError:
            print("Dato invalido: ingrese un numero entero.")    

def validar_peligrosidad():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese el nivel de peligrosidad del bicho: "))
            if 1.0 <= peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("Error: Ingrese un numero decimal entre 1.0 y 10.0")
        except ValueError:
            print("Dato invalido: ingrese un numero decimal entre 1.0 y 10.0")

def agregar_bicho():
    nombre_bicho_validado = validar_especie() 
    longitud_bicho_validada = validar_longitud()
    peligrosidad_bicho_validada = validar_peligrosidad()

    bicho_registrado = {
        "nombre_bicho": nombre_bicho_validado,
        "longitud_bicho": longitud_bicho_validada,
        "peligrosidad_bicho": peligrosidad_bicho_validada,
        "es_peligroso": False
    }

    lista_bichos.append(bicho_registrado)
    print("¡Bicho registrado exitosamente!")

def buscar_bicho_por_nombre(nombre_del_bicho_a_buscar):
    if cada_bicho["nombre_bicho"] == nombre_del_bicho_a_buscar:
        print("Bicho encontrado.")
    else:
        print("Bicho no existente.")    

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("====================================")

def opcion_menu_usuario():
    while True:
        opcion_elegida = input("Ingrese su opción (1 al 6): ")
        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida 
        else:
            print("Opción invalida, vuelva a intentarlo")  


lista_bichos = []


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_seleccionada = opcion_menu_usuario()

        if opcion_menu_seleccionada == "1":
            agregar_bicho()
    
iniciar_programa()