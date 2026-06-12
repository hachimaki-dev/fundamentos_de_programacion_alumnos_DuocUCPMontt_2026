while True:
    try:
        num1 = int(input("ingrese el primer numero:"))
        num2 = int(input("ingrese el segundo numero:"))

        resultado = num1 / num2
        print(f"el resultado de la division es {resultado}")
        break
    except ValueError:
        print("ha ocurrido un error se esperaba un numero entero")
    except ZeroDivisionError:
        print("no se pue con el zero po")