lista_de_todos_los_bichos = []

def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho\n2. Buscar bicho\n3. Eliminar bicho\n4. Actualizar estados\n5. Mostrar bichos \n6. Salir")
    print("=====================================")

def opcion_menu_usuario():
    while True:
        try:
            opcion_elegida = int(input("Ingrese su opcion:      "))
            if opcion_elegida in [1 , 2 , 3 ,4 ,5 , 6]:
                return opcion_elegida
            else:
                print("Opcion Invalida , Vuelva a intentarlo")
        except ValueError:
            print("Ingrese una opcion valida")

def agregar_bicho():
    nombre_bicho_validado = validar_nombre_bicho()
    longitud_bicho_validado = validar_tamaño_del_bicho()
    peligrosidad_bicho_validado = validar_peligrosidad_del_bicho()

    datos_del_bicho = {
        "nombre_especie" : nombre_bicho_validado , 
        "longitud_especie" : longitud_bicho_validado ,
        "peligrosidad_especie" : peligrosidad_bicho_validado ,
        "es_peligroso" : False
    }

    lista_de_todos_los_bichos.append(datos_del_bicho)

def validar_nombre_bicho():
    while True:
        nombre_bicho = input("Ingrese nombre del bicho :    ")
        if " " in nombre_bicho or len(nombre_bicho) <= 0:
            print("Nombre Invalido , Vuelva a intentarlo\n")
        else:
            return nombre_bicho

def validar_tamaño_del_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del Bicho :       "))
            if longitud_bicho <= 0 :
                print("Ingrse un nuemro Mayor a 0 \n")
            else:
                return longitud_bicho
        except ValueError:
            print("Ingrese una Opcion valida , Vuelva a intentarlo\n")


def validar_peligrosidad_del_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese la Peligrosidad del Bicho :       "))
            if peligrosidad_bicho < 1.0 or peligrosidad_bicho > 10.0:
                print("Ingrese Un numero entre 1.0 y 10.0 , Vuelva a intentarlo\n")
            else:
                return peligrosidad_bicho
        except ValueError:
            print("Ingrese una opcion valida\n")


def salir_del_programa():
    print("\nGracias por usar el Cazabichos. ¡Hasta la próxima expedición!\n")


def buscar_bicho():
    if len(lista_de_todos_los_bichos) < 1:
        print("\nEsta la lista Vacia , Vuelva a intentarlo en otro momento\n")
    else:
        while True:
            bandera_buscar_bicho = False
            nombre_bicho_a_buscar = input("Ingrese el nombre del bicho a Buscar:     ").lower()
            for cada_bicho in lista_de_todos_los_bichos:
                if cada_bicho["nombre_especie"].lower() == nombre_bicho_a_buscar:
                    bandera_buscar_bicho = True
                    return print(f"\nDatos del Bicho que busco :\n Nombre del Bicho : {cada_bicho["nombre_especie"]} | Tamaño del Bicho : {cada_bicho["longitud_especie"]} | Peligrosidad del Bicho : {cada_bicho["peligrosidad_especie"]} | Es Peligroso el bicho : {cada_bicho["es_peligroso"]}\n ")

            if not bandera_buscar_bicho:
                print("Bicho no encontrado , vuelva a intentarlo")


def eliminar_bicho():
    if len(lista_de_todos_los_bichos) < 1:
        print("\nEsta la lista Vacia , Vuelva a intentarlo en otro momento\n")
    else:
        while True:
            bandera_eliminar_bicho = False
            nombre_eliminar_bicho = input("Ingrese el nombre De la especie del Bicho que Quiera Eliminar :     ").lower()
            for cada_bicho in lista_de_todos_los_bichos:
                if cada_bicho["nombre_especie"].lower() == nombre_eliminar_bicho:
                    bandera_eliminar_bicho = True
                    lista_de_todos_los_bichos.remove(cada_bicho)
                    return print(f"\nUsted a Eliminado la Especie llamada {cada_bicho["nombre_especie"]}\n ")

            if not bandera_eliminar_bicho:
                print("Especie no Encontrada , Vuelva a intentarlo")


def actualizar_datos_bichos():
    if len(lista_de_todos_los_bichos) < 1:
        print("\nEsta la lista Vacia , Vuelva a intentarlo en otro momento\n")
    else:
        for i in lista_de_todos_los_bichos:
            if i["peligrosidad_especie"] >= 7.0 :
                i["es_peligroso"] = True
            else:
                i["es_peligroso"] = False
        
        print("\nProceso Terminado , Datos Ya Actualizados\n")


def main():
    while True:
        menu_principal()
        opcion_menu_seleccionada = opcion_menu_usuario()

        if opcion_menu_seleccionada == 1:
            agregar_bicho()
        elif opcion_menu_seleccionada == 2:
            buscar_bicho()
        elif opcion_menu_seleccionada == 3:
            eliminar_bicho()
        elif opcion_menu_seleccionada == 4:
            actualizar_datos_bichos()
        elif opcion_menu_seleccionada == 5:
            if len(lista_de_todos_los_bichos) <= 0:
                print("Todavia no hay Bichos Registrados\n")
            else:
                print("\nLos bichos Registrados Son:\n")
                for i in lista_de_todos_los_bichos:
                    print(f"Nombre del Bicho : {i["nombre_especie"]} | Tamaño del Bicho : {i["longitud_especie"]} | Peligrosidad del Bicho : {i["peligrosidad_especie"]} | Es Peligroso el bicho : {i["es_peligroso"]} ")
                    print("********************************************"*3)
                print()
        elif opcion_menu_seleccionada == 6:
            salir_del_programa()
            break
        else:
            print("Ingrese una opcion valida")

main()