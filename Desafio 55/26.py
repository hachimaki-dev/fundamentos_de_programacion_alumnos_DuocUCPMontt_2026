hojas_restantes = 5
hojas_gastadas = 0

impresiones = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

gasto_hoja_texto = 1
gasto_hoja_foto = 3

for impresion in impresiones :
    if impresion == "TEXTO" :
        hojas_gastadas += gasto_hoja_texto
    elif impresion == "FOTO" :
        hojas_gastadas += gasto_hoja_foto

    if hojas_gastadas > 5 :
        print("Sin papel")
        break
    else :
        print(f"Imprimiendo {impresion}")