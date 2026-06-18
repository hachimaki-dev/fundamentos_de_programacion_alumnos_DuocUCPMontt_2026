lista_de_todos_los_bicho = []

def mostrar_menú():
    print(f"1. Ingresar bicho")
    print(f"2. Buscar bicho")
    print(f"3. Eliminar bicho")
    print(f"4. Actiañozar estadp de tpdps ñps bichos")
    print(f"5. Mostrar todos los bichos")
    print(f"6. Salir")

def opcion_menú_usuario():
    
    while True: 
        opcion_elegida = input("Ingresa su opcion (entre 1 a 6): ")
        if opcion_elegida in ["1" , "2" , "3" , "4" , "5" , "6"]:
            return opcion_elegida
        else:
            print("Opcion invalida, vuelva a intentarlo")

def validar_nombre_bicho():
    while True:
        nombre_bicho = input("Ingrese nombre de la especie del Bicho: \n")
        if " " in nombre_bicho or len(nombre_bicho <= 0):
            print("Nombre invalido, vuelva a intentar")
        else:
            return nombre_bicho
        
def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese longitud del bicho: "))
            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("La longitud debe ser mayor que cero")
        except ValueError:
            print("Valor no valiod")

def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_del_bicho = int(input("Ingrese el nivel de peligrosidad del bicho: \n"))
            if peligrosidad_del_bicho > 0:
                return peligrosidad_del_bicho
            else:
                print("La peligrosidad del bicho debe ser mayor que cero")
        except ValueError:
            print("Valor no valiod")

#def longitud_bicho(longitud_del_bicho_str):
#    try:
#        tamaño_del_bicho = int(longitud_del_bicho_str)
#        if tamaño_del_bicho > 0:
#            return True
#        else:
#            return False
#    except ValueError:
#        return False

def agregar_bicho():
    validar_nombre_bicho = validar_nombre_bicho()
    validar_longitud_bicho = validar_longitud_bicho()
    validar_peligrosidad_bicho = validar_peligrosidad_bicho()

    datos_de_bicho = {
        "nombre_bicho" :validar_nombre_bicho ,
        "peligrosidad_bicho": validar_peligrosidad_bicho ,
        "longitud_bicho": validar_longitud_bicho ,
        "es_peligroso": False
    }

    lista_de_todos_los_bicho.apperd(datos_de_bicho)

def iniciar_programa():
    while True: 
        mostrar_menú()
        opcion_seleccionada_del_menú = opcion_menú_usuario()

        if opcion_seleccionada_del_menú == "1":
            print("Se manda a llamar la funcion que se agrega")
        elif opcion_seleccionada_del_menú == "2":
            print("Se llama la funcion que busca")
        elif opcion_seleccionada_del_menú == "3":
            print("se llama la funcion de eliminar")
        elif opcion_seleccionada_del_menú == "4":
            print("Se manda a llamar la funcion que muestra todo los bichos")
        elif opcion_seleccionada_del_menú == "5":
            print("Se manda a llamar la funcion que Actualiza el estado")
        elif opcion_seleccionada_del_menú == "6":
            print("Adios")
            break

iniciar_programa()