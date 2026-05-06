hojas_impresora = 5
Imprimiendo = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
if hojas_impresora > 0:
    print(f"Imprimiendo {"TEXTO"}")
    hojas_impresora = hojas_impresora - 1
    print(f"Imprimiendo {"FOTO"}")
    hojas_impresora = hojas_impresora - 3
    print(f"Imprimiendo {"TEXTO"}")
    hojas_impresora = hojas_impresora - 1
    print("Sin papel")