# SISTEMA CAZABICHOS — Solución Completa

def validar_especie(especie):
    especie_limpia = especie.strip()
    if especie_limpia != "":
        return True
    else:
        return False


def validar_tamano(tamano_str):
    try:
        tamano = int(tamano_str)
        if tamano > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validar_peligrosidad(peligrosidad_str):
    try:
        peligrosidad = float(peligrosidad_str)
        if 1.0 <= peligrosidad <= 10.0:
            return True
        else:
            return False
    except ValueError:
        return False


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        opcion = input("Seleccione una opción (1-6): ")
        if opcion.isdigit():
            num = int(opcion)
            if 1 <= num <= 6:
                return num
        print("Opción inválida. Ingrese un número entre 1 y 6.")


def agregar_bicho(lista):
    especie = input("Ingrese especie del bicho: ")
    if not validar_especie(especie):
        print("Error: La especie no puede estar vacía.")
        return

    tamano_str = input("Ingrese tamaño en cm: ")
    if not validar_tamano(tamano_str):
        print("Error: El tamaño debe ser un número entero mayor a 0.")
        return

    peligrosidad_str = input("Ingrese nivel de peligrosidad (1.0 - 10.0): ")
    if not validar_peligrosidad(peligrosidad_str):
        print("Error: La peligrosidad debe ser un número decimal entre 1.0 y 10.0.")
        return

    bicho = {
        "especie": especie.strip(),
        "tamaño": int(tamano_str),
        "peligrosidad": float(peligrosidad_str),
        "peligroso": False
    }
    lista.append(bicho)
    print("¡Bicho registrado exitosamente!")


def buscar_bicho(lista, especie_buscada):
    for i in range(len(lista)):
        if lista[i]["especie"] == especie_buscada:
            return i
    return -1


def actualizar_estados(lista):
    for bicho in lista:
        if bicho["peligrosidad"] >= 7.0:
            bicho["peligroso"] = True
        else:
            bicho["peligroso"] = False


def mostrar_bichos(lista):
    actualizar_estados(lista)
    print("\n=== LISTA DE BICHOS ===")

    if len(lista) == 0:
        print("No hay bichos registrados en esta expedición.")
        return

    for bicho in lista:
        if bicho["peligroso"]:
            estado_str = "PELIGROSO"
        else:
            estado_str = "NO PELIGROSO"

        print(f"Especie: {bicho['especie']}")
        print(f"Tamaño: {bicho['tamaño']}")
        print(f"Peligrosidad: {bicho['peligrosidad']}")
        print(f"Estado: {estado_str}")
        print("*" * 44)


lista_bichos = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_bicho(lista_bichos)

    elif opcion == 2:
        especie = input("Ingrese especie a buscar: ")
        pos = buscar_bicho(lista_bichos, especie)
        if pos != -1:
            b = lista_bichos[pos]
            print(f"\nBicho encontrado en posición {pos}:")
            print(f"  Especie: {b['especie']}")
            print(f"  Tamaño: {b['tamaño']} cm")
            print(f"  Peligrosidad: {b['peligrosidad']}")
        else:
            print("Especie no registrada.")

    elif opcion == 3:
        especie = input("Ingrese especie a eliminar: ")
        pos = buscar_bicho(lista_bichos, especie)
        if pos != -1:
            eliminado = lista_bichos.pop(pos)
            print(f"Se eliminó el bicho '{eliminado['especie']}' correctamente.")
        else:
            print(f"El bicho '{especie}' no se encuentra registrado.")

    elif opcion == 4:
        actualizar_estados(lista_bichos)
        print("Estados actualizados correctamente.")

    elif opcion == 5:
        mostrar_bichos(lista_bichos)

    elif opcion == 6:
        print("Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
        break