while True:
    try:
        registro_de_pasajeros = int(input('capasidad de pasajeros: '))
        if registro_de_pasajeros >= 1   :
            break
        else:
            print('Error ingresa un numero positivo de pasajeros')
    except ValueError:    
        print('Error ingresa un numero positivo de pasajeros')
print(f'Vuelo registrado con {registro_de_pasajeros} pasajeros')        