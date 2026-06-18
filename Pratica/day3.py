def saludar_usuario():
    nombre = input("¿Como te llamas?: ")
    print(f"\nHola, {nombre} Bienvenido \n")

def sumar():
    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(f"\n El resultado es {n1 + n2}")

def dibujar_cuadrado():
    tamaño = int(input("¿De que tamaño quieres el cuadro?: "))
    print()
    for i in range(tamaño):
        for j in range(tamaño):
            print("* ", end="")
        print()


def cuenta_regresiva():
    inicio = int(input("Desde el numero inicial a su cuenta regresiva: "))
    print("\n Inicio Cuenta")
    for i in range(inicio, - 1, -1):
        print(f"La cuenta regresiva es {i}")

def salir():
    print("Salida")

def menú():
    continuar = True

    while continuar:
        print()
        print()
        print()
        print()
        print()

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            saludar_usuario
        elif opcion == "2":
            sumar
        elif opcion == "3":
            dibujar_cuadrado
        elif opcion == "4":
            cuenta_regresiva
        elif opcion == "5":
            salir
        continuar = False