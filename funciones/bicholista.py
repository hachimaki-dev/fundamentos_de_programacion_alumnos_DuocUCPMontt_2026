lista_bichos = []

def mostrar_menu():
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    
def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_usuario = leer_opcion()
        
        if opcion_usuario == "1":
            agregar_bicho()
        elif opcion_usuario == "2":
            nombra_buscar = input("Ingrese el nombre del bicho a buscar: \n")  
            indice_del_bicho = buscar_nombre_bicho(nombra_buscar)
            if indice_del_bicho is not None:
                print("Bicho encontrado")
            else:
                print("Bicho no existe")
                
        elif opcion_usuario == "3":
            bicho_eliminar = input("Ingrese el bicho que desee eliminar:")
            eliminado = eliminar_bicho_nombre(nombre_bicho_eliminar):
            if eliminado == True:
                print("Se elimino")
            else:
                print("No se pudo eliminar")
        elif opcion_usuario == "4":
            actualizar_peligro()
            print("Se actualizado el peligro de los bichos")
        elif opcion_usuario == "5":
            mostrar_todos_bichos()
        elif opcion_usuario == "6":
            print("llamar funcion terminar programa")
            break
        
def mostrar_todos_bichos():
    print(lista_bichos)
    
def leer_opcion():
    while True:
        opcion_ingresada = input("Seleccione opcion: ")
        
        if opcion_ingresada
    
       