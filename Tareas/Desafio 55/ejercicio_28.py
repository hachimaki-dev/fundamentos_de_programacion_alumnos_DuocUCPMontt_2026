# Búsqueda del Sospechoso (Cámaras)
#La policía está buscando un auto robado en la lista de cámaras del peaje.

patentes = ['XY11', 'ZZ99', 'AB12', 'XX00'] # patentes de los veiculos 

for policia in patentes:
    print('buscando patente', policia)

    # condicio para detener el bucle 
    if policia == 'AB12':
        print('patente encontrada, no tiene sentido mirar los autos que pasaron después')
        break
print('Imprime todo paso a paso')    

