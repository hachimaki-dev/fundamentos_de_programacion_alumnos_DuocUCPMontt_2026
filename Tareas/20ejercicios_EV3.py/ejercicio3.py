while True:
    try:
        edad = int(input('Ingresa tu edad del conductor: '))
        if edad >= 0:
            break
        else:
            print('Dato invalido, tu numero deve ser posivo')
    except ValueError:
        print('Dato invalido, tu numero deve ser posivo')
print('Edad registrado: ', edad, 'años')                