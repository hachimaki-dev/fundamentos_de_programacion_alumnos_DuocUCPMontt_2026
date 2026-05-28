opcion = 0

def sumar(num_1, num_2):
    return num_1 + num_2

def restar(num_1, num_2):
    return num_1 - num_2

def multiplicar(num_1, num_2):
    return num_1 * num_2

def dividir(num_1, num_2):
    if num_2 == 0:
        print("No puedes dividir por 0")
        return
    else:
        return num_1 / num_2

while opcion != 5:
    opcion = 0
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while opcion < 1 or opcion > 5:
        opcion = int(input("Ingresa tu opcion: "))

        if opcion < 1 and opcion > 5:
            print("Ingresa una opción válida")

    if opcion == 5:
        break

    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))

    match (opcion):
        case 1:
            print(f"Resultado: {sumar(num_1, num_2)}")
        case 2:
            print(f"Resultado: {restar(num_1, num_2)}")
        case 3:
            print(f"Resultado: {multiplicar(num_1, num_2)}")
        case 4:
            print(f"Resultado: {dividir(num_1, num_2)}")
        case _:
            print("Error")
    