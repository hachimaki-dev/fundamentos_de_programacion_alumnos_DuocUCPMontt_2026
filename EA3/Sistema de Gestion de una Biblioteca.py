lista_de_biblioteca

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========\n" \
    "1. Agregar libro\n" \
    "2. Buscar libro\n" \
    "3. Eliminar libro\n" \
    "4. Actulizar disponiblidad\n" \
    "5. Mostrar libros\n" \
    "6. Salir")

def opcion_menu_usuario():
    while True:
        opcion_elegida = input("Ingrese su opción (1 al 6): ")
        
        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida
        else:
            print("Opción inválida, vuelva a intentarlo")



def iniciar_prgrama():
    while True:
        mostrar_menu()
        opcion_menu_seleccionada = opcion_menu_usuario()

        if opcion_menu_seleccionada == "1":
        elif opcion_menu_seleccionada == "1":
        elif opcion_menu_seleccionada == "1":
        elif opcion_menu_seleccionada == "1":
        elif opcion_menu_seleccionada == "1":
        elif opcion_menu_seleccionada == "1":
        else:
            print("Opción inválida, vuelva a intentarlo")