def mostrar_menu():
    print("----MENU PRINCIPAL----")
    print("1. agregar bicho")
    print("2. buscar bicho")
    print("3. eliminar bicho")
    print("4. actualizar estados de nivel de peligrosidad")
    print("5. mostrar bichos")
    print("6. salir")
    print("----------------------")
    def leer_opcion():
        while True:
            opcion = int(input("ingrese una opcion: "))
            if opcion.isdigit():
                num = int(opcion)
                if 1 <= num <= 6:
                    return num
                print("opcion no valida, debe ingresar una opcion entre 1 y 6")


def validar_especie():
    return bool(especie and especie.isalpha())
