patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
buscada = 'AB12'

for patente in patentes:
    print(f'Buscando en {patente}...')

    if patente == buscada:
        print('Sospechoso encontrado')
        break