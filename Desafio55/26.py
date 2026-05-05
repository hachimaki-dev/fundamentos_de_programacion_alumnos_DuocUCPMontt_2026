hojas_de_impresora = 5
imprimir = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for i in imprimir:
    if i == "TEXTO":
        uso_de_hojas = 1
    elif i == "FOTO":
        uso_de_hojas = 3

    if hojas_de_impresora >= uso_de_hojas:
        print(f"imprimiento {i}")
        hojas_de_impresora -= uso_de_hojas
    else:
        print("Sin papel")