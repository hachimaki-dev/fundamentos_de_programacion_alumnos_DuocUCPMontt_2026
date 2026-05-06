patentesdetectadas=['XY11', 'ZZ99', 'AB12', 'XX00']

sospechoso=['AB12']

for i in patentesdetectadas:
    print(f'Buscando en {i}...')
    if i in sospechoso:
        print('Sospechoso encontrado')
        break
    