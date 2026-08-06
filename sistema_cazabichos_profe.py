lista_bichos = []

def mostrar_menu():
    print(f"1. Ingresar bicho")
    print(f"2. Buscar bicho")
    print(f"3. Eliminar bicho")
    print(f"4. Actualizar estado de todos los bichos (si es peligroso o no)")
    print(f"5. Mostrar todos los bichos")
    print(f"6. Salir")

def opcion_menu_usuario():

  while True:

    opcion_elegida = input("Ingrese su opción (1 al 6)")

    if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
        return opcion_elegida 

    else:
        print("Opción invalida, vuelva a intentarlo")  

def validar_nombre_bicho():

  while True:
    nombre_bicho = input("Ingrese nombre del bicho: \n")

    if " " in nombre_bicho or len(nombre_bicho) <= 0:
        print("Nombre invalido, vuelva a intentar")

    else:
        return nombre_bicho

def validar_longitud_bicho():
    while True:
        try:
            tamaño_bicho = int(input("Ingrese el tamaño del bicho: \n"))
        except ValueError:
            print("ERROR, ingrese un numero entero positivo")
            continue

        if tamaño_bicho <= 0:
            print("ingrese un tamaño valido")
        else:
            return tamaño_bicho
       
def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese el nivel de peligrosidad de el bicho"))
        except ValueError:
            print("ERROR, ingrese un numero positivo")
            continue

        if peligrosidad_bicho <= 0:
            print("ERROR, ingrese un número mayor a 0")
        else:
            return peligrosidad_bicho


def agregar_bicho():
    nombre_bicho_validado = validar_nombre_bicho()
    tamaño_bicho_validado = validar_longitud_bicho()
    peligrosidad_bicho_validado = validar_peligrosidad_bicho()

    datos_bichos = {
        "nombre_bicho" : nombre_bicho_validado,
        "tamaño_bicho" : tamaño_bicho_validado,
        "peligrosidad_bicho" : peligrosidad_bicho_validado,
        "es_peligroso" : False
    }

    lista_bichos.append(datos_bichos)

def mostrar_todos_los_bichos():
    print(lista_bichos)

def buscar_bicho():
    nombre_bicho_a_buscar = input("Ingrese el nombre del bicho: ")

    for cada_bicho in lista_bichos:
        if cada_bicho["nombre_bicho"] == nombre_bicho_a_buscar:
            print("Bicho encontrado\n")
            print(f"Su nombre: {cada_bicho['nombre_bicho']}")
            print(f"Su longitud_bicho: {cada_bicho['longitud_bicho']}")
            print(f"Su peligrosidad_bicho: {cada_bicho['peligrosidad_bicho']}")
        else:
            print("Bicho no encontrado")

def main():

  while True:

    mostrar_menu()

    opcion_menu_seleccionada = opcion_menu_usuario()

    if opcion_menu_seleccionada == "1":
        agregar_bicho()

    elif opcion_menu_seleccionada == "2":
        buscar_bicho()

    elif opcion_menu_seleccionada == "3":
        print("Se manda a llamar la funcion que elimina")

    elif opcion_menu_seleccionada == "4":
        print("Se manda a llamar la funcion que Actualiza el estado")

    elif opcion_menu_seleccionada == "5":
        mostrar_todos_los_bichos()

    elif opcion_menu_seleccionada == "6":
        print("Adios")
        break

    else:
        print("La opcion ingresada no es una opción valida")

main()