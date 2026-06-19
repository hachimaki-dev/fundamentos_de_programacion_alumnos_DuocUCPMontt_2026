# Taller: Sistema Cazabichos
lista_De_bichos = [
    {'especie': 'Himenópteros',
     'tamaño': 5,
     'peligrosidad': (1.0-10.0),
    'peligrosos': False}
]

# Menu Interactivo
while True:
    print('1. Agregar bicho')
    print('2. Buscar bicho')
    print('3. Eliminar bicho')
    print('4. Actualizar estados')
    print('5. Mostrar bichos')
    print('6. Salir')

    # opcciona seleccionada
    eligue_una_opcion = input('Selecciona una opcciona querido programa: ')
    
    # Agregar un ficho
    if eligue_una_opcion == '1':
        especie = input('Ingresa la especie')
        tamaño =  int(input('Ingresa el tamaño'))
        Peligrosidad = float(input('Ingrese la peligrosidad del bichos escoguido: '))

        # validar especie
        if not especie:
            print()

