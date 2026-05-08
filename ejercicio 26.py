hojas = 5
espera = ["texto", "foto", "texto", "foto"]

for documento in espera:
    if documento == "texto":
        if hojas >= 1:
            print(f"Imprimiendo {documento}") 
            hojas -= 1
        else:
            print("Sin papel")
            break
    elif documento == "foto":
        if hojas >= 3:
            print(f"Imprimiendo {documento}")
            hojas -= 3
        else:
            print("Sin papel")
            break
 
print()
 