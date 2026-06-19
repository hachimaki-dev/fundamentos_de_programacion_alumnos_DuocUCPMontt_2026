# bichos = []


# while True:
#     print("========== MENÚ PRINCIPAL ==========")
#     print("1. Agregar bicho")
#     print("2. Buscar bicho")
#     print("3. Eliminar bicho")
#     print("4. Actualizar estados")
#     print("5. Mostrar bichos")
#     print("6. Salir")
#     print("=====================================")


#     opcion = int(input("que opcion quiere ver: "))

#     if opcion == 1:
#         try:
#             especie = input("")
#             if " " not in especie:
#                 break
#         except ValueError:
#             print("el numero debe ser mayor a cero")
        
#         try:
#             tamaño = int(input(""))
#             if tamaño > 0:
#                 break
#             else:
#                 print("el numero tiene que ser mayor a cero")
#         except ValueError:
#             print("")
        
#         try:
#             nivel_peligrosidad = int(input(""))
#             if nivel_peligrosidad > 0 and nivel_peligrosidad <= 10:
#                 break
#             else:
#                 print("el numero tiene que ser positivo")
#         except ValueError:
#             print("el numero tiene que ser positivo")

#     elif opcion == 2:

#         print
#     elif opcion == 3:
#         print
#     elif opcion == 4:
#         print
#     elif opcion == 5:
#         print("gracias por usar el cazabichos. ¡Hasta la próxima expedición!")
#         break



#-----------------------------------------------------------------------

#version con funciones


bichos = []


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("=====================================")

def main():
    mostrar_menu()
    opcion_del_usuario = leer_opcion()
    while True:
        if opcion_del_usuario == 1:
            agregar_bicho()
            
        elif opcion_del_usuario == 2:
            print("")
        elif opcion_del_usuario == 3:
            print("")
        elif opcion_del_usuario == 4:
            print("")
        elif opcion_del_usuario == 5:
            mostrar_bichos()
        elif opcion_del_usuario == 6:
            print("")
            break
        else:
            print("opcion invalida")

def mostrar_bichos():
    print("esto son los datos")

def leer_opcion():
    while True:
        opcion_ingresada = int(input("seleccionar opcion: "))


        if opcion_ingresada in [1, 2, 3, 4, 5, 6]:
            return opcion_ingresada
        else: 
            print("opcion invalida")


def validar_nombre():
    while True:
        especie = input("ingrese la especie del bicho: ")
        if " " in especie or len(especie) < 0:
            print("el nombre de la especie no es valido")
        else:
            return especie
        
def validar_tamaño():
    while True:
        try:
            tamaño = int(input("ingrese el tamaño del bicho: "))
            if tamaño <= 0:
                print("el numero debe ser mayor a cero")
            else:
                return tamaño
        except ValueError:
            print("ingresa numero valido")
def validar_peligrosidad():
    while True:
        try:
            peligrosidad = float(input("ingresa nivel de peligrosidad: "))
            if peligrosidad <= 0:
                print("el numero tiene que ser mayor a 1")
            elif peligrosidad >= 10:
                print("el tope es hasta 10.0")
            else:
                return peligrosidad
        except ValueError:
            print("dato invalido")

def registrar_especie(recibir_diccionario):
    bichos.append(recibir_diccionario)
    print("el bicho se registro exitosamente")
    return True

def agregar_bicho():
    #nombre
    nombre_valido = validar_nombre()
    print(f"El nombre de la espcie es: {nombre_valido}")
    #tamaño
    tamaño_validado = validar_tamaño()
    print(f"El tamaño de la especie es: {tamaño_validado}")
    #peligrosidad (1 a 10) con float
    peligrosidad_valida = validar_peligrosidad()
    print(f"la peligrosidad de la especie es: {peligrosidad_valida}")
    
    datos_especie = {
        "nombre_especie": nombre_valido,
        "tamaño": tamaño_validado,
        "peligrosidad": peligrosidad_valida,
        "es_peligroso": False
    }

    exito_registro = registrar_especie(datos_especie)
    if exito_registro == True:
        print("se registro")
        return True
    else:
        print("algo inesperado sucede")
        return False

main()























