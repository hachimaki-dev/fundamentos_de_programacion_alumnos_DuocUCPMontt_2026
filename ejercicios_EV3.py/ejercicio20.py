stock = 60
capasidad_maxima = 60
historial = 0

while True:

    print('\nBiblioteca Tecnologica universitaria ')
    print("1. Ver equipos disponibles")
    print("2. Prestar equpo(s)")
    print("3. Recivir devolucion")
    print("4. Ver historial de prestamo")
    print("3. salir")
    opcion = input("Selecione una opcion: ")
    
    if opcion == "1":
        print(f'Equipos deisponibles: {stock}')

    elif opcion == "2":
        try:
            cantidad = int(input('¿ Cuanto equipos deseas prestar?: '))
            if cantidad <= 0:
                print('Error: debes ingresar un numero entero positivo')
            elif cantidad > stock:
                print('Error: no hay equipos suficientes')
            else:
                stock -= cantidad
                historial += cantidad
                print(f'Se prestaron {cantidad} equipos.')
        except ValueError:
            print('Debe ingresar un numero entero positivo')

    elif opcion == "3":
        try:
            cantidad = int(input('¿Cuanto equipo desea devolver?: '))
            if cantidad <= 0:
                print('Error: debes ingresar un numero entero positivo')
            elif cantidad > historial:
                print('Error: no se puede devolver más equipo de los que estan prestado')
            else:
                stock += cantidad
                historial -= cantidad
                print(f'Se devolviero{cantidad} equipos.')        
        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == '4':
        print(f'prestamos activos {historial}')
    
    elif opcion == '5':
        print('Gracias por utilizar el sistema. Hasta pronto.')  
        break 

    else:
        print('Opcion invalida')     