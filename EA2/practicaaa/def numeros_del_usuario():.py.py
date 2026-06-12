def suma(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 / numero_2

def numeros_del_usuario():
    numero_1 = int(input("Ingrese numero: "))
    numero_2 = int(input("Ingrese numero: "))
    
    return numero_1, numero_2

while True:

    print("1. suma")
    print("2. resta")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        numero_1, numero_2 = numeros_del_usuario()
        print(suma(numero_1, numero_2))

    elif opcion == 2:
        numero_1, numero_2 = numeros_del_usuario()
        print(resta(numero_1, numero_2))

    elif opcion == 3:
        numero_1, numero_2 = numeros_del_usuario()
        print(multiplicacion(numero_1, numero_2))

    elif opcion == 4:
        numero_1, numero_2 = numeros_del_usuario()
        print(division(numero_1, numero_2))

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("Opcion invalida")