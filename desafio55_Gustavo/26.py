impresora = 5
impresion = ["TEXTO","FOTO","TEXTO","FOTO"]

for i in impresion :

    if i == "TEXTO":
        print(f"Imprimiendo {i}")
        impresora -=1
    elif i == "FOTO":
        print(f"Imprimiendo {i}")
        impresora -=3
    if impresora <= 0 :
        break

print("Sin papel")