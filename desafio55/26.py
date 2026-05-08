impresiones = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

hojas_impresoras = 5

for impresion in impresiones:
    if impresion == "TEXTO":
        hojas_impresoras = hojas_impresoras - 1
    elif impresion == "FOTO":
        hojas_impresoras = hojas_impresoras -3
    elif hojas_impresoras < impresiones:
        print("Sin papel")

print("imprimiento", impresion)