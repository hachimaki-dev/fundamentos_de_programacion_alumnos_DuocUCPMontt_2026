while True:
    try:
        numero =int(input('Ingresa un numero: '))
        break
    except ValueError:
        print('El numero tiene que ser entero')
print('Numero recivido', numero)