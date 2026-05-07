
vehiculo = 'Camion'
velocidad = 95

if vehiculo == 'Auto' and velocidad > 120:
    print('Multa Gravísima')
elif vehiculo == 'Camion' and velocidad > 80:
    print('Multa Grave Camión')
else:
    print('Sin multa')