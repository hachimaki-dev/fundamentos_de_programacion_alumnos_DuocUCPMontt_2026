def suma(numero_1 , numero_2):
    return numero_1 + numero_2
def resta(numero_1 , numero_2):
    return numero_1 - numero_2
def multi(numero_1 , numero_2):
    return numero_1 * numero_2
def divi(numero_1 , numero_2):
    return numero_1 / numero_2
def solicitardosnumeros():
    numero_1 = int(input("ponga su primer numero"))
    numero_2 = int(input("ponga su segundo numero"))
while True:
    print("----CALCULADORA----")
    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 division")
    print("5 salir")
    usuario = int(input("ingrese su opcion"))
    if usuario == 1:
        numero_1 , numero_2 = solicitardosnumeros()
        print(suma(numero_1 , numero_2))
    elif usuario == 2:
        numero_1 , numero_2 = solicitardosnumeros()
        print(resta(numero_1 , numero_2))
    elif usuario == 3:
        numero_1 , numero_2 = solicitardosnumeros()
        print(multi(numero_1 , numero_2))
    elif usuario == 4:
        numero_1 , numero_2 = solicitardosnumeros()
        print(divi(numero_1 , numero_2))
    elif usuario == 5:
        break

#TAREA HACER MENU INTERACTIVO 1 SUMA 2 RESTA 3 MULTI 4 DIVI5ION  SALIR CUALQUIER OTRO NUMERO INVALIDO