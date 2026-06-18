def menu_usuario(): 
    print("--Menu Principal--")
    print("1 . Agregar bicho")
    print("2 . Buscar bicho")
    print("3 . Eliminar bicho")
    print("4 . Actualizar estados")
    print("5 . Mostrar bichos")
    print("6 . Salir")
def opcion_escogida_usuario():
        while True:
            try:
                opcion_elegida_por_el_usuario = int(input("Ingrese una opcion (1 al 6)"))
                if  1 <= opcion_elegida_por_el_usuario <= 6:
                    return opcion_elegida_por_el_usuario
                else:
                    print("No puede ser menor que 0")
                    continue
            except ValueError:
                print("Debe ser del 1 al 6")
def opciones():
    if opcion_elegida_por_el_usuario == 1:
        print("Agregar bichos")
    if opcion_elegida_por_el_usuario == 2:


menu_usuario()
opcion_escogida_usuario()
opciones()



