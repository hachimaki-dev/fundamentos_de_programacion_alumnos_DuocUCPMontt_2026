while True:
    try:
        numero1 =int(input('ingresa algo: '))
        numero2 = int(input('ingresa algo: '))
        resultado = numero1/numero2
        break
    except ValueError:
        print('que no sea una letra0')
    except ZeroDivisionError:
        print('xd')        
    except:
        print('ocurrio un error ¿, pero no se')    