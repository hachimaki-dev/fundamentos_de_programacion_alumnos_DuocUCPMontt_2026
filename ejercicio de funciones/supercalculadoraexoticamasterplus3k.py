#CREAR MENU INTERACTIVO DONDE n1 ES SUMA, n2 RESTA, n3 MULTIPLICACION, n4 DIVISION, 5 salir
def suma(numero_1, numero_2):
    return numero_1+numero_2

def resta(numero_1,numero_2):
    return numero_1-numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1*numero_2

def division(numero_1, numero_2):
    return numero_1/numero_2

def numeros_deL_usuario():
    numero_1 = int(input("Escoja su primer número.\n"))
    numero_2 = int(input("Escoja su segundo número.\n"))
    return numero_1, numero_2

while True:
    print("== SELECCIONA UNA OPERACIÓN ==")
    operacion = int(input("1.SUMA\n2.RESTA\n3.MULTIPLICAR\n4.DIVISION\n5.SALIR.\n"))
    if operacion == 5:
        print("Ha salido de la súper calculadora.")
        break
    if operacion == 1:
        numero_1, numero_2 = numeros_deL_usuario()                               #BOILERPLATEADO (REPETITIVO) - - - - SE PUEDE ARREGLAR CON UN DEF
        print(f"Resultado: {suma(numero_1,numero_2)}.")
    elif operacion == 2:
        numero_1, numero_2 = numeros_deL_usuario()
        print(f"Resultado: {resta(numero_1,numero_2)}.")
    elif operacion == 3:
        numero_1, numero_2 = numeros_deL_usuario()
        print(f"Resultado: {multiplicacion(numero_1,numero_2)}.")
    elif operacion == 4:
        numero_1, numero_2 = numeros_deL_usuario()
        print(f"Resultado: {division(numero_1, numero_2)}.")
    else:
        print("OPCIÓN INVALIDA.")