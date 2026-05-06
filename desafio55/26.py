
hojas_restantes = 5

cola_de_imprecion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

contador = 0
for impresion in cola_de_imprecion:
    if impresion == 'TEXTO':
        if hojas_restantes >= 1:
            print(f"imprimimiendo el documento N {contador + 1}")
            hojas_restantes -= 1
    elif impresion == 'FOTO':
        if hojas_restantes >= 3:
            print(f"imprimimiendo el documento N {contador + 1}")
            hojas_restantes -= 2
        contador += 1
    else:
        print("tipo de documento no reconocido")