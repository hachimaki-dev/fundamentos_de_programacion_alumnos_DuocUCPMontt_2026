hojas_impresora=5
impresiones=["TEXTO", "FOTO", "TEXTO", "FOTO"]
for i in impresiones:
    if i =="TEXTO":
        hojas_impresora-=1
        print(f"Imprimiendo {i}")
    elif i =="FOTO":
        hojas_impresora-=3
        print(f"Imprimiendo {i}")
    if hojas_impresora<=0:
        print("Sin Papel")
        break