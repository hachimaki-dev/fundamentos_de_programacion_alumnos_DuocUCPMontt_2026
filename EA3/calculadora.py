def suma(num_1, num_2):
    return num1 + num2
def resta(num_1, num_2):
    return num1 - num2
def multiplicacion(num_1, num_2):
    return num1 * num2
def division(num_1, num_2):
    return num1 // num2



while True:
    print("\n=== Menu ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = int(input("Seleccione una opcion:"))
    if opcion == 5:
        print("Saliendo del programa")
        break
    elif opcion >= 1 and opcion <= 4:
        num1 = float(input("Ingrese el primer numero"))
        num2 = float(input("Ingrese el segundo numero"))

    if opcion == 1:
       print("La suma es: ", num1 + num2)
    elif opcion == 2:
        print("La resta es : ", num1 - num2)
    elif opcion == 3:
       print("La multiplicacion es : ", num1 * num2)
    elif opcion == 4:
        if num2 != 0:
            print("La division es : ", num1 // num2)

    else:
        print("Error: no se puede dividir por cero")

else:
    print("Opcion invalida")
    


    


  