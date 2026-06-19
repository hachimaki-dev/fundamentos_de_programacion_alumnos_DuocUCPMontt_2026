# Procesar cola de impresión
# controla cuántas hojas le quedan a la impresora antes de imprimir un documento
hojas = 5

documentos = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for documento in documentos:

    if documento == 'TEXTO':
        hojas_necesarias = 1

    elif documento == 'FOTO':
        hojas_necesarias = 3

    if hojas < hojas_necesarias:
        print('Sin papel')
        break

    print('Imprimiendo', documento)

    hojas = hojas - hojas_necesarias