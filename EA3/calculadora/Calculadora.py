def suma(numero_1 , numero_2):
    return numero_1 + numero_2
def resta(numero_1 , numero_2):
    return numero_1 - numero_2
def multiplicacion(numero_1 , numero_2):
    return numero_1 * numero_2
def division(numero_1 , numero_2):
    return numero_1 // numero_2

def solicitar_dos_numeros():
    numero_1 = int(input("Ingrese primer numero: "))
    numero_2 = int(input("Ingrese el otro numero: ")) 
    return numero_1 , numero_2

while True:
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        numero_1 , numero_2 = solicitar_dos_numeros()
        print(suma(numero_1 , numero_2))
    elif opcion == 2:
        numero_1 , numero_2 = solicitar_dos_numeros()
        print(resta(numero_1 , numero_2))
    elif opcion == 3:
        numero_1 , numero_2 = solicitar_dos_numeros()
        print(multiplicacion(numero_1 , numero_2))
    elif opcion == 4:
        numero_1 , numero_2 = solicitar_dos_numeros()
        print(division(numero_1 , numero_2))
    elif opcion == 5:
        break
    else:
        print("Ingrese una opcion valida")