coleccion_general = []


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("7. Insertar datos de prueba")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_del_usuario = leer_opcion()

        if opcion_del_usuario == 1:
            agregar_bicho()
        elif opcion_del_usuario == 2:
            nombre_a_buscar = input("Ingrese el nombre del bicho que desea buscar: \n")
            indice_del_bicho = buscar_bicho_por_nombre(nombre_a_buscar)
            if indice_del_bicho is not None:
                print("Bicho encontrado")
            else:
                print("Este no exite")
        elif opcion_de_usuario == "3":
            nombre_del_bicho_a_eliminar = input("Ingrese el nombre del bicho que desea eliminar: \n")
            fue_eliminado = eliminar_bicho_por_nombre(nombre_del_bicho_a_eliminar)
            if fue_eliminado == True:
                print("Se elimino")
            else:
                print("no se pudo eliminar")
        elif opcion_de_usuario == "4":
            actualizar_si_es_peligroso()
            print("Se han actualiado todos los bichos peligrosos")
        elif opcion_de_usuario == "5":
            mostrar_todos_los_bichos()
        elif opcion_de_usuario == "6":
            print("LLAMAR A LA FUNCION QUE FINALIZA EL PROGRAMA")
            break
        elif opcion_de_usuario == "7":
            insertar_datos_de_prueba()
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
    
def buscar_bicho_por_nombre(nombre_del_bicho_a_buscar):
    for cada_bicho in coleccion_general:
        if cada_bicho["nombre_especie"] == nombre_del_bicho_a_buscar:
            print("Existe")
            indice_bicho_encontrado = coleccion_general.index(cada_bicho)
            return indice_bicho_encontrado

def eliminar_bicho_por_nombre(nombre_del_bicho_a_buscar_por_parametro):
    indice_del_bicho_a_buscar = buscar_bicho_por_nombre(nombre_del_bicho_a_buscar_por_parametro)
    if indice_del_bicho_a_buscar is not None:
        if lista_de_todos_los_bichos.pop(indice_del_bicho_a_buscar):
            print("Eliminado")
            return True
        else:
            print("no se pudo eliminar")
            return False


def actualizar_si_es_peligroso():
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["peligrosidad_especie"] >= 7.0:
            print("Es peligroso, entonces actualicemos su estado")
            cada_bicho["es_peligroso"] = True

def insertar_datos_de_prueba():
    lista_de_todos_los_bichos.append({
        "nombre_especie": "mariposa",
        "longitud_especie": 5,
        "peligrosidad_especie": 9.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_especie": "gusano",
        "longitud_especie": 8,
        "peligrosidad_especie": 2.9,
        "es_peligroso": False,
    })
    lista_de_todos_los_bichos.append({
        "nombre_especie": "pulga",
        "longitud_especie": 1,
        "peligrosidad_especie": 8.9,
        "es_peligroso": False,
    })

iniciar_programa()
