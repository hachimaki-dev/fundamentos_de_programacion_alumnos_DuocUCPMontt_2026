hojas_impresora = 5
impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for trabajo in impresion:
    
    if trabajo == "TEXTO":
        hojas_necesarias = 1
    elif trabajo == "FOTO":
        hojas_necesarias = 3

    if hojas_impresora < hojas_necesarias:
        print("Sin papel")
        break

    hojas_impresora -= hojas_necesarias
    print(f"Imprimiendo {trabajo}")