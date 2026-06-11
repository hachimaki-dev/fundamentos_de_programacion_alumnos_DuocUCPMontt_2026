
def suma(numero_1, numero_2):
    return numero_1 + numero_2

def resta(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(numero_1, numero_2):
    return numero_1 // numero_2

def solicitar_dos_numeros():
    numero_1=int(input())
    numero_2=int(input())
    return numero_1, numero_2

#Tarea hacer menu interactivo, 1 es suma, 2 es resta, 3 es multiplicacion, 4 es division, 5 es salir, y cuyaquier otro numero es una opcion invalida, 
#el programa se debe ejecutar hasta que el usuario elija salir.


while True:
    print("\nCALCULADORA\n")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. SALIR\n")

    operacion=int(input("INGRESE UNA OPCION "))

    if operacion==1:
        numero_1, numero_2=solicitar_dos_numeros()
        print(suma(numero_1,numero_2))
    elif operacion==2:
        numero_1, numero_2=solicitar_dos_numeros()
        print(resta(numero_1,numero_2))
    elif operacion==3:
        numero_1, numero_2=solicitar_dos_numeros()
        print(multiplicacion(numero_1,numero_2))
    elif operacion==4:
        numero_1, numero_2=solicitar_dos_numeros()
        print(division(numero_1,numero_2))
    elif operacion==5:
        print("hola")
        break
