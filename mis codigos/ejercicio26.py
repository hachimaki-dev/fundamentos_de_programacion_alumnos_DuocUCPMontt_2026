hojas_disponibles = 5

impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for documento in impresion:
    
    if documento == 'TEXTO':
        gasto = 1
    else: 
        gasto = 3

    if hojas_disponibles >= gasto:
        print(f"Imprimiendo {documento}")
        hojas_disponibles -= gasto  

    else:       
        print("Sin papel")
        break