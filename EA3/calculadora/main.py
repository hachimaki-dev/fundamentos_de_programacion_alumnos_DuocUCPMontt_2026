
def suma(numero_1, numero_2):
    return numero_1 + numero_2
def resta(numero_1, numero_2):
    return numero_1 - numero_2
def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2
def division(numero_1, numero_2):
    return numero_1 / numero_2
def solicitar_dos_numeros():
    print("inserte el numero 1")
    numero_1 = int(input(" "))
    print("inserte el numero 2")
    numero_2 = int(input(" "))
    return numero_1, numero_2

numero_1 = 0
numero_2 = 0
opción_user = 0
while True:
    print("CALCULADORA CALCIO\n" \
    "(1) SUMA\n" \
    "(2) RESTA\n" \
    "(3) MULTIPLICACIÓN\n" \
    "(4) DIVISIÓN\n" \
    "(5) SALIR")

    opción_user = int(input(" "))
    if opción_user == 1:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(suma(numero_1, numero_2))
    elif opción_user == 2:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(resta(numero_1, numero_2))
    elif opción_user == 3:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(multiplicacion(numero_1, numero_2))
    elif opción_user == 4:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(division(numero_1, numero_2))
    elif opción_user == 5:
        break
    else:
        print("ingrese una opción válida")