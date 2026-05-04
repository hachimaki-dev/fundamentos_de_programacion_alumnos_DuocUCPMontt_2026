tipovehiculo='Camion'
velocidad=95#En KM POR HORA

if tipovehiculo=='Auto':
    if velocidad > 120:
        print('Multa Gravísima')
    else:
        print('ok')
elif tipovehiculo=='Camion':
    if velocidad > 80:
        print('Multa Grave Camión')
    else:
        print('Ok')    
