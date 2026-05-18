
def suma(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 // numero_2


print("Holaa, Bienvenido a la calculadora.")
continuar = True
while continuar:

    print("Elija una opcion, Porfavor.")
    print("1) Suma")
    print("2) resta")
    print("3) multiplicacion")
    print("4) division")
    print("5) salir")

    opcion = int(input("--"))
    if opcion == 1:
        numero_1 = int(input("ingrese numero 1 :   "))
        numero_2 = int(input("ingrese numero 2 :   "))
        print(suma(numero_1, numero_2))

    elif opcion == 2:
        numero_1 = int(input("ingrese numero 1 :   "))
        numero_2 = int(input("ingrese numero 2 :   "))
        print(resta(numero_1, numero_2))

    elif opcion == 3:
        numero_1 = int(input("ingrese numero 1 :   "))
        numero_2 = int(input("ingrese numero 2 :   "))
        print(multiplicacion(numero_1, numero_2))

    elif opcion == 4:
        numero_1 = int(input("ingrese numero 1 :   "))
        numero_2 = int(input("ingrese numero 2 :   "))
        print(division(numero_1, numero_2))
    
    elif opcion == 5:
        print("Saliendo")
        continuar = False
    else:
        print("Numero invalido we")




