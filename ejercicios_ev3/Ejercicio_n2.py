def main():
    mostrarMenuPrincipal()
    desicionMenuPrincipal()
    
    decision_menu = decision_menu_elegida

    if decision_menu_elegida == 1:
        print("Usted ha elegido "Agregar Registro" ")




def mostrarMenuPrincipal():
    print("========MENÚ PRINCIPAL======== \n")
    print("1.Agregar Registro")
    print("2.Buscar Registro")
    print("3.Eliminar Registro")
    print("4.Actualizar estados")
    print("5.Mostrar Registros")
    print("6.Salir")

def desicionMenuPrincipal():
    while True:
        try:
            desicion_menu = int(input("Eliga la acción que desea realizar, ingresando su respectivo número: \n"))
            if desicion_menu > 0 and desicion_menu < 7:
                return desicion_menu
            else:
                print("Ingrese un valor válido entre 1-6 porfavor")
        except ValueError:
            print("El valor debe ser insertado en números enteros, no letras.")

def agregarRegistro():
        ingresoNombreEstudiante()
        copia_nombre_sin_espacios = nombre_validado
        ingresoNombreAsignatura()
        nombre_asignatura_sin_espacios = asignatura_validada
        


def ingresoNombreEstudiante():
    while True:
        nombre_ingresado = input("Ingrese el nombre de el estudiante: \n")
        copia_nombre_sin_espacios = nombre_ingresado.strip()
        if copia_nombre_sin_espacios > 0:
            print("El nombre ingresado es válido, y ha sido ingresado.")
            return copia_nombre_sin_espacios
        else:
            print("El nombre no es válido, recuerde que no pueden ser solo espacios, ni estar vacío")

def ingresoNombreAsignatura():
    while True:
        nombre_asignatura = input("Ingrese el nombre de la asignatura: \n")
        nombre_asignatura_sin_espacios = nombre_asignatura.strip()
        if nombre_asignatura_sin_espacios > 0:
            print("La asignatura ingresada es válida, y ha sido ingresada.")
            return nombre_asignatura_sin_espacios
        else:
            print("La asignatura no es válida, recuerde que no pueden ser solo espacios ni estar vacía.")        
        
        

main()