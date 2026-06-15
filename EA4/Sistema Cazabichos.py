coleccion_general = []


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_del_usuario = leer_opcion()

        if opcion_del_usuario == 1:
            agregar_bicho()
        elif opcion_del_usuario == 2:
            print("Llamar a la funcion que busca")
        elif opcion_del_usuario == 3:
            print("Llamar a la funcion que elimina")
        elif opcion_del_usuario == 4:
            print("Llamar a la funcion que actualiza")
        elif opcion_del_usuario == 5:
            print(coleccion_general)
        elif opcion_del_usuario == 6:
            print("Llama a la funcion que finaliza el programa")
        else:
            print("Opcion invalida, vuelva a intentarlo")

def leer_opcion():
    while True:
        opcion_ingresada = int(input("Seleccione una opcion: "))
        if opcion_ingresada in [1, 2, 3, 4, 5, 6]:
            return opcion_ingresada
        else:
            print("La opcion ingresada no es valida")

def validar_nombre_especie():
    while True:
        nombre_especie = input("Ingrese la especie del bicho: \n").strip()
        if len(nombre_especie) <= 0:
            print("El nombre de la especie no puede estar vacio")
        else:
            return nombre_especie


def validar_tamaño_bicho():
    while True:
        try:
            tamaño_bicho = int(input("Ingrese el tamaño del bicho: \n"))
            if tamaño_bicho > 0:
                return tamaño_bicho
            else:
                print("La longitud debe ser mayor que 0")
        except ValueError:
            print("Ingrese un numero valido")


def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese la peligrosidad del bicho: \n"))
            if 1.0 <= peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("La peligrosidad_especie debe ser mayor que 0")
        except ValueError:
            print("Ingrese un numero valido")

def registrar_especie(dicionario_de_la_especie):
    coleccion_general.append(dicionario_de_la_especie)
    print("El bicho se registro de forma exitosa")
    return True

def agregar_bicho():
    nombre_especie_validado = validar_nombre_especie()
    print(f"El nombre de la espcie es {nombre_especie_validado}")
    tamaño_bicho_validado = validar_tamaño_bicho()
    print(f"El tamaño del bicho es de {tamaño_bicho_validado}")
    peligrosidad_bicho_validado = validar_peligrosidad_bicho()
    print(f"La peligrosidad del bicho es de {peligrosidad_bicho_validado}")

    print(f"Los datos son: Nombre {nombre_especie_validado} su longitud es {tamaño_bicho_validado} y su peligrosidad es {peligrosidad_bicho_validado}")

    datos_de_la_especie = {
        "nombre_especie" : nombre_especie_validado,
        "tamaño_bicho" : tamaño_bicho_validado,
        "peligrosidad_bicho" : peligrosidad_bicho_validado,
        "es_peligroso" : False
    }
    
    se_registro = registrar_especie(datos_de_la_especie)
    

iniciar_programa()
