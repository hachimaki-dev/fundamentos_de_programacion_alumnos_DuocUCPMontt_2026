

def menu_principal ():
    print("====MENU PRINCIPAL====")
    print("1. registar animal ")
    print("2. buscar animal ")
    print("3. eliminar animal")
    print("4. actualizar alertas ")
    print("5. mostrar animales ")
    print("6. salir ")
    print("======================")

def opcion_menu():
    while True:
        opcion_elegida = input("ingrese su opcion(1 al 6): ")

        if opcion_elegida in [1, 2, 3, 4, 5, 6]:
            return opcion_elegida

        else:
            print("opcion invalida vuelve a intentarlo :(")

def salir ():
    mostrar_menu()
salir()

def registar_animales():


