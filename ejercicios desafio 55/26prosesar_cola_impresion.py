hojas_en_la_impresora = 5
imprimir_texto = 1
imprimir_foto = 3 
cosas_a_imprimir = [imprimir_texto, imprimir_foto, imprimir_texto, imprimir_foto]
for impresion in cosas_a_imprimir:
    hojas_en_la_impresora = hojas_en_la_impresora - impresion
    if impresion == 1:
        print("imprimiendo texto")
    elif impresion == 3:
        print("imprimiendo foto")
    if hojas_en_la_impresora == 0:
        print("sin papel")
        break