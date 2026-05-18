#Tarea: Implementar esta claculadora con
#Menu de opciones 1 suma. 2 resta., 3 multiplica, 4 divide, 5 sale, cualquyier otro numeo es invalido. Los numeros deben ser inputs 

def sumar(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 // numero_2

def solicitar_dos_numeros():
    numero_1 = int(input("Ingrese primer número"))
    numero_2 = int(input("Ingrese segundo número"))

    return  numero_1, numero_2


while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese una opción"))

    if opcion == 1:
        #sumamos
        numero_1, numero_2 = solicitar_dos_numeros()
        print(sumar(numero_1 , numero_2))
       
    elif opcion == 2:
        #restamos
        numero_1, numero_2 = solicitar_dos_numeros()
        print(resta(numero_1 , numero_2))
    elif opcion == 3:
        #multipliamos
        numero_1, numero_2 = solicitar_dos_numeros()
        print(multiplicar(numero_1 , numero_2))
    elif opcion == 4:
        #dividir
        numero_1, numero_2 = solicitar_dos_numeros()
        print(division(numero_1 , numero_2))
    elif opcion == 5:
        break
    else:
        print("opición invalida")
