hojas_impresora = 5
hojas_maximas = 5

texto_fotos = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for elemento in texto_fotos:

    print(f"Imprimiendo {elemento}... ")
        
    

    if elemento == 'FOTO' and hojas_impresora >= 3:
        hojas_impresora -= 3


    elif elemento == 'TEXTO' and hojas_impresora >= 1:
        hojas_impresora -= 1

    if hojas_impresora < 0:
        print("¡Sin papel!")
        break

    

