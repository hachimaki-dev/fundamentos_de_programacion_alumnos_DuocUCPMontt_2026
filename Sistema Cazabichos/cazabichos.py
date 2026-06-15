lista_bichos = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("=====================================")

def elegir_opcion_menu():
    while True:
        opcion = input("Elija una opción (1/2/3/4/5/6): ")
        if opcion in ('1','2','3','4','5','6'):
            return opcion # funciona como break
        else:
            print("Opción inválida. Ingrese una opción dentro del rango [1-6]")
    
def validar_especie_bicho():
    while True:
        especie = input("Ingrese la especie del bicho: ")
        if " " in especie or len(especie) <= 0:
            print("Este campo no puede estar vacío ni ser solo espacios en blanco.\nVuelva a intentar.")
        else:
            return especie

def validar_longitud_bicho():
    while True:
        try:
            longitud = int(input("Ingrese el tamano del bicho: "))
            if longitud > 0:
                return longitud
            else:
                print("El tamaño del bicho debe ser superior a cero.")
        except ValueError:
            print("Tipo de dato invalido. Ingrese un entero mayor a cero.")

def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad = float(input("Ingrese la peligrosidad del bicho: "))
            if 1.0 <= peligrosidad <= 10.0:
                return peligrosidad
            else:
                print("La peligrosidad debe estar dentro del rango [1.0 - 10.0]. Vuelva a intentar.")
        except ValueError:
            print("Tipo de dato invalido. Ingrese un decimal entre 1.0 y 10.0")

def agregar_bicho():
    especie_bicho_validada = validar_especie_bicho()
    longitud_bicho_validada = validar_longitud_bicho()
    peligrosidad_bicho_validada = validar_peligrosidad_bicho()

    datos_del_bicho = {
        'especie': especie_bicho_validada,
        'longitud': longitud_bicho_validada,
        'peligrosidad': peligrosidad_bicho_validada,
        'es_peligroso': False
    }

    lista_bichos.append(datos_del_bicho)

def buscar_bicho():
    bicho_buscado = input("Ingrese la especie del bicho a buscar: ")
    for i in range(len(lista_bichos)):
        if lista_bichos[i]['especie'] == bicho_buscado:
            return lista_bichos[i]
        else:
            print("No esta el bicho")
            return -1
            
def eliminar_bicho():
    # agregar validacion cuando no esta el bicho

    dict_bicho_eliminar = buscar_bicho()
    if dict_bicho_eliminar != -1:
        lista_bichos.remove(dict_bicho_eliminar)
    else:
        print("No esta el bicho")

def actualizar_estados_bichos():
    for i in range(len(lista_bichos)):
        if lista_bichos[i]['peligrosidad'] >= 7.0:
            lista_bichos[i]['es_peligroso'] == True

def mostrar_todos_los_bichos():
    return lista_bichos


def iniciar_programa(): # funcion main
    while True:
        mostrar_menu()
        opcion_menu_seleccionada = elegir_opcion_menu()
        if opcion_menu_seleccionada == '1':
            agregar_bicho()
        elif opcion_menu_seleccionada == '2':
            print(buscar_bicho())
        elif opcion_menu_seleccionada == '3':
            eliminar_bicho()
        elif opcion_menu_seleccionada == '4':
            actualizar_estados_bichos()
        elif opcion_menu_seleccionada == '5':
            print(mostrar_todos_los_bichos())
        elif opcion_menu_seleccionada == '6':
            break
        else:
            print("La opcion ingresada no es una opcion valida.")

iniciar_programa()        