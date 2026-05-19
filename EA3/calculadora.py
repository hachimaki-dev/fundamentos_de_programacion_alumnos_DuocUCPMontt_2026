def suma(numero_1,numero_2):
    return numero_1 + numero_2

    


def resta(numero_1,numero_2) :
    return numero_1 - numero_2
    


def multiplicacion(numero_1,numero_2):
    return numero_1 * numero_2
                   



def division(numero_1,numero_2) :
    return numero_1 // numero_2
                   


while True :
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Salir")

    opcion_usuario = int(input("Elija su opcion: "))
    
    if opcion_usuario == 1 :
        numero_1 = int(input("Elija su numero a sumar: "))
        numero_2 = int(input("Elija su segundo numero: "))
        print(suma(numero_1,numero_2))
    
    elif opcion_usuario == 2 :
        numero_1 = int(input("Elija su numero a restar: "))
        numero_2 = int(input("Elija su segundo numero: "))
        print(resta(numero_1,numero_2))
    elif opcion_usuario == 3 :
        numero_1 = int(input("Elija su numero a multiplicar: "))
        numero_2 = int(input("Elija su segundo numero: "))
        print(multiplicacion(numero_1,numero_2))

    elif opcion_usuario == 4 :
        numero_1 = int(input("Elija su numero a dividir: "))
        numero_2 = int(input("Elija su segundo numero: "))
        print(division(numero_1,numero_2))

    elif opcion_usuario == 5 :
        print("El usuario ha decidido salir")
        break
    else :
        print("Opcion invalida")
    







