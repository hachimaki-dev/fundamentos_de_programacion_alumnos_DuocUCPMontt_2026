while True:
    try:
        numero1 = int(input("Ingresa un numero"))
        numero2 = int(input("Ingresa el denominador"))
        resultado = numero1/numero2
        break
    except ValueError:
        print("Por favor ingrese un numero entero valido")
    except ZeroDivisionError:
        print("Estai chistoso, no se puede dividir por cero")
    except:
        print("Ocurrio un error, pero no se cual, solo se que algo fallo")
    finally:
        print("Soy choro, simpre me ejecuto")