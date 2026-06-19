bichos = [
    {"especie": "", # String
    "tamaño": "", # Numero mayor a 0
    "peligrosidad": "", # Del 1.0 al 10.0
    "peligroso": "" # Booleano, True or False
    }
]

def menuDeInicio():
        print("================== Menu Principal ==================")
        print("1. Agregar un bicho \n2. Buscar bicho \n3. Eliminar Bicho \n4. Actualizar estados \n5. Mostrar bichos \n6. Salir")
        print("====================================================")

def seleccionDelMenuPorElUsuario():
    while True:
        try:
            seleccion = int(input("[]: "))
            if seleccion > 0 and seleccion < 7:
                return seleccion
                break
            else:
                print("Porfavor ingrese un numero valido")
        except ValueError:
            print("El valor tiene que ser un numero")

def AgregarUnBichoNuevo(bichos):
    while True:
        especie = input("Ingrese la especie \n[]: ").rstrip
        if especie == "":
            print("El tipo de especie no puede ser vacio")
            continue
        else:
            break
    while True:
        try:
            tamaño = int(input("Ingrese el tamaño del bicho (en cm) \n[]: "))
            break
        except ValueError:
            print("El tamaño necesita ser un numero entero")
