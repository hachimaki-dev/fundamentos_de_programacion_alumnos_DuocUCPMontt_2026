#Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.

hojas_restantes = 5

cola_de_impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

contador = 0
for impresion in cola_de_impresion:
    if impresion == "TEXTO":
        if hojas_restantes >= 1:
            print(f"Imprimiendo el documento N {contador + 1}")
            hojas_restantes = hojas_restantes - 1
            contador += 1
    elif impresion == "FOTO":
        if hojas_restantes >= 3:
            print(f"Imprimiendo el documento N {contador + 1}")
            hojas_restantes = hojas_restantes - 3
            contador += 1
    else:
        print("Impresion No soportada")
