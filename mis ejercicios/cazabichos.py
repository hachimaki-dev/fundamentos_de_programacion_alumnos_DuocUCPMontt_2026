lista_de_todos_los_bichos = []
#mustra el menu
def mostrar_menu():
    print(f"========== MENÚ PRINCIPAL ==========\n 1. Agregar bicho \n 2. Buscar bicho \n 3. Eliminar bicho \n 4. Actualizar estados \n 5. Mostrar bichos \n 6. Salir")
#inicia el programa
def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_usuario = leer_opcion()
        if opcion_usuario == "1":
            agregar_bichos()
        elif opcion_usuario == "2":
            print("buscar bichos")
        elif opcion_usuario == "3":
            print("eliminar bichos")
        elif opcion_usuario == "4":
            print("actualizar estados")
        elif opcion_usuario == "5":
            mostar_bichos()
        elif opcion_usuario == "6":
            print("salir")
            break
        else:
            print("opcion invalida")
def mostar_bichos():
    print(lista_de_todos_los_bichos)

#valida la opcion escogida
def leer_opcion():
    while True:
        opcion_escogida = input("seleccione una opcion del 1-6")
        if opcion_escogida in ["1","2","3","4","5","6"]:
                return opcion_escogida
        else:
            print("la opcion ingresada no es una opcion valida")
#valida el nombre del bicho
def validar_nombre_especie():
    nombre_especie = input("ingrese la especie del bicho")
    while True:
        if " " in nombre_especie or len(nombre_especie) < 0:
            print("el nombre de la especie es invalido")
        else:
            return nombre_especie
#valida el tamaño del bicho
def longitud_del_bicho():
    longitud_de_la_especie = int(input("ingrese el tamaño de la especie: \n"))
    while True:
        try:
            if longitud_de_la_especie <= 0:
                print("tamaño del bocho no es mayor a 0")
            else:
                return longitud_de_la_especie
        except ValueError:
            print("dato ingresado es invalido")
# valida la peligrosidad
def validar_peligrosidad():
    peligrosidad = float(input("ingrese la peligrosidad del la especie: \n "))
    while True:
        try:
            if 1.0 < peligrosidad > 10.0:
                print("dato invalido la peligrsidad debe de estar entre 1.0 y 10.0")
            else:
                return peligrosidad
        except ValueError:
            print("dato invalido")


def agregar_bichos():
    #nombre del bicho
    #tamaño del bicho
    #peligrosidad 1 a 10
    #el programa determina si es o no peligroso
    nombre_validado = validar_nombre_especie()
    longitud_valida = longitud_del_bicho()
    peligrosidad_valida = validar_peligrosidad()
    print(f"los datos nombres: {nombre_validado}, su tamaño es: {longitud_valida}, peligrosidad: {peligrosidad_valida}")
    datos_de_los_bichos = {"especie": nombre_validado,"tamaño del bicho": longitud_valida,"peligrosidad": peligrosidad_valida, "es_peligroso": False}
    se_registro =registrar_especie(datos_de_los_bichos)
    if se_registro == True:
        print("registro completdo")
        return True
    else:
        print("algo paso")
        return False

#registrar los bichos en una lista
def registrar_especie(diccionario_de_los_bichos):
    lista_de_todos_los_bichos.append(diccionario_de_los_bichos)
    return True



    


iniciar_programa()






        












