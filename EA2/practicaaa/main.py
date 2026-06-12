print("---'CONOCIENDO LAS MATEMATICAS'---" )

def suma(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 / numero_2

while True:
    print("1. suma")
    print("2. resta")
    print("3. multiplicar")
    print("4. dividir")
    
    opcion = int(input("ingrese su opcion"))

    if opcion == 1:
        #suma
        numero_1 = int(input("ingrese numero:"))
        numero_2 = int(input("ingrese numero:"))
        suma(numero_1,numero_2)
    elif opcion == 2:
        #restar
    elif opcion == 3:
        #multiplicar
    elif opcion == 4:
        #divicion
    elif opcion == 4:
        #salir
    
