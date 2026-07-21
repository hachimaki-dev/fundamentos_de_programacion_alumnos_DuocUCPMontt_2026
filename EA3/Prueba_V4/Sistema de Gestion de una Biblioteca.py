def validar_titulo_del_libro():
    while True:
        nombre_titulo = input("Ingrese nombre del Titulo: ").strip()

        if " " in nombre_titulo or len(nombre_titulo) <= 0:
            print("Titulo inválido, vuelva a intentar")
        else:
            return nombre_titulo
        
def validar_autor_del_libro():
    while True:
        nombre_autor = input("Ingrese nombre del Autor: ").strip()

        if " " in nombre_autor or len(nombre_autor) <= 0:
            print("Autor inválido, vuelva a intentar")
        else:
             return nombre_autor

def validar_ejemplares_del_libro():
    while True:
        cantidad_ejemplares = int(input("Ingrese la cantidad de ejemplares del libro: "))
        
        if cantidad_ejemplares >= 0:
            return cantidad_ejemplares
        
        else:
            print("La cantidad de ejemplares ingresada no es valida")





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

        elif opcion_menu_seleccionada == "2":
        elif opcion_menu_seleccionada == "3":
        elif opcion_menu_seleccionada == "4":
        elif opcion_menu_seleccionada == "5":
        elif opcion_menu_seleccionada == "6":
        else:
            print("Opción inválida, vuelva a intentarlo")