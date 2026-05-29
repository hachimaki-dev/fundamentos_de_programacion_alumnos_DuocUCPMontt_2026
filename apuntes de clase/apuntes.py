#while True:
#    try:
#        numero1 = int(input("Ingresa el numerador: "))
#        numero2 = int(input("Ingresa el denominador: "))
#    
#        resultado = numero1/numero2
#        break
#    except ValueError:
#        print("Por favor ingrese un numero entero valido")
#    except ZeroDivisionError:
#        print("Estai chistoso, no se puede dividir el 0")
#    except :
#        print("Ocurrio un error pero no se sabe cual")
while True:
    try:
        numero_ingresado = int(input("Ingresa un número:\n"))
        print(f"Numero ingresado: {numero_ingresado}")
        break
    except ValueError:
        print("Error: Eso no es un numero:\n")