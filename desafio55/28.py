patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
buscado = 'AB12'

for patente in patentes:
    print("buscando en:", patente + '....')
    
    if patente == buscado:
        print("sospechoso encontado")
        break

