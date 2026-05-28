def eltripledeunnumero(numero_ingresado):
    return numero_ingresado * 3

print(  eltripledeunnumero(8)  )

def suma(numero1 , numero2):
    print(suma)
    return numero1 + numero2


def resta(numero1 , numero2):
    return numero1 - numero2

def multiplicacion(numero1 , numero2):
    return numero1 * numero2

def division(numero1 , numero2):
    return numero1 // numero2

while True:
    print("========== CALCULADORA ==========")
    numero1 = int(input("Ingresa tu primer numero: "))
    numero2 = int(input("Ingresa tu segundo numero: "))

    suma(numero1=numero1, numero2=numero2)
    resta(numero1=numero1, numero2=numero2)
    multiplicacion(numero1=numero1, numero2=numero2)
    division(numero1=numero1, numero2=numero2)
    Sumar = 1
    Restar = 2
    Multiplicar = 3
    Dividir = 4 

    print(f"Operaciones: Suma:{Sumar}, Resta:{Restar}, Multiplicacion:{Multiplicar} y Division:{Dividir}. ")

    Operacion = input("Que Operacion desea utilizar? ")

    if Operacion == 1:
        print(f"Su numero es:{suma}")
        break
    elif Operacion == 2:
        print(resta)
        break
    elif Operacion == 3:
        print(multiplicacion)
        break
    else:
        print(division)
        break
